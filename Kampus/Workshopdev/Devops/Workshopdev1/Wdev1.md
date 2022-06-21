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
<style scoped> {
  font-size: 32px;
}
</style>

```py
def type_int():
    print("entiers")
    a = 10 # a est un entier
    al = 10_000_000_000_000_000
    print(a)
    print(al)
    b = a
    print(f'{b = }')
    print(f'{id(a) = }, {id(b) = }')
    ...
```
Ici au moment de l'affectation `b = a`, a et b sont 2 **références** qui pointent vers la même zone mémoire.
Les 'id' respectifs de chaque variable (ou objet) sont identiques

---
<style scoped> {
  font-size: 32px;
}
</style>

Je modifie `b`

```py
    print('je modifie b'.center(60, '-'))
    b += 10
    print(f'{a = }, {b = }')
    print(f'{id(a) = }, {id(b) =}')
```

Les 'ìd' de chaque sont différents. il s'agit donc de 2 zones mémoires différentes. 
Ce comportement est lié à une caractéristique associée au type (ici les `int`) qui est la notion de **mutabilité** (ou caractére muable) ou pas.

Les `int` sont des variables **immutables** (ou **immuable**), cad que le contenu est constant. Toute modification du contenu entraine la mise en place d'une nouvelle zone mémoire.

---
### Les booléens

```py
def type_bool():
    print("booléen")
    bot = True
    bof = False
    print(f'{bot = }, {bof = }')
```
les `bool` sont des variables **immuable**. Les 2 valeurs possibles sont des 'singletons', cad des valeurs uniques dns l'interpréteur Python.

---
### Les nombres à virgule

```py
def type_float():
    print('flottant')
    f = 0.5
    print(f'{f = }')
    f2 = 1.21e-19
    print(f'{f2 = }')
    print(f'Conversion vers un entier: {int(f) = Ò}')

```
Les `float` sont des variables **immuable**.

---
### Les complexes

```py
    def type_cplx():
        print("complexe")
        cplx = 2j + 9
        print(f'{cplx = }, {type(cplx) = }')
```
Les `complex` sont des variables **immuable**.

---
### la valeur nulle
```py
    def type_none():
        print("valeur nulle")
        n = None
        print(f'{n = } - {type(None)}')
```
La valeur `None` est un singleton **imumable**.

---
### Les chaines de caractéres

```py
```

les `str` sont des variables **immuable**.

---
## Les types avancés, composés.




