from datetime import datetime

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

# Format YYYY-MM-DD