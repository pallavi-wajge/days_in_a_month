def is_leap(year): 

  if year % 4 == 0: 

    if year % 100 == 0: 

      if year % 400 == 0: 

        print("Leap year") 

        return True 

      else: 

        print("Not leap year") 

    else: 

      print("Leap year") 

      return True 

  else: 

    print("Not leap year") 

def days_in_month(year, month): 

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

  if is_leap(year) is True and month == 2: 

    return 29 

    """ 

    Apple pie apple 

    """ 

    #if year is leap feb 29 days 

  else: 

    return month_days[month - 1] 


year = int(input("Enter a year: ")) # Enter a year 

month = int(input("Enter a month: ")) # Enter a month 

days = days_in_month(year, month) 

print(days) 

  

 
