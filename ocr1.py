import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_CUBIC)

kernal = np.ones((5,5),np.uint8)
#img = cv2.imread('C:/Users/sachin/Downloads/ocr2.jpg')
capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frame = rescale(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 15, 255, cv2.THRESH_OTSU, cv2.THRESH_BINARY)
    #gaussian = cv2.GaussianBlur(thresh,(5,5),0)
    median = cv2.medianBlur(thresh,ksize = 5)


    print(pytesseract.image_to_string(median))

    boxes = pytesseract.image_to_boxes(median)
    height,width = frame.shape[:2]

    for box in boxes.splitlines():

        box = box.split(' ')
        x1,y1,x2,y2 = int(box[1]),int(box[2]),int(box[3]),int(box[4])
        cv2.rectangle(frame,(x1,height-y1),(x2,height-y2),(0,255,0),2)



    cv2.imshow('ocr',frame)
    #cv2.imshow('gray',gray)
    cv2.imshow('thresh',thresh)
    #cv2.imshow('gaussian',gaussian)

    if cv2.waitKey(1) & 0xff == 13:
        break

capture.release()
cv2.destroyAllWindows()
