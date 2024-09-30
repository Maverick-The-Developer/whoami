FROM python:3.12

RUN apt-get update && apt-get install build-essential -y

RUN apt-get install ffmpeg libsm6 libxext6 -y

RUN pip3 install --upgrade pip setuptools wheel

WORKDIR /app

COPY . .

# RUN pip3 install -r requirements.txt
RUN pip3 install chromadb fastapi uvicorn deepface

RUN pip3 install tf-keras python-multipart

EXPOSE 8088

CMD ["python", "server.py"]