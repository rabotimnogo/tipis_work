"""
копия с ноутбука, фит линейной регрессии, ручное разбиение на тест/трейн дату
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import RobustScaler

df = pd.read_csv("src/data/creditcard.csv")

new_df = df.copy()
new_df["Amount"] = RobustScaler().fit_transform(
    new_df["Amount"].to_numpy().reshape(-1, 1)
)

time = new_df["Time"]
new_df["Time"] = (time - time.min()) / (time.max() - time.min())

not_frauds = new_df.query("Class == 0")
frauds = new_df.query("Class == 1")

balanced_df = pd.concat([frauds, not_frauds.sample(len(frauds), random_state=1)])

balanced_df = balanced_df.sample(frac=1, random_state=1)

balanced_df_np = balanced_df.to_numpy()  # можно не преобразовывать, опционально

# ручное разбиение
x_train_b, y_train_b = balanced_df_np[:700, :-1], balanced_df_np[:700, -1].astype(int)
x_test_b, y_test_b = balanced_df_np[700:842, :-1], balanced_df_np[700:842, -1].astype(
    int
)
x_val_b, y_val_b = balanced_df_np[842:, :-1], balanced_df_np[842:, -1].astype(int)

# обучение модели
logistic_model_b = LogisticRegression()
logistic_model_b.fit(x_train_b, y_train_b)

# eval модели
print(
    classification_report(
        y_val_b, logistic_model_b.predict(x_val_b), target_names=["Not Fraud", "Fraud"]
    )
)
print('модель обучена')
"""
супер
              precision    recall  f1-score   support

   Not Fraud       0.92      1.00      0.96        72
       Fraud       1.00      0.91      0.96        70

    accuracy                           0.96       142
   macro avg       0.96      0.96      0.96       142
weighted avg       0.96      0.96      0.96       142
"""

