def gen(arr):
    for i in range(len(arr)):
        yield i

    
for item in gen(arr=[1, 3, 2, 6]):
    print(item)