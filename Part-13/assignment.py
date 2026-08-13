# age=int(input("enter age :"))
# if age<0 and age >150:
#     print("invalid age")
# elif age<=13:
#     print("child -no access")
# elif age>=13 and age<=17:
#     print("Teenager - linited acess")
# elif age>=18 and age <=64 :
#     print("Adult -full acess")
# else:
#     print("senior")


# balance = 10000
# pin = "1234"

# pin=input("enter pin :")

# if pin =="1234":
#     amount=int(input("enter withdrwal amount :"))
#     if amount<0 :
#         print("amount is not contain ")
#     elif amount<=balance:
#         balance-=amount
#         print(f"remaining amount is {balance}")
#     else:
#         print("the amount is not found")


# else:
#     print("incorrect pin")


age = int(input("Age: "))
has_ticket = input("Have ticket? (yes/no): ")
has_id = input("Have ID? (yes/no): ")

if age >= 18:
    if has_ticket == "yes":
        if has_id == "yes":
            print("Welcome to the event!")
        else:
            print("ID required for entry")
    else:
        print("You need a ticket")
else:
    print("Must be 18 or older")
