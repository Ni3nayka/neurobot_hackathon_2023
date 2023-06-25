# pip install opencv-contrib-python

import cv2
import cv2.aruco as aruco

# установка адреса и порта для подключения к DroidCam
address = 'http://172.22.22.115:4747/video'

# создание объекта VideoCapture для захвата видео с DroidCam
cap = cv2.VideoCapture(address)
#cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# проверка успешности подключения
if not cap.isOpened():
    print("Ошибка подключения к DroidCam")
    exit()

# задание параметров для определения аруко датчиков
#aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
#parameters = aruco.DetectorParameters_create()
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
parameters = aruco.DetectorParameters()

# цикл для вывода видео с DroidCam и определения аруко датчиков
while True:
    ret, frame = cap.read()

    if not ret:
        print("Ошибка чтения кадра")
        break

    # определение аруко датчиков
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    # отрисовка найденных аруко датчиков
    frame = aruco.drawDetectedMarkers(frame, corners, ids)

    # вывод кадра
    cv2.imshow('DroidCam', frame)

    # выход из цикла при нажатии клавиши 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# освобождение ресурсов
cap.release()
cv2.destroyAllWindows()