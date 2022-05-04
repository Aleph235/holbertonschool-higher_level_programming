#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_ints = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string)
    result = 0
    if roman_string is None:
        return 0
    for i in range(length):
        if roman_string[i] in roman_ints:
            result += roman_ints.get(roman_string[i])
    for i in range(length - 1):
        if roman_string[i] == 'I' and (roman_string[i+1] == 'V'
           or roman_string[i+1] == 'X'):

            result -= 2*roman_ints.get(roman_string[i])
        elif roman_string[i] == 'X' and (roman_string[i+1] == 'L'
                                         or roman_string[i+1] == 'C'):

            result -= 2*roman_ints.get(roman_string[i])
        elif roman_string[i] == 'C' and (roman_string[i+1] == 'D'
                                         or roman_string[i+1] == 'M'):

            result -= 2*roman_ints.get(roman_string[i])
    return(result)
