
#https://www.kaggle.com/code/hmendonca/proper-clustering-with-facenet-embeddings-eda#Prepare-and-Export-Clusters
import os
import pandas as pd
import cv2
# See github.com/timesler/facenet-pytorch:
from facenet_pytorch import MTCNN, InceptionResnetV1, extract_face
from matplotlib import pyplot as plt
import torch
from PIL import Image
from torchvision.transforms import ToTensor

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Running on device: {device}')

tf_img = lambda i: ToTensor()(i).unsqueeze(0)
embeddings = lambda input: resnet(input)

resnet = InceptionResnetV1(pretrained='vggface2', device=device).eval()


df = pd.DataFrame(columns=['image_path','embedding'])

#1445
count = 0
count_all = 0
percent = 0
with torch.no_grad():    
    for root,dirs,files in os.walk('/home/aleksei/Загрузки/Silicon.Valley.2014-2019.web-dlrip_[teko]'):
        for file in files:
            count_all += 1
            if '.jpg' in file:
                count += 1
                if count % 1445 == 0:
                    percent += 1
                    print(f'{count=} {percent=} %')
                image_path = os.path.join(root,file)
                img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
                resized = cv2.resize(img, (150,150), interpolation = cv2.INTER_AREA)
                t = tf_img(resized).to(device)
                e = embeddings(t).squeeze().cpu().tolist()        
                new_row = {'image_path':image_path, 'embedding':e}
                df = df.append(new_row, ignore_index=True)
print(f'{df.shape=}')
df.to_feather('data.feather')
print('saved')
