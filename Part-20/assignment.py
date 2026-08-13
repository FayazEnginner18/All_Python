# | Method                          | Purpose                                    |
# | ------------------------------- | ------------------------------------------ |
# | `add()`                         | Add one element                            |
# | `update()`                      | Add multiple elements                      |
# | `remove()`                      | Remove element, error if absent            |
# | `discard()`                     | Remove element, no error if absent         |
# | `pop()`                         | Remove and return an arbitrary element     |
# | `clear()`                       | Remove everything                          |
# | `copy()`                        | Create a copy                              |
# | `union()`                       | Combine sets                               |
# | `intersection()`                | Find common elements                       |
# | `difference()`                  | Find elements only in first set            |
# | `symmetric_difference()`        | Find non common elements                   |
# | `intersection_update()`         | Update with common elements                |
# | `difference_update()`           | Remove common elements                     |
# | `symmetric_difference_update()` | Update with non common elements            |
# | `issubset()`                    | Check subset                               |
# | `issuperset()`                  | Check superset                             |
# | `isdisjoint()`                  | Check whether sets have no common elements |


# class_a = {"Rahul", "Arun", "Priya", "Sneha", "Kiran"}
# class_b = {"Priya", "Kiran", "Amit", "Sneha", "Ravi"}

# print(class_a & class_b)
# print(class_a)
# print(class_b)
# print(class_a.symmetric_difference(class_b))

# numbers = {10, 20, 10, 30, 20, 40, 30, 50}
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(40 in numbers)
# print(100 in numbers)
# print()

# A = {10, 20, 30}
# B = {10, 20, 30, 40, 50}

# print(A.issubset(B))
# print(B.issubset(A))
# print(A.issuperset(B))
# print(B.issuperset(A))

# print()
# print(A<=B)
# print(B<=A)
# print(A>=B)
# print(B>=A)

# print()
# words = {"python", "java", "python", "c", "java", "html", "css"}

# print(words)
# print("python" in words)
# print("javascript" in words)
# words.add("javascript")
# words.remove("java")
# print(words)

# print()
# all_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# present = {1, 2, 4, 5, 7, 10}
# print(all_numbers-present)

# print()
# word = "programming"
# sets=set(word)
# print(sets)
# print("g" in sets)
# print("z" in sets)

# print()
# python_students = {"A", "B", "C", "D", "E"}
# java_students = {"C", "D", "E", "F", "G"}

# print(python_students & java_students)
# print(python_students)
# print(java_students)
# print(python_students | java_students)
# print(python_students.symmetric_difference(java_students))


# print()
# morning = {1, 2, 3, 4}
# evening = {5, 6, 7, 8}
# print(morning.isdisjoint(evening))
# evening = {5, 6, 7,  4}
# print(morning.isdisjoint(evening))

# print("\n"*2)
# A = {10, 20, 30, 40, 50}
# B = {30, 40, 60, 70} 
# A.intersection_update(B)

# print(A)
# A.update([80,90])
# print(A)
# A.remove(30)
# A.discard(100)
# print(A)


# print("\n"*2)
# num=set()
# num.update({15,25,35,15,45,25,55,65,35})
# print(num)
# print(len(num))
# print(45 in num)
# print(100 in num)
# num.remove(25)
# print(num)
# num.add(75)
# print(num)


class_a = ["Asha", "Ravi", "Priya", "Dev", "Meera", "Ravi"]
class_b = ["Ravi", "Dev", "Kiran", "Nisha", "Asha", "Kiran"]

class_a=set(class_a)
class_b=set(class_b)

print(f"class_a= {class_a},class_b = {class_b}")
print(class_a & class_b)
print( class_a-class_b)
print(class_b - class_a)
print(class_a | class_b)
print(class_a.symmetric_difference(class_b))