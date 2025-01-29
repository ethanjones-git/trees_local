
"""
Ethan Jones
01/13/2024

Impliment the following bounding box example
https://pytorch.org/vision/main/auto_examples/others/plot_repurposing_annotations.html#sphx-glr-auto-examples-others-plot-repurposing-annotations-py

"""

import os
import numpy as np
import torch
import matplotlib.pyplot as plt
import torchvision.transforms.functional as F
from torchvision.io import decode_image


def image_loader():
    path = os.getcwd()  
    img_path =path+'/data/images/park_32_740834_117_15834400000017.png'

    out = decode_image(img_path)
    mask = torch.zeros_like(out[0])  # Create a mask of zeros

    return mask
    #mask_path = os.path.join(ASSETS_DIRECTORY, "FudanPed00054_mask.png")
    #img = decode_image(img_path)
    #mask = decode_image(mask_path)