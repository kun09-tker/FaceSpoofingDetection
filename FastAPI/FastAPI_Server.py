import base64
import json
import pickle

import cv2
import numpy as np
from fastapi import FastAPI
from matplotlib import pyplot as plt

from FastAPI.Products.Client import Client
from FastAPI.utils.cvt_Image import cvt_ImageCv2

app = FastAPI()

@app.get("/")
async def root(name: str):
    return{f"Hello World {name}"}

@app.post("/Frame")
async def create_upload_file(data: Client):
    dict_frame_client = []
    for frame in data.frameArray:
        res = json.loads(frame)
        frame_to_cv2 = cvt_ImageCv2(res["frame"])
        base64_frame_client = res["frame"]
        video_id = res["name"]
        dict_frame_client.append(frame_to_cv2)
    f, axarr = plt.subplots(2, 5, figsize=(20, 20))
    for id_frame, frame in enumerate(dict_frame_client):
        axarr[id_frame//5, id_frame%5].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        axarr[id_frame//5, id_frame%5].axis('off')
    return {
        "data": "attack",
        "video_id": video_id,
        "image": base64_frame_client
    }