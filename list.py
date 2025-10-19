cloorslist = ["blue", "white", "red","green", ]
num = [1,2,3,4]
print(len(cloorslist))

################
name = "Ali"
trainessInAi = ["Ahmed", "Noor"]
n = len(trainessInAi)

for i in range(n):
    print(i, trainessInAi[i])
#######################
##using for loop to finding max numbers
numbers = [2,4,-2,20,4]
max = numbers[0]
for i in numbers:
    if max < i:
       max = i
print(max)
#######
numbers = [3,2,5,6]
for i in range(len(numbers)):
       if numbers [i] % 2 == 0:
        print(numbers[i], "the no is even")
       else:
        print(numbers[i], "the no is odd")
###########
numbers = []  
newNo = 0
while True:
    newNo = (input("Enter element or q to stop: "))
    if newNo == "q" :
        break
    if newNo.isdigit():
        newNo = int(newNo)
        numbers.append((newNo))
    else:
        numbers.append((newNo))
print("The list of numbers is: ",numbers)

##########
newList = ["ali", 2, "2"]
newList.insert(2, "4")
print(newList)
#########
friends = ["Harry","Bob","Cari","Emily"]
if "Emily" in friends:
    n = friends.index("Emily")
    print(n)
###
friends = ["Harry","Bob","Cari","Emily"]
if "Emily" in friends:
    n = friends.pop(2)
    print(n)   
####
oldFriends = ["Harry","Bob","Cari","Emily"]
newFriends = ["Emily","Ali"]
allFrinds = oldFriends  + newFriends
print(allFriends)
##replication
list[1,2,3]
newList = list * 100
print(newList)
##max min
list[1,2,3]
print(max(list))
