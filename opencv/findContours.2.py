import sys
import numpy as np
import cv2 as cv

# hsv_min = np.array((2, 28, 65), np.uint8)
# hsv_max = np.array((26, 238, 255), np.uint8)

hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((0, 0, 0), np.uint8)


#######gif read###
file = r"c:\myProject\nalog\captcha\751616\legvuehp.1xt.png";

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
contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL  , cv.CHAIN_APPROX_TC89_KCOS)
contours = []
for cnt in contours0:
    if cv.contourArea(cnt) > 50:
        (x,y,w,h) = cv.boundingRect(cnt)
        if w / h > 1.25:
            # This contour is too wide to be a single letter!
            # Split it in half into two letter regions!
            half_width = int(w / 2)
            contours.append((x, y, half_width, h))
            contours.append((x + half_width, y, half_width, h))
        else:
            # This is a normal letter by itself
            contours.append((x, y, w, h))
        ###############
        # if w / h > 1.25:
        #     half_width = int(w / 2)
        #     contours.append({'w_new':half_width,'x_new':x})
        #     contours.append({'w_new':half_width,'x_new':x + half_width})
        # else:
        #     contours.append({'w_new':w,'x_new':x})
        # for c in contours:
        #     cv.rectangle(img, (c['x_new'] , y),(c['x_new'] + c['w_new'], y + h), (0,0,255),2)
        #     roi = thresh[y:y + h, c['x_new']:c['x_new'] + c['w_new']]
        #     roismall = cv.resize(roi,(10,10))
        #     letter_image = gray[y - 2:y + h + 2, c['x_new'] - 2:c['x_new'] + c['w_new'] + 2]
        #     cv.imshow('norm',img)
        #     cv.imshow('letter_image',letter_image)

        #     cv.waitKey()
        # contours = []
        ###############

print(len(contours))
if len(contours) != 6:
    exit

contours = sorted(contours, key=lambda x: x[0])

for x,y,w,h in contours:
    letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]
    cv.imshow('letter_image',letter_image)
    cv.waitKey()

#cv.imshow('norm',img)

index = 0
layer = 0
# x,y,w,h = cv.boundingRect(contours0)
# print(x)
#print(hierarchy)



# def update():
#     vis = img.copy()
#     cv.drawContours( vis, contours0, index, (255,0,0), 2, cv.LINE_AA, hierarchy, layer )
#     cv.drawContours( vis, contours0, index, (255,0,0), 2, cv.LINE_AA, hierarchy, layer )
#     cv.imshow('contours', vis)
#     print(len(contours0))
#     for i in contours0:
#         print('i',type(i))

# def update_index(v):
#     global index
#     index = v-1
#     update()

# def update_layer(v):
#     global layer
#     layer = v
#     update()

# update_index(0)
# update_layer(1)
# cv.createTrackbar( "contour", "contours", 0, 7, update_index )
# cv.createTrackbar( "layers", "contours", 0, 7, update_layer )

cv.waitKey()
cv.destroyAllWindows()