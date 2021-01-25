from PIL import Image
from io import BytesIO
import numpy as np
from deepface import DeepFace
from deepface.extendedmodels import Glasses

# INPUT_SHAPE_1 = (480, 480)
INPUT_SHAPE_2 = (224, 224)


def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image


def detect_face(image: Image.Image):
    # image = image.resize(INPUT_SHAPE_1)
    prediction = []
    arr_image = np.asarray(image)

    #detect emtion
    try:
        obj = DeepFace.analyze(img_path=arr_image, actions=[ "emotion"])
        prediction.append(obj["dominant_emotion"])
    except ValueError:
        prediction.append("undefined")

    #detect gender
    try:
        obj = DeepFace.analyze(img_path=arr_image, actions=[ "gender"])
        prediction.append(obj["gender"])
    except ValueError:
        prediction.append("undefined")

    #detect glasses 
    prediction.append(Glasses.find_glasses(image))

    return prediction


def predict(image: np.ndarray, df):
    pred = detect_face(image)
    gender = pred[1]
    emotion = pred[0]
    if gender == "WOMEN":
        if emotion == "happy":
            caption = df[1]
        else:
            caption = df[2]
    else:
        if emotion == "happy":
            caption = df[3]
        else:
            caption = df[4]

    num = np.random.randint(len(caption))
    return pred, caption.iloc[num][0]
