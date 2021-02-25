dictionary   =    { "x" : 5,"y" : [ [ 1 , 2 ] , [ 3 , 4 ] ]}
def DictionaryDepth(dictionary):
    global Depth
    Depth = 0
    CurrentDepth = 0
    #checking if the initial dictionary is empty
    if(not bool(dictionary)):
        print("Biggest depth is 0")
        return
    else:
        Depth = 1
    def DictDepthFinder(dictionary,CurrentDepth):
        global Depth
        #if we have a dictionary because i is the key of the dicionary and not the value that
        #might contain an array type variable and i is a string I have made 2 cases
        #one where we find a dictionary and one where we have the other array type variables
        #since i cant do dictionary[i] on non dictionaries
        if(not bool(dictionary)):
            print("empty" ,Depth, CurrentDepth)
            if(Depth <= CurrentDepth):
                Depth = CurrentDepth-1  #here we check if there is an empty NESTED array type variable/object because it doesnt affect depth
        else:
            if(isinstance(dictionary, dict)):
                for i in dictionary:
                    if (isinstance(dictionary[i],(list,tuple,dict,set,frozenset))):
                        dictionary = dictionary[i]
                        if(Depth < CurrentDepth+1):
                            Depth = CurrentDepth+1
                        DictDepthFinder(dictionary,CurrentDepth+1)
            else:
                for i in dictionary:
                    if(isinstance(i,(list,tuple,dict,set,frozenset))):
                        dictionary = i
                        if(Depth < CurrentDepth+1):
                            Depth = CurrentDepth+1
                        DictDepthFinder(dictionary,CurrentDepth+1)
        return Depth
    print("Biggest depth is",DictDepthFinder(dictionary,1))
DictionaryDepth(dictionary)
