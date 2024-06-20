class operation():

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __opt__(self):
        result = self.num_1 + self.num_2
        return f'{self.num_1} + {self.num_2} = {result}'
    
    
class power(operation):

    def __init__(self, num_1, num_2):
        super().__init__(num_1, num_2)

    def __opt__(self):
        result = self.num_2** self.num_1
        return f'{self.num_2} ^ {self.num_1} = {result}'
    


operation_1 = power(4, 5)
operation_2 = operation(4, 5)

print(operation_1.__opt__())
print(operation_2.__opt__())

        