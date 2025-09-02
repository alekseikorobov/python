import sys
import numpy as np
import cv2 as cv

# hsv_min = np.array((2, 28, 65), np.uint8)
# hsv_max = np.array((26, 238, 255), np.uint8)

hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((0, 0, 0), np.uint8)


#######gif read###
file = r"c:\\myProject\\nalog\\captcha\\out\result\zrpkxn2j.1v1_0_2.png";

gif = cv.VideoCapture(file)
ret, img = gif.read()
#################

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
element = cv.getStructuringElement(cv.MORPH_CROSS,(2,2))
# Выполняем операции эрозия и дилатация
erode_dilate = cv.dilate(cv.erode(gray,element),element)

blur = cv.GaussianBlur(erode_dilate,(5,5),0)
thresh = cv.adaptiveThreshold(blur,255,1,1,11,2)

# cv.imshow('erode_dilate',erode_dilate)
# cv.waitKey()
##########################
# imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# ret,thresh = cv.threshold(imgray,127,255,0)
# contours0, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
##########################


# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# # cv.imshow('frame',gray)
# # cv.waitKey()
# #img = cv.imread(file)

# #hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
# thresh = cv.inRange( hsv, hsv_min, hsv_max )

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# ## Threshold 
# ret, threshed = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
# thresh = cv.threshold(image, 0, 255,
#                            cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
####
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # Add some extra padding around the image
# gray = cv.copyMakeBorder(gray, 8, 8, 8, 8, cv.BORDER_REPLICATE)
# # threshold the image (convert it to pure black and white)
# thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
####
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
        print('x = {} y = {} w = {} h = {} w/h = {} p = {}'.format(x,y,w,h,w / h,w * h) )
        for (x,y,w,h) in seporate(x,y,w,h):
            cord.append((x,y,w,h))

cordResult = [];
for (x,y,w,h) in cord:
    for (x,y,w,h) in seporate(x,y,w,h):
        cordResult.append((x,y,w,h))

cordResult = sorted(cordResult, key=lambda x: x[0])

print('------')
for (x,y,w,h) in cordResult:
    print('x = {} y = {} w = {} h = {} w/h = {} p = {}'.format(x,y,w,h,w / h,w * h) )
    cv.rectangle(img, (x , y),(x + w, y + h), (0,0,255),2)
    roi = thresh[y:y + h, x:x + w]
    roismall = cv.resize(roi,(10,10))
    letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]
    # cv.imshow('norm',img)
    # cv.imshow('letter_image',letter_image)
    # cv.waitKey()
cv.imshow('norm',img)



cv.waitKey()
cv.destroyAllWindows()