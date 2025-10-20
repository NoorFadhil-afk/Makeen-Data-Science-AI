#sort numbers use for loop
numbers = [1, 16, 9, 4]
while True:
    value = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            x = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = x
            value = True
    if not value:
         break
print(numbers)
        
