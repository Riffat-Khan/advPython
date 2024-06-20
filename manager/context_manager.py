#built-in context manager
with open("title.txt" , "w") as f:
    f.write("123")

print(f.closed)


#createing a context manager
class Manager():

    def __init__(self , fileName , fileMode):
        self.fileName = fileName
        self.fileMode = fileMode
        self.file = None

    def __enter__(self):
        self.file = open(self.fileName , self.fileMode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with Manager("title.txt" , "a") as f:
    f.write("\nwhatever!!!!!!")

print(f.closed)
