from PIL import Image
import tensorflow as tf


def find_glasses(image: Image.Image):
  #load model 
  model = tf.keras.applications.InceptionV3(weights="imagenet")

  #pre-process image
  image = image.resize((299,299))
  img_array = tf.keras.preprocessing.image.img_to_array(image)
  img_array = tf.expand_dims(img_array, 0) 
  img_array = tf.keras.applications.inception_v3.preprocess_input(img_array)

  #prediction 
  glasses_prediction = model.predict(img_array)

  #decode prediction
  glasses_prediction = tf.keras.applications.inception_v3.decode_predictions(glasses_prediction, top=20)[0]
  for pred in glasses_prediction:
    if pred[1] == "sunglass" or pred[1] == "sunglasses" or pred[1]== "sunscreen":
      prediction = "glasses"
      return prediction
    else:
      prediction = "no_glasses"
  return prediction
