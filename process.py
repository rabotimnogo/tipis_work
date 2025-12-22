import numpy as np
import pandas as pd

from sklearn.preprocessing import RobustScaler

class Prepocessor:
    '''
    класс для предобработки данных
    '''
    def __init__(self, data: pd.DataFrame = pd.read_csv("src/data/creditcard.csv")):
        self.df = data

    def _scalling(self) -> np.NdArray:
        '''
        Метод предобрабатывает данные для модели.
        '''

        # делаем данные робастными
        new_df: pd.DataFrame = self.df.copy()
        new_df["Amount"] = RobustScaler().fit_transform(
            new_df["Amount"].to_numpy().reshape(-1, 1)
        )

        # скелинг, для лучшей сходимости градиента 
        time = new_df["Time"]
        new_df["Time"] = (time - time.min()) / (time.max() - time.min())

        # убираем таргет, чтобы моделька делала предикт
        scalling: pd.DataFrame = new_df.drop('class', axis=1)

        return scalling
