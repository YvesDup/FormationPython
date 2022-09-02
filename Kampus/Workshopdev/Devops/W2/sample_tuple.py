import sys

t = (10, "tttt")

d = {}
d[t] = 10
print(f'{d =}')

t1 = (10, [10, "zzz"], "tttt")
# d[t1] = 89
print(f'{d =}')
print(f'{hash(t1) = }')
