
import cv2
import numpy as np

vid = cv2.VideoCapture('vtest.avi')
if vid.isOpened() == False:
    print('failed to open video source')
ret, prev = vid.read()
prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

while True:
    ret, cur = vid.read()
    if cur is None:
        print("frame is none")
        break
    width = cur.shape[1]
    height = cur.shape[0]
    mask = np.zeros(prev.shape)
    cur = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)

    t1 = cv2.getTickCount()
    mask = np.where(np.abs(cur.astype(np.int) - prev.astype(np.int)) > 50, 255, 0)
    #for i in range(height):
    #    for j in range(width):
    #        if abs(int(cur[i, j]) - int(prev[i, j])) > 50:
    #            mask[i, j] = 255
    print((cv2.getTickCount() - t1) / cv2.getTickFrequency())
    cv2.imshow('prev', prev)
    cv2.imshow('cur', cur)
    cv2.imshow('mask', mask.astype(np.uint8))
    prev = cur
    cv2.waitKey(1)

