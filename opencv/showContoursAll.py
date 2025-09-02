import sys,os
import numpy as np
import cv2 as cv

#######gif read###
#file = r"c:\myProject\nalog\captcha\221459\za1aloeh.ztt.png";

def show_image_with_contours(file):
    gif = cv.VideoCapture(file)
    ret, img = gif.read()
    #################

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    element = cv.getStructuringElement(cv.MORPH_CROSS,(2,2))
    # Выполняем операции эрозия и дилатация
    erode_dilate = cv.dilate(cv.erode(gray,element),element)

    blur = cv.GaussianBlur(erode_dilate,(5,5),0)
    thresh = cv.adaptiveThreshold(blur,255,1,1,11,2)

    contours0, hierarchy = cv.findContours( thresh.copy(), cv.RETR_EXTERNAL  , cv.CHAIN_APPROX_TC89_KCOS)

    def seporate(x,y,w,h):
        cord = [];
        if w / h >= 1.25:
            half_width = int(w / 2)
            cord.append((x,y,half_width,h))
            cord.append((x+half_width,y,half_width,h))
        else:
            cord.append((x,y,w,h))
        return cord;

    cord = [];
    for cnt in contours0:
        if cv.contourArea(cnt) > 50:
            [x,y,w,h] = cv.boundingRect(cnt)
            print('x = {} y = {} w = {} h = {} w/h = {}'.format(x,y,w,h,w / h) )
            for (x,y,w,h) in seporate(x,y,w,h):
                cord.append((x,y,w,h))

    cordResult = [];
    for (x,y,w,h) in cord:
        for (x,y,w,h) in seporate(x,y,w,h):
            cordResult.append((x,y,w,h))

    cordResult = sorted(cordResult, key=lambda x: x[0])
    print('------')
    for (x,y,w,h) in cordResult:
        print('x = {} y = {} w = {} h = {} w/h = {}'.format(x,y,w,h,w / h) )
        cv.rectangle(img, (x , y),(x + w, y + h), (0,0,255),2)
        roi = thresh[y:y + h, x:x + w]
        roismall = cv.resize(roi,(10,10))
        letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]

    cv.imshow('norm',img)

for root, dirnames, filenames in os.walk(r"c:\\myProject\\nalog\\captcha\\"):
    for filename in filenames:
        file = os.path.join(root, filename)
        show_image_with_contours(file)
        # 13 entry
        # 32 space
        key = cv.waitKey()
        if(key == 13):
            break
        print('------------------')

# 0  right
cv.destroyAllWindows()