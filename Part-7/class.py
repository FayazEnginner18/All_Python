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

print()

x=10
x=20
x=30
x=40
print(x)