import io
import os
import cv2
import base64
from matplotlib import image
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import os
from matplotlib import pyplot as plt

list_dir_file = []
dict_frame_client = {}
# Take in base64 string and return PIL image
    

# def arrayToImage(a):
#     list_img = []
#     for ai in a:
#         img = Image.fromarray((ai).astype(np.uint8))
#         b, g, r = img.split()
#         img = Image.merge("RGB", (r, g, b))
#         imgArray = np.asarray(img)
#         list_img.append(imgArray)
#     return np.array(list_img).reshape([-1,240,320,3,10])

def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    pil_image = Image.open(io.BytesIO(imgdata)).convert('RGB')
    return pil_image

# convert PIL Image to an RGB image( technically a numpy array ) that's compatible with opencv
# def toRGB(image):
#     return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

def predict(list_image):
    np_img = np.array(list_image).reshape([-1,240,320,3,10])
    # print(np_img.shape)
    labels = {0 : 'attack', 1 : 'real'}
    path_model = os.path.join("FaceSpoofingDetection",'anti_spoofing_training-11-04_best.h5')
    # print(path_model)
    model = load_model(path_model)
    y_prob = model.predict(np_img)
    y_predict = np.argmax(y_prob, axis = 1)
    # print(labels[y_predict[0]])
    return labels[y_predict[0]]

def cvt_ImagePIL(imageData):
    imagePIL = stringToImage(imageData.replace('data:image/png;base64,', '').replace(' ', '+'))
    newsize = (320, 240)
    imagePIL = imagePIL.resize(newsize)
    # print(np.array(imagePIL).shape)
    return np.array(imagePIL)

# np_test = np.array([np.load('FaceSpoofingDetection/dumamay/x_valid_1138_attack.npy')])
# np_test = np.array(np_test).reshape([10,240,320,3])
# f, axarr = plt.subplots(2, 10, figsize=(20, 20))
# for id_frame, frame in enumerate(np_test):
#     axarr[0, id_frame%10].imshow(frame)
#     axarr[0, id_frame%10].axis('off')
# plt.show()
# predict(np_test)


