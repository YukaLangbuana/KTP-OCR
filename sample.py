from ktpocr import KTPOCR

data = KTPOCR("ktpocr/dataset/ktp_test.png")
print(data.extract())