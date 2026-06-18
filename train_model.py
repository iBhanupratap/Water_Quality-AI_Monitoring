import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("dataset/water_potability.csv")

print("Dataset Shape:", df.shape)

# ==========================
# HANDLE MISSING VALUES
# ==========================

for col in ['ph', 'Sulfate', 'Trihalomethanes']:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# FEATURES & TARGET
# ==========================

X = df.drop("Potability", axis=1)
y = df["Potability"]

# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ==========================
# FINAL MODEL
# ==========================

rf_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    min_samples_leaf=4,
    min_samples_split=10,
    class_weight='balanced',
    random_state=42
)

# Train
rf_model.fit(X_train, y_train)

# Predict
y_pred = rf_model.predict(X_test)

# ==========================
# EVALUATION
# ==========================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==========================
# CROSS VALIDATION
# ==========================

cv_scores = cross_val_score(
    rf_model,
    X,
    y,
    cv=5,
    scoring='recall'
)

print("\nRecall CV Scores:", cv_scores)
print("Average Recall:", cv_scores.mean())

# ==========================
# SAVE MODEL
# ==========================

joblib.dump(rf_model, "model.pkl")

print("\nModel saved successfully!")