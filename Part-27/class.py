call_count = 0
cache={}
def fibonacci(n):
    global call_count
    call_count += 1
    if n in cache:
        return cache[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    result= fibonacci(n - 1) + fibonacci(n - 2)
    cache[n]=result
    return result

fibonacci(900)
print(f"Calls: {call_count}")   # Calls: 2692537

from functools import lru_cache
call_count = 0
@lru_cache
def fibonacci(n):
    global call_count
    call_count += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(900)
print(f"Calls: {call_count}")   # Calls: 2692537
""
""