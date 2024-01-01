from dataclasses import dataclass
from datetime import date
from typing import Self
import math
from leaument.constants import CALENDER_BEGINNING, EXTRA_DAYS, MONTHS


def republican_year_started_on_year(year: int) -> int:
    """
    This is the year that begins on the Gregorian year. Example : 1792 -> An I, 1800 -> An IX
    """
    return year - 1791


def start_of_year(year: int) -> int:
    """
    This function returns the day of September on which the republican
    year began this year. This is mostly in sync, but unsyncs itself each
    time a year that should be a leap year (multiple of 4) isn't (because it's
    a multiple of 100) in either calendar.
    """

    def non_leap_year_multiple_of_4(since: int, a: int) -> int:
        """
        returns the number of supposed leap years that weren't leap years
        between two years.
        """
        return sum(
            1 for b in range(math.ceil(since / 100), math.ceil(a / 100)) if b % 4 != 0
        )

    republican_year = republican_year_started_on_year(year)

    # We add 1 to the gregorian year, since the intercalar day is added before the start
    # of the Republican year.
    return (
        22
        + non_leap_year_multiple_of_4(1792, year + 1)
        - non_leap_year_multiple_of_4(1, republican_year)
    )


def get_republican_year(gregorian_date: date) -> tuple[int, int]:
    """
    From a Gregorian date, return (Republican year, number of days into the year)
    """
    assert gregorian_date >= CALENDER_BEGINNING
    republican_year_started = republican_year_started_on_year(gregorian_date.year)
    start_of_republican_year = date(
        gregorian_date.year, 9, start_of_year(gregorian_date.year)
    )

    if gregorian_date >= start_of_republican_year:
        return republican_year_started, (gregorian_date - start_of_republican_year).days

    start_of_previous_year = date(
        gregorian_date.year - 1, 9, start_of_year(gregorian_date.year - 1)
    )
    return republican_year_started - 1, (gregorian_date - start_of_previous_year).days


@dataclass
class RepublicanDate:
    year: int
    month: int
    day: int

    @classmethod
    def from_gregorian(cls, gregorian: date) -> Self:
        year, days_into_year = get_republican_year(gregorian)

        return cls(
            year,
            days_into_year // 30,
            (days_into_year % 30) + 1,
        )

    def is_extra_day(self) -> bool:
        return self.month == 12

    def format_day(self) -> str:
        return f"{self.day} {MONTHS[self.month]}"
    
    def __str__(self) -> str:
        day = EXTRA_DAYS[self.day - 1] if self.is_extra_day() else self.format_day()

        return f"{day}, an {self.year}"
