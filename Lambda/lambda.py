# lambda arguments : expression

product = lambda a , b : a*b

print(product(5 , 7))


def pow(num):
    return lambda n : num ** n


power = pow(5) #num = 5
print(power(3)) # n = 3