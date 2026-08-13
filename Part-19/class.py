# shop_place=(5,12)
# print(type(shop_place))
# name=tuple("fayaz")
# print(name)

name=("a","b")
print(id(name))
name=("a","b")
print(id(name))

products = ("Rice", "Dal", "Oil", "Sugar")

print(products[0])      # Rice
print(products[-1])     # Sugar
print(products[1:3])    # ('Dal', 'Oil')
print(products[::-1])   # ('Sugar', 'Oil', 'Dal', 'Rice')


first = "Rice"
second = "Dal"

first, second = second, first

print(first)   # Dal
print(second)  # Rice


item1, *others,last = ["Rice", "Dal", "Oil", "Sugar", "Tea"]

print(item1)   # Rice
print(others)
print(last)  # ['Dal', 'Oil', 'Sugar', 'Tea']


result=divmod(450,100)
#divmod(a, b) returns (a // b, a % b) 
print(result)
print(id(result))



# Same rupee amounts can repeat on a bill — tuples allow duplicates
amounts = (450, 120, 210, 120, 450)

print(amounts.count(120))    # 2
print(amounts.index(210))  # 2 (position of first 210)
print(amounts.index(120, 2)) # 3 — optional start (and stop), same idea as list `.index` in Part 18


tup=(1,2,1,2,4,2,1,2,12,1,35,1,2,4,1)
print(tup.index(1,7,10))
print(45 in tup)
print("45"*6)

a,b,c=(1,2,3)
print(a)
print(b)
print(c)
list=list(tup)
list.append(90)
print(list)
tup=tuple(list)
print(tup)


#Tuples Use Less Memory Than Lists
import sys
list=[1,2,3,4,5,8]
tup=(1,2,3,4,5)
print(sys.getsizeof(list))
print(sys.getsizeof(tup))