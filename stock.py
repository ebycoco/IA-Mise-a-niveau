import csv

class Produit:
    def __init__(self, nom: str, quantite: int, prix_unitaire: float):
        self.nom = nom
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def __repr__(self):
        return f"Produit(nom={self.nom!r}, quantite={self.quantite}, prix_unitaire={self.prix_unitaire})"


class Inventaire:
    def __init__(self):
        self.produits = []  # list[Produit]

    def ajouter_produit(self, nom, quantite, prix):
        for p in self.produits:
            if p.nom == nom:
                raise ValueError(f"Le produit {nom!r} existe déjà")
        self.produits.append(Produit(nom, quantite, prix))

    def modifier_produit(self, nom, nouvelle_quantite=None, nouveau_prix=None):
        for p in self.produits:
            if p.nom == nom:
                if nouvelle_quantite is not None:
                    p.quantite = nouvelle_quantite
                if nouveau_prix is not None:
                    p.prix_unitaire = nouveau_prix
                return
        raise ValueError(f"Produit {nom!r} non trouvé")

    def supprimer_produit(self, nom):
        initial = len(self.produits)
        self.produits = [p for p in self.produits if p.nom != nom]
        if len(self.produits) == initial:
            raise ValueError(f"Produit {nom!r} non trouvé")

    def afficher_inventaire(self):
        if not self.produits:
            print("Inventaire vide.")
            return
        print("Inventaire actuel :")
        for p in self.produits:
            ca = p.quantite * p.prix_unitaire
            print(f"- {p.nom} : {p.quantite} unités × {p.prix_unitaire} € → CA = {ca:.2f} €")

    def charger_depuis_csv(self, chemin):
        with open(chemin, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.produits.append(
                    Produit(
                        row["nom"],
                        int(row["quantite"]),
                        float(row["prix_unitaire"])
                    )
                )

    def sauvegarder_vers_csv(self, chemin):
        with open(chemin, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["nom", "quantite", "prix_unitaire"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in self.produits:
                writer.writerow({
                    "nom": p.nom,
                    "quantite": p.quantite,
                    "prix_unitaire": p.prix_unitaire
                })

