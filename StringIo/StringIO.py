from io import StringIO

string = "Hey!! Welcome to the fictional life"

file = StringIO(string)

print(file.read())

file.write("\nWhat're you gonna write here?")

file.seek(0)

print(file.getvalue())

print(file.writable())
print(file.readable())

print(file.tell())

file.truncate(30)
print(file.read())

print(file.tell())