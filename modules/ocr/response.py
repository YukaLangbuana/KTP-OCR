from flask import request
import numpy
import cv2
from modules.ocr.extractor import ImageExtractor

def get_response():
    image = request.files['ktp_image'].read()
    npimg = numpy.fromstring(image, numpy.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
    result = ImageExtractor(img)
    return result.get_information()