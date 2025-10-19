# x % 2 ==0    #condition
x = int(input("Enter a number: "))
if x >= 0:
    print("The number is positive")
    if x % 2 == 0:
        print(" an even")
    else:
         print(" an odd")
else:
    print("The number is negative")
