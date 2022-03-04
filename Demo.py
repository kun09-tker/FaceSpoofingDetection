import cv2
from Split import SplitFrame

cap = cv2.VideoCapture('capture.avi')

if (cap.isOpened() == False):
    print("Error opening video  file")

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        list_frame = SplitFrame(frame)
        for idx, f in enumerate(list_frame):
            cv2.imshow(str(idx),f)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()