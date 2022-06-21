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
<style scoped> {
  font-size: 29px;
}
</style>

Les chaines de caractère en Python sont enregistrées en 'Unicode'. Python supporte donc tous les alphabets existants (environ 150).

```py
   def type_string():
        print("string")
        s1 = "hello"
        s2 = 'world !!'
        s3 = """hello
    salut,             yyyyy
    encore"""
        print(f'{s3 = }')
        s4 = s1
        print(f'{s1 = }, {s4 = }')
```
Les `str` sont des variables **immuable**. cela implique la modification d'une chaine entraine la création d'une nouvelle chaine de caractères.

---
#### Opérations sur les chaines

Les `str` sont des séquences. C'est à dire qu'il est possible:
+ connaitre sa longueur: `len(s)`.
+ savoir si élément est contenu dans la chaine: `'x' in s`
+ parcourir ses éléments: `for item in s: print(item)`
+ d'avoir un accès direct à l'un des éléments via un indice: `s[0]` ou `s[-2]`.
+ extraire des sous-chaine avec le mécanisme du `slicing`.

---
#### le slicing
<style scoped> {
  font-size: 29px;
}
</style>

Le `slicing`est un mécanisme qui permet d'extraire des sous-séquences d'une séquence en spécifiant, un intervalle et un pas, comme suit avec le tryptique:
+ start: indique la position de départ,
+ stop: qui indique la position de fin, exclue,
+ step: qui indique dans cet interval la fréquence des caractères conservés

Ces 3 valeurs, dans cet ordre sont associées avec l'opérateur `:` comme suit: `start:stop:step`. Par exemple la sous-chaine suivante va prendre à partir du 2° caractére, jusqu'a 5° inclus, 1 caractère sur 2.
```py
    s = 'rodondindron'
    print(f'{s = }, {s[1:5:2] = }') # -> 'oo'
```

---
<style scoped> {
  font-size: 29px;
}
</style>

**Slicing suite (1/2)**

Quand une des valeurs de l'intervalle est omise, la valeur retenue est alors `None`. La valeur par défaut pour le pas est `1`.

Quelques exemples de slicing:

+ `s[::2]`: la sous-chaine contient 1 caractère sur 2 provenant de `s`.
+ `s[3:]`: la sous-chaine de `s` qui démarre au 4° caractére.
+ `s[:3]`: la sous-chaine de `s` qui contient les 3 premiers caractéres.

---
<style scoped> {
  font-size: 29px;
}
</style>

**Slicing suite (2/2)**

Comme pour les accès directs, des indices négatifs peuvent être utilisés dans les valeurs du tryptique

+ `s[-2:]`: les 2 derniers caractéres de `s`.
+ `s[::-1]`: la chaine `s` est inversée.
+ `s[-2:0:1]`: une chaine vide.

Le mécanisme du slicing se fait via une classe `slice` qui peut utilisée via une instance à la place de la syntaxe `s[1:5:1]` comme ceci:
+ `s[slice(1, 5, 1)]`
+ `sl = slice(1, 5, 1); s[sl]`

---
<style scoped> {
  font-size: 29px;
}
</style>

#### Quelques méthodes sur les chaines

* `s.count('a')` : compte les occurrences de 'a' sans s.
* `s.split(sep)`: produit une liste de sous-chaîne.
* `s.find('xyz')`: cherche la positon de la chaine 'xyz' dans s.
* `s.upper()`, `s.lower()`, `s.title()`: modifie la casse de la chaine.
* `s.starswith('ab')`: indique si la chaine démarre avec la chaine 'ab'. Il existe aussi la méthode `endswith`.


---
## Les types avancés, composés

Voici un rappel de ces types

Types composés | Exemples|
|-------|----|
| listes  | [], [10, True, "string", 1.22]|
|dictionnaires| {"dix":10, 20:"XX"}|
| ensembles | {10, "20", 30.0},  {(1,"un"), 'I'}|
| tuples | ("un",),  (10, True, "string", 1.22)|


---
### Les listes

<style scoped> {
  font-size: 22 px;
}
</style>

Les listes correspondent à un tableau dont le contenu est hétéroclite en terme de type. Par exemple:

```py
        # liste
        print('liste')
        l = []
        print(f'{l = }, {type(l) = }')
        l = [10, "vingt", 20.000 , None]
        print(f'{l = }')
```
Les `list` sont des variables **muable**. Cela implique que la modification du contenu de la liste n'entraine pas la création d'une nouvelle liste.

---

