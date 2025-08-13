#activity 1
from datetime import date , time , datetime

today = date.today()
now = datetime.now()
print("today's date is", today)
print("\n Current date and time is", now)

print("\n Date components", today.year, today.month, today.day)

#activity 2
import random
import time

def getRandomDate(startDate, endDate):
    print("Print Random date between ", startDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate
    
print("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))

#activity 3
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475
    
def rental_car_cost(days):
    if days >= 7:
        return 40*days - 50
    elif days >=3:
        return 40*days - 50
    else:
        return 40*days
    
def trip_cost(city, days, spenting_money):
    return rental_car_cost(days)+ hotel_cost(days)+ plane_ride_cost(city)+ spenting_money

print("cost of car rental", rental_car_cost(5))

print("cost of plane ride", plane_ride_cost("los angeles"))

print("cost of hotel room", hotel_cost(7))

print("total cost of the trip", trip_cost("los angeles", 7,500))

print(trip_cost("Tampa", 6,500))



    