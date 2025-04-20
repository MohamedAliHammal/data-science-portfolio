# Utilisation d'une compréhension de liste pour filtrer
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = [n for n in nombres if n % 2 == 0]
print(f"Nombres pairs : {nombres_pairs}")

# Utilisation d'un dictionnaire pour regrouper des informations
personnes = [
    {"nom": "Alice", "ville": "Paris"},
    {"nom": "Bob", "ville": "Lyon"},
    {"nom": "Charlie", "ville": "Paris"},
]
villes_personnes = {}
for personne in personnes:
    ville = personne["ville"]
    nom = personne["nom"]
    if ville not in villes_personnes:
        villes_personnes[ville] = []
    villes_personnes[ville].append(nom)
print(f"Personnes par ville : {villes_personnes}")

# Utilisation d'un ensemble pour éliminer les doublons
liste_avec_doublons = [1, 2, 2, 3, 4, 4, 5]
nombres_uniques = set(liste_avec_doublons)
print(f"Nombres uniques : {nombres_uniques}")