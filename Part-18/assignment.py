cart_items = ["Rice", "Dal", "Oil", "Sugar", "Tea"]
cart_prices = [450, 120, 210, 50, 150]

for i,(j,k) in enumerate (zip(cart_items,cart_prices),1):
    print(f"{i}. {j} - ₹{k}")

rows=list(zip(cart_prices,cart_items))
print(rows)

ordered=sorted(rows,reverse=True)
print(ordered)
for rank,(price,item) in enumerate(ordered,1):
    print(f"{rank}. {item} - ₹{price}")