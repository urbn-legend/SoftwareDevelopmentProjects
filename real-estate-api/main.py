from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "*"],  # Ensure it's a valid Python list
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Use valid Python list
    allow_headers=["Content-Type", "Authorization"]
)

@app.get("/")
def home():
    return {"message": "CORS is working!"}
