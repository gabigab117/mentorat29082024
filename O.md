# Complexité algorithmique en Python : O(n) et O(1)

## Définitions simples

- **O(n) - Complexité linéaire** : 
  Le temps d'exécution augmente proportionnellement au nombre d'éléments. En d'autres termes, plus il y a d'éléments, plus l'opération prend de temps.

- **O(1) - Complexité constante** : 
  Le temps d'exécution reste le même, quel que soit le nombre d'éléments. L'opération prend toujours approximativement le même temps, peu importe la taille de l'entrée.

## O(n) - Complexité linéaire

### Exemples :

1. **Parcourir une structure de données**
   ```python
   for item in my_list:  # O(n)
       print(item)
   ```

2. **Recherche linéaire**
   ```python
   def linear_search(lst, target):
       for item in lst:  # O(n)
           if item == target:
               return True
       return False
   ```

3. **Copier une structure de données**
   Toutes ces méthodes ont une complexité O(n) car elles doivent parcourir tous les éléments :
   ```python
   new_list1 = list(original_list)  # O(n)
   new_list2 = original_list[:]  # O(n)
   new_list3 = original_list.copy()  # O(n)
   ```

4. **Méthodes comme .count() ou .index() sur une liste**
   ```python
   occurrences = my_list.count(value)  # O(n)
   ```

5. **Concaténation de listes**
   ```python
   result = list1 + list2  # O(n), où n est la somme des longueurs
   ```

## O(1) - Complexité constante

### Exemples :

1. **Accès à un élément par index**
   ```python
   element = my_list[5]  # O(1)
   ```

2. **Opérations sur un dictionnaire**
   ```python
   value = my_dict['key']  # O(1)
   my_dict['new_key'] = 'new_value'  # O(1)
   del my_dict['key']  # O(1)
   ```

3. **Ajout/suppression à la fin d'une liste**
   ```python
   my_list.append(item)  # O(1) en moyenne
   my_list.pop()  # O(1)
   ```

4. **Opérations arithmétiques simples**
   ```python
   result = a + b  # O(1)
   ```

5. **Opérations sur une deque**
   ```python
   from collections import deque
   d = deque([1, 2, 3, 4, 5])
   first = d[0]  # O(1)
   last = d[-1]  # O(1)
   d.appendleft(0)  # O(1)
   d.append(6)  # O(1)
   d.popleft()  # O(1)
   d.pop()  # O(1)
   ```

## Notes importantes

- Les complexités O(n) signifient que le temps d'exécution augmente avec le nombre d'éléments.
- Les complexités O(1) signifient que le temps d'exécution reste constant, quel que soit le nombre d'éléments.
- Ces complexités sont des moyennes ou des cas typiques. Dans certains cas particuliers, le comportement peut varier.
- Pour la copie de liste, le choix entre `list()`, `[:]`, et `.copy()` dépend souvent de la lisibilité du code et des préférences personnelles ou de l'équipe.