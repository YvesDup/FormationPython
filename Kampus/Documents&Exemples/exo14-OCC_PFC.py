# ceci est un commentaire: tout ce qui est après le # est un commentaire. 
# Cad que ce n'est pas du code Python
import sys         # import des fonctions systeme
import random     # import des fonctions de nombres aléatoires

# liste des mots possibles 
PFC = ("pierre", "feuille", "ciseau")

# le mot-clé 'def' indique la définition d'une fonction
def qui_gagne(choix_joueur, choix_ordinateur):
    """
    Ce champ entre 2 séries de 3 double-quotes (en ligne 10 et 23) est une docstring 

    Placée en debut de fonction, cette zone permet d'expliquer ce que fait la fonction
    et pourra être exploitée par la fonction interne 'help'
    -----------------------------------------------------------------------
    * Fonction qui détermine qui gagne entre le joueur et l'ordinateur

    En entrée, sont passés les choix du joueur et de l'ordinateur
    En sortie, renvoie le nombre de points gagnés respectivement pour le joueur et l'ordinateur
    Par exemple 0, 0 est renvoyé quand les 2 joueurs ont le même tirage
    Par exemple 0, 1 est renvoyé quand l'ordinateur bat le joueur
    """
    # même choix, donc match nul
    if choix_joueur == choix_ordinateur:
        return 0, 0

    # pas le même choix, on commence par pierre
    if choix_joueur == "pierre":
        if choix_ordinateur == "ciseau":
            return 1, 0
        elif choix_ordinateur == "feuille":
            return 0, 1

    # puis on examine feuille
    elif choix_joueur == "feuille":
        if choix_ordinateur == "pierre":
            return 1, 0
        else:
            # ici c'est donc ciseau qui gagne
            return 0, 1

    # puis on teste avec ciseau
    elif choix_joueur == "ciseau":
        if choix_ordinateur == "feuille":
            return 1, 0
        # ici c'est pierre qui gagne
        return 0, 1


def joueur_choisir():
    """
    Fonction qui récupère la saisie du joueur
    * En entrée, aucun paramètre
    * En sortie, renvoie le choix valide du joueur
    """

    choix = ""
    # tant que la valeur lue au clavier n'est pas une parmi
    # celles de la liste, la saisie continue
    while choix not in PFC:
        choix = input(f"Veuillez saisir votre choix parmi {PFC}:")

    return choix


def ordinateur_choisir():
    """
    Fonction qui récupère le choix de l'ordinateur
    * En entrée, aucun paramètre
    * En sortie, renvoie le tirage aléatoire effectué pour l'ordinateur
    """

    # la fonction choice prend une valeur au hasard parmi PFC
    return random.choice(PFC)


def jouer_pfc(nb_points):
    """
    Fonction principale

    Saisie le nom du joueur
    Explique le but à atteindre
    Et contrôle le lancement et l'exécution du jeu
    * En entrée, est passé le nombre de points à atteindre pour gagner
    """
    # saisie du noms des joueur
    nom_joueur = input("Donner votre nom:")

    #rappel des règles
    print(f"Bonjour {nom_joueur}, vous jouez contre l'ordinateur")
    print(f"le premier joueur avec {nb_points} points à gagner, Ok ?")
    print(f"Vous devez choisir parmi {PFC} à chaque tour.")

    # mise a zéro des scores
    score_ordinateur = 0
    score_joueur = 0

    # tant qu'un des 2 joueurs n'a pas atteint le nombre de points
    while max(score_joueur, score_ordinateur) < nb_points:
        """
        """
        #choix du joueur
        choix_joueur = joueur_choisir()

        # choix aléatoire de l'ordi
        choix_ordinateur = ordinateur_choisir()

        # affiche les forces en présence
        print(f"Tour\t->\tordinateur:{choix_ordinateur}\tvs\t{nom_joueur}:{choix_joueur}")

        # calcul des gains
        gain_joueur, gain_ordinateur = qui_gagne(choix_joueur, choix_ordinateur)

        # mise à jour des scores
        score_joueur = score_joueur + gain_joueur
        score_ordinateur += gain_ordinateur # equivalent a score_ordinateur = score_ordinateur + gain_jour 

        # affichage du score
        print(f"Score\t->\tordinateur:{score_ordinateur}\tvs\t{nom_joueur}:{score_joueur}")


    # fin de partie, indique qui a gagné
    if score_joueur == nb_points:
        print(f"{nom_joueur} a gagné")
    else:
        print(f"L'ordinateur a gagné")

# lancer le jeu
jouer_pfc(3)