# import cv2
import sys
import json

#img = cv2.imread('/home/shivansh/ed/sudoku_interface/public/images/' + sys.argv[1])

arr = [
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8],
    [0,1,2,3,4,5,6,7,8]
]
for i in range(9):
    for j in range(9):
        print(arr[i][j])


# print(1,2,3)
# print(4,5,6)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
