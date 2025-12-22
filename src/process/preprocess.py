import numpy as np
import pandas as pd

from sklearn.preprocessing import RobustScaler

class Prepocessor:
    '''
    класс для предобработки данных
    '''
    def __init__(self, data: pd.DataFrame):
        self.df = pd.read_csv("src/data/creditcard.csv")
        self._scalling()

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
        not_frauds = new_df.query("Class == 0")
        frauds = new_df.query("Class == 1")

        # собираем сбалансированный датафрейм
        balanced_df: pd.DataFrame = pd.concat([frauds, not_frauds.sample(len(frauds), random_state=1)])

        # сэмплируем дф
        balanced_df: pd.DataFrame = balanced_df.sample(frac=1, random_state=1)

        # можно не преобразовывать, опционально
        balanced_df_np: np.NdArray = balanced_df.to_numpy()  

        return balanced_df_np
