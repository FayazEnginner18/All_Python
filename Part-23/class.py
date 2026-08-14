items = [1, 2, 3, 4, 5]
result=list(map(lambda x : x + 1,items))
print(result)

doubles=[n*2 for n in items]
print(doubles)

clean=[name.title() for name in ["dal gee","rice","kushka"]]
print(clean)

even=[n for n in range(1,11) if n%2==0]
print(even)

labels=["value" if n%2==0 else "odd" for n in range(1,12)]
print(labels)

#Dictionary Comprehesion

items=["Rice","Dal","Oil"]
prices=[450,250,362]

prices_map={item:price for item ,price in zip(items,prices) if price>250}
print(prices_map)

listr={i:item for i ,item in enumerate(items)}

print(listr)