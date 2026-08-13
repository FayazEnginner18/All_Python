#match
age=18
if age >=18:
    pass
else:
    print("minor")


ages="adult" if age >=18 else "minor"
print(ages)

command="start"
# Python — match
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "restart":
        print("Restarting...")
    case _:
        print(f"Unknown command: {command}")