# Descripteurs & Property


## Rappel sur le modèle Objet

L'acces aux attrbuts d'un objet se fait via  l'opérateur . et le nom de l'attribut, 
principalement pour 2 actions 
* la consultation de l'attribut
* la modification de l'attribut

IL est possible de contrôler ces accès via des méthodes internes de l'objet qui s'appelle des 'accessor'. Il existe 2 variétés de methodes
* les getter -> consultation
* les setter -> mise à jour

En plus de contrôler l'accès à l'attribut, l'autre intéret d'un 'accessor' est que cela masque l'implémentation de l'attribut. Cad:

Pour un objet Time, le stockage interne est sous la forme d'un nombre flottant
Et poutant on peut récupérer ou mettre à jour l'heure, la minute ou la seconde de chaque objet


## Descripteurs

Les descripteurs permettent de normaliser via un protocole les accès à un attribut.
Ce protocole repose sur 3 méthodes qui seront invoquées dans ce mécanisme d'accès, en fonction de l'opération initiale:

* en consultation c'est la methode `__get__`
* en mise à jour c'est la methode `__set__`
* en suppression, c'est la methode `__delete__`

Il peut y avoir un descripteur pour chaque attribut.

## Property

Cette classe `property` permet le lien entre le descripteur et les accessors d'un attribut. Il y aura autant d'instance de property que d'attribut cible.

2 méthodes pour mettre en place un property, via la mise en place d'une variable statique:
* par la création d'une variable de classe (statique) dans la classe où est définie l'attribut
* par le positionnement d'un décorateur @property sur le setter de l'attribut, puis d'un autre décorateur @name_attribut.setter, et éventuellement d'un dernier @name_attribut sur le deleter

Voici les 2 exemples de mise en oeuvre
````py

class Circle:
    """
    """    
    def __init__(self, ray: float, color: tuple=(0, 0, 0)):
        # list sur _ray pour un historique des valeurs
        self._ray = ray
        self._color = color
    
    def get_ray(self) -> float:
        return self._ray
    
    def set_ray(self, new_ray: float):
        if not isinstance(new_ray, (int, float)):
            raise TypeError('new_ray must be a number')
        self._ray = new_ray
        
    def del_ray(self) -> None: # exemple d'annotation
        del self._ray

    # Mise en oeuvre 1
    # creation d'un objet statique de classe de type property *ray*
    ray = property(fget=get_ray, fset=set_ray, fdel=del_ray)


    # Mise en oeuvre 2
    # creer un objet static `property` qui s'appelle *color*
    @property # color = property(fget=color) 
    def color(self) -> tuple:
        return self._color
    
    @color.setter # color = color.setter(fget=color.fget, fset=color)
    def color(self, new_color):
        self._color = new_color
    
    @color.deleter # color = color.setter(fget=color.fget, fset=color.fset, fdel=color)
    def color(self):
        del self._color 
        
    def __str__(self) -> str:
        return f'(Circle:{self.get_ray()} )'
    
    def perimetre(self) -> float:
        return math.pi * 2 * self.get_ray()


c = Circle(10, (255, 255, 111))
print(c._ray)
print(c.get_ray())
print(c.ray) # getter
c.ray = 10 # setter
c.color = (127, 127, 127) # fset, setter (color) de mon object Circle

```

## Références

https://docs.python.org/fr/3.8/howto/descriptor.html#properties

https://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors
