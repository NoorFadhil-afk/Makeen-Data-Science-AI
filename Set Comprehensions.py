###Set Operations
a = {1,2,3,4}
b = {2,4,6,8,6,6}
print('a= ',a)
print('b= ',b)
s1= a|b
print('Union: a|b =',s1)
s2= a&b
print('Intersection: a&b =',s2)
s3= a-b
print('Difference: a-b =',s3)
s4= a^b
print('aSymetric Diff: a^b =',s4)

###Set Comprehensions

L = [1,3,2,6,4]
ll = [x*10 for x in L]
print(ll)
ss = {x*10 for x in L}
print(ss )
L.extend([1,2])
print(L)
ss = {x*10 for x in L}
print(ss)
a = {1,2,3}
b = {x*2 for x in a|{4,5}}
print(b)
print(type(b))
