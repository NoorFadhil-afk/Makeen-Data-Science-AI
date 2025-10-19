correct_pin = "1234"

balance = 100.0

attempts = 0

max_attempts = 3

while attempts < max_attempts:

    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:

        print("Welcome!")

        break

    else:

        attempts += 1

        if attempts < max_attempts:

            print("Incorrect PIN. Try again.")

        else:

            print("Account locked. Try again later.")

            exit()

while True:

    print("1. Check Balance")

    print("2. Deposit Money")

    print("3. Withdraw Money")

    print("4. Exit")

    

    choice = input("Choose an option: ")

    

    if choice == "1":

        print("Your balance is", balance, "OMR")

    

    elif choice == "2":

        deposit = float(input("Enter deposit amount: "))

        if deposit > 0:

            balance += deposit

            print("Deposit successful! New balance is", balance, "OMR")

        else:

            print("Invalid amount. Try again.")

    

    elif choice == "3":

        withdraw = float(input("Enter withdraw amount: "))

        if withdraw > balance:

            print("Insufficient balance.")

        elif withdraw <= 0:

            print("Invalid amount. Try again.")

        else:

            balance -= withdraw

            print("Withdrawal successful! New balance is", balance, "OMR")

    

    elif choice == "4":

        print("Thank you for using our ATM. Goodbye!")

        break

    

    else:

        print("Invalid choice")

