import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

class KTPInformationForm(object):
    def __init__(self):
        self.nik = ""
        self.nama = ""
        self.tempat_lahir = ""
        self.tanggal_lahir = ""
        self.jenis_kelamin = ""
        self.alamat = ""
        self.rt = ""
        self.rw = ""
        self.kelurahan_atau_desa = ""
        self.kecamatan = ""
        self.agama = ""
        self.status_perkawinan = ""
        self.pekerjaan = ""
        self.kewarganegaraan = ""
        berlaku_hingga = "SEMUR HIDUP"

class ImageExtractor(object):
    def __init__(self, image):
        self.image = image
        self.th, self.threshed = cv2.threshold(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_TRUNC)
        self.result = KTPInformationForm()

    def process(self, image):
        result = pytesseract.image_to_string((self.threshed), lang="ind")
        return result

    def word_to_number_converter(self, word):
        word_dict = {
            "L" : 1,
            'l' : 1,
            'O' : 0,
            'o' : 0,
        }
        res = ""
        for letter in word:
            if letter in word_dict:
                res += word_dict[letter]
            else:
                res += letter
        return res
    
    def extract(self, extracted_result):
        for word in extracted_result.split("\n"):
            if "NIK" in word:
                word = word.split(':')
                self.result.nik = self.word_to_number_converter(word[-1].replace(" ", ""))

    def get_information(self):
        processed_image = self.process(self.image)
        self.extract(processed_image)
        return self.result.__dict__


