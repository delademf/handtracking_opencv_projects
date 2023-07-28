import cv2 as cv
import mediapipe as mp
import time

capture = cv.VideoCapture(0)

#sort of like calling the solutions for my hands from the package
mpHands =mp.solutions.hands
hands = mpHands.Hands()
mpdraw = mp.solutions.drawing_utils

pTime=0
cTime=0

while True:
    isTrue,frame =capture.read()
    #mp works in RGB hence has to be changed
    imgRGB = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #this below check position of hand
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLns in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(frame,handLns,mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv.putText(frame,str(int(fps)),(10,78),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)


    cv.imshow('live video',frame)
    cv.waitKey(1)