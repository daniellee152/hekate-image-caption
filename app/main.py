import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# 1. Library imports
import uvicorn
from fastapi import FastAPI, File, UploadFile
from prediction import read_image, predict
import time
import pandas as pd

# 2. Create the app object
app = FastAPI()
df = pd.read_excel("./data/Caption.xlsx", sheet_name=[1, 2, 3, 4], header=None, engine="openpyxl")


@app.get("/")
def index():
    """
    This is a first docstring.
    """
    return {"message": "Hello, WORLD"}


@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    """
    Predict gender of people in picture.
    """
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    start = time.time()

    image = read_image(await file.read())

    pred, prediction = predict(image, df)
    end = time.time()
    print(f"Total prediction time : {end-start:.2f} seconds.")
    return pred, prediction


# 5. Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app)
