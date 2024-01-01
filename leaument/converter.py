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

def int_to_roman(a: int) -> str:
    """
    This is horrible. Rome must burn.

    Largely inspired by Donald Knuth's TeX implementation.
    """
    if a > 3999:
        return f"why must you hurt me this way ({a})"
    
    values = "MDCLXVI"
    current_value = 1000
    pointer = 0
    result = ""
    
    while True:
        while a >= current_value:
            result += values[pointer]
            a -= current_value

        if a <= 0:
            return result

        next_pointer = pointer + 1
        divide_by = 5 if pointer % 2 else 2
        next_value = current_value // divide_by

        if divide_by == 2:
            # if dividing by 2 (1000 -> 500, 100 -> 50), we have
            # to take into account the substractive nature of
            # roman numerals, so we look even further to add the substraction.
            #
            # therefore, next_pointer always refers to a power of 10.
            next_pointer += 1
            next_value //= 5

        # For example, if 900 + 100 >= 1000, we have to substract 100
        # and go back to the start of the loop with the same values.
        # we add next_value to a, since we have substracted it here.
        if (a + next_value) >= current_value:
            result += values[next_pointer]
            a += next_value
        else:
            # if we're completely done with this substraction shit,
            # we can safely go to the next value. spare me please.
            current_value //= divide_by
            pointer += 1

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
            (days_into_year // 30) + 1,
            (days_into_year % 30) + 1,
        )

    def is_extra_day(self) -> bool:
        return self.month == 13

    def format_day(self) -> str:
        return f"{self.day} {MONTHS[self.month - 1]}"
    
    def __str__(self) -> str:
        day = EXTRA_DAYS[self.day - 1] if self.is_extra_day() else self.format_day()

        return f"{day}, an {int_to_roman(self.year)}"
