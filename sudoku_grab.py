
import cv2
import numpy as np
from scipy.spatial import distance as dist

def preprocess_image(img):
    proc = cv2.GaussianBlur(img.copy(),(9,9),0)
    proc = cv2.adaptiveThreshold(proc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    proc = cv2.bitwise_not(proc,proc)
    kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]], np.uint8)
    thresh = cv2.dilate(proc, kernel)
    return thresh

def extract_sudoku(thresh):
    contour,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour_grille = None
    max_area = 0
    for c in contour:
        area = cv2.contourArea(c)
        if(area>30000):
            peri = cv2.arcLength(c,True)
            polygon = cv2.approxPolyDP(c,0.01*peri,True)
            if(area>max_area and len(polygon)==4):
                contour_grille = polygon
                max_area = area
    print(max_area)


    if contour_grille is not None:
        cv2.drawContours(img, [contour_grille], 0, (0, 0, 255), 2)

        print('Contour detected')

        corners = contour_grille.ravel()
        corners = np.reshape(corners,(4,2))
        corners = sorted(corners,key=lambda x:x[0])


        if(corners[0][1]>corners[1][1]):
            tl = corners[1]
            bl = corners[0]
        else:
            tl=corners[0]
            bl=corners[1]
        
        if(corners[2][1]>corners[3][1]):
            tr = corners[3]
            br = corners[2]
        else:
            tr=corners[2]
            br=corners[3]
        
        corners = [tl,tr,br,bl]

        width_A = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        width_B = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

        height_A = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        height_B = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))


        max_width = max(int(width_A), int(width_B))
        max_height = max(int(height_A), int(height_B))

        dst = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]], dtype = "float32")

        perspective_transformed_matrix = cv2.getPerspectiveTransform(np.array(corners,dtype='float32'), dst)
        warp = cv2.warpPerspective(img, perspective_transformed_matrix, (max_width, max_height))
    return warp


img = cv2.imread('sudokus/sudoku1.jpg',0)
thresh = preprocess_image(img)
warp = extract_sudoku(thresh)
cv2.imwrite('warp_image.jpg',warp)