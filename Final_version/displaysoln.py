import numpy as np
import cv2

def displaynum(img,solution,color=(0,0,255)):
    """Creates a mask and then writes only numbers that are part of the solution"""
    W = int(img.shape[1]/9)
    H = int(img.shape[0]/9)
    for i in range(9):
        for j in range(9):
            if(solution[i][j]!=0):
                cv2.putText(img,str(solution[i][j]),(j*W+int(W/2)-int((W/4)), int((i+0.7)*H)), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2, cv2.LINE_AA)
    return img

def get_INV_perspective(img,mask,location,height=900,width=900):
    """Applies the solution mask to original image thereby displaying the solution to the sudoku"""
    i2 = np.float32([location[0],location[3],location[1],location[2]])
    i1 = np.float32([[0,0],[width,0],[0,height],[width,height]])

    matrix = cv2.getPerspectiveTransform(i1,i2)
    result = cv2.warpPerspective(mask,matrix,(img.shape[1],img.shape[0]))
    return result