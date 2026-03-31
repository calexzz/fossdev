# datetools

[![test.pypi](https://img.shields.io/badge/test.pypi-datetools-blue)](https://test.pypi.org/project/datetools/)
[![Python](https://img.shields.io/badge/python-3.8+-green)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A small collection of date utility functions with no external dependencies.

**Repository:** https://github.com/calexzz/fossdev

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [How It Works](#how-it-works)
- [Development](#development)
- [License](#license)

## Installation

From test.pypi.org:
```bash
pip install --index-url https://test.pypi.org/simple/ datetools
```

From the repository:
```bash
pip install git+https://github.com/calexzz/fossdev.git
```

## Usage
```python
from datetime import date
from datetools import is_leap_year, day_of_week, days_diff, age

is_leap_year(2024)          # True
is_leap_year(1900)          # False

day_of_week(date(2024, 1, 1))   # 'Monday'

days_diff(date(2026, 12, 31))   # positive → days until
days_diff(date(2020, 1, 1))     # negative → days since

age(date(2000, 6, 15))      # 25
```

## API Reference

### `is_leap_year(year: int) -> bool`

Returns `True` if the given year is a leap year. A year is a leap year if it is divisible by 4, except for century years which must be divisible by 400.

### `day_of_week(d: date) -> str`

Returns the English weekday name for the given `datetime.date` object. For example, `date(2024, 1, 1)` returns `'Monday'`.

### `days_diff(d: date) -> int`

Returns the number of days between today and `d`. Positive means the date is in the future, negative means it is in the past, zero means today.

### `age(birthdate: date) -> int`

Returns the current age in full completed years. Raises `ValueError` if the birthdate is in the future.

## How It Works

All functions rely exclusively on Python's built-in `datetime` module — no external dependencies.

**Leap year** logic follows the Gregorian calendar rule: divisible by 4, but century years only count if divisible by 400.

**Day of week** delegates to `date.strftime("%A")` which uses the current locale-independent English names.

**Days diff** subtracts today's date from the target date; Python's `timedelta` returns the signed integer difference via `.days`.

**Age** computes the year difference and subtracts 1 if the birthday hasn't occurred yet this year, by comparing `(month, day)` tuples.

## Development
```bash
make install      # create venv and install dependencies
make lint         # flake8 style check
make typecheck    # mypy type check
make test         # run pytest
make build        # build wheel + sdist
make publish-test # upload to test.pypi.org
make clean        # remove build artifacts
```

## License

MIT — see [LICENSE](LICENSE).