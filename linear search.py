#linear search
numbers = [1, 16, 9, 4]
target = int(input("Enter the number: "))
if target in numbers:
    print("The element is in the list"+ str(numbers.index(target)))
else:
    print("The element is not in the list")
             