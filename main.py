from stock import Inventaire

def main():
    inv = Inventaire()

    # Charger l’inventaire initial
    inv.charger_depuis_csv("inventaire_initial.csv")

    # Opérations CRUD
    inv.ajouter_produit("Stylo", 50, 1.2)
    inv.modifier_produit("Gomme", nouvelle_quantite=25)
    try:
        inv.supprimer_produit("AncienProduit")
    except ValueError as e:
        print(e)

    # Afficher et sauvegarder
    inv.afficher_inventaire()
    inv.sauvegarder_vers_csv("inventaire_final.csv")

if __name__ == "__main__":
    main()
