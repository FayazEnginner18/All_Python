name='''my name is fayaz
my class 3rdd year
agmr college varur '''
print(name)
print(id(name))
print(name[0])
print(name[20])
print(name[45])
print(name[5]=="m")
name="you'r "+name[3:]
print(name)
text="fayaz"
print(text[:])
print(text[0:])
print(text[0:5])
print(text[-1:-5])
print(text[0::2])
print(text[2::3])
print(text[2::-1])

origin="fayaz"
new=origin[0:3]
print(id(origin))
print(id(new))
print(id(origin)==id(new))


print("Line 1\nLine 2")
print("Name:\tOnePercentDev")
print("Path: C:\\Users\\onepercentdev")
print(r"C:\Users\new_folder")  # Prints literally, \n is NOT a newline


a = 10
b = 3
print(f"{a} divided by {b} is {a / b}")
# 10 divided by 3 is 3.3333333333333335


price = 49.99
tax = price * 0.18
total = price + tax

print(f"Price: {price:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total: {total:.2f}")

name="      fayaz  "
age=21
print("the nmae is {} age {}older ".format(name,age))

print(name + str( age ))
print(name.strip("y"))

name="fayaz"
for i in name:
    arr=bin(ord(i))
    print(arr.replace("0b",""),end="")


text="faYaz soartoor"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


user="yes"


if user.lower() == "yes":
    print("confirmed")
else:
    print("not confirmed")

rep="        Hello WOrld        "
print(rep.lstrip())
print(rep.rstrip())
print(rep.strip())

new="i am fayaz"
print(name.find("ya"))
print(name.find("yaz"))
print(new.count("a"))
print(new.replace("fayaz","niyaz"))



print("12345".isdigit())     # True
print("hello".isalpha())     # True
print("hello123".isalnum())  # True
print("HELLO".isupper())     # True
print("hello".islower())     # True
print("  ".isspace())        # True


age_input ="21"

if age_input.isdigit():
    age = int(age_input)
    print(f"Your age is {age}")
else:
    print("Invalid input. Please enter a number.")




filename = "report_2026.pdf"

print(filename.startswith("report"))   # True
print(filename.endswith(".pdf"))       # True
print(filename.endswith(".csv"))       # False



url = "https://api.example.com/data"

if url.startswith("https:/"):
    print("Secure connection")

file = "data.json"
if file.endswith(".json"):
    print("JSON file detected")


#split()
name="my nnmae is fayaz ag coleg varrur"
print(name.split(sep=" ",maxsplit=2))

#join()
list=["26","3","2006"]
new_list="-".join(list)
print(list)
print(new_list)


greeting = "ನ ಮ ಸ್ಕಾ ರ"  # Kannada
print(greeting)
print(len(greeting))


name="name"
print(name.zfill(9))
print(name.center(50,"="))
print(name.rjust(14,"/"))
print(name.ljust(14,"/"))