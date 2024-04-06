from unbirthday import add_ordinal_indicator, get_todays_date, years_passed, your_current_day_on_earth, calculate_unbirthday, find_startdate_unbirthday, find_enddate_unbirthday

your_birthdate = "2006-01-02"

print(f"Today is {get_todays_date()}")
print(f"This is your {add_ordinal_indicator(your_current_day_on_earth(your_birthdate))} day on earth")
print(f"You've had {years_passed(your_birthdate) + 1} birthdays (including the day you were born)")
print(f"So, this is your {add_ordinal_indicator(calculate_unbirthday(your_birthdate))} unbirthday!")



# Dynamic function example
'''
def dynamic_unbirthday_function(start_date, end_date, unbirthdays):
    if start_date != None and end_date != None:
        print(f"{add_ordinal_indicator(calculate_unbirthday(start_date, end_date))} Unbirthday")
    elif start_date != None and unbirthdays != None:
        print(f"End Date: {find_enddate_unbirthday(unbirthdays, start_date)}")
    elif end_date != None and unbirthdays != None:
        print(f"Start Date: {find_startdate_unbirthday(unbirthdays, end_date)}")
    else:
        raise Exception("Invalid Parameters")



## Date Format YYYY-MM-DD    
## Input two arguments, put None for the argument you want to search.  

start_date = None
end_date = "2022-10-07"
unbirthdays = 3047

dynamic_unbirthday_function(start_date, end_date, unbirthdays)
'''