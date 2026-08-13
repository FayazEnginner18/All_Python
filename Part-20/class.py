# set={1,2,43,435,4356,546}
# print(set)
# # set.add(9230)
# # print((id(set)+id(set)))
# # set23=set
# # print(id(set23))

# set2={43,5,9,3,6,2,3}
# # print(hash(2.5))
# for i in set:
#     print(i)

# set1=set2.symmetric_difference_update(set)
# print(set1)

# print(set|set2)




#s={10,20,30,40}
# x=s.copy()
# s.add(50)
# print(f"added",s)
# s.update([60,70,80,90,100])
# print(s)
# s.remove(70)
# print(s)
# s.discard(60)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
# print(x)


# s1={10,20,30,40}
# s2={5,3,6,8,30,2}
#union
# print(s1|s2) #all element
# #intersection
# print(s1 & s2) #common element
# #diffrence
# print(s1-s2) #s1 element value without s2 element

# #symmentric diffrence
# print(s1^s2) #  print all elemtnt without common element

# #intersection update
# s1 &= s2
# print(s1)


# s1 |= s2
# print(s1)

# s1-=s2
# print(s2)

#symmetric_difference_update()
# s1^=s2
# print(s1)

a={1,2}
b={1,2,3,4}
#issubset()
print(a<=b)


#issuperset()

print(b>=a)
# issubset   → Is A inside B?
# issuperset → Does A contain B?



#isdisjoint()
#Checks whether two sets have no common elements.

a={1,2,3}
b={4,5,6}
print(a.isdisjoint(b))
print(3 not in b)

x = "apple"

print(hash(x))
x=frozenset("fayaz")

print(x)