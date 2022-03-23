import io
import os
import cv2
import base64
import numpy as np
from PIL import Image

list_dir_file = []
dict_frame_client = {}
# Take in base64 string and return PIL image
def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    pil_image = Image.open(io.BytesIO(imgdata)).convert('RGB')
    open_cv_image = np.array(pil_image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image

# convert PIL Image to an RGB image( technically a numpy array ) that's compatible with opencv
def toRGB(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

for root, dirs, files in os.walk("./frameData", topdown=False):
    number_of_client = len(files)
    for name in files:
        dir_file = str(os.path.join(root, name)).replace("\\", "/")
        f = open(dir_file, "r")
        name = dir_file.split('/')[-1][:-4]
        imgdata = stringToImage(f.read().replace('data:image/png;base64,', '').replace(' ', '+'))
        if name is not dict_frame_client.keys():
            dict_frame_client[name] = [imgdata]
        else:
            dict_frame_client[name].append(imgdata)

print(dict_frame_client)


