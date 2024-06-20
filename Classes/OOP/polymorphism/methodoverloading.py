class power():

    def __init__(self, num_1):
        self.num_1 = num_1

    def __power__(self):
        result = self.num_1**2
        return f'{self.num_1} ^ 2 = {result}'
    
    
class sqr(power):

    def __init__(self, num_1, num_2):
        super().__init__(num_1)
        self.num_2 = num_2

    def __power__(self, pow_val):
        result = self.num_2** pow_val
        return f'{self.num_2} ^ {pow_val} = {result}'
    


operation_1 = power(4)
operation_2 = sqr(5, 7)

print(operation_1.__power__())
print(operation_2.__power__(pow_val=8))
        