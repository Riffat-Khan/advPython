from itertools import count

for i in count(start = 5, step =3):
    print(i**3)
    if i**3 >= 1000000: break