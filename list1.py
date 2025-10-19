numbers = []  
newNo = 0
while True:
    newNo = (input("Enter element or q to stop: "))
    if newNo == "q" :
        break
    if newNo.lstrip("-").isdigit():
        newNo = int(newNo)
        numbers.append((newNo))
    else:
        numbers.append((newNo))
print("The list of numbers is: ",numbers)

#######################################################################################
lis = []
while True:
    inputStr = input("Enter an element or q to  exit/stop: ")
    if inputStr.isdigit():
        lis.append(int(inputStr))
    elif inputStr[0] == '-' and inputStr[1:].isdigit():
        lis.append(int(inputStr[1:]) * -1)
    elif inputStr== "q":
    
      break
    else:   
       lis.append(inputStr)
print(lis)

















