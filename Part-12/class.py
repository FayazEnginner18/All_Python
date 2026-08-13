a=True
b=False

print(a and b)
print(not a and b)
print(a and not b)
print(not a and not b)


print()
print(a or b)
print(not a or b)
print(a or not b)
print(not a or not b)

print()
print("hello" and "world")   # "world"  — NOT True
print("" and "world")        # ""       — NOT False
print("hello" or "world")    # "hello"  — NOT True
print("" or "world")         # "world"  — NOT True
print(0 or 42)               # 42       — NOT True
print(None or "default")     # "default"
print(None and "default")  

user=input() or "fayaz"
print(user)

name=""
print(name and name[0])

x=None
print(x is None)
print(id(None))


#in operator

print("f" in "fayaz")

age=25
print(age >=18 and age <=65)

print(18 <= age <=65)

x=2
print(1 <= x <=3)

print(2*6//3+6*8+4-75*2)