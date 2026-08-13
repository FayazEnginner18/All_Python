x=10
y=x
print(f"x= {x}, type ={type(x)} ,id ={id(x)}")
print(f"y= {y}, type ={type(y)} ,id ={id(y)}")
print(f"same object {x is y}")
print(f"same object {id(x)==id(y)}")


x = 10
print(f"x = {x}, id = {id(x)}")

x = 20
print(f"x = {x}, id = {id(x)}")


x=1000
y=1000
print(f"id {id(x)}")
print(f"id {id(y)}")
print(x == y)


a=257
b=int(input("enter number :"))
print(id(a))
print(id(b))
print(a is b)
print(a==b)

print()

name='fayaz'
print(id(name))
name='najju'
print(id(name))