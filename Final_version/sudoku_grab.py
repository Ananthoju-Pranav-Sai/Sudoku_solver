import cv2
import numpy as np
import imutils

def get_perspective(img,location,height = 900,width=900):
    """Takes an image and a location and returns the selected region with perspective transformation."""
    i1 = np.float32([location[0],location[3],location[1],location[2]])
    i2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(i1,i2)
    res = cv2.warpPerspective(img,matrix,(width,height))
    return res

def preprocess_img(img):
    """Takes an image and returns the image after preprocessing it."""
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    bifilter = cv2.bilateralFilter(gray,10,20,25)
    edged = cv2.Canny(bifilter,20,100)
    return edged

def extract_sudoku(img):
    """Takes the image, preprocesses it and finds sudoku board inside of it."""
    pre_img = preprocess_img(img)
    points = cv2.findContours(pre_img.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(points)

    #sorting contours in descending order based on area
    contours = sorted(contours,key=cv2.contourArea,reverse=True)[:15]
    board_loc = None

    for contour in contours:
        approx = cv2.approxPolyDP(contour,15,True)
        if(len(approx)==4):
            board_loc = approx
            break
    res = get_perspective(img,board_loc)
    return res,board_loc