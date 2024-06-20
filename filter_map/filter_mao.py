List = [4, 3, 7, 23, 89, 76, 34]

def check(x):

    print( x ," = Even") if x%2 == 0 else print(x ," = Odd")

EvenOdd = filter(check , List)

for x in EvenOdd:
    print(x)


def power(x):
    return x**2

res = map(power , List)

for i in res: print(i)