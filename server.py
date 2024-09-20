import cv2
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
#
from services import search_face

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.post("/whoami", status_code=200)
async def whoami(photo: UploadFile = File(...)):
    imagedata = await photo.read()
    np_array = np.frombuffer(imagedata, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    result = await search_face(image)
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8088, reload=True)