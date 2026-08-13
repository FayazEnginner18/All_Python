
#assignment 1
brand="onePercentDev"
print(brand[0],brand[-1])

print(brand[::-1])
print(f"total number of charcter : {len(brand)}")

print(brand[0:3],brand[:-4:-1])
#OePretDv

#assignment 2
user=input("enter sentence:")
print(user.strip())
print(user.lower())
lens=user.split(sep="a")
print(lens)
print(len(lens))

print(user.replace("y","t"))