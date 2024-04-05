from datetime import datetime, timedelta
import math

def add_ordinal_indicator(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return str(num) + suffix

def get_todays_date():
    return datetime.today().strftime('%Y-%m-%d')

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def years_passed(start_date, end_date=None):
    if end_date == None:
        end_date = get_todays_date()

    start_year, start_month, start_day = map(int, start_date.split('-'))
    end_year, end_month, end_day = map(int, end_date.split('-'))
    
    # Calculate the years difference
    years_diff = end_year - start_year
    
    # If end_date is before the start_date's anniversary, subtract one year
    if (end_month, end_day) < (start_month, start_day):
        years_diff -= 1
    # If end_date is the same as start_date's anniversary, check for leap year
    elif (end_month, end_day) == (start_month, start_day):
        if is_leap_year(start_year) and start_month == 2 and start_day == 29:
            # If start_date is Feb 29th of a leap year, check if end_date's year is a leap year
            if not is_leap_year(end_year):
                years_diff -= 1
    
    return years_diff

def your_current_day_on_earth(start_date, end_date=None):
    if end_date == None:
        end_date = get_todays_date()

    # Convert the string dates to datetime objects
    d1 = datetime.strptime(start_date, "%Y-%m-%d")
    d2 = datetime.strptime(end_date, "%Y-%m-%d")
    
    # Calculate the difference between the two dates
    delta = abs(d2 - d1).days + 1

    # Return the difference in days
    return delta


def calculate_unbirthday(start_date, end_date=None):
    if end_date == None:
        end_date = get_todays_date()

    # How to calculate unbirthdays

    # 1. Take your current day on earth
    # 2. Subtract 1 day because the day you were born counts as a birthday
    # 3. Subtract the amount of birthdays you had

    birthdays = years_passed(start_date, end_date)


    # Take your current day on earth
    unbirthday = your_current_day_on_earth(start_date, end_date)

    # Subtract 1 day because the day you were born counts as a birthday
    unbirthday = unbirthday - 1

    # Subtract the amount of birthdays you had
    unbirthday = unbirthday - birthdays


    # There you go! Your current unbirthday!
    return unbirthday


def count_back_past_date(days, input_date):
    # Convert the input date string to a datetime object
    days = days - 1
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(input_date, date_format)
    
    # Calculate the new date by subtracting the days
    new_date = current_date - timedelta(days=days)
    
    # Convert the new date back to a string and return it
    return new_date.strftime(date_format)

def reverse_unbirthday(unbirthday, current_date=None):
    if current_date == None:
        current_date = get_todays_date()
    
    # Assume how many birthdays has passed based on the amount of unbirthdays
    birthdays = math.floor(unbirthday / 364)

    # To reverse the unbirthday:
    # Add one because the day you were born
    reverse_your_current_day_on_earth = unbirthday + 1

    # Add the amount of birthdays
    reverse_your_current_day_on_earth = reverse_your_current_day_on_earth + birthdays

    # Count backwards the amount of days
    reverse_unbirthday = count_back_past_date(reverse_your_current_day_on_earth, current_date)

    return reverse_unbirthday

# Format YYYY-MM-DD