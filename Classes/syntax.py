class number:
    x = 5  #properties


cls1 = number()
print(cls1.x)

# __init__

class data:
    def __init__(self , name , age):
        self.name = name
        self.age = age

obj1 = data("jhon" , 45)
print(obj1.name , obj1.age)
print(obj1)