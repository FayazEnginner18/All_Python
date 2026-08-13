stores = [
    ("DMart Bangalore", 4),
    ("DMart Delhi", 6),
    ("DMart Mumbai", 5),
    ("DMart Shimla", 2),
    ("DMart Chennai", 7),
]
for store ,temprature in stores:
    print(store,"=",temprature,"°C")

warmest_store,warmest_temp=stores[0]
coldest_store,clodest_temp=stores[0]

for stores,temprature in stores:
    if temprature>warmest_temp:
        warmest_store=store
        warmest_temp=temprature

    if temprature<clodest_temp:
        coldest_store=store
        coldest_temp=temprature

print("Warmest",warmest_store,warmest_temp,"°C")
print("Coldest:", coldest_store, coldest_temp, "°C")


# 4. divmod() on warmest temperature

quotient, remainder = divmod(warmest_temp, 5)

print("Quotient:", quotient)
print("Remainder:", remainder)