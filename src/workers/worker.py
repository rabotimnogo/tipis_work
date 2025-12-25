# import streamlit as st
# import pickle

# from src.process.preprocess import Prepocessor
# from src.lib.models.model import LogRegBalanced
# from src.lib.loader.data_loader import DataLoader


# class Worker:
#     def __init__(self):
#         self._build()
        
#     def _build() -> bool:
        
#         loader = DataLoader()
#         model = LogRegBalanced()

#         # Основное приложение
#         st.title("Fraud Detection App")
#         st.markdown("---")


#         # Кнопка 1: Предикт на встроенных данных
#         if st.button("Предикт"):
#             df_builtin = loader.load_builtin()
            
#             if df is not None:
#                 processed_builtin_data = Prepocessor(df_builtin)
#                 X_builtin, y_builtin = processed_builtin_data.get_data()
                
#                 y_pred_builtin = model.predict(X_builtin)

#                 # Вывод отчета
#                 st.text("Classification Report:")
#                 st.text(y_pred)
#                 st.text(model.eval_model(y_true=y_builtin, y_pred=y_pred_builtin))
#             else:
#                 st.error("Файл не найден! Положите creditcard.csv в src/data/")

#         st.markdown("---")

#         # Кнопка 2: Предикт на данных пользователя
#         st.write("Или загрузите свои данные:")
#         uploaded_file = st.file_uploader("Выберите CSV файл", type=['csv'])

#         if uploaded_file and st.button("Предикт по вашим данным"):

#             df_user = = loader.load_user(uploaded_file)
#             st.write(f'файл загружен')

#             processed_builtin_data = Prepocessor(df_user)
#             X_user, y_user = processed_builtin_data.get_data()
                
#             y_pred_user = model.predict(X)

#             # Вывод отчета
#             st.text("Classification Report:")
#             st.text(y_pred)
#             st.text(model.eval_model(y_true=y_user, y_pred=y_pred_user))

#             print('сбилдилось')


            