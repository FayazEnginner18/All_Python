list=[("name","fayaz"),("age",21)]

dic=dict(list)
dict=dic.copy()
print(dic)
print(dic.get("name","fayaz"))
dic["city"]="yaraguppi"
dic["clg"]="agm"

#1 keys()
print(dic.keys())

#2 values
print(dic.values())

#3 items
print(type(dic.items()))

#4 get("keys",default)
print(dic.get("name","0"))

#5 update({"keys":"values"})
dic.update({"name":"arafata"})
print(dic)

#6 pop("key")
print(dic.pop("age"))
print(dic)


#7 popitem() : Removes and returns the last inserted key value pair.
print(dic.popitem())


#8 clear()
dic.clear()
print(dic)

#9 copy() : copy the dictionary
#dict=dic.copy()


#10 se10. setdefault()

# Returns the value if the key exists.

# If the key does not exist, it creates the key with the given value.
print(dict.setdefault("clg","AGM"))
print(dict)
#11 len(variavle)
print(len(dict))

#12 type
print(type(dict))

#13 str
print(str(dict))
for key in dict.keys():
    print(f"le bsdk key ida {key} adka value ida le ")

#14
d = {"c": 30, "a": 10, "b": 20}

print(sorted(d.items()))
print("name" in dic)