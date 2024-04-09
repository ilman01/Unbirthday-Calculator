# Unbirthday (Calculator)

## Introduction

Unbirthday is a Python module that provides functions to calculate and manage "unbirthdays," which are days celebrated as not being a person's birthday. This project is a tribute to the show *Alice's Wonderland Bakery (2022-2024)*.

## Inspiration

Unbirthday is a Python module that pays tribute to the whimsical concept of "unbirthdays" introduced in the show Alice's Wonderland Bakery. In the whimsical world of Wonderland, birthdays aren't the only occasions worth celebrating. The idea of celebrating unbirthdays - every day that is not your birthday - adds a delightful twist to the traditional notion of birthdays.

In Alice's Wonderland Bakery, the characters celebrate unbirthdays as a way to embrace the joy of everyday life. This concept resonates with the spirit of curiosity, playfulness, and appreciation for the little moments that make life special. Inspired by this imaginative celebration, the Unbirthday project aims to bring a touch of Wonderland magic to the realm of programming.

By offering functions to calculate and manage unbirthdays, this project invites users to explore the whimsy of unbirthday celebrations in their own programming adventures. Whether you're curious about how many unbirthdays have passed since a certain date or eager to find out when your next unbirthday will be, the Unbirthday module adds a playful twist to date calculations.

Join us in celebrating the spirit of Wonderland by incorporating a bit of unbirthday magic into your Python projects. Let's all savor the joy of everyday celebrations and the wonder of unexpected surprises. After all, as the Hatter famously said, "A very merry unbirthday to you!"

## Installation

You can install the `unbirthday` module using pip:

```bash
pip install unbirthday
```

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

## Discord NotSoBot Version

```python
.code python
####||
G=print
C='%Y-%m-%d'
A=None
from datetime import datetime as B,timedelta as D
import math
def H(n):
    A=n
    if 10<=A%100<=20:B='th'
    else:B={1:'st',2:'nd',3:'rd'}.get(A%10,'th')
    return str(A)+B
def E():return B.today().strftime(C)
def F(y):A=y;return A%4==0 and(A%100!=0 or A%400==0)
def I(s,e=A):
    B=e
    if B==A:B=E()
    H,C,D=map(int,s.split('-'));I,J,K=map(int,B.split('-'));G=I-H
    if(J,K)<(C,D):G-=1
    elif(J,K)==(C,D):
        if F(H)and C==2 and D==29:
            if not F(I):G-=1
    return G
def J(s,e=A):
    D=e
    if D==A:D=E()
    F=B.strptime(s,C);G=B.strptime(D,C);H=abs(G-F).days+1;return H
def K(s,e=A):
    D=s;C=e
    if C==A:C=E()
    F=I(D,C);B=J(D,C);B=B-1;B=B-F;return B
def L(a,e):
    E=a;A=e;A=B.strptime(A,C);E=E-1;G=0
    while E>=365:
        if F(A.year-1):A=A-D(days=366);E-=366
        else:A=A-D(days=365);E-=365
        E+=1;G+=1
    return G
def M(d,i):A=d;A=A-1;E=C;F=B.strptime(i,E);G=F-D(days=A);return G.strftime(E)
def N(u,e=A):
    D=u;B=e
    if B==A:B=E()
    F=L(D,B);C=D+1;C=C+F;G=M(C,B);return G
def O(a,s):
    E=a;A=s;A=B.strptime(A,C);E=E-1;G=0
    while E>=365:
        if F(A.year+1):A=A+D(days=366);E-=366
        else:A=A+D(days=365);E-=365
        E+=1;G+=1
    return G
def P(d,i):A=d;A=A-1;E=C;F=B.strptime(i,E);G=F+D(days=A);return G.strftime(E)
def Q(u,s):C=s;B=u;D=O(B,C);A=B+1;A=A+D;E=P(A,C);return E
def R(s,e,u):
    D=u;C=e;B=s
    if B!=A and C!=A:G(f"{H(K(B,C))} Unbirthday")
    elif B!=A and D!=A:G(f"End Date: {Q(D,B)}")
    elif C!=A and D!=A:G(f"Start Date: {N(D,C)}")
    else:raise Exception('Invalid Parameters')
####||

# Unbirthday Calculator (Powered by NotSoBot)

### Date Format YYYY-MM-DD    
### Input two arguments, put None for the argument you want to search.  

start_date = None
end_date = "2022-10-07"
unbirthdays = 3047

R(start_date, end_date, unbirthdays)
```

This is if you want to use NotSoBot's `.code` command to run the code.

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