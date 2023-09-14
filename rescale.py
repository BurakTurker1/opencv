import cv2 as cv



def rescaleFrame(frame,scale=0.75):
    # Images, Videos and live
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


def changeRes(width,height):
    # live and video
    capture.set(3, width)
    capture.set(4, height)


hurly = cv.imread('photo/lost_hurly.jpg')
cv.imshow('THE LOST', hurly)
resized_imgage = rescaleFrame(hurly)
cv.imshow('image resized', hurly)
cv.waitKey(0)

# reading videos

capture = cv.VideoCapture('video/lost_video1.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('video resized', frame_resized)
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()

cv.destroyWindow()