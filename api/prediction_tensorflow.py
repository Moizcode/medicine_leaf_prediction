from keras.models import load_model
import pickle as pkl
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

model = load_model(
    r"/app/Model/best_model.keras")
clss_to_number = {}
with open(r"/app/Model/class_to_number.pkl", 'rb') as file:
    clss_to_number = pkl.load(file)


def preprocess_image(image_path, target_size=(400, 300)):
    image = Image.open(image_path)
    image = image.convert('RGB')
    image = image.resize(target_size)
    image = img_to_array(image)
    image = image.astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


def leaf_recognition(image_path):
    image = preprocess_image(image_path)
    predictions = model.predict(image)
    predicted_class_index = np.argmax(predictions)
    predicted_label = [key for key, value in clss_to_number.items(
    ) if value == predicted_class_index][0]
    prediction_score = predictions[0][predicted_class_index]
    return predicted_label, prediction_score
