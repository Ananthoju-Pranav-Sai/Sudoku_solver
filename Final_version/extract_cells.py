from sudoku_grab import *
from tensorflow.keras.models import load_model

classes = np.arange(0,10)
# we will load a pretrained model for detecting digits
model = load_model("model-OCR.h5")

def split_cells(board_img):
    """Takes the image of sudoku board as the input and splits into 81 cells"""
    rows = np.array_split(board_img,9,axis=0)
    cells = []
    for row in rows:
        cols = np.array_split(row,9,axis=1)
        for cell in cols:
            cell = cv2.resize(cell,(48,48))/255
            cells.append(cell)
    return cells

def predict_board(cells):
    """Predicts the numbers in the cells using the pretrained model and returns the board"""
    cells = np.array(cells).reshape(-1,48,48,1)
    pred = model.predict(cells)
    board = []
    for i in pred:
        pred_num = classes[np.argmax(i)]
        board.append(pred_num)
    board = np.array(board).astype('uint8').reshape(9,9)
    return board