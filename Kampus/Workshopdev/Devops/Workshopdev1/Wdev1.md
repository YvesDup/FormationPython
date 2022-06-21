---
marp: true
theme: gaia
paginate: true
_paginate: false
header: ![w:150](img/logo_kampus.png)
footer: (c) yduprat@gmail.com
---
# Formation Python - ![h:100 w:280](img/logo_bnc.png)

Juin/Septembre 2022

_

![h:250](https://www.python.org/static/community_logos/python-logo-generic.svg)

---

# Workshopdev #1

Voici les thèmes abordés:

* les types simples.
* les types avancés, composés.

---
## Les type simples
<style scoped> {
  font-size: 30px;
}
</style>

|Types simples | Exemples |
|-------|----|
|nombres entiers| 10, 10_000_000|
|booléens| True, False |
|nombres à virgule| -3.14, 1.21e-19|
|nombres complexes| 2j + 9|
|chaines de caractères|'Hello', "world", """\thep\ntoi!!"""|
|tableau d'octets| bytearray('hello'), |
|valeur nulle| None |


---
### Les entiers

```py
    print("entiers")
    a = 10 # a est un entier
    al = 10_000_000_000_000_000
    print(a)
    print(al)
    b = a
    print(f'{b = }')
    print(f'{id(a) = }, {id(b) = }')
```
Ici au moment de l'affectation `b = a`, a et b sont 2 **références** qui pointent vers la même zone mémoire.
Les 'id' respectifs de chaque variable (ou objet) sont identiques

---
Je modifie `b`

```py
    print('je modifie b'.center(60, '-'))
    b += 10
    print(f'{a = }, {b = }')
    print(f'{id(a) = }, {id(b) =}')
```

Les 'ìd' de chaque sont différents. il s'agit donc de 2 zones mémoires différentes. 
Ce comportement est lié à une caractéristique associée au type (ici les `int`) qui est la notion de **mutabilité** (ou caractére muable).

---
### les nombres à virgule

```py
```


---
### Mutabilité (muable) / Immutabilité (immuable)


---
## les types avancés, composés.




