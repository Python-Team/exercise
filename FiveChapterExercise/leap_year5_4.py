'''
Created on May 17, 2013

@author: user
'''

def leap_year():
    year = int(raw_input("please enter the year."))
    if year%4 == 0 and year%100 != 0:
        return "%s is leap year" %year
    else:
        if year%400 == 0:
            return "%s is leap year" %year
        else:
            return "%s is not leap year" %year
    
if __name__ == "__main__":
    print leap_year()