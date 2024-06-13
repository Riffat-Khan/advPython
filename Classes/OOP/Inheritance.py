from datetime import date

class biodata():

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __age__(self, birthYear):
        current = date.today().year
        age = current - birthYear
        return f'{self.name} is {age} years old and lives in {self.city}'

    def __print__(self):
        return f'{self.name} is {self.age} years old and lives in {self.city}'
    

# ahann = biodata("ahann" , 34 , "lhr")
# print(ahann.__print__())
# print(ahann.__age__(2002))


class profession(biodata):

    def __init__(self, name, age, city , profession_name):
        biodata.__init__(self, name, age, city)
        self.profession = profession_name

    def __prof__(self):
        return f'{biodata.__print__(self) } and the profession opted is {self.profession}'
    

# ahann = profession("ahann" , 34 , "lhr" , "doctor")
# print(ahann.__print__(), ahann.__prof__())


class hobby():

    def __init__(self, hobby_name):
        self.hobby = hobby_name

    def __hobb__(self):
        return f'likes {self.hobby}'
    

#<-------------------------MULTIPLE INHERITANCE-------------------------->

class info(profession,  hobby):
    
    def __init__(self, name, age, city, profession_name,  hobby_name, gender):
        profession.__init__(self, name, age, city, profession_name)
        hobby.__init__(self, hobby_name)
        self.gender = gender

    def __display__(self):
        profession_dis = profession.__prof__(self)
        hobby_dis = hobby.__hobb__(self)
        return f'{self.gender}: {profession_dis} plus likes {hobby_dis}'
    


person1 = info("rahul", 25, "lahore", "doctor" ,"badminton", "male")
print(person1.__display__())



#<-------------------------MULTILEVEL INHERITANCE-------------------------->

class religion(profession):

    def __init__(self, religion_name,  name, age, city, profession_name):
        self.religion = religion_name
        profession.__init__(self, name, age, city, profession_name)

    def _result__(self):
        return f'The religion is {self.religion} and {profession.__prof__(self)}' 
    

data_1 = religion("Islam", "hanzla", 20, "quetta", "artist")
print(data_1._result__())
