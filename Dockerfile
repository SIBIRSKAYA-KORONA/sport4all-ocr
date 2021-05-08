FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-rus

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
