# #1
# dmart_cart=["Rice","Dal","Oil"]
# for i in dmart_cart:
#     print(i)
# print(len(dmart_cart))

# #2
# vegetables=["Tomato","Onion","Potato","Carrot"]
# print(vegetables[0])
# print(vegetables[-1])
# print(vegetables[-2])

# #3
# prices=[149,56,30,210,85,120,199]
# print(prices[0:3])
# print(prices[2:5])

# print(prices[4:])
# prices.sort(reverse=True)
# print(prices)

# #4
# mutate=["rice","dal","oil"]
# mutate[0]="Basmati rice"
# mutate.append("sugar")
# print(mutate)


# #5
# prices=[149,56,30,210,85,120,199]
# print(id(prices))
# prices[0]=54
# print(prices)
# print(id(prices))

# name="fayaz"
# print(id(name))
# name="new anenjne"
# print(id(name))


# #6
# a=["rice","dal"]
# b=a
# b.append("oil")
# print(a)
# print(id(a))
# print(id(b))
# b=a.copy()
# print(id(a))
# print(id(b))


# #7
# rows=[["rice","dal"],["Tomato","onion"]]
# copy=rows.copy()
# copy[0][0]="basmati"
# print(rows)
# print(copy)

# #8
# met=["Rice","Dal","oil"]
# met.pop()
# print(met)
# met.remove("Dal")
# met.append("Ghee")
# print(met)
# print(len(met))

# #9
# cart=[]
# print(bool(cart))
# if not cart :
#     print("Empty")
# elif "Rice" in cart:
#     print("Has Rice")
# else:
#     print("NO rice")


# #10
# list=[]
# while True:
#     choice=input("enter choice(add/view/remove/quit)")

#     if choice == "add":
#         item=input("enter item:")
#         list.append(item)
#         print(f"{item} is added")

#     elif choice == "view":
#         print(list)

#     elif choice == "remove":
#         item=input("enter remove item:")
#         try:
#             list.remove(item)
#             print(f"item {item} is removed")
#         except ValueError:
#             print(f"{item} is not found")

#     elif choice == "quit":
#         print("quit")
#         break

#     else:
#         print("invalid choice !")


#11
#


#12
#prices=[149,45,50,30,210,85]
# new_list=[]
# for i in prices:
#     if i>50:
#         new_list.append(i)


# print(f"new list is :{new_list}")

#13
# dmart = [
#     ["Rice", "Dal", "Sugar"],
#     ["Potato", "Carrot", "Tomato"],
#     ["Soap", "Shampoo", "Toothpaste"]
# ]

# print(*dmart[0], sep=",")
# print(dmart[1][1])

#14
# items = ["Rice", "Dal", "Oil"]
# prices = [450, 120, 210]

# total=0
# for i ,j in zip(items,prices):
#     print(i,"=",j)
#     total+=j

# print(total)


#15

num=int(input("enter number:"))
square=[]
for i in range(1,num+1):
    square.append(i*i)
print(square)