from typing import Any, Optional, Final
import numpy as np
import pandas as pd
from pandas import read_csv, DataFrame, Series
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("# ================= CLASSE PER EDA =================")

class EDA:
    def __init__(self, df: DataFrame, feature_cols: list[str], target_col: str):
        self.df: DataFrame = df
        self.feature_cols: list[str] = feature_cols
        self.target_col: str = target_col

    def visual(self) -> None:
        frutti_order: list[str] = self.df[self.target_col].value_counts().index.tolist()
        palette_colors = sns.color_palette("Set3", n_colors=len(frutti_order))

        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x=self.target_col)
        plt.title(f"Distribuzione dei frutti")
        plt.xlabel(self.target_col)
        plt.ylabel("Count")
        plt.grid(True)
        plt.show()

        for feature in self.feature_cols:
            plt.figure(figsize=(12, 6))
            sns.boxplot(data=self.df, x=self.target_col, y=feature, order=frutti_order, palette=palette_colors)
            plt.title(f"Distribuzione di {feature} per tipo di frutto")
            plt.xlabel(self.target_col)
            plt.ylabel(feature)
            plt.grid(True)
            plt.show()

    def correlation(self) -> None:
        corr: DataFrame = self.df[self.feature_cols].corr()
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="Set2", square=True)
        plt.title("Correlazione tra feature")
        plt.show()

print("# ================= CLASSE PER KNN =================")
class KNNModel:
    def __init__(self, X: pd.DataFrame, y: pd.Series):
        self.X: pd.DataFrame = X
        self.y: pd.Series = y
        self.scaler: MinMaxScaler = MinMaxScaler()
        self.X_train_scaled: Optional[np.ndarray] = None
        self.X_test_scaled: Optional[np.ndarray] = None
        self.y_train: Optional[pd.Series] = None
        self.y_test: Optional[pd.Series] = None

    def preprocess(self, test_size: float = 0.2, random_state: int = 42) -> None:
        self.X = self.X.fillna(self.X.mean())
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state
        )
        self.X_train_scaled = self.scaler.fit_transform(X_train)
        self.X_test_scaled = self.scaler.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test

    def ricerca_k_migliore(self, max_k: int = 20) -> int:
        accuracy_list: list[float] = []
        for k in range(1, max_k + 1): #provato questo tipo di ottimizzazione
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(self.X_train_scaled, self.y_train)
            prediction: np.ndarray = model.predict(self.X_test_scaled)
            accuracy: float = accuracy_score(self.y_test, prediction)
            accuracy_list.append(accuracy)

        K_migliore: int = accuracy_list.index(max(accuracy_list)) + 1

        plt.figure(figsize=(10,6))
        plt.plot(range(1, max_k + 1), accuracy_list, marker='o', label='Accuracy')
        plt.scatter(K_migliore, accuracy_list[K_migliore - 1], color='red', s=100, label=f'K migliore = {K_migliore}')
        plt.xlabel("Numero di vicini (K)")
        plt.ylabel("Accuracy sul test set")
        plt.title("Accuracy vs K")
        plt.grid(True)
        plt.legend()
        plt.show()

        return K_migliore

    def _print_metrics(self, y_true: pd.Series, y_pred: np.ndarray) -> None:
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='macro')
        recall = recall_score(y_true, y_pred, average='macro')
        f1 = f1_score(y_true, y_pred, average='macro')
        confusion_matr = confusion_matrix(y_true, y_pred)
        print(f"Accuracy: {accuracy:.4f}, Precision (macro): {precision:.4f}, Recall (macro): {recall:.4f}, F1-score (macro): {f1:.4f}")
        print("Matrice di confusione:")
        print(confusion_matr)

    def train_evaluate(self, k: int) -> None:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(self.X_train_scaled, self.y_train)
        prediction: np.ndarray = model.predict(self.X_test_scaled)
        assert self.y_test is not None
        self._print_metrics(self.y_test, prediction)
        scores: np.ndarray = cross_val_score(model, self.X_train_scaled, self.y_train, cv=10)
        print("Mean CV accuracy:", scores.mean())

    def cross_validation(self, n_splits: int = 5, k: int = 3) -> None:
        K_fold: KFold = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        for fold, (train_index, val_index) in enumerate(K_fold.split(self.X), start=1):
            X_train_fold: pd.DataFrame = self.X.iloc[train_index]
            y_train_fold: Series = self.y.iloc[train_index]
            X_val_fold: pd.DataFrame = self.X.iloc[val_index]
            y_val_fold: Series = self.y.iloc[val_index]

            scaler: MinMaxScaler = MinMaxScaler()
            X_train_fold_scaled: np.ndarray = scaler.fit_transform(X_train_fold)
            X_val_fold_scaled: np.ndarray = scaler.transform(X_val_fold)

            model: KNeighborsClassifier = KNeighborsClassifier(n_neighbors=k)
            model.fit(X_train_fold_scaled, y_train_fold)
            y_pred: np.ndarray = model.predict(X_val_fold_scaled)

            print(f"Fold {fold} metrics:")
            self._print_metrics(y_val_fold, y_pred)

print("# ================= MAIN =================")
PATH: Final[str] = r"C:\Users\tiain\PycharmProjects\PythonProject\fruits.csv"
df: DataFrame = read_csv(PATH)
df.columns = [col.strip() for col in df.columns]

print("Colonne presenti nel CSV:", df.columns.tolist())

feature_cols: list[str] = [
    "Peso (g)",
    "Diametro medio (mm)",
    "Lunghezza media (mm)",
    "Durezza buccia (1-10)",
    "Dolcezza (1-10)"
]
target_col: str = "Frutto"

for col in feature_cols + [target_col]:
    if col not in df.columns:
        raise ValueError(f"Colonna '{col}' non trovata nel CSV!")

X: DataFrame = df[feature_cols]
y: Series = df[target_col]

print("\nPrime righe del dataset:")
print(df.head())

print("\nValori nulli nelle feature:")
print(X.isnull().sum())

print("# ================= EDA =================")
eda: EDA = EDA(df, feature_cols, target_col)
eda.visual()
eda.correlation()

print("# ================= KNN =================")
knn_model: KNNModel = KNNModel(X, y)
knn_model.preprocess()
K_migliore: int = knn_model.ricerca_k_migliore()
knn_model.train_evaluate(K_migliore)
knn_model.cross_validation(k=K_migliore)

print("Progetto finale di Mattia Dellanoce. "
      "Ps:(Grazie di cuore per tutto)")