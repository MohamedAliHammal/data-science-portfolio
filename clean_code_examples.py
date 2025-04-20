"""
Ce fichier présente des exemples de code suivant les principes de PEP 8.
"""

def calculer_somme(nombre1, nombre2):
    """
    Calcule et retourne la somme de deux nombres.

    Args:
        nombre1 (int): Le premier nombre.
        nombre2 (int): Le deuxième nombre.

    Returns:
        int: La somme des deux nombres.
    """
    resultat = nombre1 + nombre2
    return resultat

# Exemple d'utilisation
premier_nombre = 10
second_nombre = 5
somme_totale = calculer_somme(premier_nombre, second_nombre)
print(f"La somme de {premier_nombre} et {second_nombre} est : {somme_totale}")