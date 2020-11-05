import cv2
import sys
import numpy as np

cap = cv2.VideoCapture("../data/vtest.avi")
if (cap.isOpened() == False):
    print('failed to open file')
    sys.exit()
frameNum = 0
while True:
    ret, cur = cap.read()
    if cur is None:
        break
    cur = cv2.cvtColor(cur, cv2.COLOR_BGR2GRAY)
    frameNum += 1
    if frameNum == 1:
        prev = cur
        continue

    sub = np.abs(cur.astype(np.int) - prev.astype(np.int))
    mask = np.where(sub > 50, 255, 0).astype(np.uint8)
    cv2.imshow('cur', cur)
    cv2.imshow('prev', prev)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    prev = cur
