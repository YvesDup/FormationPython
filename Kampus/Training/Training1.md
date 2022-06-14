---
marp: true
theme: gaia
paginate: true
header: '**Kampus-training**'
footer: yduprat@gmail.com

---
# Formation Python BNC

Juillet/Septembre 2022


![h:400w:600](https://www.python.org/static/community_logos/python-logo-generic.svg)

---
# Sommaire

* L'organisation de la formation
* Le contenu de cette formation
* Le programme du jour

---
## Organisation de la formation

![w:880](img/Scheduled.png)

---
## Le contenu de la formation

4 parties ditinctes
* 
* 
* La programmation objet
* Syntaxe avancée

---
## Le programme du jour
* Présentation du langage Python
* Langage interprété vs Langage compilé
* Typage fort, dynmanique, le `duck` typing
* La structuration d'un programme en Python
* L'interpréteur Python
* Explorations des types en Python
* Introduction aux fonctions

---
### Présentation du langage Python
<style scoped>
table {
  font-size: 9px;
}
</style>

Un peu d'histoire, cela commence à la fin des années 1980 (le dernier millénaire)
* v1 en fév 1992
* v2 en octobre 2000, la v2.7 est la dernière
* v3 en decembre 2008

Depuis la v3.9, publication annuelle d'une nouvelle version: La v3.11 est programmée pour le 3 octobre 2022.

[voir le langage Pythonsur wikipedia](https://fr.wikipedia.org/wiki/Python_(langage))

---
### 
---
### L'interpréteur Python

Dans un terminal:
```zsh
yves@MacBook-Pro-de-yves cpython % python3
Python 3.10.1 (v3.10.1:2cd268a3a9, Dec  6 2021, 14:28:59) [Clang 13.0.0 (clang-1300.0.29.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit() or Ctrl+D, to quit
```

La commande `python3 --help` permet de découvrir toutes les options. 

---

Quelques options intéressantes:

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

---

Lancer le profiler sur un script Python `setup.py`

```zsh
python3 -m cProfile -o result.cprof setup.py
yves@MacBook-Pro-de-yves cpython %
```


