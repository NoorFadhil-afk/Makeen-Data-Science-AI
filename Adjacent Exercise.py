previous = None
n = 3 

for i in range(n):
    current = int(input("Enter value" + str(i + 1) + " = "))
    if previous is not None and current == previous:
       print("The numbers are same")
    previous = current

