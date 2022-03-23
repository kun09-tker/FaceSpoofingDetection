from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    image: str
    name: str

@app.get("/")
async def root(name: str):
    return{f"Hello World {name}"}

@app.post("/Frame")
async def create_file(
    file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }