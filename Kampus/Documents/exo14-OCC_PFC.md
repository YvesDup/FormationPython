1. Explications

Le symbole **#** correspond à un commentaire en Python.
Tout ce qui est écrit après ce symbole n'est jamais pris en compte par l'interpréteur Python

Les lignes 3 et 4 permettent d'importer des bibliothèques de fonctions et de constantes via le mot-clé **import**.

La ligne 7 correspond à la déclaration d'une variable PFC qui contient la liste des possibles du jeu. Mettre en majuscule une variable indique que cette variable est constante

Les lignes *10, 51 et 67* spécifient des définitions de fonctions via le mot-clé **def**
Ici les fonctions sont créées mais pas exécutées. Pour les exécutées, il faut les appeler par leur nom.

Une fonction est un assemblage d'instructions qui est exécuté à la demande avec des données en entrée et un resultat en sortie

Par exemple la fonction **ordinateur_choisir** est definie en ligne *67* et est exécutée en ligne *107*. Elle ne prend de données en entrée et renvoie le choix de l'ordinateur en sortie.

La fonction principale **jouer_pfc** est définie en ligne *78* et est appelée en ligne *130*
Elle prend une seule donnée en entrée qui correspond au nombre de tours à gagner pour être déclaré vainqueur

La fonction **input** est une fonction de Python qui permet de lire une saisie depuis le clavier

La notion de bloc est une notion importante dans n'importe quel langage informatique. En python elle est symbolisée par la retrait ou tabulation et sert à rassembler plusieurs instructions. C'est à dire que toutes les instructions d'un même bloc seront exécutées séquentiellement.

Dans une fonction, la première ligne contient le mot-clé **def** puis le nom de la fonction, puis les données en entrée. Le dernier caractère de la ligne est le caractère **':'**. Toutes les lignes suivantes débutent avec un retrait en début de ligne et font parties de la fonction. Elles sont dans le même bloc.

La notion de bloc en python démarre donc au caractère **':'** avec toutes les lignes suivantes qui commencent par un retrait. Un bloc contient au moins une ligne d'instruction.

Dans ces blocs, se trouvent des instructions de plusieurs types:

  1. les boucles ou répétitions
  1. les branchements conditionnels ou 'test'
  1. les affectations

Dans une boucle, la première ligne contient le mot-clé **while** ou **for** puis suivi d'une condition de boucle, puis le caractère de fin de ligne **':'**.
Toutes les lignes suivantes demarrent avec un retrait et forment le bloc de la boucle.
	Ce concept est illustré dans la fonction **joueur_choisir**

Dans un test, la première ligne contient le mot-clé **if** avec une conditon puis le caractère de fin de ligne **':'**. Toutes les lignes suivantes demarrent avec un retrait.
Le mot-clé **if** peut être associé avec les mots-clé **elif** ou **else**.
Ces 2 mots-clé peuvent avoir chacun un bloc d'instructions.
	Ce concept est illustré dans la fonction **qui_gagne**

Une affectation correspond à la mise à jour d'une variable. Elle s'effectue avec le sigle **=**.
La partie gauche de l'affectaion doit toujours être une variable, la partie droite est une autre variable, soit une valeur, soit le résultat d'une fonction
	Ce concept est illustré dans les affectations des lignes *96*, *116* et *107*

A noter que dans un bloc, il peut y avoir d'autres blocs symbolisés par un **':'** et un retrait


1. Questions

  2. Combien de fois est utilisée la fonction **input** ? A quoi cela correspond il ?
  2. Combien de boucles détectez-vous dans ce script ? Indiquez dans quelle fonction ?
  2. Combien y a t il de ligne dans le bloc d'instruction associé à la boucle **while** de la fonction **joueur_choisir** ?
  2. Dans la fonction **qui_gagne**, quel est le maximum de blocs imbriqués (bloc dans un bloc)
  2. Dans quelle fonction est traitée la détermination du gagnant lors d'un tour ?
  2. Comment faire pour que le joueur gagne tout le temps ?
  2. Comment faire pour que le nombre de tours à gagner soit de 5 ?
