def create_profile(name, age, **extras):
    print(f"name:{name}")
    print(f"age:{age}")

    for key,value in extras.items():
        print(f"{key}: {value}")


create_profile("Fayaz",21,clg="AGM",Father="Khajesab",place="Yaraguppi")

def print_separator(char="-", length=40):
    print(char*length)
print_separator()
def display_profiles(*profiles):
    for profile in profiles:
        if profile  in profiles:
            print(profile)
            print("=" * 30)


display_profiles(
    {"name": "Fayaz", "age": 20, "city": "Hubli"},
     {"name": "Fayaz", "age": 20, "city": "Hubli"},
    {"name": "Aisha", "age": 22, "city": "Bangalore"},
    {"name": "Rahul", "age": 21, "city": "Mysore"}
)
