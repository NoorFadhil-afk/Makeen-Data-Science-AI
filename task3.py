#Use Boolean operators (and, or, not)
username = input("Enter username: ")
password = input("Enter password: ")
if (username == "admin" and password == "12345")or (username == "Admin" and not password == "54321"):
    print("Access granted")
else:
    print("Access denied")

