# src/logistic_regression.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def load_data(path):
    data = pd.read_csv(path)

    data = data.drop(["sl_no", "salary"], axis=1)

    cols = [
        "gender",
        "ssc_b",
        "hsc_b",
        "hsc_s",
        "degree_t",
        "workex",
        "specialisation",
        "status"
    ]

    le = LabelEncoder()

    for col in cols:
        data[col] = le.fit_transform(data[col])

    return data


def train_model(data):

    X = data.drop("status", axis=1)
    y = data["status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = DecisionTreeClassifier()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy:.4f}")

    return model


if __name__ == "__main__":

    dataset = load_data("data/Placement.csv")

    model = train_model(dataset)
