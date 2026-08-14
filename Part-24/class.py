def add(num1,num2):
    return num1+num2
print(add(3,453))


def C_area(length, width):
    #Docstrings
    """This is area formula this is imp
    Docstring Rules
    Use triple quotes 
    First line: brief description of what the function does
    Optional: parameters, return value, examples
    Keep it concise but useful
"""
    area=length*width
    print(area)
C_area(50,40)
C_area(50,400)
help(C_area)


x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)

outer()

counter=0
def increment():
    global counter
    counter+=1
increment()
increment()
print(counter)

def func(positional, default="value", *args, keyword_only, **kwargs):
    pass