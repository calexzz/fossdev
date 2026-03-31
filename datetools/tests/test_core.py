"""Tests for datetools.core module."""

import pytest
from datetime import date, timedelta

from datetools.core import age, day_of_week, days_diff, is_leap_year


# --- is_leap_year ---

def test_leap_year_divisible_by_400() -> None:
    assert is_leap_year(2000) is True


def test_leap_year_divisible_by_4_not_100() -> None:
    assert is_leap_year(2024) is True


def test_not_leap_year_divisible_by_100_not_400() -> None:
    assert is_leap_year(1900) is False


def test_not_leap_year_regular() -> None:
    assert is_leap_year(2023) is False


# --- day_of_week ---

def test_day_of_week_monday() -> None:
    assert day_of_week(date(2024, 1, 1)) == "Monday"


def test_day_of_week_sunday() -> None:
    assert day_of_week(date(2024, 1, 7)) == "Sunday"


def test_day_of_week_returns_string() -> None:
    assert isinstance(day_of_week(date(2024, 6, 15)), str)


# --- days_diff ---

def test_days_diff_future() -> None:
    future = date(date.today().year + 1, 1, 1)
    assert days_diff(future) > 0


def test_days_diff_past() -> None:
    past = date(2000, 1, 1)
    assert days_diff(past) < 0


def test_days_diff_today() -> None:
    assert days_diff(date.today()) == 0


# --- age ---

def test_age_basic() -> None:
    today = date.today()
    birthdate = date(today.year - 20, today.month, today.day)
    assert age(birthdate) == 20


def test_age_not_yet_birthday() -> None:
    today = date.today()
    tomorrow = today + timedelta(days=1)
    birthdate = date(today.year - 25, tomorrow.month, tomorrow.day)
    assert age(birthdate) == 24


def test_age_future_raises() -> None:
    with pytest.raises(ValueError):
        age(date(date.today().year + 1, 1, 1))
