import copy
user={
    "name":"fayaz",
    "age":21,
    "address":{
        "city":"hubbali",
        "state":"karnataka",
        "pin":580023
    },

    "skills":["python","java","HTML","CSS"]
}
print(user["address"]["state"])
print(user["skills"][3])
new_user=user.copy()
new_user2=copy.deepcopy(new_user)
print(user.pop("skills"))


print(new_user2)