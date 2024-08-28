class ProduitStock:
    def __init__(self, nom, prix, quantite):
        self._nom = nom
        self._prix = prix  # Pas d'accès direct à l'attribut ! getter setter
        self._quantite = quantite

    @property
    def nom(self):
        return self._nom

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, nouveau_prix):
        if nouveau_prix < 0:
            raise ValueError("Le prix ne peut pas être négatif")
        self._prix = nouveau_prix

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, nouvelle_quantite):
        if nouvelle_quantite < 0:
            raise ValueError("La quantité ne peut pas être négative")
        self._quantite = nouvelle_quantite

    @property
    def valeur_stock(self):
        return self._prix * self._quantite


class GestionStock:
    def __init__(self):
        self.produits = {}

    def ajouter_produit(self, produit):
        self.produits[produit.nom] = produit

    def afficher_stock(self):
        print("État du stock :")
        for nom, produit in self.produits.items():
            print(f"{nom}: Prix = {produit.prix}€, Quantité = {produit.quantite}, Valeur = {produit.valeur_stock}€")

    def valeur_totale_stock(self):
        return sum(produit.valeur_stock for produit in self.produits.values())


# Exemple d'utilisation
if __name__ == "__main__":
    gestion = GestionStock()

    # Création et ajout de produits
    produit1 = ProduitStock("Ordinateur portable", 800, 10)
    produit2 = ProduitStock("Souris sans fil", 25, 50)

    gestion.ajouter_produit(produit1)
    gestion.ajouter_produit(produit2)

    # Affichage initial du stock
    gestion.afficher_stock()

    # Modification du prix et de la quantité
    try:
        produit1.prix = 750  # Réduction de prix
        produit2.quantite = 60  # Augmentation du stock
    except ValueError as e:
        print(f"Erreur : {e}")

    # Affichage du stock mis à jour
    print("\nAprès modifications :")
    gestion.afficher_stock()

    # Affichage de la valeur totale du stock
    print(f"\nValeur totale du stock : {gestion.valeur_totale_stock()}€")

    # Tentative de modification invalide
    try:
        produit1.quantite = -5  # Ceci devrait lever une exception
    except ValueError as e:
        print(f"\nErreur : {e}")

    # produit1.prix = -1
