import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# قراءة البيانات
df = pd.read_csv("dataset.csv")

# الموديل يعمل على النص مباشرة
X = df["url"]
y = df["label"]

# تحويل الروابط إلى أرقام (Vectorization)
vectorizer = CountVectorizer()
X_vectors = vectorizer.fit_transform(X)

# تدريب النموذج
model = LogisticRegression()
model.fit(X_vectors, y)

# استخراج الأوزان مع الكلمات
import json

feature_weights = model.coef_[0]
feature_names = vectorizer.get_feature_names_out()

weights_data = {
    "features": feature_names.tolist(),
    "weights": feature_weights.tolist()
}

with open("weights.json", "w", encoding="utf-8") as f:
    json.dump(weights_data, f)

print("Weights saved successfully!")
# حفظ النموذج
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")