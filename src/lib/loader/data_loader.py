import pandas as pd
import streamlit as st
from pathlib import Path
from datetime import datetime
import uuid

class DataLoader:
    """
    Простой загрузчик данных.
    Загружает: 
    1. Встроенные данные из src/data/creditcard.csv
    2. Данные пользователя 
    """
    
    def __init__(self):
        self.data_path = Path("src/data")
        self.data_path.mkdir(parents=True, exist_ok=True)
        self.builtin_file = "creditcard.csv"
    
    def load_builtin(self) -> pd.DataFrame:

        file_path = self.data_path / self.builtin_file
        df = pd.read_csv(file_path)
        
        return df
    
    def load_user(self, uploaded_file) -> pd.DataFrame:
        
        if uploaded_file is None:
            return None
        
        # Читаем данные
        df = pd.read_csv(uploaded_file)
        
        # Генерируем уникальное имя для сохранения
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = str(uuid.uuid4())[:8]
        original_name = Path(uploaded_file.name).stem
        save_filename = f"user_{timestamp}_{unique_id}_{original_name}.csv"
        save_path = self.data_path / save_filename
        
        # Сохраняем с уникальным именем
        df.to_csv(save_path, index=False)
        
        st.success(f" Файл сохранен как: {save_filename}")
        
        return df