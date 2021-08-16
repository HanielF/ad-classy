#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tqdm import tqdm
import shutil
import os

root = "/hetu_group/wuxiangyu/cx/Games/data/ad_classy/训练集"
for dir in tqdm(os.listdir(root)):
    dirroot = os.path.join(root, dir)
    files = os.listdir(dirroot)
    filenum = len(files)
    
    for i,file in enumerate(files):
        srcpath = os.path.join(dirroot, file)
        if i < 0.9*filenum:
            topath = srcpath.replace("训练集", "train")
            todir = dirroot.replace("训练集", "train")
        else:
            topath = srcpath.replace("训练集", "test")
            todir = dirroot.replace("训练集", "test")
        if not os.path.exists(todir):
            os.mkdir(todir)
            
        shutil.copyfile(srcpath, topath)
