import re
import tldextract
import whois
from datetime import datetime

async def extract_features(url: str):
    features = {}

    features["length"] = len(url)
    features["has_https"] = url.startswith("https://")

    ip_pattern = r"http[s]?://(\d{1,3}\.){3}\d{1,3}"
    features["has_ip"] = bool(re.search(ip_pattern, url))

    suspicious = ["login", "verify", "absher"]
    features["suspicious_words"] = [w for w in suspicious if w in url.lower()]

    parsed = tldextract.extract(url)
    domain = f"{parsed.domain}.{parsed.suffix}"
    features["domain"] = domain

    # عمر الدومين
    try:
        w = whois.whois(domain)
        if isinstance(w.creation_date, list):
            creation = w.creation_date[0]
        else:
            creation = w.creation_date

        if creation:
            age = (datetime.utcnow() - creation).days
            features["domain_age_days"] = age
        else:
            features["domain_age_days"] = None

    except:
        features["domain_age_days"] = None

    return features
