import cv2 as cv
import numpy as np

claire = cv.imread('photo/lost_claire.jpg')
resized_claire = cv.resize(claire, (800, 800))
cv.imshow('claire', resized_claire)

# Translation


def translate(img, x, y):

    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)

# -x -->Left
# -y -->Up
#  x -->Right
#  y -->Down


translated = translate(resized_claire, 100, 100)
cv.imshow('translated', translated)

# Rotation


def rotate(img, angle, rotpoint=None):

    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotmat, dimensions)


rotated = rotate(resized_claire, 45)
cv.imshow('rotated', rotated)

# Flipping
flip = cv.flip(resized_claire, -1)
cv.imshow('flip', flip)
cv.waitKey(0)
