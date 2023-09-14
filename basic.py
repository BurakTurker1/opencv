import cv2 as cv

island = cv.imread('photo/lost_island.jpg')
cv.imshow('THE LOST', island)

# Converting to grayscale
gray = cv.cvtColor(island, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(island, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(island, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(island, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Cropping
cropped = island[80:300, 300:500]
cv.imshow('cropped',cropped)
cv.waitKey(0)