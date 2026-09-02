import joblib
import json


# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load feature weights
try:
    with open("weights.json", "r", encoding="utf-8") as f:
        feature_weights_data = json.load(f)
        feature_weights = dict(zip(feature_weights_data["features"], feature_weights_data["weights"]))
except Exception as e:
    print("Could not load weights.json:", e)
    feature_weights = {}

# === AI-based classification ===
def classify_with_ai(url: str):
    vector = vectorizer.transform([url])
    prediction = model.predict(vector)[0]  # "safe" or "malicious"
    ai_reasons = explain_prediction(url)["ai_reason"]
    return {"prediction": prediction, "ai_reasons": ai_reasons}

# === Rule-based classification ===
def classify_features(features):
    score = 0
    reasons = []

    # Rule: suspicious words
    if features.get("suspicious_words"):
        score += len(features["suspicious_words"])
        reasons.extend([f"Suspicious word: {w}" for w in features["suspicious_words"]])

    # Rule: HTTPS check
    if not features.get("has_https"):
        score += 1
        reasons.append("URL does not use HTTPS")

    # Rule: IP instead of domain
    if features.get("has_ip"):
        score += 1
        reasons.append("URL contains an IP address instead of a domain")

    # Final result
    result = "malicious" if score > 0 else "safe"

    return result, score, reasons

# === Explain AI decision ===
def explain_prediction(url: str):
    results = {
        "ai_reason": [],
        "debug": []
    }
    try:
        vector = vectorizer.transform([url])
        arr = vector.toarray()[0]

        words = url.lower().split("/")
        for w in words:
            w = w.strip()
            if w in feature_weights:
                weight = feature_weights[w]
                if weight > 0:
                    results["ai_reason"].append(f"The word '{w}' indicates phishing behavior (weight={weight})")
                elif weight < 0:
                    results["ai_reason"].append(f"The word '{w}' indicates safety (weight={weight})")

        if not results["ai_reason"]:
            results["ai_reason"].append("No specific pattern found — decision based on AI model only.")

    except Exception as e:
        results["ai_reason"].append("AI prediction could not be explained.")
        results["debug"].append(str(e))

    return results