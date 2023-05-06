FROM python:3.8-alpine

WORKDIR /app
COPY . /app

RUN apk add --no-cache ffmpeg libsm6 libxext6 && \
    apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

CMD ["python3", "app.py"]

# FROM python:3.8-slim-buster
# WORKDIR /app
# COPY . /app
 
# RUN apt update -y && apt install awscli -y

# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
# CMD ["python3", "app.py" ]