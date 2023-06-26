import cv2
import numpy as np
#import video

if __name__ == '__main__':
   def callback(*arg):
       print (arg)

cv2.namedWindow( "result" )

cap = video.create_capture(0)
#cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

hsv_min = np.array((83, 0, 42), np.uint8)
hsv_max = np.array((132, 69, 114), np.uint8)

while True:
    flag, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)

    cv2.imshow('result', thresh)

    if cv2.waitKey(5) ==  27:
        break

cap.release()
cv2.destroyAllWindows()