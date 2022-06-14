---
marp: true
theme: gaia
paginate: true
_paginate: false
header: '**Kampus-training**'
footer: (c) yduprat@gmail.com
---
# Formation Python BNC

Juin/Septembre 2022

_

![h:250](https://www.python.org/static/community_logos/python-logo-generic.svg)



---
# Sommaire

* Le calendrier de la formation
* Le contenu de cette formation
* Le programme du jour

---
## Le calendrier de la formation

![center, h:450](img/Scheduled.png)

---
## Le contenu de la formation

3 chapîtres sont définis:

* Les structures de base du langage.
* La programmation `objet`.
* Le développement avancé.

**A noter:** Les principales bibliothèques internes seront utilisées à travers les exercices.

---
### Les structures de base du langage.

* Les types de données simples.
* Les types évolués: listes, tuples, dictionnaires et ensemble.
* Les branchements conditionnels et les boucles.
* Les fonctions en Python.
* La documentation
* La structure d’un fichier Python.
* Les notations en compréhension.
* La gestion des bibliothèques externes.

---
### La programmation `objet`.
* Rappel sur le modèle objet : classe, objet, attribut, méthode. 
* Les constructeurs et destructeurs.
* Le paramètre `self`.
* Les noms et fonctions internes des classes et objets.
* Les méthodes magiques, fonctionnelles.
* La visibilité des attributs et méthodes: public, privée.
* Attributs et méthodes de classe.
* Les mécanismes d'héritage.

---
### Le développement avancé.
* Les bonnes pratiques.
* La gestion des erreurs.
* Les environnements virtuels.
* L’unpacking et l’opérateur `splat`.
* Les fonctions internes `map`, `filter`, `zip`.
* Les itérateurs, les générateurs.
* Les bibliothèques `collections`, `itertools` et `functools`.
* L’utilisation de décorateurs.
* L’utilisation de gestionnaire de contexte.

---
## Le programme du jour (début du chapître 1).

* Présentation du langage Python
* Langage interprété vs Langage compilé.
* Typage fort, dynamique, le `duck` typing.
* La structuration d'un programme en Python.
* L'interpréteur Python.
* Exploration des types en Python.
* Introduction aux fonctions.

---
### Présentation du langage Python
<style scoped> {
  font-size: 28px;
}
</style>

Le langage Python est un langage interprété, procédural et objet. Il est multi-plateforme et a été développé par Guido Van Rossum. 

Le début du développement commence à la fin des années 1980 (le dernier millénaire)

+ v1 en fév 1992 :smile:
+ v2 en octobre 2000, la v2.7 est la dernière
+ v3 en décembre 2008

Depuis la v3.9, publication annuelle d'une nouvelle version: La v3.11 est programmée pour le 3 octobre 2022.

[Python sur wikipedia](https://fr.wikipedia.org/wiki/Python_(langage))

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
  * le programme est exécutée au fur et à mesure de la lecture des instructions par un programme: l'interpréteur.

En Python, il existe un mécanisme de transformation en 'bytecode' d'un source Python.  C'est ce 'bytecode' qui est lu l'interpréteur.

**Note:** La bibliothèque [`dis`](https://docs.python.org/fr/3.9/library/dis.html) de Python permet de voir le 'bytecode' produit.

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

La commande `python3 hello.py Guido` execute le script `hello.py` et passe la valeur 'Guido' comme paramètre au script

```zsh
yves@MacBook-Pro-de-yves cpython % python3 hello.py Guido
"Hello -Guido- !!!"
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

---
### Exploration des types en Python
<style scoped> {
  font-size: 28px;
}
</style>
Types simples:
* nombres entiers
* nombres à virgule
* chaines de caractéres
* autres

Types composés:
* listes
* tuples
* ensembles
* dictionnaires

---
### Exploration des types en Python

Répartition des types composés

* conteneurs
* collections
* séquences
* tableaux associatifs


---
### Structuration conditionnelle et répétition
<style scoped> {
  font-size: 28px;
}
</style>

La notion de bloc en Python est toujours rattachée à des instructions ou des définitions. Le bloc démarre dès le symbole `:`. Toutes les instructions du bloc seront positionnés avec le même retrait (4 espacecs en génral). Les instructions concernées sont: 
* if, elif, else,
* for, while,
* with

```py
if x == 0: # début de bloc
    x += 1
    y = -y
# fin de bloc
d = ...
```

---
<style scoped> {
  font-size: 28px;
}
</style>
* définitions:
   * fonctions ou méthode
   * générateur
   * classe 
```py
def somme_des_opposes(a, b ,c): # debut de bloc
    """Ceci est une docstring
    """
    tout = a + b + c
    return -tout

# fin de bloc
x = somme_des_opposes(10, 2, -5)
```

Naturellement dans une fonction ou une méthode, des instructions contiennent leur propre bloc.

---
### Introduction aux fonctions

