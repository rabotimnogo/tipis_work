import numpy as np 
import pandas as pd

from src.lib.models.train import logistic_model_b
from sklearn.metrics import classification_report

class LogRegBalanced:
    def __init__(self, model=logistic_model_b):
        self.model = model

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        prediction = self.model.predict(X)

        print('предикт совершен')

        return prediction
    
    def eval_model(self, y_true: pd.DataFrame, y_pred: pd.Series) -> None:
        print('eval совершен')
        return classification_report(y_true, y_pred, target_names=["Not Fraud", "Fraud"])
        