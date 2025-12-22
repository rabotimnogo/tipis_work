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
            
            # сохраняем модель
            joblib.dump(model, 'src/models/saved_logreg.joblib')

            # проверяем что файл создался
            if os.path.exists('src/models/saved_logreg.joblib'):
                print('модель сохранилась')
                return True

            else:
                print('модель не сохранилась')
                return False

        except Exception as e:
            print(f'ошибка сохранения: {e}')
            return False
