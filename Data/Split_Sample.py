import os
import cv2

def read_video(filename,dir,batch,sample):

    dir_split = dir.split("\\")
    dir_ = dir_split[0]
    for d in dir_split[1:]:
        if os.path.isdir(dir_) is False:
            os.mkdir(dir_)
        dir_ += "/" + str(d)

    list_frame = []
    for root, dirs, files in os.walk(filename, topdown=False):
        for name in files:
            dir_file = str(os.path.join(root, name))
            dir_file_split = dir_file.split("\\")
            dir_ = dir
            for f in dir_file_split[1:]:
                if os.path.isdir(dir_) is False:
                    os.mkdir(dir_)
                dir_ += "/" + str(f)

            cap = cv2.VideoCapture(dir_file)
            if (cap.isOpened() == False):
                print("Error opening video  file")
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    list_frame.append(frame)
                else:
                    break
            cap.release()
            cv2.destroyAllWindows()
            print(len(list_frame))
            if os.path.isdir(dir_[:-4]) is False:
                os.mkdir(dir_[:-4])
            for b in range(batch):
                dir_sample = dir_[:-4]+"/batch"+str(b)
                if os.path.isdir(dir_sample) is False:
                    os.mkdir(dir_sample)
                for s in range(sample):
                    cv2.imwrite(str(dir_sample)+"/sample_"+str(s)+".png",list_frame[b*len(list_frame)//sample//batch+s*len(list_frame)//sample])
            list_frame.clear()

read_video("data","data/sample",12,10)


