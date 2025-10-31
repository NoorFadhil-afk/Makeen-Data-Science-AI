#linear search
numbers = [2, 12, 5, 3, 20, 13]
target = int(input("Enter your target: "))
position = -1

for i in range(len(numbers)):
    if target == numbers[i]:
        position = i
   
    else:
        position = -1

    print(position)   
print("The target is on position: ", position)





    