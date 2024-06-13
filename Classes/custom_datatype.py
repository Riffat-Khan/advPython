class customDataType():

    def __init__(self):
        self.ListOfDict = []

    def __check__(self, value):
        if isinstance(value, dict) : self.ListOfDict.append(value)
        print(type(value))
        return self.ListOfDict
    

List_1 = customDataType().__check__(value={"name": "rayah"})
print(List_1)