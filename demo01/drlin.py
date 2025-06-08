import cv2
import random
from PIL import Image, ImageFilter
from PIL.Image import Image
import numpy as np
import math


def apply_vignette(image, center=(150, 150), radius=200, strength=0.5):
    h, w = image.shape[:2]
    yy, xx = np.ogrid[:h, :w]
    distance = np.sqrt((xx - center[0]) ** 2 + (yy - center[1]) ** 2)
    mask = np.clip(1 - strength * (distance / radius), 0, 1)
    mask = mask[..., np.newaxis]
    vignette_image = image * mask
    vignette_image = np.clip(vignette_image, 0, 255).astype(np.uint8)

    return vignette_image

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

    def aoyi(self):
        img_1 = cv2.imread(self)
        img_0 = cv2.imread("static/image/snow.png")
        # img_1=cv2.imread("D://image//bear.jpg")#,cv2.IMREAD_GRAYSCALE
        rows = img_1.shape[0]
        cols = img_1.shape[1]
        x = 1280 / max(cols, rows)
        w = round(x * cols)
        h = round(x * rows)
        m = (w, h)
        img_1 = cv2.resize(img_1, m, interpolation=cv2.INTER_AREA)
        img_2 = cv2.resize(img_0, m, interpolation=cv2.INTER_AREA)

        rows = img_1.shape[0]
        cols = img_1.shape[1]

        img_pro = np.zeros((rows, cols), np.uint8)

        img_add = cv2.addWeighted(img_1, 0.8, img_2, 0.2, 1)
        cv2.imwrite('D://image//transing//1.jpg', img_add)

        height, width, channel = img_2.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = 30
        folder_selected = "static/mp4"
        video = cv2.VideoWriter(folder_selected + '/output.mp4', fourcc, fps, (width, height))
        x = round(width / 85)
        x0 = round(width / 150)
        y = round(height / 150)
        o = round(width * 0.2)
        p = round(width * 0.5)
        q = round(width * 0.8)
        for i in range(30):
            img_new = img_add.copy()
            cv2.line(img_new, (p + x * i, 1), (p + x * i, rows), (0, 0, 0), 1)
            cv2.line(img_new, (o + x * i, 1), (o + x * i, rows), (0, 0, 0), 1)
            cv2.line(img_new, (q - 2 * x * i, 1), (q - 2 * x * i, rows), (0, 0, 0), 2)
            x1 = x0 * math.sin(i)
            y1 = y * math.sin(i)
            x2 = x0 * 1.5 * math.sin(0.5 * i)
            y2 = y * 1.5 * math.sin(0.5 * i)
            M = np.float32([[1, 0, x1], [0, 1, y1]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            M = np.float32([[1, 0, -x2], [0, 1, -y2]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            img_new = apply_vignette(img_new, center=(img_new.shape[1] // 2, img_new.shape[0] // 2),
                                     radius=max(cols, rows) // 1.5, strength=1)
            video.write(img_new)
        o = round(width * 0.9)
        p = round(width * 0.1)
        q = round(width * 0.2)
        for i in range(30):
            img_new = img_add.copy()
            cv2.line(img_new, (p + x * i, 1), (p + x * i, rows), (0, 0, 0), 1)
            cv2.line(img_new, (o - 2 * x * i, 1), (o - 2 * x * i, rows), (0, 0, 0), 2)
            cv2.line(img_new, (q + x * i, 1), (q + x * i, rows), (0, 0, 0), 1)
            x1 = x0 * math.sin(i)
            y1 = y * math.sin(i)
            x2 = x0 * 3 * math.sin(0.5 * i)
            y2 = y * 3 * math.sin(0.5 * i)
            M = np.float32([[1, 0, x1], [0, 1, y1]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            M = np.float32([[1, 0, -x2], [0, 1, y2]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            img_new = apply_vignette(img_new, center=(img_new.shape[1] // 2, img_new.shape[0] // 2),
                                     radius=max(cols, rows) // 1.5, strength=1)
            video.write(img_new)
        o = round(width * 0.85)
        p = round(width * 0.4)
        q = round(width * 0.7)
        for i in range(30):
            img_new = img_add.copy()
            cv2.line(img_new, (p + x * i, 1), (p + x * i, rows), (0, 0, 0), 1)
            cv2.line(img_new, (o - 2 * x * i, 1), (o - 2 * x * i, rows), (0, 0, 0), 2)
            cv2.line(img_new, (q + x * i, 1), (q + x * i, rows), (0, 0, 0), 1)
            x1 = x0 * 3 * math.sin(0.8 * i)
            y1 = y * 3 * math.sin(0.8 * i)
            x2 = x0 * math.sin(0.5 * i)
            y2 = y * math.sin(0.5 * i)
            M = np.float32([[1, 0, x1], [0, 1, y1]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            M = np.float32([[1, 0, x2], [0, 1, -y2]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            img_new = apply_vignette(img_new, center=(img_new.shape[1] // 2, img_new.shape[0] // 2),
                                     radius=max(cols, rows) // 1.5, strength=1)
            video.write(img_new)
        o = round(width * 0.2)
        p = round(width * 0.5)
        q = round(width * 0.8)
        for i in range(30):
            img_new = img_add.copy()
            cv2.line(img_new, (p + x * i, 1), (p + x * i, rows), (0, 0, 0), 1)
            cv2.line(img_new, (o + x * i, 1), (o + x * i, rows), (0, 0, 0), 1)
            cv2.line(img_new, (q - 2 * x * i, 1), (q - 2 * x * i, rows), (0, 0, 0), 2)
            x1 = x0 * math.sin(i)
            y1 = y * math.sin(i)
            x2 = x0 * 1.5 * math.sin(0.5 * i)
            y2 = y * 1.5 * math.sin(0.5 * i)
            M = np.float32([[1, 0, x1], [0, 1, y1]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            M = np.float32([[1, 0, -x2], [0, 1, -y2]])
            img_new = cv2.warpAffine(img_new, M, (cols, rows))
            img_new = apply_vignette(img_new, center=(img_new.shape[1] // 2, img_new.shape[0] // 2),
                                     radius=max(cols, rows) // 1.5, strength=1)
            video.write(img_new)
        video.release()
