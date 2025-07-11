import pandas as pd
import cv2
# See github.com/timesler/facenet-pytorch:
from facenet_pytorch import MTCNN, InceptionResnetV1, extract_face
from matplotlib import pyplot as plt
import torch
from PIL import Image
from torchvision.transforms import ToTensor

df = pd.read_feather('data.feather')

# print(df.info())
# print(df.describe())
# print(df.head(2))


import sklearn.cluster as cluster

print(f'{df.shape=} start...')

#print([list(l) for l in df['embedding'].values])
import hdbscan
#clusters = cluster.OPTICS(n_jobs=-1, eps=1.0, min_samples=1, cluster_method = 'dbscan').fit_predict([list(l) for l in df['embedding'].values])
clusters = hdbscan.HDBSCAN(alpha=1.0, min_cluster_size=13, min_samples=13).fit_predict([list(l) for l in df['embedding'].values])
df['cluster'] = clusters

print(f'{df.shape=}')
df.to_feather('data_1.feather')
print('saved')
