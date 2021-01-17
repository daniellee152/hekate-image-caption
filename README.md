# Detect face and assign caption for image
---
## Run with docker
    > docker-compose up
Server api: http://127.0.0.1:8088/docs

## Run without docker
    > python3 --version
    Python 3.7.9
    > pip3 install -r requirements.txt
    > cd app
    > uvicorn main:app --reload
Server api: http://127.0.0.1:8000/docs
