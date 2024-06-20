class customDataType():

    def __init__(self):
        self.ListOfDict = []

    def __append__(self, value):
        if isinstance(value, dict) : self.ListOfDict.append(value)
        print(type(value))
        return self.ListOfDict
    
    def __len__(self):
        return len(self.ListOfDict)
    
    def __key__(self):
        for item in range(len(self.ListOfDict)): 
            return self.ListOfDict[item].keys()

    def __value__(self):
        for item in range(len(self.ListOfDict)): 
            return self.ListOfDict[item].values()
        
    def __items__(self):
        for item in range(len(self.ListOfDict)): 
            return self.ListOfDict[item].items()
        
    def __pop__(self):
        self.ListOfDict.pop()
        return self.ListOfDict
    
    def __update__(self):
        self.ListOfDict[-1].update({"math": 567})
        return self.ListOfDict
    
    

List_1 = customDataType()
print(List_1.__append__(value={"name": "rayah"}))
print(List_1.__key__())
print(List_1.__value__())
print(List_1.__items__())
print(List_1.__update__())
print(List_1.__pop__())
