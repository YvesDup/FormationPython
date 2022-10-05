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
  font-size: 26px;
}
</style>
# Les tests unitaires en Python

Les tests unitaires en Python se font à travers des bibliothèques dédiées. Un framework de test `unittest` est fourni en standard en Python, mais il existe d'autres bibliothèques externes (donc à installer), comme:

+ pytest (qui sait jouer des tests `unittest`)
+ nose2
+ doctest

---
<style scoped> {
  font-size: 27px;
}
</style>
## La bibliothèque interne `unittest``

Cette bibliothèque, qui s'inspire de **JUnit**, comprend 4 parties principales:

+ l'environnement du test (préparation et finalisation)
+ la définiton du test unitaire
+ le regroupement de tests unitaires à exécuter ensemble
+ le lancement des tests

---
<style scoped> {
  font-size: 20px;
}
</style>

Voici un premier exemple simple:
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

---
<style scoped> {
  font-size: 21px;
}
</style>

### La définition d'un test unitaire

Ici il s'agit de tester via une méthode contenant un jeu d'instruction restreint, que le résultat produit est conforme aux attentes. La validité de cette méthode se fait via la fonction interne `assert` qui a été encapsulée dans la classe de regroupement des tests unitaires.

Ici, sont fournis via l'instance de cette classe les méthodes de vérification dont voici une liste non exhaustive:

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

---
<style scoped> {
  font-size: 22px;
}
</style>
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
---
<style scoped> {
  font-size: 26px;
}
</style>

### Le regroupement de tests

Ce regroupement de tests se fait dans une classe dédiée `unittest.TestCase` qui permet le lancement de tous les tests unitaires inclus. Dans l'exemple initial, il y a donc 3 tests unitaires pour la classe de regroupement `TestStringMethods`.

Un fichier de test unitaire Python peut contenir plusieurs instances de classes `unittest.TestCase`.

Il existe une classe de regroupement dédiée au tests unitaires de module asynchrone: `IsolatedAsyncioTestCase`

---
<style scoped> {
  font-size: 25px;
}
</style>
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

---
<style scoped> {
  font-size: 23px;
}
</style>

### La préparation des tests

Avant l'exécution de chaque test unitaire, il est possible d'appeler une fonction de préparation et après l'exécution de chaque test, une fonction de clôture est appelable également. Ces 2 fonctions correspondent à 2 méthodes de la classe `unittest.TestCase`:

+ avant:  `setUp`, toujours appélé mais si elle est échoue, le test n'est pas exécuté.
+ après: `tearDown`, toujours appelé même si le test échoue, sauf si le `setUp` échoue.

Il est possible de rajouter des fonctions (avec paramètres) via la méthode `addCleanup` qui seront appelées de manière inversée à leur ajout(LIFO) après le `tearDown` ou le `setUp`s'il échoue.
Ces fonctions sont en réalité appelées par la méthode `doCleanups`, qui d'ailleurs peut être invoquée à n'importe quel moment. 

Pour la préparation et la clôture de tests asynchrones, 2 méthodes dédiées existent et se comportent comme celles présentées en programmation synchrone, à savoir:

+ avant: `asyncSetUp`
+ après: `asyncTearDown`

---
<style scoped> {
  font-size: 21px;
}
</style>
### Et encore ....

#### L'exécution conditionnelle des tests

Contextuellement certains tests unitaires (ou regroupement de tests) peuvent être volontairement ignorés lors de leur lancement, comme par exemple:
+ Version de python inappropriée, OS d'exécution non ciblé
+ Absence d'une bibliothèque, test non valide

La non exécution du test est signalée par l'utilisation du décorateur `@unittest.skip` et ses autres formes.

```py
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     "not supported in this python version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass
```

---
<style scoped> {
  font-size: 21px;
}
</style>
#### La gestion des signaux

Ce module prend en compte la gestion des signaux en particulier les cas de **Ctrl+C**. [voir le chapitre dédié](https://docs.python.org/3.8/library/unittest.html#signal-handling)

#### Les mocks
Le module `unittest.mock` permet d'utiliser des `mock` dans les tests unitaires afin de simuler une fonction ou d'une classe sans pour autant les définir complétement.

Sont proposées principalement 3 classes:
+ `Mock`
+ `MagicMock`
+ `AsyncMock`

Voici un exemple simple de mock:
```py
m = unittest.MagicMock(return_value=3)
print(m()) # 3 
e = unittest.Mock(side_effect=TypeError('must be an integer'))
e() # raise a TypeError exception
o = Mock()
o.test = 10
print(o.test, ",", hasattr(o, 'u')) #  10, True
```


---
<style scoped> {
  font-size: 25px;
}
</style>
## Annexe

[La bibliothèque interne `unittest`](https://docs.python.org/3.10/library/unittest.html#unittest.TestCase)
[La bibliothèque interne `unittest.Mock`](https://docs.python.org/3.8/library/unittest.mock.html)
[la bibiothèque `pytest`](https://docs.pytest.org/en/7.1.x/)