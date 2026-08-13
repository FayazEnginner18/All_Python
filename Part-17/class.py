my_cart="fayaz"
print(id(my_cart))
my_cart="shivy"
print(id(my_cart))


list1=[1,2,3,2,3,4,5,5,6]
list2=list1.copy()
list1.append(8)
print(list1)
print(list2)
print(list1.count(2))
list1.extend([5,6,7,9])
print(list1)
list1.insert(3,10)
print(list1)
list1.sort()
print(list1)
list1.clear()
print(list1)
print(list2)

list1=[[[[[[[[[[[1,2]]]]]]]]]]]
print(list1[0][0][0][0][0][0][0][0][0][0])