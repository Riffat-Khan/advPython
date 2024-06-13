def theFunc ():
    print("That the inside function")

def theDecorator(theFunc):
    print("WELCOME HERE!!!!")
    theFunc()
    print("Thanks!")

theDecorator(theFunc)()


def theDecorator(theFunc):
    print("WELCOME HERE!!!!")
    theFunc()
    print("Thanks!")

@theDecorator
def theFunc ():
    print("That the inside function")

theFunc()


def decorator(f):
    def newFunc():
        print("Start!!!!")
        f()

    return newFunc()

@decorator
def initial():
    print("continue")


initial()


# - Decorators (Write custom decorators), Class Based Decorators
#     1. Parameterised Decorator:
#         1. Create a decorator @repeat(n) that repeats the decorated function n times. It should also accept an argument for whether to print the results each time. Apply this decorator to a simple function.
            

class repeat:
    def repeat(self, n):
        def repeatFunc(Func):
            rep = 0
            while rep < n:
                ask = input("Want to repeat? (Y/N): ")
                if ask.lower() == "y":
                    Func()
                rep += 1

        return repeatFunc


class MyClass:
    def __init__(self):
        pass
    
    @repeat().repeat(6)
    def Func():
        print("I'm repeating")


obj = MyClass()
obj.Func()


#     2. Timing Decorator:
#         1. Write a decorator @timing that measures the time it takes for a function to execute and prints the execution time. Apply this decorator to various functions and compare their execution times.


import time

class Timing:
    def timing(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            execution_time = end - start
            print(f"Execution time: {execution_time}")
        return wrapper


class calculating:
    def __init__(self):
        pass
    
    @Timing().timing
    def sum(self, num_1, num_2):
        print(f"Sum: {num_1 + num_2}")

    @Timing().timing
    def div(self, num_1, num_2):
        print(f"Division: {num_1 // num_2}")


obj = calculating()
obj.sum(5, 6)
obj.div(340, 45)



#     3. Basic Decorator:
#         1. Create a decorator called @uppercase_decorator that converts the result of a function to uppercase. Apply this decorator to a function that returns a string and test it.


class converter:
    def uppercase_decorator (self, string):
        def wrapper(instance, *args, **kwargs):
            strToConvert = string(instance, *args, **kwargs)
            res = strToConvert.upper()
            print(f"String to upper case: {res}")
        return wrapper


class StringToConvert:
    def __init__(self):
        pass
    
    @converter().uppercase_decorator
    def string(self, text):
        return text


obj = StringToConvert()
obj.string("saima")