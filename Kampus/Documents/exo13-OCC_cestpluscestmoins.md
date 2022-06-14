1 - Explications

Le symbole **#** correspond à un commentaire en Python.
Tout ce qui est écrit après ce symbole n'est jamais pris en compte par l'interpréteur Python

Les lignes 3, 4 et 5 permettent d'importer des bibliothèques de fonctions et de constantes via le mot-clé **import**. 

Les lignes *10, 20, 40 et 60* spécifient des définitions de fonctions via le mot-clé **def**
Ici les fonctions sont créées mais pas exécutées. Pour les exécutées, il faut les appeler par leur nom. La première fonction appelée est celle située en dernière ligne 

Une fonction est un assemblage d'instructions qui est exécuté à la demande avec des données en entrée et des données en sortie (le résultat)

Par exemple la fonction **choix_ordinateur** est definie en ligne *40* et est exécutée en ligne *67* de la fonction **jouer_cestplus_cestmoins**. Cette fonction prend en entrée l'intervalle dans lequel sera choisi le nombre à deviner par le joueur. La fonction renvoie le choix (tirage aléatoire) en sortie.

La fonction principale **jouer_cestplus_cestmoins** est définie en ligne *60* et est appelée depuis la dernière ligne *100*
Elle prend un couple de données qui correspondent à l'intervalle dans lequel le nombre sera à deviner.

La fonction **input** est une fonction de Python qui permet de lire une saisie depuis le clavier

La notion de bloc est une notion importante dans n'importe quel langage informatique. En python elle est symbolisée par la retrait ou tabulation et sert à rassembler plusieurs instructions. C'est à dire que toutes les instructions d'un même bloc seront exécutées séquentiellement. 

Dans une fonction, la première ligne contient le mot-clé **def** puis le nom de la fonction, puis les données en entrée. Le dernier caractère de la ligne est le caractère **':'**. Toutes les lignes suivantes avec un retrait en début de ligne sont dans le même bloc.

La notion de bloc en python démarre donc au caractère **':'** avec toutes les lignes suivantes qui commencent par un retrait. Un bloc contient au moins une ligne d'instruction.

Dans une boucle, la première ligne contient le mot-clé **while** ou **for**. Ainsi toutes les lignes suivantes demarrent avec un retrait.
Ce concept est illustré dans la fonction **choix_joueur** 

Dans un test, la première ligne contient le mot-clé **if** avec une conditon puis le caractère de fin de ligne **':'**. Toutes les lignes suivantes demarrent avec un retrait.
Le mot-clé **if** peut être associé avec les mots-clé **elif** ou **else**. 
Ces 2 mots-clés peuvent avoir chacun un bloc d'instructions.

A noter que dans un bloc, il peut y avoir d'autres blocs symbolisés par un **':'** et un retrait


2 - Questions

1. Combien de fois est utilisée la fonction **input** ? A quoi cela correspond il ?
1. Combien de boucles détectez-vous dans ce script ? Indiquez dans quelles fonctions ?
1. Combien y a t il de lignes dans le bloc d'instruction associé à la boucle **while** de la fonction **choix_joueur** ?
1. Dans cette fonction, à quoi sert la directive **try:** puis **except:**
1. Ou est calculé le nombre de coups à jouer ?
1. Comment faire pour que le joueur gagne tout le temps ?
1. Comment faire limiter le nombre de coup à jouer ?
