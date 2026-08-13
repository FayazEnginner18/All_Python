print(abs(0.1+0.2) )
print(bin(10))
print(bin(255))
n="fayaz"
for i in n:
    print(bin(ord(i)),sep=" ",end="")

big=10**10

print(big)

population=8_00_00_00_00 
print(population)

samll=10_34_23_89.5_0_0_0_0_0_9
print(samll)
a=0.1+0.2+0.63651
print(round(a,4))
print(round(14,-1))
print(round(.1+.2,2)==0.3)

from decimal import Decimal
print(Decimal('0.1')+Decimal('0.2'))

print(10//3)


x=10
print(f"x={x}")
x+=3
print(f"x={x}")
x-=3
print(f"x={x}")
x*=3
print(f"x={x}")
x/=3
print(f"x={x}")
x//=3
print(f"x={x}")
x%=4
print(f"x={x}")
x**=3
print(f"x={x}")



print(abs(-1.5))

print(abs(-.2))

l=[12,23,45,56,67,78,89,90]
sum=sum(l)
print(sum)
print(f"avarege ={sum/len(l)}")
print(round(2.5))


age = input("Enter age: ")  # This is a string
print(int(age) + 1)  # TypeError: can't add str and int
