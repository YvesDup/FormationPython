import functools


def fibo(n):
    if n < 2:
        return 1

    return fibo(n-1) + fibo(n-2)

print(f'{fibo(10) = }')
print(f'{fibo(20) = }')
print(f'{fibo(40) = }')

d = {} 
def fibo2(n):
    if n < 2:
        return 1
    if n in d:
        return d[n]
    d[n] = fibo2(n-1) + fibo2(n-2) 
    return d[n]

print(f'{fibo2(10) = }')
print(f'{fibo2(20) = }')
print(f'{fibo2(40) = }')

def fibo3(n):
    if n < 2:
        return 1

    return fibo3(n-1) + fibo3(n-2)