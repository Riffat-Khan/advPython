def printing():
    yield "START!!"
    yield "processing"
    yield "END..."

res = printing()

for x in res: print(x)