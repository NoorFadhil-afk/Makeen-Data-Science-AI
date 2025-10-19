#Q1 Variable and input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name + ",you are", age, "years old.")

#Q2 
firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))
sum = firstnumber + secondnumber
print("The sum is", sum)

#Q3
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 > num2
print("Is the first number greater?", result)

#@4
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
if age >= 18 and nationality == "Omani":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
#Q5
num = float(input("Enter the number: "))
if num > 0:
    print("The number is positive.")
#Q6
num = int(input("Enter the number: "))
if num % 2 ==0:
    print("The number is even")
else:
   print("The number is odd")
#Q7
marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 70:
     print("Good")
elif marks >= 50:
     print("Pass")
else:
    print("Fail")
#Q8
age = int(input("Enter your age: "))
license_status = input("Do you have license? ").lower()
if age >=18:
    if license_status == "yes":
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
        print("You are too young to drive.")
#@9
num = 1
while num <= 5:
    print(num)
    num += 1
#Q10
num = int(input("Enter a number: "))
i = 1
while i <= num:
    if i % 2 == 0:
        print(i)
        i += 1
    