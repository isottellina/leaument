from leaument.constants import DAY_VALUES


def test_day_values_right_length():
    assert len(DAY_VALUES) == 12
    for month in DAY_VALUES:
        assert len(month) == 30
