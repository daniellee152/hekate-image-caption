FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /app/requirements.txt
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
