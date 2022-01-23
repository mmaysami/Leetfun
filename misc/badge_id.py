"""
Validate Employee Badge ID [Shopify]
An organization issues ID cards to its employees with unique ID codes.
The ID code for an employee named Jigarius Caesar looks as follows: CAJI202002196.
Here’s how the ID code is derived:

    CA: First 2 characters of the employee’s last name.
    JI: First 2 characters of the employee’s first name.
    2020: Full year of joining.
    02: 2 digit representation of the month of joining.
    19: Indicates that this is the 19th employee who joined in Feb 2020.
        This will have at least 2 digits, starting with 01, 02, and so on.
    6: The last digit is a verification digit which is computed as follows:
        Take the numeric part of the ID code (without the verification digit).
        Sum all digits in odd positions. Say this is O.
        Sum all digits in even positions. Say this is E.
        Difference between O & E. Say this is V.
        If V is negative, ignore the sign, e.g., -6 is treated as 6. Say this is V.
        If V is greater than 9, divide it by 10 and take the reminder. Say this is V.
        V is the verification code.

For the above ID card, here’s how you‘ll test the verification digit.
    CAJI202002196 # ID code
    202002196 # Numeric part
    20200219 # Ignoring verification digit
    2 + 2 + 0 + 1 = 5 # Sum of odd position digits, i.e. O
    0 + 0 + 2 + 9 = 11 # Sum of even position digits, i.e. E
    5 - 11 = -6 # V = O - E
    6 # Verification digit, ignoring sign

An ID code is considered valid if:
    The first 4 characters of the card are correct, i.e. CAJI.
    The verification digit is correct, i.e. 6.

Problem:
    Write a command-line program in your preferred coding language that:
        Allows the user to enter their First name, Last name and ID code.
        Prints PASS if the ID code seems valid.
        Prints INVESTIGATE otherwise.
    Write relevant tests.
        It is not necessary to use a testing library.
        You can use your custom implementation of tests.
"""

import re
from datetime import datetime as dt

def validate_id(first, last, code):
    pattern_name =  r'[a-zA-Z]{2}.*'
    pattern_code = r'^(?P<last>[a-zA-Z]{2})(?P<first>[a-zA-Z]{2})(?P<number>\d{9})$'

    check_first = re.match(pattern_name, first, re.I)
    check_last = re.match(pattern_name, last, re.I)
    check_code = re.match(pattern_code, code, re.I)

    if check_first is None:
        raise AssertionError('First name needs to start with at least two alphabetical characters. ({})'.format(first))

    if check_last is None:
        raise AssertionError('Last name needs to start with at least two alphabetical characters. ({})'.format(last))

    if check_code is None:
        raise AssertionError('Code ID needs to be in format of "AABByyyymm###". ({})'.format(code))

    # Verify First Name
    if check_code.groupdict()['first'].lower() != first.lower()[0:2]:
        return 'INVESTIGATE', 'First Name'

    # Verify Last Name
    if check_code.groupdict()['last'].lower() != last.lower()[0:2]:
        return 'INVESTIGATE', 'Last Name'

    # Verify Hire Date (Valid Date and Before Now)
    try:
        hire_date = dt.strptime(check_code.groupdict()['number'][0:6],'%Y%m')
    except ValueError:
        return 'INVESTIGATE', 'Invalid Date'
    else:
        if hire_date > dt.now():
            return 'INVESTIGATE', 'Future Hire Date'

    # Validate Verification Code
    evens = [int(e) for e in list(check_code.groupdict()['number'][0:-1:2])]
    odds = [int(e) for e in list(check_code.groupdict()['number'][1:-1:2])]
    verify = abs(sum(odds)-sum(evens))%10

    print(odds, evens, verify)
    if verify != check_code.groupdict()['number'][-1]:
        return 'INVESTIGATE', 'Verification Code'

    return 'PASS'

# ========================================================
# Edge Cases:
#   Names: A.J. C. (Short Name, Non Character)
#   Hire Date > Now
#   Hire Month not in (1,12)
#   Hire Rank == 0 ?
#   Verify Code

# first = input('Enter your first name?')
# last = input('Enter your last name?')
# code = input('Enter your ID Code?')
out = validate_id('Jina','Carl. Jr.', 'CAJI202002196')

print(out)