#LEGACY VERSION

import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

## (1) Read
img = cv2.imread("ktpocr/dataset/ktp_test.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## (2) Threshold
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

## (3) Detect
result = pytesseract.image_to_string((threshed), lang="ind")

## (5) Normalize
for word in result.split("\n"):
  if "”—" in word:
    word = word.replace("”—", ":")
  
  #normalize NIK
  if "NIK" in word:
    nik_char = word.split()
    if "D" in word:
      word = word.replace("D", "0")
    if "?" in word:
      word = word.replace("?", "7") 
  
  print(word)