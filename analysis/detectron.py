import sys, os, distutils.core
import torch, detectron2
from detectron2.utils.logger import setup_logger
import os, json, cv2, random

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

setup_logger()

print(os.getcwd())

im = cv2.imread("/image_detectron_test/dectron_image_test.png")
#cv2_imshow(im)