from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend JS to call API without CORS errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only, restrict later!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the static files (html, css, js, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root URL
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Meal suggestions database
meal_suggestions = {
    "happy": ["smoothie", "salad", "wrap"],
    "sad": ["soup", "chocolate"],
    "hungry": ["pasta", "wrap", "salad"],
    "tired": ["smoothie", "soup"],
}

@app.post("/get_meals")
async def get_meals(request: Request):
    data = await request.json()
    mood = data.get("mood", "").lower()
    if mood not in meal_suggestions:
        return JSONResponse(status_code=404, content={"error": f"Sorry, no meals for '{mood}'"})
    return {"meals": meal_suggestions[mood]}
