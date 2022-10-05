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
# Les tests unitaires en Python

Les tests unitaires en Python se font à travers des bibliothèques dédiées. 
Un framework de test `unittest` est fourni en standard en Python, mais il existe d'autres bibliothèques externes (donc à installer), comme:

+ pytest (qui sait jouer des tests `unittest`)
+ nose2
+ doctest

## La bibliothèque interne `unittest``

Cette bibliothèque, qui s'inspire de **JUnit**, comprend 4 parties principales:

+ le jeu de test (préparation et finalisation)
+ le test unitaire
+ le regroupement de tests unitaires à exécuter ensemble
+ le lancement des tests

Voici un exemple:
```py
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```
Cet exemple est enregistré dans le fichier test_strings.py
La vérification se fait en exécutant ce script comme suit:
```zh
python test_scripts.py
```

### Le test unitaire

La validité d'un test unitaire dans ce module est basée sur la fonction interne `assert` qui a été encapsulée dans la classe de regroupement des tests unitaires.

Ici, sont fournis via l'instance de cette classe les méthodes de tests dont voici une liste non exaustive:

| assertion | exemple |
| --------------- | ------- |
| self.assertTrue | self.assertTrue(1 == 2-1) |
| self.assertEqual | self.assertEqual(10 == 10+9) |
| self.assertIs| t = True ; self.assertIs(t, True)|
| self.assertIsNone| self.assertIsNone(None)|
| self.assertIsinstance| self.assertIsinstance(10, int) |
| self.assertIn| self.assertIn(10, (20, True, "10", 10)) |
| self.assertGreaterEqual| self.assertGreaterEqual(10, 5)|
| self.assertSequenceEqual| st.assertSequenceEqual([10], (10,))|
| self.assertDictEqual |self.assertDictEqual({1:"1", 2:"2", 3:"3"}, dict(((2, "2"), (3, "3"), (1, "1"))))|

Le test pour vérifier qu'une exception est bien levée se fait via avec un gestion de contexte comme suit:
```py
...
    def test_catch_error(self):

        with self.assertRaises(TypeError) as cm:
            ['hello', 10]["10"]

        with self.assertRaisesRegex(TypeError, 'list indices'):
            ['hello', 10]["10"]
...
```
### Le regroupement de tests

Ce regroupement de tests se fait dans une classe dédiée `unittest.TestCase` qui permet le lancement de tous les tests unitaires inclus. Dans l'exemple initial, il y a donc 3 tests unitaires pour la classe de regroupement `TestStringMethods`.

Un fichier de test unitaire Python peut contenir plusieurs instances de classes `unittest.TestCase`.

Il existe une classe de regroupement dédiée au tests unitaires de module asynchrone: `IsolatedAsyncioTestCase`

### Le lancement des tests

Le lancement des tests peut se faire en ligne de commande avec l'appel au module `unittest` via le lancement de l'interpréteur avec l'option `-m`. Cela permet de lancer les tests avec plus de possibilités que globalement. Voici quelques options:

```zh
echo 2 fichiers avec tous les regroupements de tests
python -m unittest test_string test_cercle 

echo le fichier 'test_string' avec juste la classe `TestStringMethods`
python -m unittest test_string.TestStringMethods

echo le fichier 'test_string' avec juste le test 'test_upper' de la classe `TestStringMethods`
python -m unittest -v test_string.TestStringMethods.test_upper

echo le fichier 'test_string' avec juste les tests qui contiennent ùpper' dans leur nom
python -m unittest -v -k upper test_string

echo Les autres options possibles
python -m unittest -h
```

### La préparation des tests

Avant l'exécution de chaque test unitaire, il est possible d'appeler une fonction de préparation et après l'exécution de chaque test, une fonction de clôture est appelable également. Ces 2 fonctions correspondent à 2 méthodes de la classe `unittest.TestCase`:

+ `setUp`, toujours appélé mais s'il est échoue, le test n'est pas exécuté.
+ `tearDown`, toujours appelé même si le test échoue, sauf si le `setUp` échoue.

Il est possible de rajouter des fonctions (avec paramètre) via la méthode `addCleanup` qui seront appelées de manière inversée (LIFO) après le `tearDown` ou le `setUp`s'il échoue. Ces fonctions sont en réalité appelé par la méthode `doCleanup`, qui d'ailleurs peut être invoqué à n'importe quel moment. 

Pour la préparation et la clôture de tests asynchrones, 2 méthodes dédiées existent et se comportent identiquement à celles déjà présentées, à savoir:

+ `asyncSetUp`
+ `asyncTearDown`

### Les compléments

Le module `unittest.mock` permet de position des `mock` pour les tests unitaires afin de pouvoir rejouer un comportements d'une fonction ou d'une classe.
Sont proposées 2 classes:
+ `Mock`
+ `MagicMock`
+ 'AsyncMock'

## La bibliothèque `Pytest`


## Annexe

[La bibliothèque interne `unittest`](https://docs.python.org/3.10/library/unittest.html#unittest.TestCase)
[La bibliothèque interne `unittest.Mock`](https://docs.python.org/3.8/library/unittest.mock.html)
[la bibiothèque `pytest`](https://docs.pytest.org/en/7.1.x/)