preferences = {"Patrick": "pommes", "Bob": "bananes"}

fruit_patrick = preferences.setdefault("Patrick", "oranges")
print(fruit_patrick)

fruit_roger = preferences.setdefault("Roger", "Cerises")
print(fruit_roger)
print(preferences)

# permet d'obtenir la valeur d'une clé dans un dictionnaire et, si cette clé n'existe pas, de l'ajouter avec une valeur par défaut.
# Concis pour initialiser des valeurs !
