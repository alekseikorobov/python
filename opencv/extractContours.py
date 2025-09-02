import sys
import os
import numpy as np
import cv2 as cv
from glob import glob
import shutil

count_empty_file = 0
not_correct_contours = 0
correct = 0
out_path = r"c:\myProject\nalog\captcha_out"


def seporate(x, y, w, h):
    cord = []
    if w / h >= 1.25:
        half_width = int(w / 2)
        cord.append((x, y, half_width, h))
        cord.append((x+half_width, y, half_width, h))
    else:
        cord.append((x, y, w, h))
    return cord


def extract_number_from_captcha(file):
    global out_path, count_empty_file, not_correct_contours, correct
    #######gif read###
    #file = r"c:\myProject\nalog\captcha\443150\0apt1h1f.tcz.png";
    number = file.split('\\')[-2]
    file_name = file.split('\\')[-1].replace('.png', '')
    if(os.stat(file).st_size == 0):
        print('file_name {} is empty'.format(file_name))
        os.remove(file)
        count_empty_file += 1
        return 1
    gif = cv.VideoCapture(file)
    ret, img = gif.read()
    #################

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    element = cv.getStructuringElement(cv.MORPH_CROSS, (2, 2))
    # Выполняем операции эрозия и дилатация
    erode_dilate = cv.dilate(cv.erode(gray, element), element)

    blur = cv.GaussianBlur(erode_dilate, (5, 5), 0)
    thresh = cv.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    contours0, hierarchy = cv.findContours(
        thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)
    contours1 = []
    for cnt in contours0:
        if cv.contourArea(cnt) > 50:
            (x, y, w, h) = cv.boundingRect(cnt)
            for (x, y, w, h) in seporate(x, y, w, h):
                contours1.append((x, y, w, h))
    contours = []
    for (x, y, w, h) in contours1:
        for (x, y, w, h) in seporate(x, y, w, h):
            contours.append((x, y, w, h))

    if len(contours) != 6:
        print('Not correct contours, {}'.format(len(contours)))
        not_correct_contours += 1
        return 1

    contours = sorted(contours, key=lambda x: x[0])
    if not list(filter(lambda x: x[3]*x[2] < 500, contours)):
        for i, (x, y, w, h) in enumerate(contours):
            letter_image = gray[y - 2:y + h + 2, x - 2:x + w + 2]
            p = os.path.join(out_path, "{}_{}_{}.png".format(
                file_name, i, number[i]))
            cv.imwrite(p, letter_image)
            correct += 1
            print('Save image by path {}'.format(p))
        return 0
    else:
        print('exists block < 500')
        return 1


# extract_number_from_captcha(r"c:\myProject\nalog\captcha\443150\0apt1h1f.tcz.png")

def notExistsFile(filename):
    global out_path
    file = os.path.join(out_path, filename.replace('.png', '*'))
    return not glob(file)


def move_result(root, filename):
    new_folder = root.replace("captcha", "captcha_result")
    old_name = os.path.join(root, filename)
    if(not os.path.isdir(new_folder)):
        os.mkdir(new_folder)
    full_name = os.path.join(new_folder, filename)
    shutil.move(old_name, full_name)


for root, dirnames, filenames in os.walk(r"c:\\myProject\\nalog\\captcha\\"):
    for filename in filenames:
        #print(os.path.join(root, filename))
        file = os.path.join(root, filename)
        try:
            if notExistsFile(filename):
                res = extract_number_from_captcha(file)
                if(res == 0):
                    move_result(root, filename)
            else:
                move_result(root, filename)
        except BaseException as e:
            print(e)
            print(file)

print('summery count_empty_file = {}, not_correct_contours = {}, correct = {}'.format(
    count_empty_file,
    not_correct_contours,
    correct
))
