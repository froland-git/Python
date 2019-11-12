#Все аргументы командной строки пересылаются в Python через массив sys.argv

import sys
import os

print ("Hello!")

print (sys.argv[1:])

x = len(sys.argv)
if x > 1:
    print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")


if x > 1:
    if sys.argv[1] == "/?":
        print("Help Requested")
        print("Usage of this program is: python.exe myfile.py argv1 argv2")
        print("Arguments entered: " + str(sys.argv[1:]))
else:
    print("Arguments NOT PROVIDED")

os.system("dir > test.txt")
#os.mkdir("my dir")
#sys.exit(2)
