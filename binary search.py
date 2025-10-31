numbers = [3,5,8,12,15,20,25]
target = int(input("Enter the number : "))
low = 0
high = len(numbers) - 1
found = False
while low <= high :
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index :", mid)
        break
    elif numbers[mid] < target :
        low = mid + 1
    else :
        high = mid - 1
else:
    print("Not found")