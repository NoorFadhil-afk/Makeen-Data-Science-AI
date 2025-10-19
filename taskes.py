#Collect Positive and Negative Numbers
positive = []
negative = []
while True:
    inputInteger = input("Enter integer")
    if inputInteger == "q":
        break
    else:
        inputInteger = int(inputInteger)
        if inputInteger >= 0:
            positive.append(inputInteger)
        else:
             negative.append(inputInteger)
print(positive, negative)

#
positive = []
negative = []
while True:
    inputInteger = input("Enter integer")
    if inputInteger == "q":
        break
   
        if inputInteger.isdigit:
           inputInteger = int(inputInteger)
           positive.append(inputInteger)
        
        elif inputInteger[0] == '-'and inputInteger[1:].isdigit():
            inputInteger = int(inputInteger[1:])*-1
            negative.append(inputInteger)
print(positive, negative)
## Sum of Numbers
numbers = []
while True:
   inputInteger = input("Enter a number or done to stop: ")
   if inputInteger == 'done':  
       break
   if inputInteger.isdigit():
      numbers.append(int(inputInteger))

   elif inputInteger[0] == '-':
         inputInteger = (int(inputInteger[1:])*-1)
         numbers.append(inputInteger)
        
   
print(sum(numbers))
    
    





