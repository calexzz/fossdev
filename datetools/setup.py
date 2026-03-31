from setuptools import setup, find_packages

setup(
    name="datetoools",
    version="0.1.0",
    description="A small collection of date utility functions: leap year, weekday, days diff, age",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="calexzz",
    url="https://github.com/calexzz/fossdev",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "mypy>=1.0",
            "flake8>=6.0",
            "build>=1.0",
            "twine>=4.0",
        ],
    },
    python_requires=">=3.8",
    keywords=["date", "datetime", "leap year", "weekday", "utilities"],
)