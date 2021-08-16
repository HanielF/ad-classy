#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from PIL import Image

# path = "/hetu_group/wuxiangyu/cx/Games/data/ad_classy/训练集/84"
# root = "/hetu_group/wuxiangyu/cx/Games/data/ad_classy/训练集/"

# img =os.listdir(path)[4]
# imgpath=os.path.join(path, img)
# print(imgpath)
# img = Image.open(imgpath)
# plt.imshow(img)

# for imgdir in os.listdir(root):
#     print(f"dir:{imgdir}, num:{len(os.listdir(os.path.join(root, imgdir)))}")
# print(len(os.listdir(root)))
# for i in range(137):
#     if not os.path.exists(root+str(i)):
#         print("???")

# path = "/hetu_group/wuxiangyu/cx/data/shenping/cover/1"
# root = "/hetu_group/wuxiangyu/cx/data/shenping/cover/"

# img =os.listdir(path)[8]
# imgpath=os.path.join(path, img)
# print(imgpath)
# img = Image.open(imgpath)
# plt.imshow(img)


imgpath="/hetu_group/wuxiangyu/cx/data/shenping/cover/0/49221352070.jpg"
print(imgpath)
img = Image.open(imgpath)
plt.imshow(img)
