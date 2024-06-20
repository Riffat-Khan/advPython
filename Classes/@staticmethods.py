class data:

    def __init__(self , name ,salary , age ):
        self.name = name
        self.age = age
        self.salary = salary

    #instance method
    def _detail(self):
        return f'{self.name} is of {self.age} and has a salary of {self.salary}'


    @staticmethod
    def info(name , salary):
        return f'{name} has a salary of {salary}'

person1 = data("akash" , 30 , 100000 )
print(person1._detail())

print(data.info(name="ali" , salary=100000))
