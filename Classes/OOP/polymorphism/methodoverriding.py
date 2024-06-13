from datetime import date

class biodata():

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __print__(self):
        return f'{self.name} is {self.age} years old and lives in {self.city}'
    

class data():

    def __init__(self, arraydata):
        self.arraydata = arraydata

    def __print__(self):
        return f'{self.arraydata[0]} , {self.arraydata[1]} and {self.arraydata[2]} topped this year'
    


obj_1 = biodata("anil", 44, "gujranwala").__print__()
obj_2 = data(["nayla", "laraib", "ismail"]).__print__()
print("biodata_function====>", obj_1, "\ndata_function   ====>", obj_2)

    


