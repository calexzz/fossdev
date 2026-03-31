"""Core date utility functions for the datetools package."""

from datetime import date


def is_leap_year(year: int) -> bool:
    """Return True if the given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def day_of_week(d: date) -> str:
    """Return the English name of the weekday for a given date."""
    return d.strftime("%A")


def days_diff(d: date) -> int:
    """Return the number of days between today and the given date.

    Positive means future, negative means past.
    """
    return (d - date.today()).days


def age(birthdate: date) -> int:
    """Return the current age in full years.

    Raises:
        ValueError: If birthdate is in the future.
    """
    today = date.today()
    if birthdate > today:
        raise ValueError("Birthdate cannot be in the future.")
    years = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        years -= 1
    return years
