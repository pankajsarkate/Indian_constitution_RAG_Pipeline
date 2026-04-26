
from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate(y_test, y_pred):
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1:", f1_score(y_test, y_pred))