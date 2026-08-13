x=10
print(x)
print(id(x))
y=x
print(y)
print(id(y))


x=20
print(x)
print(id(x))
print(id(y))
print(f"id is {id(x)==id(y)}")