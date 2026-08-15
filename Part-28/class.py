# number=[1,2,3,4,5]
# squares=list(map(lambda x:x**2,number))
# print(squares)


#Map
# The function can be:

# A normal function (square)
# A built in function (int, str, len)
# A lambda function

# So lambda is optional. map() works perfectly without it.


x=[1,2,3,4,5,6,6]
y=[1,2,3,4]

squares=list(map(lambda x ,y:2*x+y,range(1,5),range(1,5)))
print(squares)


#filter(function, list)
#Yes, filter() is mainly used with conditions.

filt=tuple(filter(lambda x:x>=2,x))
print(filt)

# What is reduce()?

# reduce() means:

# Take all values and reduce them to a single value.

from functools import reduce

numbers=[1,2,3,4,5]

numberss=[1,2,3,4,5,6]

result=reduce(lambda a,b:a*b,numbers)
print(result)