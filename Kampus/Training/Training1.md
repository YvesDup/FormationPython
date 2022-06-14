---
marp: true
theme: gaia
paginate: true
header: '**Kampus-training**'
footer: (c) yduprat@gmail.com
---
# Formation Python BNC

Juin/Septembre 2022

_

![h:250](https://www.python.org/static/community_logos/python-logo-generic.svg)



---
# Sommaire

* L'organisation de la formation
* Le contenu de cette formation
* Le programme du jour

---
## Organisation de la formation

![center, h:450](img/Scheduled.png)

---
## Le contenu de la formation

3 chapîtres:

1. Structure de base du langage.
1. La programmation objet.
1. Syntaxe avancée.

**A noter:** Les principales bibliothèques internes seront utilisées à travers les exercices.

---
## Le programme du jour (issu du chapître 1)

* Présentation du langage Python
* Langage interprété vs Langage compilé.
* Typage fort, dynmanique, le `duck` typing.
* La structuration d'un programme en Python.
* L'interpréteur Python.
* Explorations des types en Python.
* Introduction aux fonctions.

---
### Présentation du langage Python
<style scoped> {
  font-size: 30px;
}
</style>

Un peu d'histoire, cela commence à la fin des années 1980 (le dernier millénaire)
* v1 en fév 1992 :smile:
* v2 en octobre 2000, la v2.7 est la dernière
* v3 en decembre 2008

Depuis la v3.9, publication annuelle d'une nouvelle version: La v3.11 est programmée pour le 3 octobre 2022.

[voir le langage Python sur wikipedia](https://fr.wikipedia.org/wiki/Python_(langage))

---
### Langage interprété vs Langage compilé.
<style scoped> {
  font-size: 30px;
}
</style>
* langage compilé:
  * plusieurs phases pour construire son programme
  * programme exécuté par le système d'exploitation.

* langage interprété:
  * le programme est exécutée au fur et à mesure de la lecture des instructions.

En Python, il existe un mécanisme de transformation en `bytecode` d'un source Python.  C'est ce `bytecode` qui passé à l'interpréteur.

Voir la bibliothèque [`dis`](https://docs.python.org/fr/3.9/library/dis.html) de Python.

---
### L'interpréteur Python
<style scoped> {
  font-size: 32px;
}
</style>

Dans un terminal, lancement de l'interpreteur Python:
```zsh
yves@MacBook-Pro-de-yves cpython % python3
Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit() or Ctrl+D, to quit
```

La commande `python3 setup.py` execute le script `setup.py`

```zsh
yves@MacBook-Pro-de-yves cpython % python3 hello.py
"Hello Guido !!!"
yves@MacBook-Pro-de-yves cpython %
```
---
<style scoped> {
  font-size: 31px;
}
</style>
Afficher la version de Python

```zsh
yves@MacBook-Pro-de-yves cpython % python3 -V
Python 3.10.1
yves@MacBook-Pro-de-yves cpython %
```

Afficher le dossier courant

```zsh
python3 -c 'import os; print(os.getcwd())'
/Users/yves/Documents/_Jobs/_Clients/cpython/cpython
yves@MacBook-Pro-de-yves cpython %
```

Lancer le module `cProfile` sur un script Python `setup.py`

```zsh
python3 -m cProfile -o result.cprof setup.py
yves@MacBook-Pro-de-yves cpython %
```

---
### Structuration d'un script Python

pour chaque script python, on distingue 3 parties, dans cet ordre :
* les `import` de bibliothèques, les constantes `SIZE=10` et les variables globales `items = []`.
* les fonctions `def xxx(): ...`, les classes `class Obj: ...`.
* le point d'entrée principal du script `__name__ == '__main__'`.

**Note**: chaque script Python est candidat pour être passé à l'interpréteur, ou pour être utilisé comme une bibliothèque locale via l'instruction `import`
