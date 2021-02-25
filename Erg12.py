#10 lines and then edits the new file and empties the list and adds the next 10 lines
#incase the file is so big it doesnt fit in RAM
def reverseAscii(character):
    asciiNumber = ord(character)
    asciiNumber = 128 - asciiNumber
    character = chr(asciiNumber)
    return character


def takeInput():
    file = input("enter file directory : ")
    try:
        fileThing = open(file ,"r")
        return file
    except:
        print("such file does not exist , make sure youre writting the directory correctly")
        takeInput()



filename = takeInput() #for some reason if i do return filething instead of file i get a weird
#error so i decided if it works inside the function i take the filename and do it outside the func
fileThing = open(filename ,"r")
inverseFile = open("inversefile.txt", "w")
lineList = []
for x in fileThing:
    lineList.append(list(x))
lineList.reverse()
for x in lineList:
    x.reverse()
    for y in x:
        inverseFile.write(reverseAscii(y))
inverseFile.close()
fileThing.close()
inversedFile = open("inversefile.txt", "r")
print(inversedFile.read())
inversedFile.close()
#so far we have just inversed the file lines and characters
#now u gotta change the characters

# asciiNumber = ord("k")
# print(asciiNumber ,"is k")
# asciiNumber = 128 - asciiNumber
# print(asciiNumber,"is ???")
# print(chr(21))
# print(ord('§'))
