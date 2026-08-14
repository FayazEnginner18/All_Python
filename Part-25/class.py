
#default paarmaetr
def area(width,legnth=50):
    return width*legnth

print(area(20))

def aadd_item(item,items=[]):
    items.append(item)
    return items
print(aadd_item("apple"))
print(aadd_item("banana"))


def func(item,items=None):
    if items is None:
        items=[]
    items.append(item)
    return items
print(func("apple"))
print(func("banana"))

#*args us in Tuple

def funs(name="fayaz",*names):
    return name,sum(names)

a=funs(1)
print(type(a))
print(a)

#**kwargs in dict

def register(username,**extras):
    print("username:",username)

    for key,value in extras.items():
        print(f"{key}:{value}")

register("Fayaz",role="Engineer",salary=200000)