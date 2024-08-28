# Système de gestion de parc automobile pour une entreprise de location

class Vehicule:
    nombre_total_vehicules = 0  # Attribut de classe

    def __init__(self, immatriculation, marque, modele, annee):
        self.immatriculation = immatriculation  # Attribut d'instance
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self._kilometrage = 0  # Attribut privé
        self._est_loue = False
        Vehicule.nombre_total_vehicules += 1

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - Immatriculation: {self.immatriculation}"

    def __repr__(self):
        return f"Vehicule(immatriculation='{self.immatriculation}', marque='{self.marque}', modele='{self.modele}', annee={self.annee})"

    def louer(self):
        if not self._est_loue:
            self._est_loue = True
            return True
        return False

    def retourner(self):
        if self._est_loue:
            self._est_loue = False
            return True
        return False

    def ajouter_kilometrage(self, distance):
        if distance > 0:
            self._kilometrage += distance
            return True
        return False

    def obtenir_kilometrage(self):
        return self._kilometrage

    @staticmethod
    def calculer_cout_location(jours, tarif_journalier):
        return jours * tarif_journalier

    @classmethod
    def depuis_import(cls, donnees_import):
        immatriculation, marque, modele, annee = donnees_import.split(',')
        return cls(immatriculation, marque, modele, int(annee))


class VoitureElectrique(Vehicule):
    def __init__(self, immatriculation, marque, modele, annee, capacite_batterie):
        super().__init__(immatriculation, marque, modele, annee)
        self.capacite_batterie = capacite_batterie

    def __str__(self):
        return f"{super().__str__()} - Batterie: {self.capacite_batterie} kWh"

    def recharger(self):
        print(f"Recharge de la batterie de {self.capacite_batterie} kWh en cours...")


class ParcAutomobile:
    def __init__(self):
        self.vehicules = []

    def ajouter_vehicule(self, vehicule):
        self.vehicules.append(vehicule)

    def retirer_vehicule(self, immatriculation):  # Ne garder que les véhicules valides
        self.vehicules = [v for v in self.vehicules if v.immatriculation != immatriculation]

    def trouver_vehicule(self, immatriculation):
        # next peut être utilisé pour rechercher un élément unique
        # une expression génératrice avec (), alors que [] est une liste (itérable)
        return next((v for v in self.vehicules if v.immatriculation == immatriculation), None)  # retourne StopIteration par défaut, ici None

    def vehicules_disponibles(self):
        return [v for v in self.vehicules if not v._est_loue]

    def louer_vehicule(self, immatriculation):
        vehicule = self.trouver_vehicule(immatriculation)
        if vehicule and vehicule.louer():  # Si on a le véhicule, et si louer() return True, car n'était pas loué
            return vehicule
        return None

    def retourner_vehicule(self, immatriculation, kilometres_parcourus):
        vehicule = self.trouver_vehicule(immatriculation)
        if vehicule and vehicule.retourner():  # True and True
            vehicule.ajouter_kilometrage(kilometres_parcourus)
            return True
        return False


# Exemple d'utilisation
parc = ParcAutomobile()

# Ajout de véhicules au parc
parc.ajouter_vehicule(Vehicule("AB-123-CD", "Renault", "Clio", 2020))
parc.ajouter_vehicule(Vehicule("EF-456-GH", "Peugeot", "308", 2021))
parc.ajouter_vehicule(VoitureElectrique("IJ-789-KL", "Tesla", "Model 3", 2022, 75))

# Location d'un véhicule
vehicule_loue = parc.louer_vehicule("AB-123-CD")
if vehicule_loue:
    print(f"Véhicule loué : {vehicule_loue}")

# Retour d'un véhicule
if parc.retourner_vehicule("AB-123-CD", 150):
    print("Véhicule retourné avec succès")

# Affichage des véhicules disponibles
print("Véhicules disponibles :")
for v in parc.vehicules_disponibles():
    print(v)

# Utilisation de la méthode statique
cout = Vehicule.calculer_cout_location(7, 50)
print(f"Coût de location pour 7 jours à 50€/jour : {cout}€")

# Création d'un véhicule à partir d'une chaîne importée
nouveau_vehicule = Vehicule.depuis_import("MN-012-OP,Citroen,C3,2019")
parc.ajouter_vehicule(nouveau_vehicule)

print(f"Nombre total de véhicules dans le système : {Vehicule.nombre_total_vehicules}")
