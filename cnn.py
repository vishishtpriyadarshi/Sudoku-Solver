from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Dropout, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras import backend as K
from tensorflow.keras.models import model_from_json
import cv2
import numpy as np
from PIL import Image

# img = cv2.imread('zzz.jpg', 0)
# #im = np.array(Image.open('zzz.jpg'))
# img = img/255
#
#
# json_file = open('mnist_model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("mnist_model.h5")
# print("Loaded model from disk")
#
# # batch_size = 64
# # num_classes = 10
# # epochs = 15
# #
# # image_rows = 28
# # image_cols = 28
#
# # (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
# # if K.image_data_format() == 'channels first':
# #     x_train = x_train.reshape(x_train.shape[0], 1, image_rows, image_cols)
# #     x_test = x_test.reshape(x_test.shape[0], 1, image_rows, image_cols)
# #     input_shape = (image_rows, image_cols, 1)
# #
# # else:
# #     x_train = x_train.reshape(x_train.shape[0], image_rows, image_cols, 1)
# #     x_test = x_test.reshape(x_test.shape[0], image_rows, image_cols, 1)
# #     input_shape = (image_rows, image_cols, 1)
#
# # x_train = x_train.astype('float32')
# # x_test = x_test.astype('float32')
# # x_train /= 255
# # x_test /= 255
# # print('x_train shape:', x_train.shape)
# # print(x_train.shape[0], 'train samples')
# # print(x_test.shape[0], 'test samples')
# #
# # y_train = keras.utils.to_categorical(y_train, num_classes)
# # y_test = keras.utils.to_categorical(y_test, num_classes)
#
# loaded_model.compile(loss = keras.losses.categorical_crossentropy, optimizer = keras.optimizers.Adam(lr=0.01), metrics = ['accuracy'])
# # score = loaded_model.evaluate(x_test, y_test, verbose=0)
# print(loaded_model.predict(img.reshape(1,28,28,1)))
#
#
# # print('Test loss:', score[0])
# # print('Test accuracy:', score[1])

def get_trained_model():

    json_file = open('mnist_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights("mnist_model.h5")
    print("Loaded model from disk")

    #loaded_model.compile(loss = keras.losses.categorical_crossentropy, optimizer = 'adam', metrics = ['accuracy'])

    #print(loaded_model.predict(img.reshape(28,28,1)))
    return loaded_model


get_trained_model()