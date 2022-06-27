# Notations en compréhension

La notation en compréhension est un mécanisme qui permet de contruire en une ligne un conteneur, une collection, une séquence ou un générateur.

## Création d'un conteneur, d'une collection ou d'une séquence

Par exemple, si je veux créer une liste de nombres négatifs à partir d'une liste référence, je vais devoir:
    Créer une liste vide
    Parcourir la liste de référence
    Et ajouter à la liste vide tous les éléments qui répondent aux critères de sélection
    exemple:

```python
    lst = [12, -5, 0, 26, 78, -6]
    neg = []
    for item in lst:
        if item < 0:
            neg.append(item)
    print(neg)
```

Ou bien j'utilise une notation en compréhension pour la création de la liste.

```python
    neg = [item for item in lst if item < 0]
    #           +---- loop ---+
    #                           +--alter--+
    #     +keep+
    print(neg)
```

Ces notations en compréhension peuvent s'utiliser pour la production:

* list
* dict
* set

Le corps de la notation en compréhension peut contenir comme instruction:

* une ou plusieurs boucles (Attention à la lisibité).
* un test avec plusieurs conditions liées par des opérateurs.

Les valeurs produites peuvent être de n'importe quel type, valeur simple ou élaborée

```python
# liste de tuple avec restriction 
l = [(item, item+2) for item in range(0, 100, 3) if item % 7 == 2]

# Liste de tuple avec boucle imbriquée ou iterools.product
l1 = [(a, b) for a in range(3) for b in 'ABC']
l1i = [(a, b, c) for a, b, c in itertools.product(range(3), 'ABC', (True, False, None))]

# dictionnaire simple 
d = {i:str(i) for i in range(5)}

# dictionnaire inversé
d_inv = {v:k for k, v in d.items()}

# dictionnaire à partir d'un dictionnaire avec une restriction
d2 = {k:d[k] for k in d if k % 2 == 0}

# set à partir d'une série de chiffre - 7 valeurs prduites mais seules 4 conservées au niveau du set
s = {x**2 for x in range(-3, 4, 1)}
```

## Création d'un générateur

Si je reprends un des exemples précédents

```python
l = [(item, item+2) for item in range(0, 100, 3) if item % 7 == 2]

# va devenir le générateur suivant
g = ((item, item+2) for item in range(0, 100, 3) if item % 7 == 2)

```

Dans ce cas, un les régles sur les générateurs s'appliquent, cad:
* la fonction `throw`
* la fonction `close`
