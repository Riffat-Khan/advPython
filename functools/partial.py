from functools import partial

def power(a ,b):
    return a**b

pow_4 = partial(power , b=4)
powOf_3 = partial(power , 3)

print(power(6,2))
print(pow_4(6))
print(powOf_3(6))