import itertools

List = [4, 2, 66, 34, 2, 45]

for i in itertools.repeat(List , len(List)):
    print(i)
