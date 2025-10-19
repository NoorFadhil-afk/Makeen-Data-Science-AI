for i in range(4):
   for j in range(4 + 1):
        if j >= 4 - i:
           print("*",end="")
        else:
           print("","", end="")
   print()