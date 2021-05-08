FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y python3-opencv tesseract-ocr libtesseract-dev tesseract-ocr-*

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
