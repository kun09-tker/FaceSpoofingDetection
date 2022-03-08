import cv2
import numpy as np
import math

def SplitFrame(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(img_gray,50,150)
    dilation = cv2.dilate(edges,None,iterations = 1)

    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(dilation,1,np.pi/180,100,minLineLength,maxLineGap)
    y1_crop = lines[0][0][1]
    y2_crop = lines[1][0][1]

    if(y1_crop > y2_crop):
        y1_crop,y2_crop = y2_crop,y1_crop

    if((y2_crop-y1_crop)/image.shape[0] <= 0.7):
        y2_crop = image.shape[0]

    frame = image[y1_crop:y2_crop, :]
    frame_gray = img_gray[y1_crop:y2_crop, :]

    thread = frame_gray[frame.shape[0]//2][1]
    print(thread)

    frame_binary_light_background = cv2.threshold(frame_gray,thread+1.5,255,cv2.THRESH_BINARY)[1]
    frame_binary_dark_background = cv2.threshold(frame_gray,thread-1.5,255,cv2.THRESH_BINARY_INV)[1]
    frame_binary = cv2.bitwise_or(frame_binary_light_background,frame_binary_dark_background)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 1))
    frame_dilation = cv2.morphologyEx(frame_binary, cv2.MORPH_DILATE, kernel)

    #cv2.imshow("f", frame)
    # cv2.imshow("fbl", frame_binary_light)
    # cv2.imshow("fbd", frame_binary_dark)
    # cv2.imshow("fb", frame_binary)
    #cv2.imshow("fd",frame_dilation)

    list_line_frame = []

    cnts, hierarchy = cv2.findContours(frame_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    temp_c = sorted(cnts, key=cv2.contourArea, reverse=True)
    max_area = cv2.contourArea(temp_c[0])
    for c in temp_c:
        area = cv2.contourArea(c)
        if(area/max_area >= 0.5):
            x, y, w, h = cv2.boundingRect(c)
            list_line_frame.append({"color":frame.copy()[y:y + h, x:x + w],"binary":frame_binary.copy()[y:y + h, x:x + w]})

    # row = col = int(math.sqrt(len(list_line_frame)))
    # if (math.sqrt(len(list_line_frame)) != row):
    #     col = col + 1
    #
    # f, axarr = plt.subplots(row + 1, col + 1, figsize=(50, 50))
    # for index, split_frame in enumerate(list_line_frame):
    #     axarr[int(index / col)][index % col].imshow(split_frame["color"])

    list_split_frame = []

    for idx,line_frame in enumerate(list_line_frame):
        #cv2.imshow(str(idx), line_frame["color"])
        cnts, hierarchy = cv2.findContours(line_frame["binary"].copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        temp_c = sorted(cnts, key=cv2.contourArea, reverse=True)
        max_area = cv2.contourArea(temp_c[0])
        for c in temp_c:
            area = cv2.contourArea(c)
            if (area/max_area >= 0.5):
                x, y, w, h = cv2.boundingRect(c)
                list_split_frame.append(line_frame["color"].copy()[y:y + h, x:x + w])
    return list_split_frame

# import matplotlib.pyplot as plt
# import math
#
# image = cv2.imread("Data/2.png")
#
# list_split_frame = SplitFrame(image)
#
# row = col = int(math.sqrt(len(list_split_frame)))
# if(math.sqrt(len(list_split_frame)) != row):
#     col = col + 1
#
# f, axarr = plt.subplots(row+1,col+1, figsize=(50,50))
# for index,split_frame in enumerate(list_split_frame):
#     axarr[int(index/col)][index%col].imshow(split_frame)
# plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()

