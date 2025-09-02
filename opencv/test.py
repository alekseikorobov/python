import sys
import numpy as np
import cv2 as cv

# hsv_min = np.array((2, 28, 65), np.uint8)
# hsv_max = np.array((26, 238, 255), np.uint8)

hsv_min = np.array((0, 0, 0), np.uint8)
hsv_max = np.array((0, 0, 0), np.uint8)


file = "c:/Temp/legvuehp.1xt.jpg";

gif = cv.VideoCapture(file)
ret, img = gif.read()

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('frame',gray)
# cv.waitKey()
#img = cv.imread(file)

#hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
# thresh = cv.inRange( hsv, hsv_min, hsv_max )

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## Threshold 
ret, threshed = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
# thresh = cv.threshold(image, 0, 255,
#                            cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
####
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# # Add some extra padding around the image
# gray = cv.copyMakeBorder(gray, 8, 8, 8, 8, cv.BORDER_REPLICATE)
# # threshold the image (convert it to pure black and white)
# thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
####
cnts, hiers = cv.findContours( threshed.copy(), cv.RETR_EXTERNAL  , cv.CHAIN_APPROX_SIMPLE)

canvas = np.zeros_like(img)
n = len(cnts)
hiers = hiers[0]

for i in range(n):
    if hiers[i][3] != -1:
        ## If is inside, the continue 
        continue
    ## draw 
    cv.drawContours(canvas, cnts, i,  (0,255,0), -1, cv.LINE_AA)

    ## Find all inner contours and draw 
    ch = hiers[i][2]
    while ch!=-1:
        print(" {:02} {}".format(ch, hiers[ch]))
        cv.drawContours(canvas, cnts, ch, (255,0,255), -1, cv.LINE_AA)
        ch = hiers[ch][0]

# cv.imwrite("001_res.png", canvas)
cv.imshow('frame',canvas)
cv.waitKey()