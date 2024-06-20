class string:

    def __init__(self , string):
        self.string = string

    def __repr__(self):
        return format(self.string)
    
    def str(self):
        return (self.string)
    
    def __add__(self, other):
        return self.string + other


        
if __name__ == '__main__':

    str1 = string("hello")

    print(str1+ " world!")