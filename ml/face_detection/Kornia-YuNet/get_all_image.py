
import cv2
import os
import kornia as K
import numpy as np
import matplotlib.pyplot as plt
import torch
from kornia.contrib import FaceDetector, FaceDetectorResult

# select the device and type
device = torch.device("cuda")  # use 'cuda:0'
dtype = torch.float32

url = "Season_05/s05e02_Reorientation.avi_f/output_00010.png"
#url = "Season_05/s05e02_Reorientation.avi_f/output_00046.png"
url = "Season_05/s05e02_Reorientation.avi_f/output_00058.png"

def get_image_file_to(image_file_from):
    path, file_name_ex = os.path.split(image_file_from)
    file_name, ext = file_name_ex.split('.')
    path_last = path.split('/')[-1]
    path_last_new = path_last.replace('_f','_r')
    path_left = '/'.join(path.split('/')[0:-1])
    path_result = os.path.join(path_left,path_last_new)
    if not os.path.exists(path_result):
        os.mkdir(path_result)
    image_file_to = os.path.join(path_result,file_name)
    #print(f'{image_file_to=}')
    return image_file_to

def image_save(image_file_from:str,image_file_to:str):
    print(f'{image_file_from=}')
    img = K.io.load_image(image_file_from, K.io.ImageLoadType.RGB8, device=device)[None, ...].to(dtype=dtype)  # BxCxHxW
    img_vis: np.ndarray = K.tensor_to_image(img.byte())  # to later visualize

    # create the detector and find the faces !
    face_detection = FaceDetector().to(device, dtype)

    with torch.no_grad():
        dets = face_detection(img)

    dets = dets[0]
    # to decode later the detections
    dets = [FaceDetectorResult(o) for o in dets]


    # blurring paramters
    k: int = 21  # kernel_size
    s: float = 35.0  # sigma


    print(f'{len(dets)=}')
    index = -1
    for b in dets:    
        # draw face bounding box around each detected face
        top_left = b.top_left.int().tolist()
        bottom_right = b.bottom_right.int().tolist()
        scores = [b.score.tolist()]
        for score, tp, br in zip(scores, top_left, bottom_right):
            index += 1
            x1, y1 = top_left
            x2, y2 = bottom_right
            
            if score < 0.7:
                print(f'WARN skeep {index=}, {score=}, {image_file_from=}')
                continue  # skip detection with low score        
            
            result = img_vis[y1:y2,x1:x2]            
            print(f'{(y1,y2,x1,x2)=}, {result.size=}')
            if result.size == 0:
                print(f'WARN size 0 {index=}, {score=}, {image_file_from=}')
                continue
            path = f'{image_file_to}_{index}_{result.size}.jpg'
            print(f'{path=}')
            f = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)        
            cv2.imwrite(path, f)
            

bases = [
    "Season_01",
    "Season_02",
    "Season_03",
    "Season_04",
    "Season_06"
    ]
for base in bases:
    for root, ds, files in os.walk(base):    
        if '_f' == root[-2:]:
            for file in files:
                image_file_from = os.path.join(root,file)
                image_file_to = get_image_file_to(image_file_from)
                image_save(image_file_from,image_file_to)