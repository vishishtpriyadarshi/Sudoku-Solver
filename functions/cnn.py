from tensorflow.keras.models import model_from_json

def get_trained_model():

    json_file = open('./CNN_Model_Parameters/mnist_model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights("./CNN_Model_Parameters/mnist_model.h5")
    print("Loaded model from disk")

    #print(loaded_model.predict(img.reshape(28,28,1)))
    return loaded_model


#get_trained_model()
