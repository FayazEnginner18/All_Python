# count=0
# number=45
# while True:
#     num=int(input("enter number :"))
#     count+=1
#     if num < number:
#         print("to low")
#     elif num == number:
#         print("correct")
#         break
#     else:
#         print("too high")
# print(f"You got it in {count} attempts.")


while True:
    print("1.dition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")

    choice=int(input("enter choice:"))
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))

    match choice:
        case 1:
            print(num1+num2)

        case 2:
            print(num1-num2)

        case 3:
            print(num1*num2)

        case 4 :
            if num1 ==0 or num2 ==0:
                print("zerodivision error")

            else:
                print(num1/num2)

        case 5:
            print(num1%num2)

        case _:
            print("invalid choice")
            break