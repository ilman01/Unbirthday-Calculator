from unbirthday import add_ordinal_indicator, get_todays_date, years_passed, your_current_day_on_earth, calculate_unbirthday

your_birthdate = "2006-01-02"

print(f"Today is {get_todays_date()}")
print(f"This is your {add_ordinal_indicator(your_current_day_on_earth(your_birthdate))} day on earth")
print(f"You've had {years_passed(your_birthdate) + 1} birthdays (including the day you were born)")
print(f"So, this is your {add_ordinal_indicator(calculate_unbirthday(your_birthdate))} unbirthday!")