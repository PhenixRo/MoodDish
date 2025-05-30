# Emotion-Aware Smart Meal Planner API 🍽️😄

This FastAPI project recommends meals based on the user's **emotions** detected from text input using NLP and transformers.

## 🔥 Features

- **Analyze Mood** from user text input using HuggingFace Transformers
- **Meal Recommendations** based on detected emotion
- **Weather-Based Meal Suggestions** (mock data)
- Simple and fast single-file FastAPI app

## 🚀 How to Run

1. Clone the project
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Start the server:
```bash
uvicorn main:app --reload
```
4. Open your browser:
```
http://127.0.0.1:8000/docs
```

## 📦 Endpoints

- `POST /analyze_mood` – Analyze mood from user input
- `GET /meal_plan?mood=sadness` – Get meals for a mood
- `GET /weather_based_meal?location=Delhi` – Weather-based suggestion (mock)

---

Made with 💙 using FastAPI + Transformers
