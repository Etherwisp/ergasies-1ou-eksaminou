import collections
import math

charList =[]
ammountOfChars = 0

#read file char by char and append to list odd ascii chars
def OddNumberAscii(file,list):
    while 1:
        char = file.read(1)
        if not char:
            break
        char = ord(char)
        if char % 2 == 1 :
            list.append(chr(char))


def TakeInput():
    file = input("enter file directory : ")
    try:
        fileThing = open(file ,"r")
        return file
    except:
        print("such file does not exist , make sure youre writting the directory correctly")
        TakeInput()

#-----------------Main-----------------------------------------------------------

#for some reason if i do return filething instead of file i get a weird
#error so i decided if it works inside the function i take the filename and do it outside the func
filename = TakeInput()
fileThing = open(filename ,"r")
OddNumberAscii(fileThing,charList)
#take list , find the % of the appearance of every char and print
ammountOfChars = len(charList)
charList = collections.Counter(charList)
for key,value in charList.items():
    percentage = (value/ammountOfChars)*100
    percentage = math.ceil(percentage)
    print(key, ":", percentage*"*")
