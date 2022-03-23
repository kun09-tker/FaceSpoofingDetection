import os
import cv2
import shutil
import random
import numpy as np


def __movefile__ (filename,dir,lenght,flag = "",pre=True):
    dir_split = dir.split("/")
    dir_ = dir_split[0]
    if os.path.isdir(dir_) is False:
        os.mkdir(dir_)
    for d in dir_split[1:]:
        dir_ += "/" + str(d)
        if os.path.isdir(dir_) is False:
            os.mkdir(dir_)

    list_frame = []
    list_dir_file = []
    x_result = np.array([])
    y_result = np.array([])

    for root, dirs, files in os.walk(filename, topdown=False):
        for name in files:
            dir_file = str(os.path.join(root, name)).replace("\\","/")
            list_dir_file.append(dir_file)
    # str_pre = ""
    # if lenght == -1:
    #     lenght = len(list_dir_file)
    #     print(lenght)
    # for idx in range(lenght):
    #     a = random.randint(0,len(list_dir_file)-1)
    #     if pre is True:
    #         str_pre = "_" + list_dir_file[a].split("/")[-2]
    #     old = list_dir_file[a]
    #     new = str(dir)+"/"+list_dir_file[a].split("/")[-1][:-4]+str_pre+"_"+ str(flag) + ".mp4"
    #     shutil.move(old, new)
    #     list_dir_file.remove(list_dir_file[a])
    for idx_dir_file in range(len(list_dir_file)):
        dir_file = list_dir_file[idx_dir_file]
        staste = dir_file.split("/")[-2]
        cap = cv2.VideoCapture(dir_file)
        if (cap.isOpened() == False):
            print("Error opening video  file")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                list_frame.append(np.array(frame))
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        batchs = len(list_frame)//(lenght*10)
        for batch in range(batchs):
            list_batch_frame = [list_frame[idx*lenght+batch*lenght*10] for idx in range(10)]
            x_result = np.append(x_result, list_batch_frame)
            if staste == "attack":
                y_result = np.append(y_result,1)
            else:
                y_result = np.append(y_result,0)
        list_frame.clear()
        x = x_result.reshape([-1,240,320,3,10])
        y = np.transpose(np.array([y_result]))
        print(idx_dir_file)
        print(x.shape)
        print(y.shape)
        x_result = np.array([])
        y_result = np.array([])
        np.save(str(dir)+"/x_valid"+str(idx_dir_file)+".npy", x)
        np.save(str(dir)+"/y_valid"+str(idx_dir_file)+".npy", y)
__movefile__("ReplayAttack/valid","ReplayAttackSample/valid",1,"",False)



