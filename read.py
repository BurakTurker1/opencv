import cv2 as cv


# reading image

hurley = cv.imread('photo/lost_hurley.jpg')
cv.imshow('THE LOST', hurley)
cv.waitKey(0)


# reading videos
capture = cv.VideoCapture('video/lost_video1.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyWindow()