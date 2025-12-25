import numpy as np
import pandas as pd

from sklearn.preprocessing import RobustScaler


class Prepocessor:
    '''
    класс для предобработки данных
    '''
    def __init__(self, df: pd.DataFrame):

        self.df = df
        self._scaling()

    def _scaling(self) -> None:
        '''
        Метод предобрабатывает данные для модели.
        '''
        # Масштабирование Amount
        self.df["Amount"] = RobustScaler().fit_transform(
            self.df["Amount"].to_numpy().reshape(-1, 1)
        )

        # нормализация для сходимости градиента
        time = self.df["Time"]
        self.df["Time"] = (time - time.min()) / (time.max() - time.min())
        
        # разделение на признаки и целевую переменную
        self.X = self.df.drop("Class", axis=1)  
        self.y = self.df["Class"]

        print('данные заскейлены')
        
    def get_data(self) -> tuple[pd.DataFrame, pd.Series]:
        print('данные получены')
        return self.X, self.y
