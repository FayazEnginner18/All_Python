numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20]
squares=[n*n for n in numbers]
print(squares)
#print(id([n*n for n in numbers]))
even=[n for n in numbers if n%2==0]
print(even)

dict={n:n*n for n in numbers}
print(dict)

set= {n%10 for  n in numbers }
print(set)

laebels=["even" if n%2==0 else "odd" for n in numbers]
print(f"The number the valu is {laebels}")



items=["Rice","Dal","Oil"]
prices=[450,250,362]

prices_map={item:price for item ,price in zip(items,prices) if price>50}
print(prices_map)


nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
flat=[n for i in nested for n in i]
print(flat)