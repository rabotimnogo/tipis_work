from src.process.preprocess import Prepocessor


class Pipeline:

    def __init__(self):
        self.process_data()
        self.split_data()
        self.fit_model()
        self.predict_data()
    
    def process_data() -> bool:
        '''
        Препроцессим данные
        '''
        if Prepocessor():
            print('Препроцесс данных удался')
            return True
        else:
            print('Препроцесс данных НЕ удался')
            return False

    def split_data() -> bool:
        pass

    def fit_model() -> bool:
        pass

    def predict_data() -> eval:
        pass
    