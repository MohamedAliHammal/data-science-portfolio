from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, r2_score
import numpy as np

def evaluate_classification(y_true, y_pred):
    """
    Évalue un modèle de classification en calculant la précision, le rappel et le F1-score.

    Args:
        y_true (list or np.ndarray): Les vraies étiquettes.
        y_pred (list or np.ndarray): Les étiquettes prédites.

    Returns:
        dict: Un dictionnaire contenant la précision, le rappel et le F1-score.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

def evaluate_regression(y_true, y_pred):
    """
    Évalue un modèle de régression en calculant l'erreur quadratique moyenne et le coefficient R².

    Args:
        y_true (list or np.ndarray): Les vraies valeurs.
        y_pred (list or np.ndarray): Les valeurs prédites.

    Returns:
        dict: Un dictionnaire contenant l'erreur quadratique moyenne et le R².
    """
    mse = mean_squared_error(y_true, y_pred)
    r_squared = r2_score(y_true, y_pred)
    return {"mean_squared_error": mse, "r_squared": r_squared}

if __name__ == "__main__":
    # Exemple d'évaluation pour la classification
    y_true_class = [0, 1, 2, 0, 1, 2]
    y_pred_class = [0, 1, 1, 0, 2, 2]
    metrics_class = evaluate_classification(y_true_class, y_pred_class)
    print("Résultats de l'évaluation pour la classification:")
    print(metrics_class)

    # Exemple d'évaluation pour la régression
    y_true_reg = np.array([3.0, 4.5, 2.1, 5.8])
    y_pred_reg = np.array([3.2, 4.3, 2.5, 5.5])
    metrics_reg = evaluate_regression(y_true_reg, y_pred_reg)
    print("\nRésultats de l'évaluation pour la régression:")
    print(metrics_reg)