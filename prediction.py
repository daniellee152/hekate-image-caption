from PIL import Image 
from io import BytesIO
import numpy as np
import pandas as pd 
from deepface import DeepFace

# INPUT_SHAPE_1 = (480, 480)
INPUT_SHAPE_2 = (224, 224)

def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return pil_image

def detect_face(image: Image.Image):
    # image = image.resize(INPUT_SHAPE_1)
    arr_image = np.asarray(image)
    try:          
        obj = DeepFace.analyze(img_path = arr_image, actions = [ 'gender', 'emotion'])
        prediction = [obj["dominant_emotion"], obj["gender"]]
    except ValueError:
        prediction = ["undefined"]
    return prediction
    
df = pd.read_excel('./data/Caption.xlsx', sheet_name=[1, 2, 3, 4], header=None)

def predict(image:np.ndarray):
    pred = detect_face(image)
    print(pred)
    gender = pred[1]
    emotion = pred[0]
    if gender == 'WOMEN':
        if emotion == 'happy':
            caption = df[1]        
        else:
            caption = df[2]
    else:
        if emotion == 'happy':
            caption = df[3]
        else:
            caption = df[4]

    num = np.random.randint(len(caption))
    return pred,caption.iloc[num][0]
