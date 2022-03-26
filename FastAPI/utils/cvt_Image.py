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
# def toRGB(image):
#     return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def cvt_ImageCv2(imageData):
    imageCv2 = stringToImage(imageData.replace('data:image/png;base64,', '').replace(' ', '+'))
    return imageCv2


