#Caling Function
def main():
    result = cubVolume(2)
    return result
def cubVolume(sideLength):
    return sideLength ** 3
print(main())
###########
def main():
    sideLength = 2
    result = cubeVolume()
    return sideLength

def cubeVolume():
    sideLength = 6
    return sideLength ** 3
print(main())
###
def main(l):
    result = cubVolume(l)
    return result

def cubeVolume(sideLength):
    return sideLength * sideLength * sideLength

length = float(input("Enter the side length: "))
print(main(length))

