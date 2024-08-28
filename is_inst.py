# https://www.docstring.fr/formations/exercices/185/


ma_chaine = "Salut Patrick"
print(isinstance(ma_chaine, str))
if isinstance(ma_chaine, str):
    print("Des caractères !")


class Animal:
    def __init__(self, name):
        self.name = name

class Chien(Animal):
    def aboyer(self):
        return f"{self.name} fait Woof!"

class Chat(Animal):
    def miauler(self):
        return f"{self.name} fait Miaou!"

# Création d'instances
rex = Chien("Rex")
felix = Chat("Felix")
inconnu = "Juste une chaîne"

# Utilisation de isinstance
def faire_du_bruit(animal):
    if isinstance(animal, Chien):
        return animal.aboyer()
    elif isinstance(animal, Chat):
        return animal.miauler()
    else:
        return "Type inconnu, pas de bruit"

print(faire_du_bruit(rex))     # Affiche : Rex fait Woof!
print(faire_du_bruit(felix))   # Affiche : Felix fait Miaou!
print(faire_du_bruit(inconnu)) # Affiche : Type inconnu, pas de bruit

# Vérification de types multiples
print(isinstance(rex, (Chien, Chat)))  # Affiche : True
print(isinstance(inconnu, (Chien, Chat)))  # Affiche : False
