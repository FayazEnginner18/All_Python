word="banana"
frequency={}

for letter in word:
    if letter in frequency:
        old=frequency[letter]
        frequency[letter]=old+1

    else:
        frequency[letter]=1
print("frequency:",list(frequency.items()))


dict={}
while True:
    actions=int(input("enter actions(1.add/2.search/3.list/4.delete/5.quit): "))
    if actions==1:
        name=input("enter name:")
        phone_no=int(input("enter number"))
        dict[name]=phone_no
        print("contact succssful")

    elif actions==2:
        name=input("enter name:")

        if name in dict:
            print("contact is ",dict[name])
        else:
            print("not found")

    elif actions == 3:
        if dict:
            for  name,phone in dict.items():
                print(name,phone)
        else:
            print("dictionary is empty")

    elif actions == 4:
        name=input("enter name:")
        if name in dict:
            print(f"deleted the item is {dict.pop(name)}")
        else:
            print("name is not found")

    elif actions == 5:
        print("Total contact is ",len(dict))
        print("good bye ! ")
        break

    else:
        print("invalid operation")

