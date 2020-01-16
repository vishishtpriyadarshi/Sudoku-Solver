from tensorflow.keras.models import model_from_json
import os

def get_trained_model():

    # path_json = os.path.abspath('./CNN_Model_Parameters/mnist_model.json')
    # path_h5 = os.path.abspath('./CNN_Model_Parameters/mnist_model.h5')

    path_json = os.path.dirname(os.path.realpath(__file__))
    path_json = os.path.join(path_json, '../CNN_Model_Parameters/mnist_model.json')

    path_h5 = os.path.dirname(os.path.realpath(__file__))
    path_h5 = os.path.join(path_h5, '../CNN_Model_Parameters/mnist_model.h5')

    # print(path_json)
    # print(path_h5)

    json_file = open(path_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights(path_h5)
    #print("Loaded model from disk")

    #print(loaded_model.predict(img.reshape(28,28,1)))
    return loaded_model


# get_trained_model()
