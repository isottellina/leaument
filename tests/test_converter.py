from datetime import date
import pytest
from leaument.converter import RepublicanDate, int_to_roman


@pytest.mark.parametrize(
    "gregorian_date, republican_date",
    (
        pytest.param(date(1871, 5, 6), RepublicanDate(79, 8, 16)),
        pytest.param(date(1989, 7, 14), RepublicanDate(197, 10, 25)),
        pytest.param(date(1994, 9, 28), RepublicanDate(203, 1, 7)),
        pytest.param(date(2000, 1, 1), RepublicanDate(208, 4, 12)),
        pytest.param(date(2020, 2, 29), RepublicanDate(228, 6, 11)),
        pytest.param(date(2021, 3, 8), RepublicanDate(229, 6, 18)),
    ),
)
def test_converter(gregorian_date, republican_date):
    assert RepublicanDate.from_gregorian(gregorian_date) == republican_date


@pytest.mark.parametrize(
    "source,result",
    (
        pytest.param(79, "LXXIX"),
        pytest.param(197, "CXCVII"),
        pytest.param(203, "CCIII"),
        pytest.param(228, "CCXXVIII"),
        pytest.param(229, "CCXXIX"),
        pytest.param(2000, "MM"),
        pytest.param(2024, "MMXXIV"),
        pytest.param(4500, "why must you hurt me this way (4500)"),
    ),
)
def test_int_to_roman(source, result):
    assert int_to_roman(source) == result
