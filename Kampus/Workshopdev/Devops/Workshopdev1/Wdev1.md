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

Les 'id' de chaque objets sont différents. il s'agit donc de 2 zones mémoires différentes. 
Ce comportement est lié à une caractéristique associée au type (ici les `int`) qui se nomme: la **mutabilité** et sa négation, l' **immutabilité**.

Les `int` sont des variables **immutable** (ou **immuable**), cad que le contenu est constant. Toute modification du contenu entraine la mise en place d'une nouvelle zone mémoire.

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
    x = int(f)
    print(f'Conversion vers un entier: {x = }, {type(x) = }')

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
Les `str` sont des variables **immuable**. Cela implique que la modification d'une chaine entraine la création d'une nouvelle chaine de caractères.

---
#### Opérations sur les chaines

Les `str` sont des séquences. C'est à dire qu'il est possible de:
+ connaitre sa longueur: `len(s)`.
+ savoir si élément est contenu dans la chaine: `'x' in s`
+ parcourir ses éléments: `for item in s: print(item)`
+ d'avoir un accès direct à l'un des éléments via un indice: `s[0]` ou `s[-2]`.
+ extraire des sous-chaines avec le mécanisme du `slicing`.

---
#### le slicing
<style scoped> {
  font-size: 29px;
}
</style>

Le `slicing` est un mécanisme qui permet d'extraire des sous-séquences d'une séquence en spécifiant, un intervalle et un pas, comme suit avec le tryptique:
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
* `s.startswith('ab')`: indique si la chaine démarre avec la chaine 'ab'. Il existe aussi la méthode `endswith`.


---
## Les types avancés, composés
<style scoped> {
  font-size: 29px;
}
</style>

Voici un rappel de ces types

Types composés | Exemples|
|-------|----|
| listes  | [], [10, True, "string", 1.22]|
|dictionnaires| {"dix":10, 20:"XX"}|
| ensembles | {10, "20", 30.0},  {(1,"un"), 'I'}|
| tuples | ("un",),  (10, True, "string", 1.22)|



---
<style scoped> {
  font-size: 30px;
}
</style>
### Les listes

Les listes correspondent à un tableau dont le contenu est hétéroclite en terme de type. Par exemple:

```py
        # liste
        print('liste')
        l = []
        print(f'{l = }, {type(l) = }')
        l = [10, "vingt", 20.000 , None]
        print(f'{l = }')
```
Les `list` sont des variables **muable**. La liste étant une séquence, toutes les manipulations vues au niveau des `str` peuvent s'utiliser ici.


---
<style scoped> {
  font-size: 30px;
}
</style>
#### Opérations sur les listes

Les modifications de liste peuvent se faire comme suit:

```py
        print("modification")
        l.append(False)
        l.insert(2, "Hooper")
        print(f'{l = }')
        print(False in l)
        l.remove(10)
        print(f'{l = }')
        l[1] *=10
        print(f'{l = }')
        l.extend('ABC')
        print(f'{l = }')
```
La méthode `extend` prend un `iterable` en entrée et ajoute tous ses éléments 1 par 1 en fin de liste. Cela correpond à une concaténation de listes.

---
<style scoped> {
  font-size: 25px;
}
</style>

#### Parcourir une liste 

Le parcours d'une liste peut se faire avec l'instruction `for`:

```py
        print("parcours de la liste")
        for item in l:
            print(item)
        print("---")

        print("affiche juste les chaines de caractères")
        for item in l:
            if isinstance(item, str):
                print(item)
        print("---")

        print("possible mais moins efficace")
        for i in range(len(l)):
            print(l[i])
        print("---")
```
Une instruction `while` peut aussi s'utiliser ici mais sera de la même efficacité que le dernière proposition ci-dessus.

---
<style scoped> {
  font-size: 29px;
}
</style>

#### Inverser ou trier une liste

```py
        print("Inverser une liste")
        print(l[::-1])

        print("Trier une liste")
        l1 = [10, 0, -5, True, 2.89, -1.2e-19]
        print(l1)
        l1.sort()
        print(l1)
```

---
<style scoped> {
  font-size: 27px;
}
</style>

#### Cas d'une liste contenant une autre liste (ou un autre objet muable)

```py
        print("append a list")
        l1 = [-5,  -1.2e-19,, 0, True, 2.89, 10]
        print(l1)
        l = [True, 20.0, "Allez", None]
        print(l)
        l1.append(l)
        print(l1)
        print("------", id(l1), id(l), id(l1[-1]))
```

Ici la liste `l` est ajoutée telle quelle à la fin de la liste `l1`. Cet ajout ne se fait pas sous la forme d'une copie de la liste `l`, mais sur l'ajout d'une référence à `l`.

```py
        l.remove(None) # l1[-1].remove(None)
        l.remove(20.0) # l1[-1].remove(20.0)
        print(l1)
```
Comme `l` est modifiée, cela sera impacté dans la liste `l1`.

---
<style scoped> {
  font-size: 27px;
}
</style>
#### Copie d'une liste (ou d'un objet muable)

Dans la mesure où une liste peut contenir d'autres objets **muables**, la copie d'une liste peut se faire de 2 façons:

+ une copie en surface où seul le premier niveau d'éléments est dupliqué.
+ une copie profonde où chaque élément contenu est dupliqué, ansi que ses sous-éléments. Voici donc ci-dessous, les 2 modes:
```py
    # copy
        print("copy")
        import copy
        lc = copy.copy(l1) # copy.copy() copie de surface
        print(f'{id(l1) = } , {id(lc) = }')
        print(f'{id(l1[-1]) = } , {id(lc[-1]) = }')
        lc = copy.deepcopy(l1) # copy.deepcopy() copie profonde
        print(f'DC {id(l1) = } , {id(lc) = }')
        print(f'DC {id(l1[-1]) = } , {id(lc[-1]) = }')

```

---
<style scoped> {
  font-size: 26px;
}
</style>
### Les dictionnaires

Les dictionnaires représentent une structure de données enregistrées sous la forme d'une clé et d'une valeur associée. L'accès à la valeur se fait toujours par la clé. Exemple:

```py
    def type_dict():
        # dictionnaire
        d = {} # dictionnaire 
        d = { "1": 10, "2": [10, 20] , 4: "quatre" }
        print(f'{d = }')
        print(f'{4 in d = }')
        print(f'{d["1"] = }') # accès à la valeur de la clé "1"

```
Les `dict` sont des variables **mutable**. Un dictionnaire n'est pas ue séquence mais un tableau associatif.

Les clès d'un dictionnaire sont hétéroclites en terme de type et chaque valeur de clé doit être d'un type '**immuable**'.

---
<style scoped> {
  font-size: 28px;
}
</style>
#### Accès aux valeurs d'un dictionnaire

```py
        print(f'{4 in d = }')
        print(f'{d[4] = }')
        d[4] = 4
        print(f'{d[4] = }')
        print(f'{d.get(5, "Pas de clé") = }')
```
 Pour savoir si une clé existe, l'opérateur `in` est utilisable. 
 L'accès à une valeur se fait via sa clé, 2 manières possibles:
 * `d[4]`: ici la clé doit exister
 * `d.get(5, "Pas de clé")`: si la clé, n'existe pas, la valeur "pas de clé" est renvoyée.

---
<style scoped> {
  font-size: 28px;
}
</style>
#### Insertion et modification des couples (clé, valeur)

La modification d'une valeur pour une clé déjà existante, donc avec déjà une valeur associée, se fait avec l'opérateur d'affection `=`.
C'est l'exemple ci-dessus `d[4] = 4`.

L'ajout d'un nouveau couple se fait avec l'instruction suivante:
`d["x"] = [] # liste vide`

La mise à jour d'un dictionnaire peut se faire à partir d'un autre dictionnaire avec la méthode `update` comme suit:
```py
        print(d)
        dd = {5:"cinq", '1':["un", "I", 1], True:"VRAI !!"}
        print(dd)
        d.update(dd) 
        print(d)

```

---
<style scoped> {
  font-size: 28px;
}
</style>

#### Accès à la totalité des données

Il existe 3 méthodes d'accès aux données d'un dictionnaire:

```py
        print("accès globaux aux donnés")
        print(d.keys())
        print(d.values())
        print(d.items())
```
+ `d.keys()` : renvoie toutes les clés.
+ `d.values()` : renvoie toutes les valeurs.
+ `d.items()` : renvoie tous les couples 'clé, valeur' sous la forme d'une liste de tuples à 2 entrées.

Le parcours d'un dictionnaire se fait toujours via l'une de ses 3 méthodes.

---
<style scoped> {
  font-size: 28px;
}
</style>

#### Parcours d'un dictionnaire

```py
       print("___"*20)
        for k in d:  # <=> d.keys(): 
            print(k, '->', d[k])

        print("___"*20)
        for item in d.items():
            print(item[0], '->', item[1])
        print("___"*20)
        for k, v in d.items():
            print(k, '->', v)
```

Il n'est pas possible de parcourir un dictionnaire avec une boucle `while`.

---
<style scoped> {
  font-size: 28px;
}
</style>
#### Suppression d'une clé

Il existe principalement 2 façons de procéder:
```py
        del d[2.01]
        v = d.pop(4)
        print(v)
```

---
<style scoped> {
  font-size: 27px;
}
</style>
### Les ensembles

Les ensembles sont des collections particulières qui ne contiennent que des objets **immutables** sans doublons. Ils mettent à disposition les opérations ensemblistes suivantes:

+ Union
+ Intersection
+ Différence
+ Différence asymétrique
+ Sur-ensemble
+ Sous-ensemble
+ Ensembles disjoints

Les ensembles sont des objets **mutable**.

---
<style scoped> {
  font-size: 27px;
}
</style>
#### La gestion des ensembles

Voici un exemple d'ensemble:

```py
        s1 = {10, 20, 40}
        print(f'{s1 = }')
        s1.add(80)
        print(f'{s1 = }')
        print(80 in s1)
        s1.add(10)
        print(f'{s1 = }')
        s1.remove(80)
```
+ `s1.add` pour ajouter un élément
+ `s1.remove` pour supprimer un élément
+ `80 in s1` ppur savoir si `80`esty dans s1.

un ensemble est parcourable avec une instruction `for`.

---
<style scoped> {
  font-size: 28px;
}
</style>
#### Les opérations ensemblistes

```py
   #operation ensembliste
        print(f'{s1=}')     # s1 = {10, 20, 40}
        print(f'{s2=}')     # s2 = {20, 30, 60, 60}
        print(f'{s1 & s2 = }')
        print(f'{s1 | s2 = }')
        print(f'{s1 ^ s2 = }')
        print(f'{s1 - s2 = }')
        print(f'{s2 - s1 = }')
        print({10, 20}.issubset(s1))
        print({100, 25}.isdisjoint(s1))
        print({10, 20, 40, 50}.issuperset(s1))

```
