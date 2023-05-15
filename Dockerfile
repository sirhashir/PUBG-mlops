FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
 
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y \
    && pip install -r requirements.txt \
    && apt-get remove -y unzip \   
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
    
CMD ["python3", "app.py"]