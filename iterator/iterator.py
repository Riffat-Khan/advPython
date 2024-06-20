x = iter([6, 8, 4])

print(next(x))
print(next(x))


class data:

    def __iter__(self):
        self.age = 67
        return self

    def __next__(self):
        if self.age <500:
            prod = self.age 
            self.age*=2
            return prod
        else: raise StopIteration


info = data()
iterator = iter(info)

for age in iterator: print(age)

print(next(iterator))
print(next(iterator))
print(next(iterator))
