#function
def cubeVolume(length):
    volume = length ** 3
    return volume
l= float(input("Enter the length of the cubeVolume:"))
cubeVolume=cubeVolume(l)
print(cubeVolume)
#######
import math
def factorial(n):
    return(math.factorial(n))
n = int(input("Enter the factorial num: "))
num = 5


#######
def factorial(n):
    result = 1
    if n == 0:
        return 1
    while n >= 1:
        result = result * n
        n = n-1
    return result
print(factorial(5))








