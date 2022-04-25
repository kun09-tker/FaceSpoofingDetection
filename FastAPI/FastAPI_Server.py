import base64
import json
import pickle
from unittest import result
import cv2
import numpy as np

from fastapi import FastAPI
from matplotlib import pyplot as plt
from FastAPI.Products.Client import Client
from FastAPI.utils.cvt_Image import cvt_ImagePIL
from FastAPI.utils.cvt_Image import predict

app = FastAPI()

@app.get("/")
async def root(name: str):
    return{f"Hello World {name}"}

@app.post("/Frame")
async def create_upload_file(data: Client):
    idx = 0
    list_frame_client = []
    for frame in data.frameArray:
        res = json.loads(frame)
        frame_to_cv2 = cvt_ImagePIL(res["frame"])
        if idx==0:
            base64_frame_client = res["frame"]
        list_frame_client.append(frame_to_cv2)
        idx += 1
    
    # predict(list_frame_client)
    # f, axarr = plt.subplots(2, 10, figsize=(20, 20))
    # for id_frame, frame in enumerate(list_frame_client):
    #     axarr[0, id_frame%10].imshow(frame)
    #     axarr[0, id_frame%10].axis('off')
    # plt.show()

    return {
        "result" : {
            "data": predict(list_frame_client),
            "image": base64_frame_client
        }
    }