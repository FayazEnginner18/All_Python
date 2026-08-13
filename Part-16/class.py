# for i in range(4):
#     for j in range(4):
#         if ( i==0 or i==3 ) or (i>0 or i<3) and  (j==0 or j==3):
#             print("*",end=" ")
#     print()

# letter=input("enter a sentence:")

# vowel_count=0
# consonant_count=0
# number=[]

# for char in letter.lower():
#     if char in "aeiou":
#         vowel_count+=1
#     elif char.isalpha():
#         consonant_count+=1
#     elif char.isalnum():
#         number.append(char)
# total=vowel_count+consonant_count
# print("vowel:",vowel_count)
# print("consonnant:",consonant_count)
# print(f"total letters {letter}")
# print(number)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}",end=" ")
    print()

target = "y"
text = "Python"

for char in text:
    if char == target:
        print(f"Found '{target}'!")
        break
else:
    print(f"'{target}' not found in '{text}'")
