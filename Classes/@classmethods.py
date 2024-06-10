class data:

    def __init__(self , name ,salary , age ):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def getting(cls, age , salary):
        if age > 18: return cls(age ,salary)

    @staticmethod
    def info(name , salary):
        return format( name , salary)    

person1 = data("akash" , 30 , 100000 )
person2 = data.getting( 54 , 50000)
print(person2)
