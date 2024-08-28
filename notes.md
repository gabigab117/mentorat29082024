# next

Dans le cas de la méthode trouver_vehicule revient à faire ça en une ligne

```python
def trouver_vehicule(self, immatriculation):
    # next peut être utilisé pour rechercher un élément unique
    # une expression génératrice avec (), alors que [] est une liste (itérable)
    return next((v for v in self.vehicules if v.immatriculation == immatriculation), None)  # retourne StopIteration par défaut, ici None

"-------------------"

def trouver_vehicule(self, immatriculation):
    for vehicule in self.vehicules:
        if vehicule.immatriculation == immatriculation:
            return vehicule
    return None
```

Manière plus courante d'utiliser next()
```python
nombres = [1, 2, 3]
iterateur = iter(nombres)
print(next(iterateur))  # Affiche 1
print(next(iterateur))  # Affiche 2
```

Pourquoi iter ? Une liste est un itérable, pas un itérateur. next fonctionne avec des itérateurs.
L'itérateur avance au fur et à mesure que vous le lisez.
une expression génératrice avec (), alors que [] est une liste (itérable)