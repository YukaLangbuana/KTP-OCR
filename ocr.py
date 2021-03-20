#LEGACY VERSION

import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import sys
from ktpocr import KTPOCR

## (1) Read
def read(ktp_path):
    img = cv2.imread(ktp_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## (2) Threshold
    th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

    ## (3) Detect
    result = pytesseract.image_to_string((threshed), lang="ind")

    final = []

    ## (5) Normalize
    for word in result.split("\n"):
        if "”—" in word:
            word = word.replace("”—", ":")
      
        #normalize NIK
        if "NIK" in word:
            nik_char = word.split()
        #if "D" in word:
        #    word = word.replace("D", "0")
        if "?" in word:
            word = word.replace("?", "7") 
      
        final.append(word)
    return final

if __name__ == "__main__":  
    try:  
        ktppath = sys.argv[1]    
    except:
        ktppath = None
        print('Define your image path. Example: python ocr.py /path/of/image.jpg')
    if ktppath:
        ocr = KTPOCR(ktppath)
        word = ocr.to_json()
        print(word)