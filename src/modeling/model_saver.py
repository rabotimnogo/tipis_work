import os
import joblib
from sklearn.linear_model import LogisticRegression
from modeling.train import logistic_model_b

class ModelSaver:
    '''
    класс для сохранения модели
    '''
    def save(self, model: LogisticRegression = logistic_model_b) -> bool:
        '''
        сохраняет модель в файл
        '''
        try:
            os.makedirs("models", exist_ok=True)

            # сохраняем модель
            joblib.dump(model, "model_saved.joblib")

            # проверяем что файл создался
            if os.path.exists("model_saved.joblib"):
                print("Модель сохранена")
                return True

            else:
                print("Модель НЕ сохранена")
                return False

        except Exception as e:
            print(f"ошибка сохранения: {e}")
            return False
