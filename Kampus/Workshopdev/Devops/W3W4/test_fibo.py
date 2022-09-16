import functools
import time

def fibo(n):
    if n < 2:
        return 1
    return fibo(n-1) + fibo(n-2)

# fibo(4) = fibo(3) + fibo(2) ** fibo(3) = fibo(2) + fiba(1)

start = time.time()
print(f'{fibo(10) = }')
print(f'{fibo(20) = }')
# print(f'{fibo(37) = }')
t = time.time() - start
print(f'temps passé est: {t:.4f}')
print('++++'*10)

d = {} 
def fibo2(n):
    if n < 2:
        return 1
    if n in d:
        return d[n]
    d[n] = fibo2(n-1) + fibo2(n-2)
    return d[n]

start = time.time()
print(f'{fibo2(10) = }')
print(f'{fibo2(20) = }')
print(f'{fibo2(37) = }')
t = time.time() - start
print(f'temps passé est: {t:.4f}')
print(d)
print('++++'*10)
exit()


@functools.cache
def fibo3(n):
    if n < 2:
        return 1

    return fibo3(n-1) + fibo3(n-2)

print(f'{fibo3(10) = }')
print(f'{fibo3(20) = }')
print(f'{fibo3(40) = }')

msg = 'hello'
print('Yves', msg)

printf = functools.partial(print, 'yves')
print(type(printf))
printf('hello')
printf('coucou')
print('hello', 'yv', sep='\t')


print(f'{functools.reduce(lambda x, y: x*(y*10), [1, 2, 3, 4, 5]) = }')


