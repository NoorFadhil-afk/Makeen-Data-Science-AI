#Task for using if + nested if
from datetime import datetime
firstTime = datetime.strptime(input("Enter the first time: "), "%H:%M")
secondTime = datetime.strptime(input("Enter the second time: "), "%H:%M")
if firstTime > secondTime:
    print("The first time comes first")
elif firstTime < secondTime:
    print("The second time comes before")
else:
    print("Both times same as")