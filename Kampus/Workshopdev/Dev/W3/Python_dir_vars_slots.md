=== les fonctions internes `dir` et `vars`, le nom interne `__slots__`


Un objet en `Python` est toujours l'instance, un exemplaire d'une classe. 1 est une instance de la classe `int`, 'hello world' est un exemplaire de la classe `str`.
La classe décrit les attributs et méthodes qui seront attachés à chaque objet.

La fonction interne `dir` peut s'appliquer soit sur une classe, soit sur un objet de cette classe. Voici une classe Test:

```python
class Test:
	"""This is a class 'Test'
	"""

	a_st = 0

	def __init__(self, x: int):
		self._x = x
		self._d = {}

	def method1(self, t: tuple):
		pass
```

en exécutant `dir(Test)`, on obtient une liste qui contient:
* toutes les méthodes de la classe, y compris celles héritées
* tous les noms interne de la classe: `__class__`, `__doc__`, `__dict__`, `__module__`, `__weakref__`
* toutes les variables statiques de la classe: `a_st` 

et un objet de classe Test
```py
	t = Test(10)
```

+ En exécutant `vars(t)`, on obtient toutes les attributs de l'objet. 
+ En exécutant `dir(t)` on obient les infos de `dir(Test)` + celles de `vars(t)`:
+ au final, `assert set(dir(t)) == (set(dir(t.__class__)) | set(vars(t))`)

Ici pour chaque objet `Test` créé, un dictionnaire contenant les attributs est présent. C'est ce dictionnaire qui permet de 'jouer' dynamiquement avec les attributs

==== nom interne `__slots__`

Il est possible de supprimer ce dictionnaire en définissant ce nom interne `__slots__` et en lui attribuant le nom des attributs de la classe sous la forme d'un `tuple` de `str`

Sur la classe précédemment décrite, ajoutons cette directive comme suit:

```python
class Test:
	"""This is a class 'Test'
	"""
	__slots__ = ("_x", "_d")

	a_st = 0

	def __init__(self, x: int):
		self._x = x
		self._d = {}

```

Ainsi, la possiblilité de 'jouer' dynamiquement avec des attributs qui ne sont pas listés dans la variable `__slots__`ne sera plus possible. 
De plus, l'entrée `__dict__` étant supprimée (voir la fonction interne `dir())`, l'occupation mémoire de chaque objet sera réduite.

Cependant, l'ajout dynmique pourra encore possible, si une entrée '__dict__' est ajoutée au `__slots__` comme suit: 
```python
	class ....:
		__slots__ = ("_x", "_d", "__dict__")
```

A noter:

* La directive `__slots__` supprime le `__dict__` de la structure interne de la classe et de l'objet.
* Le `__slots__' n'est pas hérité comme toute variable statique,
* Quand une classe est définie à partie d'une classe qui contient `__slots__`, aucune attribut n'est hérité.