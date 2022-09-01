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
<style scoped> {
  font-size: 22px;
}
</style>
# Classe en Python

Cette notion, correspond à un regroupement de données et de fonctions qui manipulent ces données.
Les données de la classe sont appelées attributs. Les fonctions sont appelées méthodes

Voici un exemple simple:

```python
class Obj:
    pass

o = Obj()
print(o)
```
Un objet crée avec des paramètres:
```python
class Test:

    def __init__(self, val):
        self.val = val

t = Test() # ne fonctionne pas car un paramètre positionnel
t = Test(10)
print(t)
```
---
<style scoped> {
  font-size: 22px;
}
</style>

Le paramètre `self` est présent comme premier paramètre dans chaque définition de mèthode.
Il représente l'instance de l'objet. Sans ce paramètre, il est impossible de travailler sur un objet.

Les méthodes préfixées et suffixées par `__` sont appelées des méthodes magiques ou `dunder`
(**d**ouble **under**score).

L'appel à une méthode ou l'accès à un attribut se fait toujours via l'objet et l'opérateur **`.`** comme suit:

```python
class Obj:
    def __init__(self, val):
        self.val = val
        self.vals = []

    def calcul_moyenne(self):
        return sum(self.vals / len(self.vals) if len(self.vals) > 0 else 0)

a = Obj(10)
a.val = 10 # Affectation d'une valeur à un attribut
x = a.calcul_moyenne() # appel à une méthode
```

---
<style scoped> {
  font-size: 22px;
}
</style>

## Création d'un objet

Un objet représente un exemplaire (ou instance) de la classe. Lors de la création de l'objet
de la mémoire est allouée, puis l'appel à une méthode spéciale `__init__` est réalisé.
Ici cette méthode indique la liste des paramètres attendus, obligatoires ou pas.

```python

class Obj:

    def __init__(self, val, nom):
        self.val = val
        self.nom = nom

# La création d'un objet de class Obj se fait comme suit:

a = Obj(10, 'cerise')
print(a.val, "et", a.nom)
```

---
<style scoped> {
  font-size: 22px;
}
</style>
## Gestion des attributs

Les attributs d'un objet en python peuvent être gérés de manière dynamique. Cad que l'attribut d'un objet python peut être supprimé, modifié ou ajouté à n'importe quel moment

```python

# sur l'objet précédemment crée
a = Obj(10, 'cerise')

# affiche tous les attribust d'un objet
print(vars(a))

a.nouveau = 'bonjour'
a.val = None
del a.nom

# affiche de nouveau tous les attribust d'un objet
print(vars(a))
```

---
<style scoped> {
  font-size: 25px;
}
</style>
## Méthodes spéciales de mise en forme

En Python, certaines méthodes permettent de représenter les objets sous forme de chaine de caractères: 

+ `__str__`: appelée lors du traitement de chaine de caractères et de l'affichage
+ `__repr__`: appelée lors de la mise en forme d'objet sous forme de composition: par exemple des objets inclus dans une liste

Ces méthodes sont également appelées lors du formatage de chaine via l'opérateur `!`, à travers la fonction `.format` ou le `f""`:

* {"ee"!s}
* {"ee"!r}

---
<style scoped> {
  font-size: 22px;
}
</style>
## Portée des variables et methodes.

En Python, les attributs et méthodes d'un objet sint **publiques**. La notion d'attribut (et de méthode) privée est gérée par la mise en place sous forme d'un préfixe sur le nom des attrinuts ou méthodes. 

**Attention:** il n'y a pas de mécanisme de blocage, de contrôle par rapport à cette convention entre developpeur Python.

```py
class Obj:
  def __init__(self, name, val):
    self._name = name
    self._val = val 

  def get_name(self) -> str:
    return self._name # appel à un attribut privé pour une méthode publique

o = Obj('Yves', 57)
print(f"{o._name = } et {o.get_name() = })
```

Un attrinut contenant un `__` comme préfix de son nom, n'est accessible depuis l'exterieur de l'objet. Par exemple, si on ajoute dans la methode `__init__` l'instruction `self.__uuid = str(uuid.uuid4())`.
* L'accès à  `o.__uuidd` engendre une erreur.

---
<style scoped> {
  font-size: 22px;
}
</style>
## Variables et methodes de classe

Les variables et méthodes de classes sont des éléments rattachés à la classe qui sont partagés par toutes les instances de la classe. De plus ces éléments sont accessibles même si aucune instance n'a été créée

Ils sont déclarés dans l'entête de classe avant toutes méthodes.
Les méthodes statiques sont décorées avec le décorateur @staticmethod

Tout appel à un élément statique se fait via le nom de la classe et l'opérateur `.`. Voici un exemple:

```python

class Test:
    # variable de classe
    cpt = 0
    # constante Python de la classe 
    TOP, BOTTOM = range(2)

    ...
    def methodeinstance(self, *args):
        """
        """
        Test.cpt += 1
```

---
<style scoped> {
  font-size: 22px;
}
</style>

Voici l'ajout d'une méthode statique.

```py
    # le self est absent
    @staticmethod
    def static_method(a, b, c)
        """
        """
        if Test.cpt == Test.TOP:
            # self n'est pas défini
            pass

ret = Test.static_method(1, 2, 3)
print(Test.cpt)
Test.cpt += 1
print(Test.cpt)

t = Test(10)
print(t)
```

---
<style scoped> {
  font-size: 22px;
}
</style>
## Héritage

Ce mécanisme propre à la programmation objet, permet de définir une nouvelle classe à partir d'une autre. Cela veut dire que cette nouvelle classe ne sera pas vierge en terme d'attributs et de méthodes mais qu'elle va récupérer tout ce qui a été définie dans la classe dont elle hérite.

### Mise en oeuvre de l'héritage

* spécialisation
* généralisation


---
<style scoped> {
  font-size: 22px;
}
</style>
### Héritage par défaut

Ce mécanisme est déjà en place, mais de manière transparente, lors de la création d'une classe de base, comme suit:

```python
class A:
    pass

print(dir(A))
```

Ici des méthodes sont définies alors que nous n'avons encore rien défini au niveau de la classe A

Pour connaitre l'arbre d'héritage d'une classe, il existe un variable interne `__mro__` qui renvoie la liste de toutes les classes héritées.

```python
class A:
    pass

print(A.__mro__)
```

Ici la classe `object` de Python est présente. C'est la classe de base de toute classe en Python

---
<style scoped> {
  font-size: 20px;
}
</style>
### Héritage simple

Pour indiquer de quelle classe une classe hérite, il suffit d'indiquer son nom lors de la définition de la classe, comme suit:

```python
class A:
    pass
class B(A): # j'hérite de A
    pass
class C(B): # j'hérite de B
    pass

print(B.__mro__)
# renvoie un tuple qui contient toutes les classes héritées
# directement ou via les classes héritées intermédiaires
# ('<class B>', '<class A>', '<class object>')

print(C.__bases__)
# Renvoie un tuple qui contient les classes parentes
# ('class B',)
```

Ici l'ordre des classes dans le tuple est important car l'accès à un attribut d'un objet se fera toujours en allant parcourir ce tuple. Dès que le mécanisme d'héritage trouve l'attribut ou la méthode recherché, il arrête de parcourir ce tuple.

En règle générale, il est toujours prudent d'étudier la faisabilité de la composition avant de décider d'un héritage

---
<style scoped> {
  font-size: 26px;
}
</style>

#### Appel en cascade à la méthode `__init__`.
Lors de la phase d'initialisation d'un objet, la mèthode `__init__` est invoquée. C'est cette méthode qui va créer et définir les attributs de chaque objet en fonction des paramètres formels.
Ainsi dans une classe héritée, l'appel à la méthode `__init__` de la classe héritée est toujours bienvenu pour pouvoir récupérer les attributs créés dans la phase d'init de de cette classe.

L'appel à cette méthode peut se faire via:

+ un appel direct de la méthode `__init__` de la classe héritée:
 `BaseClass.__init__(self, arg1, arg2, ...)`.
+ un appel via la fonction interne `super()` qui trouvera elle même la classe 'mère':
`super().__init__(arg1, arg2, ...)`.
---
<style scoped> {
  font-size: 26px;
}
</style>

### Héritage multiple

L'héritage multiple permet d'hériter de plusieurs classes, et ainsi de leurs attributs et méthodes respectives. Ainsi l'ordre dans lequel est spécifié les classes hérités est important. Il sera le même que celui du tuple issu de l'attribut interne `__mro__`

Examinons ici, le mécanisme d'héritage multiple, avec les classes A et B telles que définies précédemment:

Ici nous définissons une classe C qui hérite de B et A

```python
class C(B, A):
    pass

print(C.__mro__)
# renvoie un tuple avec la liste des classes suivantes; 
# A préciser
```

---
<style scoped> {
  font-size: 26px;
}
</style>

### Héritage multiple
Ici nous définissons une classe D qui hérite de A et B

```python
class D(A, B):
    pass

print(D.__mro__)
# renvoie un tuple avec la liste des classes suivantes; 
# A préciser
```

**Références**:

[Héritage multiple](https://stackoverflow.com/questions/47808926/why-is-this-an-ambiguous-mro)
[Héritage multiple erreur](https://stackoverflow.com/questions/29214888/typeerror-cannot-create-a-consistent-method-resolution-order-mro)

---
<style scoped> {
  font-size: 24px;
}
</style>
### Dynamicité des attributs: mécanisme interne, première approche

Il existe 4 fonctions internes en python qui permettent de savoir si un attribut ou une méthode existe dans un objet:

+ `hasattr` qui vérifie si un nom d'attribut existe: `hasattr(obj, 'cpt')`.
+ `getattr`qui renvoie la valeur de l'attribut: `getattr(obj, 'cpt')` équivalent à `obj.cpt`.
+ `setattr` qui créer ou modifier la valeur d'un attribut: `setattr(obj, 'cpt', 10)` équivalent à `obj.cpt = 10`.
+ `delattr` qui supprime un attribut et sa valeur: `delattr(obj, 'cpt')` équivalent à `del obj.cpt`.

Ces fonctions travaillent sur le stockage interne des attributs dans la variable interne de chaque obejt: `__dict__`.  `getattr(o, 'val')` est équivalent à `o.__dict__['val']`
**A noter**: la dynamicté des attributs (et méthodes) se joue sur chaque instance d'un objet.

---
<style scoped> {
  font-size: 22px;
}
</style>
## Annexe

### Attribut interne **magic** ou **dunder**

Description:

* `__name__` : classe.__name__ renvoie le nom de la classe

* `__mro__` : classe.__mro__ renvoie un tuple qui contient la liste des classes héritées

* `__base__`: classe.__base__ renvoie la classe parente 

* `__annotations__` : classe.__annotations__ ou objet.__annotations__ Renvoie les annotations de la classe interrogée

* `__doc__` : classe.__doc__ ou objet.__doc__ Renvoie la docstring de la classe interrogée

* `__dict__` : classe.__dict__ Renvoie un dictionnaire des méthodes, variables statiques de la classe

* `__dict__` : objet.__dict__ Renvoie un dictionnaire des méthodes et attributs disponibles pour l'objet

* `__class__` : objet.__class__ permet de connaître à partir de quelle classe l'objet a été créé

* `__module__` : Permet de connaître le nom du module dans lequel est codée une fonction ou une classe.

---
<style scoped> {
  font-size: 22px;
}
</style>

### Correspondance entre fonctions internes et méthodes magiques

voici un aperçu des principales méthodes

* len     -> __len__
* obj     -> __bool__

* []    -> __getitem__ / __setitem__
* .     -> __getattribute__ / __getattr__

* in    -> __contains__
* ==,!= -> __eq__, __ne__

* ()    -> __call__

* {}    -> __hash__ , key of dict, value of set (internal)
* '-'     -> __neg__, __pos__ unary operator

* '+'     -> __add__, __radd__
* '+='    -> __iadd__

---
<style scoped> {
  font-size: 22px;
}
</style>
* '**'    -> __pow__

* &, |    -> __and__, __or__
* cast  -> __int__, __float__

* ctor    -> __new__, __init__ * exemple du singleton
* dtor  -> __del__

* for   -> __iter__, __next__

* with  -> __enter__, __exit__

* str   -> __str__ via {'toto':>30s}
* repr  -> __repr__ via {'toto':^80r}

### Référence

* see: 'http://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html'
