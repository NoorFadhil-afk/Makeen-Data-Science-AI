balance = 30000
years = 6
rate = 0.05
for i in range(1,years+1):
    balance = balance + (balance * rate)
    print(i , balance)