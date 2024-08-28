a = (i for i in range(1, 3))
print(a)
print(next(a))
print(next(a))
# print(next(a))  # StopIteration

for i in a:
    # On aura déjà consommé l'itérateur
    print(f"Dans la boucle for {i}")