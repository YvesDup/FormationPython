class Obj:
    pass

o1 = Obj()
print(f'{o1 = }')
o2 = o1 
print(f'{o1 is o2 =}')

l = [o1]
l.append(o2)
print(l)