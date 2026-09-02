from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from features import extract_features
from classifier import classify_features, classify_with_ai

app = FastAPI()

# حل مشكلة CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# لعرض صفحة HTML
@app.get("/")
async def home():
    return FileResponse("index.html")


# استقبال الرابط من المستخدم
class LinkIn(BaseModel):
    url: str


# تحليل الرابط
@app.post("/analyze")
async def analyze(link: LinkIn):
    url = link.url

    # استخراج الخصائص
    features = await extract_features(url)

    # تصنيف بواسطة القواعد
    rule_result, score, reasons = classify_features(features)

    # تصنيف بواسطة الذكاء الاصطناعي
    ai_result = classify_with_ai(url)

    # تحديد مستوى الخطر
    risk_score = min(score * 25, 100)
    if risk_score >= 75:
        risk_level = "High"
    elif risk_score >= 50:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    # دمج النتائج
    final_result = {
        "rule_based": rule_result,
        "ai_based": ai_result["prediction"],
        "risk_score": risk_score,
        "risk_level": risk_level
    }

    return {
        "url": url,
        "result": final_result,
        "rule_reasons": reasons,
        "ai_reasons": ai_result["ai_reasons"],
        "features": features
    }


# ============================
#     Additional Future APIs  
# ============================

@app.get("/behavior-fingerprint")
async def behavior_fingerprint():
    return {
        "status": "coming_soon",
        "description": "AI-based behavioral fingerprinting will detect unusual login behavior and suspicious devices."
    }

@app.get("/fraud-radar")
async def fraud_radar():
    return {
        "status": "coming_soon",
        "description": "Live national fraud radar will show real-time fraud attempts distributed by region."
    }

@app.get("/trusted-device-shield")
async def trusted_device_shield():
    return {
        "status": "coming_soon",
        "description": "System will block unknown devices and require advanced verification."
    }

@app.get("/predictive-engine")
async def predictive_engine():
    return {
        "status": "coming_soon",
        "description": "AI engine will predict phishing campaigns before they start using domain and pattern analysis."
    }

@app.get("/fraudster-observatory")
async def fraudster_observatory():
    return {
        "status": "coming_soon",
        "description": "Observatory will identify recurring fraud patterns and recognize repeated attackers."
    }