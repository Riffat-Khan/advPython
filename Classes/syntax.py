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


# count number of em ployees
class employees:

    employee_count = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        employees.employee_count +=1

    def display_count(self):
        return self.employee_count
    
    def employee_data(self):
        return "name :", self.name, "position :", self.position
    

emp_1 = employees("rahul", "senior developer")
emp_2 = employees("rahul", "senior developer")
emp_4 = employees("rahul", "senior developer")
print(emp_4.display_count())
print(emp_1.employee_data())