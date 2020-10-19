#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_vktran2.py (replace [Seneca_name] with your Seneca User name)
Author: Victor Tran
The python code in this file (a1_vktran2.py) is original work written by
"Victor Tran". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    Nested if statements test years if they are divisible by 4, 100, and 400 with no remainder
    if the year is divisible by 4 but not 100, or is divisible by 4, 100, and 400 then the function will be returned true
    if the year is not divisible by 4 or not divisible by 4, 100, and 400 then the function will return false
    '''
    if (obj % 4) == 0:
       if (obj % 100) == 0:
          if (obj % 400) == 0:
             status = True
          else:
             status = False
       else:
          status = True
    else:
       status = False
    return status

def sanitize(obj1,obj2):
    '''
    check if ALL characters in obj1 for characters in obj2 if all values are true then true will be returned
    if not, false will be returned
    '''
    results = str(filter(obj2, obj1)) 

    return results

def size_check(obj, intobj):
    '''
    If statement to check if the length of the collected data is equal to the expected length
    If it is equal reutrn true, if not return false
    '''
    length = len(obj)
    if length == intobj:
       status = True
    else:
       status = False

    return status

def range_check(obj1, obj2):
    '''
    Check if the given integer is in the tuple
    '''
    if obj1 in obj2:
       status = True
    else:
       status = False
    return status
    
def usage():    
    '''
    return the format of the script usage
    '''
    status = 'Usage: a1_vktran2.py YYYYMMDD | YYYY/MM/DD | YYYY-MM-DD | YYYY.MM.DD'
    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      usage()
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  
