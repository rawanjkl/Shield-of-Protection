SecureLink Shield – AI-Powered Protection for Absher Users

SecureLink Shield is an intelligent security system designed to protect Absher users from phishing attempts, malicious links, and digital fraud.
The system analyzes URLs in real time using a combination of:
 • Rule-based detection
 • AI-based detection (Machine Learning Model)
 • URL feature extraction
 • Risk scoring & classification

It is built to integrate seamlessly with Absher, providing users with instant protection and giving government entities a real-time view of phishing campaigns across the Kingdom.

⸻

 Core Features (MVP Delivered)

1. Rule-Based Detection

The system applies predefined security rules to identify:
 • Suspicious words (e.g., “login”, “verify”, “absher”)
 • Lack of HTTPS
 • IP-based domains
 • Recently created domains (domain age)

2. AI-Based Detection

A machine learning model trained on real phishing datasets:
 • Classifies the URL as safe/malicious
 • Generates AI-based reasons using feature weights
 • Explains which words contributed to the decision

 3. URL Feature Extraction

The system extracts key features such as:
 • URL length
 • HTTPS usage
 • Suspicious keywords
 • Domain name
 • Domain age (via WHOIS)
 • IP-based URL detection

These features contribute to the risk score displayed to the user.

4. Risk Scoring System

A clear scoring mechanism based on combined rule-based + AI signals:
 • 0–49 → Low Risk
 • 50–74 → Medium Risk
 • 75–100 → High Risk

A detailed explanation is shown to the user through the interface.

⸻

 Future Advanced Features (Integrated into API Endpoints)

The backend already includes endpoints for future expansion to emulate a full national-level digital security ecosystem for Absher.

These features are not in the MVP but are ready for integration after approval and backend access from the Ministry of Interior.

⸻

1. Digital Behavior Fingerprint

AI-based behavioral biometrics that learn:
 • Login time patterns
 • Trusted devices
 • Typing rhythm
 • Touch speed
 • Link-opening habits

If suspicious behavior occurs, the system triggers an alert.

⸻

 2. National Fraud Radar

A real-time dashboard that shows:
 • Live phishing attempts by region
 • Heatmaps of active threats
 • Volume of reported URLs
 • Detection trends across Saudi cities

Allows authorities to anticipate and respond to campaigns early.

⸻

3. Trusted Device Shield

A device protection layer that:
 • Identifies new/untrusted devices
 • Requires additional verification
 • Prevents malicious link access from unknown devices
 • Notifies users of suspicious device activity

⸻

 4. Attack Prediction Engine

A predictive AI system that analyzes:
 • Newly registered domains
 • Emerging phishing patterns
 • Daily attack trends
 • Language cues in phishing messages

And generates forecasts like:
“A new phishing campaign targeting Absher login pages is expected within 48 hours.”

⸻

5. Fraudster Observatory

A pattern-matching system that detects repeated attackers by analyzing:
 • Message structure
 • Domain patterns
 • Writing style
 • Typing similarities
 • Link-building templates

Helps identify organized fraud groups.

⸻

6. Smart QR Analysis

Advanced QR code inspection:
 • Decodes hidden URLs
 • Detects fake payment links
 • Validates source of QR generation
 • Identifies manipulated or re-generated QR codes

⸻

7. Device Identity Integrity Check

A multi-layer device authenticity check:
 • IP history
 • Device fingerprinting (non-invasive)
 • Touch/interaction behavior
 • Repeated location history

Detects fake devices and emulators commonly used by attackers.

⸻

 Tech Stack

Backend:
 • Python
 • FastAPI
 • Uvicorn
 • Scikit-Learn
 • Joblib
 • Pandas
 • tldextract
 • python-whois

Frontend:
 • Pure HTML, CSS, JavaScript
 • Fully redesigned to look identical to Absher’s style guideline

⸻

How to Run the Project

1. Install dependencies:

pip install -r requirements.txt

2. Run backend server:

uvicorn main:app --reload

3. Open the index.html file in a browser.

Project Structure

SecureLink-Shiel│── main.py
│── features.py
│── classifier.py
│── model_train.py
│── phishing_model.pkl
│── vectorizer.pkl
│── weights.json
│── index.html
│── requirements.txt
│── README.md

🛡️ Purpose
This project aims to enhance digital safety for Absher users, detect threats early, and support national cybersecurity efforts with real-time intelligence and predictive analytics.

