import cv2 as cv
import pytesseract as ts
# img = cv.imread('sample.jpg')
# cv.imshow('Sample',img)
def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_CUBIC)


capture = cv.VideoCapture(0)      #webCam configuration
while True:
    isTrue, frame = capture.read()
    # frame_resized = Rescale(frame, scale=0.5)
    # cv.imshow('video_rescale', frame_resized)
    frame_resized1 = rescale(frame, scale=1)
    gray = cv.cvtColor(frame_resized1, cv.COLOR_BGR2GRAY)
    cv.imshow('video_rescale1', gray)
    text = ts.image_to_string(frame_resized1)     #printing realtime text
    print(text)

    if cv.waitKey(20) & 0xff == ord('d'):
        break


cv.waitKey(0)
cv.destroyAllWindows()
