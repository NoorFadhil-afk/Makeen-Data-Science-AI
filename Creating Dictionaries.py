#Dictionary
myFriend = {"myfriend1" : 999999, "Noor" :97476}
print(myFriend)



###use for loop

myFriends = {"myfriend1" : 999999, "Noor" :97476 , "muna" : 7656}
for i in myFriends:
       print(i, myFriends[i])
    
##get
myFriends = {"Muna2":999999,"Noor":98876}
munaNo = myFriends.get("Muna",'0000')
print(munaNo)
myFriends["Amira"] =98665

###To add
myFriends = {}
for i in range(1):
    newFriend = input("Enter your new friend name: ")
    friendNo = input("Enter your new friend's number: ")
    myFriends[newFriend] = friendNo
    
print(myFriends)


#Tuples to print keys and values
myFriends = {"Noor":1111,"ali":2222}
for i in myFriends.items():
    print(i)
    
###
myStudent = {"Noor":99, "Ali":70,"Nada":98}    
print(max(myStudent.values()))

##
myStudent = {"Noor":99, "Ali":70,"Nada":98}
max = max(myStudent.values())
for i in myStudent.items():
    if i[1] == max:
        print(i)
        
### use .pop to remove
myStudent = {"Noor":99, "Ali":70,"Nada":98}
myStudent.pop("Ali")
print(myStudent)

###To sorted
myStudent = {"Noor":99, "Ali":70,"Nada":98}

for k in sorted(myStudent):
    print("%-10s %d " %(k,myStudent[k]))
    
###to print indix  immutable
t3 = (200, "A", [2,10,5], 3.2)
lis0 = t3[2][1]   #1 is index in [2,10,5] 
print (lis0)

## to find index in index

myTuple = (200, "A", [2,10, 5,[1,4]], 3.2)
print(myTuple[2][3][1])

### to reversed order [::-1] use in tuple + list
myTuple = (200, "A", [2,10, 5,[1,4]], 3.2)
print(myTuple[::-1])


