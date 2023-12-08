'''
This script is used to calculate a person's age in years, months, and days.
'''
import datetime
import calendar
def judge_leap_year(year):
    '''
    Determines if a year is a leap year.
    '''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def month_days(month, leap_year):
    '''
    Calculates the number of days in a given month.
    '''
    if month == 2:
        if leap_year:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
def calculate_age(name, age):
    '''
    Calculates the age in years, months, and days.
    '''
    current_date = datetime.date.today()
    birth_year = current_date.year - age
    birth_month = current_date.month
    birth_day = current_date.day
    leap_year = judge_leap_year(birth_year)
    days_in_birth_month = month_days(birth_month, leap_year)
    if birth_day > current_date.day:
        birth_month -= 1
        if birth_month == 0:
            birth_month = 12
            birth_year -= 1
        days_in_birth_month = month_days(birth_month, leap_year)
    if birth_month > current_date.month:
        birth_month -= 12
        birth_year -= 1
    years = current_date.year - birth_year
    months = current_date.month - birth_month
    days = current_date.day - birth_day
    if days < 0:
        months -= 1
        if months == 0:
            months = 12
            years -= 1
        days += days_in_birth_month
    return f"{name}'s age is {years} years or {months} months or {days} days"
if __name__ == "__main__":
    name = input("Input your name: ")
    try:
        age = int(input("Input your age: "))
        result = calculate_age(name, age)
        print(result)
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")