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
    dict_frame_client = {}
    for frame in data.frameArray:
        res = json.loads(frame)
        frame_to_cv2 = cvt_ImageCv2(res["frame"])
        if res["name"] not in dict_frame_client.keys():
            dict_frame_client[res["name"]] = [frame_to_cv2]
        else:
            dict_frame_client[res["name"]].append(frame_to_cv2)
    f, axarr = plt.subplots(len(dict_frame_client.keys()) + 1, 10, figsize=(20, 20))
    idx = 0
    for key in dict_frame_client.keys():
        for id_frame, frame in enumerate(dict_frame_client[key]):
            axarr[idx, id_frame].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            axarr[idx, id_frame].axis('off')
        idx += 1
    plt.show()
    encoded_string = base64.b64encode(dict_frame_client["localVideo"][0])
    return {
        "data": "attack",
        "image": encoded_string
    }