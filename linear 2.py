#linear search2
limit = 100
pos = 0
values = [2, 3, 1, 200, 2]
found = False
while pos < len(values) and not found :
     if values[pos] > limit :
         found = True
     else :
         pos = pos + 1
if found :
     print("Found at position:", pos)
else :
     print("Not found")
