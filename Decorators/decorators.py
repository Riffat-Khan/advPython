# def theFunc ():
#     print("That the inside function")

# def theDecorator(theFunc):
#     print("WELCOME HERE!!!!")
#     theFunc()
#     print("Thanks!")

# theDecorator(theFunc)()


# def theDecorator(theFunc):
#     print("WELCOME HERE!!!!")
#     theFunc()
#     print("Thanks!")

# @theDecorator
# def theFunc ():
#     print("That the inside function")

# theFunc()


def decorator(f):
    def newFunc():
        print("Start!!!!")
        f()

    return newFunc()

@decorator
def initial():
    print("continue")


initial()
