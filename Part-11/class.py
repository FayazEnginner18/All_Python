# word=True
# print(f"value={word},type ={type(word)},id={id(word)}")

# word=False
# print(f"value={word},type ={type(word)},id={id(word)}")


# #True and False Are Singletons


# t1=True
# t2=False
# print(t1 is t2)
# print(id(t1))
# print(id(t2))

# print(t1>t2)

# print(True+True+True+True+True*10-True)
# print(True*102+False+True//True)
# print(sum([True,True,True,True,True,False+2*6,False,True]))

# print(type(True))
# print("0")
# print("Fasle")
# print("2")
# print(25)
# print("1")
# print(True)

# name=["fayaz","julekha","najju"]
# print(name[True+1])
# print(name[False])


# a = 10
# b = 20

# print(a == b)    # False  (equal to)
# print(a != b)    # True   (not equal to)
# print(a > b)     # False  (greater than)
# print(a < b)     # True   (less than)
# print(a >= 10)   # True   (greater than or equal to)
# print(a <= 5)    # False  (less than or equal to)


# print("apple" < "banana")   # True — a(97) < b(98)
# print("abc" == "abc")       # True
# print("A" < "a")            # True — A(65) < a(97), uppercase is "smaller"


# a = 256
# b = 256
# print(a == b)    # True  — same value
# print(a is b)    # True  — same object (256 is a cached singleton from Part 9)

a = 10000
b = 10000
print(id(a),id(b))
print(a == b)    # True  — same value
print(a is b)    # False — different objects in heap (1000 is outside cache range)


print(10 == 10.0)     # True  — int and float, same mathematical value
print(10 == 10.00)     # False — int and str, different types = not equal
print(True == 1)      # True  — bool is subclass of int
print(False == 0)     # True
print(True == 1.0)    # True  — 1.0 equals 1 equals True
