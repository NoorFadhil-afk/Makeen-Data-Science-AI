###Examples immutable be repeated 
t1 = ("a", "b", "c")
print(t1[::-1])
t2 = ("a", "b", "c")

t3 = t1 + t2
print(t3)
t3 = t3 * 4
print(t3)

for i in t3:
     print(i, end = " ")
     
######### nested
t = ((10,20,30),(1,2))

for i in range(len(t)):
    for j in range(len(t[i])):
        print(t[i][j])
        

        


    