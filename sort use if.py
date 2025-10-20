#sort numbers use for loop
num = [1, 16, 9, 4]
while True:
    value = False
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            x = num[i]
            num[i] = num[i + 1]
            num[i + 1] = x
            value = True
    if not value:
         break
print(num)
        
