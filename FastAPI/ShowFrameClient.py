import pickle
import cv2
import matplotlib.pyplot as plt

with open("Data/data.json","rb") as json_file:
    dict_frame_client = pickle.load(json_file)

f, axarr = plt.subplots(len(dict_frame_client.keys()) + 1, 10,figsize=(20,20))
idx = 0
for key in dict_frame_client.keys():
    for id_frame, frame in enumerate(dict_frame_client[key]):
        axarr[idx, id_frame].imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        axarr[idx, id_frame].axis('off')
    idx += 1
plt.show()