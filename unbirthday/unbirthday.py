from datetime import datetime, timedelta
import math

def add_ordinal_indicator(num):
    '''Adds the ordinal indicator (e.g., "st", "nd", "rd", "th") to a given number.'''
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return str(num) + suffix

def get_todays_date():
    '''Gets the current date in the format "YYYY-MM-DD".'''
    return datetime.today().strftime('%Y-%m-%d')

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def years_passed(start_date, end_date=None):
    '''Calculates the number of years passed between two dates.'''
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
    '''Calculates the number of days between two dates.'''
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
    '''Calculates the current unbirthday based on the provided start and end dates.'''
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



def unbirthday_enddate_to_years(amount_of_days, end_date):
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    amount_of_days = amount_of_days - 1
    years_back = 0

    while amount_of_days >= 365:
        if is_leap_year(end_date.year - 1):
            # If the previous year was a leap year, subtract 366 days
            end_date = end_date - timedelta(days=366)
            amount_of_days -= 366
        else:
            # Otherwise, subtract 365 days
            end_date = end_date - timedelta(days=365)
            amount_of_days -= 365
        
        # Add one day to the remaining amount of days
        amount_of_days += 1
        # Increment the count of years gone back
        years_back += 1

    return years_back

def count_back_past_date(days, input_date):
    # Convert the input date string to a datetime object
    days = days - 1
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(input_date, date_format)
    
    # Calculate the new date by subtracting the days
    new_date = current_date - timedelta(days=days)
    
    # Convert the new date back to a string and return it
    return new_date.strftime(date_format)

def find_startdate_unbirthday(unbirthday, end_date=None):
    '''Calculates the start date (birth date) based on the provided unbirthday and end dates.'''
    if end_date == None:
        end_date = get_todays_date()
    
    # Assume how many birthdays has passed based on the amount of unbirthdays
    birthdays = unbirthday_enddate_to_years(unbirthday, end_date)

    # To reverse the unbirthday:
    # Add one because the day you were born
    reverse_your_current_day_on_earth = unbirthday + 1

    # Add the amount of birthdays
    reverse_your_current_day_on_earth = reverse_your_current_day_on_earth + birthdays

    # Count backwards the amount of days
    reverse_unbirthday = count_back_past_date(reverse_your_current_day_on_earth, end_date)

    return reverse_unbirthday



def unbirthday_startdate_to_years(amount_of_days, start_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    amount_of_days = amount_of_days - 1
    years_forward = 0

    while amount_of_days >= 365:
        if is_leap_year(start_date.year + 1):
            # If the current year is a leap year, add 366 days
            start_date = start_date + timedelta(days=366)
            amount_of_days -= 366
        else:
            # Otherwise, add 365 days
            start_date = start_date + timedelta(days=365)
            amount_of_days -= 365
        
        # Add one day to the remaining amount of days
        amount_of_days += 1
        # Increment the count of years gone forward
        years_forward += 1

    return years_forward

def count_forward_future_date(days, input_date):
    days = days - 1

    # Convert the input date string to a datetime object
    date_format = "%Y-%m-%d"
    current_date = datetime.strptime(input_date, date_format)
    
    # Calculate the new date by adding the days
    new_date = current_date + timedelta(days=days)
    
    # Convert the new date back to a string and return it
    return new_date.strftime(date_format)

def find_enddate_unbirthday(unbirthday, start_date):
    '''Calculates the end date (current date) based on the provided unbirthday and start dates.'''
    # Assume how many birthdays will pass based on the amount of unbirthdays
    birthdays = unbirthday_startdate_to_years(unbirthday, start_date)

    # To reverse the unbirthday:
    # Add one because the day you were born
    reverse_your_current_day_on_earth = unbirthday + 1

    # Add the amount of birthdays
    reverse_your_current_day_on_earth = reverse_your_current_day_on_earth + birthdays

    # Count forwards the amount of days
    reverse_unbirthday = count_forward_future_date(reverse_your_current_day_on_earth, start_date)

    return reverse_unbirthday

# Format YYYY-MM-DD