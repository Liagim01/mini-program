
# Calculate Your Age!

## Overview

This Python script calculates and prints your age in three different formats: years, months, and days. It is a simple yet effective tool to understand how long one has lived in different time units, utilizing Python's built-in modules and straightforward logic.

## Purpose

The script's purpose is to provide a fun and interactive way for users to see their age in a more detailed perspective, breaking it down into years, months, and days.

## Prerequisites

- Python 3.x installed on your system.
  - You can download Python from [here](https://www.python.org/downloads/).

## How to Run the Script

1. Ensure Python 3.x is installed on your system.
2. Download the script to your local machine.
3. Open a terminal and navigate to the directory where the script is saved.
4. Execute the script using the following command:

   ```bash
   python calculate.py
   ```

## Script Details

### Main Features

- **Leap Year Calculation:** Determines if a year is a leap year to accurately calculate the number of days in February.
- **Month-wise Day Calculation:** Calculates the number of days for each month, adjusting for leap years.
- **Age Calculation in Different Units:** Converts the user's age from years to months and days.

### Functionality

- `judge_leap_year(year)`: Determines if the given year is a leap year.
- `month_days(month, leap_year)`: Returns the number of days in a given month, accounting for leap years.
- The script calculates the user's age in years, then converts it to months and days, considering the current date.

### User Interaction

- The script prompts the user to input their name and age.
- It then displays the age in years, months, and days.

## Sample Use of the Script

```bash
$ python calculate.py 
input your name: John
input your age: 25
John's age is 25 years or 306 months or 9300 days
```

## Author

[Gaodong](https://github.com/xlgd)

