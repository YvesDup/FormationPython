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

# Training2

Voici les thèmes abordés:

* La gestion des erreurs.
* Les bibliohèques externes.
* Les environnements virtuels.
* Les annotations de types.
* Les bonnes pratiques

---
<style scoped> {
  font-size: 19px;
}
</style>
## La gestion des erreurs

En python, la gestion des erreurs est basée sur le mécanisme des exceptions. Lorsqu'une erreur intervient, un message spécifique s'affiche en indiquant:
+ le nom de l'erreur
+ la localisation de l'erreur avec:
  + un nom de fichier, un numéro de ligne et un nom de fonction
+ la liste de tous les appels des fonctions précédents l'erreur

```python
Traceback (most recent call last):
  File "C:\Users\robert\Desktop\hanoi_towers.py", line 11, in <module>
    move(n, 'A', 'B', 'C')
  File "C:\Users\robert\Desktop\hanoi_towers.py", line 5, in move
    move(disk-1, _from, _aux, _to)
  File "C:\Users\robert\Desktop\hanoi_towers.py", line 5, in move
    move(disk-1, _from, _aux, _to)
  File "C:\Users\robert\Desktop\hanoi_towers.py", line 7, in move
    uu
NameError: name 'uu' is not defined

```

Il faut lire ces informations en sens inverse, du bas vers le haut

Ici, dans notre exemple, le script python s'est arrêté. Cependant le programmeur peut décider si programme continue, ou pas.

---
<style scoped> {
  font-size: 24px;
}
</style>

### Le mécanisme des exceptions

Ce mécanisme est basé sur le tryptique de bloc `try, except, else`. Les 2 premiers blocs sont obligatoires. Il peut y avoir plusieurs blocs `except`, mais un seul bloc `try` et un seul bloc `else`, toujours en dernière position. Voici un exemple:

```python
try:
	a = 10
	b = "20"
	a + b

except Erreur1:
	print('Il y a soucis sur Erreur1')

except Erreur2:
	print('Il y a soucis sur Erreur2')

else:
	print('Pas d\'exception levée')

```

---
<style scoped> {
  font-size: 23px;
}
</style>
#### Le bloc `try`

Ce bloc permet de délimiter un ensemble d'instructions qui seront sous la surveillance
du mécanisme de gestion d'erreur.

```python
try:
  a = 10
	a += 'yo'
	z = u
	try:
		a === 10
	except ...:
		pass
except ...:
		pass
```

Ici les 3 lignes du 1° bloc `try` sont surveillées par le mécanisme d'erreur, ainsi que le bloc `try/except` imbriqué.

---
<style scoped> {
  font-size: 22px;
}
</style>
#### Le bloc `except`

Ce bloc sert à intercepter une erreur. Comme plusieurs blocs successifs sont possibles, l'ordre des blocs est important.

Les exceptions sont basées sur le mécanisme de l'héritage. L'exception de référence `BaseException` est la plus générique (classe mère ou de référence). Toutes les exceptions en Python dérivent de celle-ci. Donc en positionnant un bloc `except BaseException` en premier, toute exception, quelle soit très spécifique ou pas, sera interceptée.

L'exception la 'plus générale' doit toujours être positionnée en dernier.

```python
import os
print('avant le try')
try:
	os.listdir('/Users/Albert/Desktop')
except OSError as e:
	print(type(e), str(e))
except BaseException as e:
	print(type(e), str(e))
	raise # ici je propage l'erreur vers l'appelant
print('ici je continue')
```
L'expression `as e` dans le bloc `except ...` permet de récupérer l'exception dans une variable.

---
<style scoped> {
  font-size: 23px;
}
</style>

Une fois que l'exeption a été interceptée, c'est au programmeur de décider de la suite à donner: 
+ soit le programme continue après un traitement spécifique ou pas,
+ soit l'erreur est renvoyée à l'appelant en propageant l'erreur par la mise en place d'une instruction `raise` dans le bloc `except`. Dans ce cas, si aucune exception n'est indiquée après le `raise`, c'est l'exception est cours qui est transmise.

**A noter:** dans le traitement d'une exception, un appel à `raise OtherException` est tout à fait possible. L'exception à l'origine de l'erreur, peut être préciser avec le mot `from` comme ceci:

```py
try:
    1/0
except ArithmeticError as e:
	print(type(e), str(e))
	raise MyOwnError from e # ici je propage l'erreur MyError vers l'appelant
```

### Le bloc `else`

Ce bloc optionnel unique est appelé quand il n'y a pas eu d'exception levée.

---
<style scoped> {
  font-size: 21px;
}
</style>
### Lever une exception

La levée d'exception se fait par l'appel à l'instruction `raise` suivie par un objet dont la classe correspond à l'erreur. Toute exception en Python est du format **XxxxxxxxError**, comme par exemple:

+ ValueError
+ TypeError
+ IndexError
+ ImportError

L'appel à une instruction `raise` invoque le mécanisme d'erreur et interrompt l'exécution de la fonction dans laquelle est située cette instruction (équivalent à une instruction `return`.

```python
def racine_carre(val):
	if not isinstance(val, (int, float)):
		# leve l'exception TypeError et quitte racine_carre
		raise TypeError('"val" doit être un nombre entier ou flottant')
	if val < 0:
		# leve l'exception ValueError et quitte racine_carre
		raise ValueError('"val "doit être un nombre positif ou nul')

	return sqrt(val)
```
---
<style scoped> {
  font-size: 21px;
}
</style>

## Créer ses propres exceptions

Pour créer ses propres exceptions il suffit de dériver d'une des classes déjà existantes

```python
class PresentationError(Exception):
	pass

def test():
	"""
	"""
	raise PresentationError("Sample from test")

try:
	test()
except PresentationError as e:
	print(type(e), str(e))

```

### Annexe1

Voir [Les exceptions de Python](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)



---
<style scoped> {
  font-size: 18px;
}
</style>
## Les bibliothèques externes

Python est livré avec de nombreuses bibliothèques internes qui sont utilisables via l'instruction `import`.
Voici un exmple de script avec:

```py
import argparse
import bisect
import collections
import datetime
import enum
import functools
import glob
import heapq
import itertools
import logging
import multiprocessing
import numbers
import os
import pickle
import queue
import re
import sys
import time
import uuid
import venv
import weakref
import xml
import zipfile
```
**A noter:** il y a autant de ligne que de bibliothèques. Les bibliothèques sont listées par ordre alphabétique
voir [Toutes les biliothèques](https://docs.python.org/fr/3.8/library/index.html)

---
<style scoped> {
  font-size: 24px;
}
</style>
### Utiliser les bibliothèques externes

Lorsque le programmeur se lance dans la réalisation d'un script, il arrive assez vite qu'il cherche des exemples sur Internet ou en interrogeant ses collègues. Dans les exemples, très souvent l'utilisation de bibliothèques externes s'imposent.

La majorité des bibliothèques se trouve dans [Python Package Installer (PyPi)](https://pypi.org/) qui est le principal dépôt où sont publiées les bibliothèques externes.

#### Installer des bibliothèques

L'outil principal fourni par Python s'appelle `pip` pour Package Installer for Python
Il peut être invoque de 2 façons:
+ via la commande `pip`
+ via l'appel  à l'interpréteur python `python -m pip`

---
<style scoped> {
  font-size: 24px;
}
</style>

Plusieurs versions de Python peuvent être installées sur un même poste de travail. C'est pouquoi l'appel à `Python`, à `pip` se fait en suffixant le numéro de version cible. Par exemple:
+ `pip3.8 --help` lancera l'aide sur le module pip de la version 3.8
+ `python3.10 -m pip --help` lancera l'aide sur le module pip de la version 3.10 

Pour installer un package la commande suivante est nécessaire:
+ `python3.8 -m pip install mon_paquet`

---
<style scoped> {
  font-size: 23px;
}
</style>
### Gérer ses bibliothèques

Lorsque l'aide de `pip` est invoquée, voici les principales commandes disponibles:
```zh
Usage:
  pip3.11 <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.
```

voir [Installation de bibliothèques externes](https://packaging.python.org/en/latest/tutorials/installing-packages/)

---
<style scoped> {
  font-size: 22px;
}
</style>

### Quelques commandes de PIP

Voici une liste non exhaustive de commandes passées avec l'utilitaire **PIP**
| commande | ligne d ecommande |
|----------|---------------|
|Installation d'une bibliothèque|```python3.8 -m pip install matplotlib```|
|Mise à jour d'une bibliothèque déjà installée|```python3.8 -m pip install matplotlib --upgrade```|
|Voir le détail d'une bibliothèque installée|```python3.8 -m pip show  matplotlib```|
|Désinstallation d'une bibliothèque|```python3.8 -m pip uninstall matplotlib```|
|Lister les bibliothèques installées|```python3.8 -m pip list```|
|Préparer un fichier texte en formaté listant les bibliothèques installées et leur version|```python3.8 -m pip freeze 2>./requirements.txt```|
|Installation les bibliothèques à partir d'un fichier texte formaté|```python3.8 -m pip install -e ./requirements.txt```|
|Examiner le détail d'une bibliothèque|```python3.8 -m pip show matplotlib```|

---
<style scoped> {
  font-size: 25px;
}
</style>

## Les environnements virtuels

Ce mode opératoire, en Python, permet de dédier une installation spécifique à un projet. C'est à dire:
+ dédiée à une version de Python,
+ dédiée à une liste de bibliothèques externes (A terme installables via un fichier texte formaté et la commande `pip install -e ...`, issu de cette installation).

Ainsi vous pouvez avoir 2 environnements spécifiques pour 2 versions de Python différentes.

Autre cas d'usage: certaines bibliothèques externes ne travaillent qu'avec qu'une et une seule version d'une autre bibliothèque externe. Or si cette dernière est aussi utilisée dans d'autres projets, vous risquez le conflit de version.

De manière générale, il est fortement recommandé, pour un nouveau projet ou même un simple 'POC', de mettre en place un environnement virtuel.

---
<style scoped> {
  font-size: 26px;
}
</style>
### Mode opératoire

Il suffit de créer un dossier dédié, de se positionner dans ce dossier et de:

+ lancer la commande `python3.9 -m venv . --prompt PACKAGE1` la mise en place
  + depuis ce dossier, lancer le batch `Scripts\activate.bat` sous Windows
ou
  + depuis ce dossier, lancer la commande `source ./bin/activate` sous Linux et Mac


Vous êtes alors dans votre environnement virtuel, prêt à travailler tout en sachant que:
* la version de python installée correspond à celle du programme python (`pythonX.Y -m venv`) qui a créé l'environnement virtuel,
* votre installation est vierge de toute biblibiothèque externe préalablement installée (sauf si vous avez utilisé l'option `--system-site-packages`).

---
<style scoped> {
  font-size: 23px;
}
</style>

Donc si vous avez besoin de partir d'une installation de Python avec des bibliothèques déjà préinstallées, vous devez ajouter le paramètre `--system-sites-packages`. Par exemple, dans votre installation de référence vous avez tous vos outils de tests (Pytest, mock) et vos outils engendrant les documentations, ainsi ces éléments ne feront pas partie de votre livrable.

Pour voir toutes les options possibles, tapez la commande: `python -m venv --help`

```zsh
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear] [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps] ENV_DIR [ENV_DIR ...]

Creates virtual Python environments in one or more target directories.

positional arguments:
  ENV_DIR               A directory to create the environment in.

options:
  -h, --help            show this help message and exit
  --system-site-packages
                        Give the virtual environment access to the system site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when symlinks are the default for the platform.
  --clear               Delete the contents of the environment directory if it already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version of Python, assuming Python has been upgraded in-place.
  --without-pip         Skips installing or upgrading pip in the virtual environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this environment.
  --upgrade-deps        Upgrade core dependencies: pip setuptools to the latest version in PyPI

Once an environment has been created, you may wish to activate it, e.g. by sourcing an activate script in its bin directory.
```

Voir [Les environements virtuels](https://docs.python.org/fr/3.8/library/venv.html)

---
<style scoped> {
  font-size: 21px;
}
</style>
## Les annotations de types: introduction

Ce système permet d'indiquer à titre informatif, les 'types' ou 'regroupements de 'types' attendus pour:
+ les paramètres d'une fonction, d'une méthode,
+ les valeurs retournées d'une fonction, d'une méthode
+ les variables locales et globales, attributs d'objet, de classe.

Voici un exemple pour la fonction `racine_carre` vue dans le chapître sur les exceptions.

```python
from typing import Union

def racine_carre(val: Union[int, float]) -> float:
	"""initialement: `def racine_carre(val):`
  etc ....."""
  if not isinstance(val, (int, float)):
		# leve l'exception TypeError et quitte racine_carre
		raise TypeError('"val" doit être un nombre entier ou flottant')
	if val < 0:
		# leve l'exception ValueError et quitte racine_carre
		raise ValueError('"val "doit être un nombre positif ou nul')

	return sqrt(val)
```

**A noter:** Les annotations de type ont été introduites à partir de la version 3.5

---
<style scoped> {
  font-size: 21px;
}
</style>
### La bibiothèque interne `typing`

```py
from typing import Callable, Union, Typevar
```
Cette bibliothèque contient les types élaborés revisités, les combinaisons, les alias qui seront utilisés pour définir les annotations. Par exemple:
+ Tuple, Dict, List, Sequence, Iterable, Collection, Callable, Generator, Coroutine
+ Option, Union, Any,
+ TypeVar, Alias de type.

voir [la bibiothèque typing](https://docs.python.org/fr/3/library/typing.html)

#### Quelques exemples d'annotations

```python
from typing import Collection

def somme_des_chiffres(collec: Collection) -> float:
  """Somme des nombres de la collection"""
  return sum(item for item in collec if isinstance(item, (int, float)))
```
**A noter:**: 
Les annotations sont stockées dans la variable interne `__annotations__` rattachée à la fonction.

---
<style scoped> {
  font-size: 20px;
}
</style>
## Les bonnes pratiques

Les bonnes pratiques en Python constitue un ensemble de règles que les développeurs s'attèlent à respecter (c'est pas toujours facile ;-)). Lors des revues de codes, les développeurs y font toujours référence.

### La [PEP8](https://peps.python.org/pep-0008/)
Les bonnes pratiques en Python sont résumées dans une document nommé PEP8 et donc voici un [résumé](https://python.sdv.univ-paris-diderot.fr/15_bonnes_pratiques/). Ici sont listés tous les cas concernant:
+ le nommage des variables, classes, fonctions, méthodes, constantes,
+ la ponctuation, les espaces, les blocs, les sauts de ligne,
+ la longueur d'une ligne.

### Les commentaires

Les commentaires en Python se retrouvent principalement sous 2 formes:
+ les `docstring` avec les trytiques de quotes `'''ceci est une docstring'''` sur les fonctions, les classes, les méthodes.
+ les commentaires standards avec le `#` comme délimiteur de début.

---
<style scoped> {
  font-size: 24px;
}
</style>
### Les linters

Ces outils de contrôle de code peuvent être installés et utilisés en ligne de commande via la commande `python -m pip install <outil>`. La plupart des IDE (PyCharm, Spyder, VSCode) propose aussi leur installation et exécution (souvent automatqie) à travers des extensions.

Il existe plusieurs outils pour vérifier, relire et proposer des améliorations sur votre code, parmi les plus utilisés voici:

* black
* flake8
* pylint
* mypy
* bandit
* coverage

---
#### Black

Cet outil est un 'formatteur' de code Python, c'est à dire qu'il repère les lignes de code qui ne respectent pas les règles de la PEP8. Il propose alors une remise en forme.

Attention, cet outil modifie votre code, uniquement sur la mise en forme.

[La bibliothèque](https://pypi.org/project/black/)

---
#### Flake8

Cet outil analyse le code d'un fichier Python, repère les lignes de code qui ne respectent pas la PEP8, et fait une analyse statique sur certains types d'anomalies comme:

+ élément non utilisés comme des variables, des paramètres, des bibliothèques,
+ noms de fonctions non trouvés.

[La bibliothèque](https://pypi.org/project/flake8/)
[La documentation](https://flake8.pycqa.org/en/latest/)

---
#### Pylint

Cet outil reprend les vérifications de flake8 et ajoute d'autres partie autour des attributs, des erreurs de syntaxes, vérifient la documentation sur les fonctions, classes et méthodes.

Le gros plus: Pylint repère les duplications de code ;-)

[La bibliothèque](https://pypi.org/project/pylint/)
[La documentation](https://pylint.pycqa.org/en/latest/)

---
#### Mypy

Cet outil analyse les annotations de type mises en oeuvre sur les fonctions et vérifient statiquement si les parmètres passés correspondent aux types déclarés dans les annotations.

[La bibliothèque](http://mypy-lang.org/)
[La documentation](https://mypy.readthedocs.io/en/stable/)

----
#### Bandit

Cet outil permet de rechercher des vulnerabilités sur le code Python

[La documentation](https://bandit.readthedocs.io/en/latest/)

----
#### Coverage

Cet outil permet de faire de la couverture de code, cest à dire de vérifier que toutes les parties d'un code sont bien utilisées (nécessaires).

[La documentation](https://coverage.readthedocs.io)

---
<style scoped> {
  font-size: 17px;
}
</style>
### Le Zen de Python

Exécuter la ligne suivante ```python3.8 -c 'import this'```

* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than * complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!


