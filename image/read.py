# here we are reading Images

import cv2 as cv
# img=cv.imread('image\wallpaper2.jpg')
# cv.imshow('wallpaper',img)
# cv.waitKey(0)

#Here we will going to read videos
capture=cv.VideoCapture('image\5 best website.mp4')
while True:
    isTrue,frame=capture.read()

    cv.imshow('Video',frame)
    
    if cv.waitKey(0) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



