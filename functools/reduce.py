from functools import reduce

List = [5, 32, 5, 98, 7, 1]

sum = reduce(lambda a , b: a+b , List)
print(sum)

largest = reduce(lambda a , b: a if a>b else b , List )

print(largest)