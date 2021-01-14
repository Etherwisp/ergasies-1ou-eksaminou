
dictionary   =    [1,2,{3,4,(5,6,(7,8,(9,10)))},11,12,(13,14,15,(16,17,(18,(19,(20,(21,22))))))]
#CurrentDepth=a   (a=0 (a=1 (a=2 (a=3 (a=4 ))))       (a=1      (a=2   (a=3(a=4(a=5(a=6  )))))))
def DictionaryDepth(dictionary):
    global Depth
    Depth = 0
    def DictDepthFinder(dictionary,CurrentDepth):
        global Depth
        for i in dictionary:
            if((type(i) is list) or (type(i) is tuple) or (type(i) is dict) or (type(i) is set) or (type(i) is frozenset)):
                dictionary = i
                if(Depth <= CurrentDepth):
                    Depth = CurrentDepth
                DictDepthFinder(dictionary,CurrentDepth+1)
        return Depth+1
    print("Biggest depth is",DictDepthFinder(dictionary,0))
DictionaryDepth(dictionary)
what the hell man!
