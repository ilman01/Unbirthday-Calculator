# Unbirthday (Calculator)

## Introduction

Unbirthday is a Python module that provides functions to calculate and manage "unbirthdays," which are days celebrated as not being a person's birthday. This project is a tribute to the show *Alice's Wonderland Bakery (2022-2024)*.

## Inspiration

Unbirthday is a Python module that pays tribute to the whimsical concept of "unbirthdays" introduced in the show Alice's Wonderland Bakery. In the whimsical world of Wonderland, birthdays aren't the only occasions worth celebrating. The idea of celebrating unbirthdays - every day that is not your birthday - adds a delightful twist to the traditional notion of birthdays.

In Alice's Wonderland Bakery, the characters celebrate unbirthdays as a way to embrace the joy of everyday life. This concept resonates with the spirit of curiosity, playfulness, and appreciation for the little moments that make life special. Inspired by this imaginative celebration, the Unbirthday project aims to bring a touch of Wonderland magic to the realm of programming.

By offering functions to calculate and manage unbirthdays, this project invites users to explore the whimsy of unbirthday celebrations in their own programming adventures. Whether you're curious about how many unbirthdays have passed since a certain date or eager to find out when your next unbirthday will be, the Unbirthday module adds a playful twist to date calculations.

Join us in celebrating the spirit of Wonderland by incorporating a bit of unbirthday magic into your Python projects. Let's all savor the joy of everyday celebrations and the wonder of unexpected surprises. After all, as the Hatter famously said, "A very merry unbirthday to you!"

## Installation

To use Unbirthday, download the `unbirthday.py` file and place it in your project directory.

## Usage

You can import functions from the `unbirthday` module using the following syntax:

```python
from unbirthday import add_ordinal_indicator, get_todays_date, years_passed, your_current_day_on_earth, calculate_unbirthday, find_startdate_unbirthday, find_enddate_unbirthday
```

## Functions

### add_ordinal_indicator(num)

Adds the ordinal indicator (e.g., "st", "nd", "rd", "th") to a given number.

Parameters:
- `num`: The number to which the ordinal indicator will be added.

Returns:
- A string representation of the number with the ordinal indicator.

### get_todays_date()

Gets the current date in the format "YYYY-MM-DD".

Returns:
- A string representing today's date in the format "YYYY-MM-DD".

### years_passed(start_date, end_date)

Calculates the number of years passed between two dates.

Parameters:
- `start_date`: The start date in the format "YYYY-MM-DD".
- `end_date` (optional): The end date in the format "YYYY-MM-DD". If not provided, the current date is used.

Returns:
- The number of years passed between the start and end dates.

### your_current_day_on_earth(start_date, end_date)

Calculates the number of days between two dates.

Parameters:
- `start_date`: The start date in the format "YYYY-MM-DD".
- `end_date` (optional): The end date in the format "YYYY-MM-DD". If not provided, the current date is used.

Returns:
- The number of days between the start and end dates.

### calculate_unbirthday(start_date, end_date)

Calculates the current unbirthday based on the provided start and end dates.

Parameters:
- `start_date`: The start date (birth date) in the format "YYYY-MM-DD".
- `end_date` (optional): The end date (current date) in the format "YYYY-MM-DD". If not provided, the current date is used.

Returns:
- The number of unbirthday days.

### find_startdate_unbirthday(unbirthday, end_date)

Calculates the start date (birth date) based on the provided unbirthday and end dates.

Parameters:
- `unbirthday`: The number of unbirthday days.
- `end_date` (optional): The end date (current date) in the format "YYYY-MM-DD". If not provided, the current date is used.

Returns:
- The start date (birth date) in the format "YYYY-MM-DD".

### find_enddate_unbirthday(unbirthday, start_date)

Calculates the end date (current date) based on the provided unbirthday and start dates.

Parameters:
- `unbirthday`: The number of unbirthday days.
- `start_date`: The start date (birth date) in the format "YYYY-MM-DD".

Returns:
- The end date (current date) in the format "YYYY-MM-DD".

## Example

```python
from unbirthday import calculate_unbirthday, add_ordinal_indicator

# Calculate current unbirthday
start_date = '2014-05-27'
end_date = '2022-10-07'
unbirthday = calculate_unbirthday(start_date, end_date)
print(f"Current Unbirthday: {add_ordinal_indicator(unbirthday)} Unbirthday")
```

This will output the number of days representing the current unbirthday.

## Thanks

**To the creators of the show *Alice's Wonderland Bakery*:**
- Chelsea Beyl

**To the songwriters and song producers:**
- John Kavanaugh
- Danny Jacob

**To all the voice actors/actresses and the rest of the crew of the show.**

**To the community:**
- [**Lilli**](https://www.youtube.com/@LillisWonderland) and (formerly known as)  [**Rosa**](https://www.youtube.com/@notjennaortega_090) who brought the community together.
- **Cj Uy**, the voice actor of Hattie (one of the characters in Alice's Wonderland Bakery), for also being a part of the community.
- **Honorable Mentions:**
  - [**Incubo**](https://github.com/OfficialIncubo)
  - **Systic**
  - [**Clay**](https://www.youtube.com/@DaClayCrew)
  - [**Ghosty**](https://discord.com/users/1056973970534051840)
  - [**Sam**](https://www.youtube.com/@ENHAPPIFY)

**And to all of the Wonderland community**

Thank you all for being part of this wonderful community!