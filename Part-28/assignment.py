students = [
    {"name": "Alice", "score": 85, "grade": "B"},
    {"name": "Bob", "score": 92, "grade": "A"},
    {"name": "Charlie", "score": 45, "grade": "F"},
    {"name": "Diana", "score": 78, "grade": "C"},
    {"name": "Eve", "score": 95, "grade": "A"},
    {"name": "Frank", "score": 62, "grade": "D"}
]

list_new=sorted(students,key=lambda x:x["score"], reverse=True)
list_new2=sorted(students,key=lambda x:x["name"])
print(list_new)
print()
print(list_new2)

filterd=filter(lambda x:x["score"]>=70 ,students)
print(list(filterd))

maped=list(map(lambda x: x["name"],students))
print(maped)
print("\n"*2)
com1=[x for x in students if x["score"] >=70]
print(com1)


com2=[x["name"] for x in students ]
print(com2)