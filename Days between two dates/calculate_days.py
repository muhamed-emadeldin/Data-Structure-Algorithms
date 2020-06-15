#!/usr/bin/env python3
'''
Define a simple nextday procedure, that assumes every mont ha 30 days
'''
monthDict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# check leap year or ordinary year
def isLeapYear(year):
  if year % 4 != 0:
    return False
  elif year % 100 != 0:
    return True
  elif year % 400 != 0:
    return False
  else:
    return True
  
# Get days in month in ordinary year or leap year
def calculateMonth(year, month):
  if isLeapYear(year):
    monthDict[2] = 29
  else:
    monthDict[2] = 28

  daysInMonth =  monthDict[month]

  return daysInMonth


# Get next day between 2 dates
def nextDay(year, month, day):
  daysMonth = calculateMonth(year, month)

  if day < daysMonth:
    day +=1
    return year, month, day

  else:
    if month == 12:
      return year +1, 1, 1
    else:
      return year, month+1, 1 

  return year, month, day


# check data input is correct or no
def defenseProgramer(year1, month1, day1, year2, month2, day2):
  if year2 > year1:
    return True
  elif year2 == year1:
    if month2 > month1:
      return True
    elif month2 == month1:
      return day2 > day1
  
  return False



def daysBetweenDates(year1, month1, day1, year2, month2, day2):

  # defense function to check inputes
  assert (defenseProgramer(year1, month1, day1, year2, month2, day2)), "AssertionError"

  # initial basic variables
  days   = 0

  while defenseProgramer(year1, month1, day1, year2, month2, day2):
    # basic condation
    if year1 == year2 and month1 == month2 and day1 == day2:
      return 0
      
    year1, month1, day1  = nextDay(year1, month1, day1)
    days += 1
  return days

  


def test():
  
  test_cases = [((2012,1,1,2012,2,28), 58), 
                ((2012,1,1,2012,3,1), 60),
                ((2011,6,30,2012,6,30), 366),
                ((2011,1,1, 2012,8,8), 585 ),
                ((1900,1,1,1999,12,31), 36523),
                ((2013,1,1,1999,12,31), "AssertionError")]
  
  testYears  = [
                (2020, True),
                (2019, False),
                (2018, False),
                (2017, False),
                (2016, True),
                (2012, True),
                (2010, False),
               ]

  testDaysMonth = [
                ((2020, 5), 31)
               ]

  for (arg, answer) in testDaysMonth:
    result = calculateMonth(*arg)
    if result == answer:
      print("Test month case passed!")
    else:
      print("Test with data:", arg, "failed")
  
  for arg,answer in testYears:
    result = isLeapYear(arg)
    if result == answer:
      print("Test case passed!")
    else:
      print("Test with data:", arg, "failed")
  
  for (args, answer) in test_cases:
      try:
          result = daysBetweenDates(*args)
          if result == answer and answer != "AssertionError":
              print("Test case year passed!")
          else:
              print("Test with data:", args, "failed")
  
      except AssertionError:
          if answer == "AssertionError":
              print( "Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
          else:
              print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))          
test()