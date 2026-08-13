name="FaYaZ"
if name.lower() == "fayaz":
    print(name)
else:
    print(name.upper())

if "hello":         # bool("hello") → True → runs
    print("truthy")

if 0:               # bool(0) → False → skipped
    print("never")

if [1, 2, 3]:       # bool([1,2,3]) → True (non-empty) → runs
    print("has items")


score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

user_exists="fayaz"
password_correct=""
account_not_banned=True
# Optimal order — cheapest and most likely to fail check first:
if user_exists and password_correct and account_not_banned:
    print("Login successful")
else:
    print("arrest him")


account_active=False
banned=False
if user_exists:
    if password_correct:
        if account_active:
            if not banned:
                print("Login successful")
            else:
                print("Account banned")
        else:
            print("Account inactive")
    else:
        print("Wrong password")
else:
    print("User not found")


# Deeply nested — hard to read:
username = input("Username: ")
password = input("Password: ")

if username != "":
    if password != "":
        if username == "admin":
            if password == "secret123":
                print("Login successful")
            else:
                print("Wrong password")
        else:
            print("Unknown user")
    else:
        print("Password cannot be empty")
else:
    print("Username cannot be empty")
