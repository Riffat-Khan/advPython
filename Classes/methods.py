class employee:

    employeeCount = 0
    company = "linked matrix"

    def __init__(self, name, age):

        self.name = name
        self.age = age
        employee.employeeCount +=1

    #instance method
    def display(self):
        return f'{self.name} is {self.age} years old and works in {employee.company}'
    
    def registeredEmp(cls):
        return f'{employee.employeeCount} = newly registered'


    @classmethod
    def companyName(cls, companyName):
        cls.company = companyName
        return f'It is now "{companyName}"'
    
    @staticmethod
    def agetobe(age):
        return "fine" if age > 18 else "cool"
    


emp_1 = employee("ali", 45)
print(emp_1.display())
print(emp_1.companyName("the matrix"))
print(emp_1.display())
print(employee.agetobe(45))

emp_2 = employee("ahad", 30)
print(emp_2.display())


print(emp_2.registeredEmp())
    
