print("Welcome to Age Calculator\nThis program calculates your age\nbased on your birth year and whatever year you desire.\n")
print("************************************")
import datetime
now = datetime.datetime.now()
print("Today's date is " + str(now.month + now.day))
print("")

bYear = int(input("Please enter your birth year and hit enter >> "))

def ageCalc():
    
    year = int(input("Please enter desired year and hit enter >> "))
    age = year - bYear

    print ('')

    if year < now.year:
        print('Your age in ' + str(year) + ' was ' + str(age))
    elif year > now.year:
        print('Your age in ' + str(year) + ' will be ' + str(age))
    else:
        print('Your age in ' + str(year) + ' is ' + str(age))
    print('')

while True:  
    ageCalc()
