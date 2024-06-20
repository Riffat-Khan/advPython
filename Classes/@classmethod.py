from datetime import date

class data:

    count = 0

    def __init__(self , name ,age ):
        self.name = name
        self.age = age

    def _detail(self):
        count+=1
        return f'{self.name} is of {self.age}, {count}'


    @classmethod
    def info(cls , name , birthYear):
        year = date.today().year
        age = year - birthYear
        return cls(name , age)

person1 = data.info(name="akash" , birthYear=2000)

print(person1._detail())
