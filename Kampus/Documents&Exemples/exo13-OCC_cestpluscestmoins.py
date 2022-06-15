# ceci est un commentaire: tout ce qui est après le # est un commentaire. 
# Cad que ce n'est pas du code Python
import sys       # import des fonctions systeme
import random    # import des fonctions de nombres aléatoires
import math      # import des fonctions mathématique


# le mot-clé 'def' indique la définition d'une fonction
# une fonction est un regroupement d'instructions
def calcul_nombre_coups(valeur_mini, valeur_maxi):
    """
    Fonction qui calcule le nombre de coups à jouer

    En entrée, les bornes entre lesquelles le nombre doit être compris
    En sortie, renvoie le nom bre de coups maximum
    """
    return min((valeur_maxi - valeur_mini)//5, 10)

    # return int(math.log(valeur_maxi - valeur_mini)//math.log(2))


def choix_joueur(valeur_mini, valeur_maxi):
    """
    Fonction qui récupère la saisie du joueur

    En entrée, les bornes entre lesquelles le nombre doit être compris
    En sortie, renvoie le choix valide du joueur
    """

    choix = valeur_mini - 1
    # tant que la valeur lue au clavier n'est pas une parmi
    # celles de l'intervalle, la saisie continue
    while not (valeur_mini < choix < valeur_maxi):
        try:
            choix = int(input(f"Veuillez saisir une valeur entre {valeur_mini} et {valeur_maxi}:"))
        except:
            choix = valeur_mini - 1

    return choix


def choix_ordinateur(valeur_mini, valeur_maxi):
    """
    Fonction qui récupère le choix de l'ordinateur

    En entrée, les bornes entre lesquelles le nombre doit être compris
    En sortie, renvoie le tirage aléatoire effectué pour l'ordinateur
    """
    # la fonction choice prend une valeur au hasard
    return random.randint(valeur_mini, valeur_maxi)

def jouer_cestplus_cestmoins(valeur_mini, valeur_maxi):
    """
    Fonction principale
    Explique le but à atteindre
    Et contrôle le lancement et l'exécution du jeu

    En entrée, est passé l'intervalle dans lequel on recherche le nombre
    """
    # calcul du nombre de coup maximum pour gtrouver le nombre
    nombre_de_coups = calcul_nombre_coups(valeur_mini, valeur_maxi)

    #rappel des règles
    print(f"Bonjour, vous devez trouver un nombre entre {valeur_mini} et {valeur_maxi}, bornes comprises")
    print(f"vous avez au maximum {nombre_de_coups} propositions à faire, Ok ?")
    print(f"C'est parti, c'est à vous !!!")

    # tirage aléatoire du nombre à trouver
    nombre_a_trouver = choix_ordinateur(valeur_mini, valeur_maxi)

    # tant que le joueur n'a pas trouvé en moins de nombre_de_coups
    coup = 0
    while coup < nombre_de_coups:
        #choix du joueur
        nombre_saisi = choix_joueur(valeur_mini, valeur_maxi)

        # c'est trouvé, on s'arrête
        if nombre_saisi == nombre_a_trouver:
            # l'instruction break interrompt la boucle
            break

        # affiche les forces en présence
        print(f"Vous avez choisi: {nombre_saisi}")
        if nombre_saisi < nombre_a_trouver:
            print(f"Le nombre à trouver est plus grand que {nombre_saisi}")
        else:
            print(f"Le nombre à trouver est plus petit que {nombre_saisi}")

        # on compte un coup
        coup = coup + 1 # ou encore coup += 1

        # affichage du score
        print(f"\nIl vous reste {nombre_de_coups-coup} coups à joueur")

    # fin du jeu
    if nombre_saisi == nombre_a_trouver:
        print(f"Bravo vous avez trouvé {nombre_a_trouver} !!")
    else:
        print(f"Oups, il fallait trouver {nombre_a_trouver} !!!")

# lancer le jeu
jouer_cestplus_cestmoins(1, 100)