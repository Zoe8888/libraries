# Exercise 1
class Bus(object):
    counter = 0

    def __init__(self, seats, color, bus_driver):
        self.seats = seats
        self.color = color
        self.bus_driver = bus_driver
        Bus.counter += 1

    def change_color(self, recolor):
        self.color = recolor

# Today's date
from datetime import datetime, timedelta, time
dt = datetime(2021, 5, 18)
answer = dt + timedelta (days=7)
x = datetime.now
print(answer)
print(x)

# Print 10 dates 14 days apart
for x in range(10):
    print(x + 1, "-", end="     ")
    print(dt.strftime("%Y/ %m/ %d - %H:%M"))
    dt = dt + timedelta(days=7)

# Exercise 2
year_born = int(input("Enter year born :"))
month_born = int(input("Enter month born :"))
day_born = int(input("Enter day born :"))

current_year = int(datetime.today().strftime("%Y"))
current_month = int(datetime.today().strftime("%m"))
current_day = int(datetime.today().strftime("%d"))

age = current_year - year_born - 1

if month_born < current_month:
    age += 1
elif month_born == current_month:
    if day_born <= current_day:
        age += 1

print("")
print("You are {} years old".format(age))


