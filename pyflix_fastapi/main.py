from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def home():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "home.html")
    return FileResponse(file_path)
