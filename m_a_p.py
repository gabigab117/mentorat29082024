# Liste des températures en Celsius
temperatures_celsius = [0, 10, 20, 30, 40]

# Fonction de conversion de Celsius à Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Utilisation de map pour convertir toutes les températures
temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))

print("Températures en Celsius :", temperatures_celsius)
print("Températures en Fahrenheit:", temperatures_fahrenheit)

# Applique une fonction à chaque élément d'un iterable

print("__________________")



# Avec plusieurs séries de données en parallèle :

# Fonction avec deux paramètres
def calculer_prix_total(prix_unitaire, quantite):
    return prix_unitaire * quantite

# Listes de données
prix_unitaires = [10, 20, 30, 40]  # Prix en euros
quantites = [2, 1, 3, 2]           # Quantités commandées

# Utilisation de map avec deux arguments
prix_totaux = list(map(calculer_prix_total, prix_unitaires, quantites))

# Affichage des résultats
for prix, quantite, total in zip(prix_unitaires, quantites, prix_totaux):
    print(f"{quantite} articles à {prix}€ = {total}€")

print("\nTotal de la commande :", sum(prix_totaux), "€")

# map() s'arrête dès que l'itérable' le plus court est épuisée !
# Sur un dict, par défaut itère sur les clés !
