import cv2
import random
from PIL import Image, ImageFilter
class drlin:
    def decode(self):
        img0 = cv2.imread(self)
        img1 = img0.copy()
        cols = img0.shape[1]
        rows = img0.shape[0]
        arrayx = [i for i in range(cols)]
        arrayy = [i for i in range(rows)]
        x0 = arrayx[:]
        y0 = arrayy[:]
        random.shuffle(x0)
        random.shuffle(y0)
        for y in range(rows):
            for x in range(cols):
                img1[y0[y], x0[x]] = img0[y, x]
        img1 = Image.fromarray(img1)
        return img1

    def defilter(self):
        img0 = cv2.imread(self)
        img1 = img0.copy()
        cols = img0.shape[1]
        rows = img0.shape[0]
        arrayx = [i for i in range(cols)]
        arrayy = [i for i in range(rows)]
        x0 = arrayx[:]
        y0 = arrayy[:]
        random.shuffle(x0)
        random.shuffle(y0)
        for y in range(rows):
            for x in range(cols):
                img1[y, x] = img0[y0[y], x0[x]]
        img1 = Image.fromarray(img1)
        return img1