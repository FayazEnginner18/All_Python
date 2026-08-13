# score=int(input("enter number:"))
# if score>=90 and score <=100:
#     print("A")
# elif score>=80 and score <90:
#     print("B")
# elif score >=70 and score <80:
#     print("C")
# elif score >=60 and score <70:
#     print("D")
# elif score >0 and score <60:
#     print("F")
# else:
#     print("invalid score")


# user_name="fayaz"
# password=1234

# user_name=input("enter the name: ")
# password=input("enter the password:")
# if user_name and user_name =="fayaz":
#     if password and password == "1234":
#         print("login")
#     else:
#         print("password incorect")
# else:
#     print("user_name is valid")


name="status"

match name:
    case "help":
        print("take any help")
    case "status":
        print("my status")
    case "quit":
        print("quit the game")
    case "_":
        print("invalid")