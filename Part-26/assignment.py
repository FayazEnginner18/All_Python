def Sum_digit(n):
    if n<10:
        return n
    else:
        return(n%10) + Sum_digit(n//10)


print(Sum_digit(12345678910))

def reverse(name):
    if len(name)<=1:
        return name
    else:
        return name[-1] + reverse(name[:-1])

print(reverse("fayaz"))

def sums(n):
    if n<=1:
        return 1
    else:
        return n+sums(n-1)
print(sums(5))

def power(n,m):
    if n<=1 or m==0:
        return 1
    else:
        return n*power(n,m-1)

print(power(2,5))

def counter(data):
   
    if data<=1:
        return 1
    else:
        
        return 1+counter(data//10)

print(counter(1234567809))

