from io import StringIO

string = "Hey!! Welcome to the fictional life"

fileStr = StringIO(string)

print(fileStr.read())

fileStr.write("\nWhat're you gonna write here?")

fileStr.seek(0)

print(fileStr.getvalue())

print(fileStr.writable())
print(fileStr.readable())

print(fileStr.tell())

fileStr.truncate(30)
print(fileStr.read())

print(fileStr.tell())