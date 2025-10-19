balance = 10000    # A global variable
def withdraw(amount) :
    # This function intends to access the 
    # global ‘balance’ variable and deduct the amount
    global balance 
    if balance >= amount :
        balance = balance - amount

withdraw(350)
print('balance after withdraw = ', balance)

def deposit(amount):
    global balance
    balance += amount # balance = balance + amount
def check():
    global balance
    return balance
deposit(500)
withdraw(200)
print(check())
print('balance after deposit and withdraw = ', balance)