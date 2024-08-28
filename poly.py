# Système de gestion des ressources humaines

# Pourquoi ABC ? Interface commune, redéfinir les abstractmethod, facilite le polymorphisme

from abc import ABC, abstractmethod


class Employe(ABC):
    def __init__(self, nom, prenom, id_employe):
        self.nom = nom
        self.prenom = prenom
        self.id_employe = id_employe

    @abstractmethod
    def calculer_salaire(self):
        pass

    @abstractmethod
    def afficher_details(self):
        pass

class EmployePermanent(Employe):
    def __init__(self, nom, prenom, id_employe, salaire_annuel):
        super().__init__(nom, prenom, id_employe)
        self.salaire_annuel = salaire_annuel

    def calculer_salaire(self):
        return self.salaire_annuel / 12

    def afficher_details(self):
        return f"Employé Permanent: {self.prenom} {self.nom} (ID: {self.id_employe}) - Salaire mensuel: {self.calculer_salaire():.2f}€"

class EmployeTemporaire(Employe):
    def __init__(self, nom, prenom, id_employe, taux_horaire, heures_travaillees):
        super().__init__(nom, prenom, id_employe)
        self.taux_horaire = taux_horaire
        self.heures_travaillees = heures_travaillees

    def calculer_salaire(self):
        return self.taux_horaire * self.heures_travaillees

    def afficher_details(self):
        return f"Employé Temporaire: {self.prenom} {self.nom} (ID: {self.id_employe}) - Salaire: {self.calculer_salaire():.2f}€"


class Consultant(Employe):
    def __init__(self, nom, prenom, id_employe, taux_journalier, jours_travailles):
        super().__init__(nom, prenom, id_employe)
        self.taux_journalier = taux_journalier
        self.jours_travailles = jours_travailles

    def calculer_salaire(self):
        return self.taux_journalier * self.jours_travailles

    def afficher_details(self):
        return f"Consultant: {self.prenom} {self.nom} (ID: {self.id_employe}) - Facturation: {self.calculer_salaire():.2f}€"


class GestionRH:
    def __init__(self):
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def retirer_employe(self, id_employe):
        self.employes = [e for e in self.employes if e.id_employe != id_employe]

    def calculer_salaires_totaux(self):
        return sum(employe.calculer_salaire() for employe in self.employes)

    def afficher_details_tous_employes(self):
        for employe in self.employes:
            print(employe.afficher_details())

def generer_rapport_paie(employes):
    for employe in employes:
        print(f"Traitement de la paie pour {employe.prenom} {employe.nom}...")
        print(f"Montant à payer: {employe.calculer_salaire():.2f}€")
        print("---")

# Exemple d'utilisation
if __name__ == "__main__":
    rh = GestionRH()

    # Ajout d'employés de différents types
    rh.ajouter_employe(EmployePermanent("Dupont", "Jean", "EP001", 50000))
    rh.ajouter_employe(EmployeTemporaire("Martin", "Sophie", "ET001", 15, 160))
    rh.ajouter_employe(Consultant("Durand", "Pierre", "C001", 500, 20))

    # Affichage des détails de tous les employés
    print("Détails de tous les employés:")
    rh.afficher_details_tous_employes()

    # Calcul et affichage du total des salaires
    total_salaires = rh.calculer_salaires_totaux()
    print(f"\nTotal des salaires à payer: {total_salaires:.2f}€")

    # Génération du rapport de paie
    print("\nGénération du rapport de paie:")
    generer_rapport_paie(rh.employes)

    # abc_class_instance = Employe()
