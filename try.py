try:
    infile=open("story.txt")
    avg = 10/0
except IOError:
    print("The file does not exist")
except Exception as expectObj:
    print("Sorry you got error!",str(expectObj))

