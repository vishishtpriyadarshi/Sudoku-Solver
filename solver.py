#from .functions.utils import *
#from .functions.cnn import *
import functions as f
import numpy as np
import cv2
#import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Dropout, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras import backend as K
from tensorflow.keras.models import model_from_json

def generate_matrix(cnn_verdict):
    model = f.get_trained_model()
    arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(9):
        for j in range(9):
            if cnn_verdict[9*i + j][1]:
                img = cnn_verdict[9*i + j][0]/255
                a = model.predict(img.reshape(1,28,28,1))
                if (np.argmax(a)==0):
                    print(a)
                    a[0][0]=0
                arr[i][j] = np.argmax(a)

    return arr



def main():

    path = 'fff.jpg'
    original = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    processed = f.pre_process_image(original)
    corners = f.find_corners_of_largest_polygon(processed)
    cropped = f.crop_and_warp(original, corners)
    squares = f.infer_grid(cropped)
    digits = f.get_digits(cropped, squares, 28)

    # print(digits[0].shape)
    # show_digits(digits)

    cnn_verdict = f.get_possible(digits)
    arr = generate_matrix(cnn_verdict)
    for i in range(9):
         print(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4], arr[i][5], arr[i][6], arr[i][7], arr[i][8])

	
	#	DEBUGGER FUNCTIONS
    # print(cnn_verdict)
    # cv2.imwrite('sample_block.jpg', cnn_verdict[3][0])
    # show_verdict(cnn_verdict)



if __name__ == '__main__':
    main()

