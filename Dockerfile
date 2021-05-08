FROM python:3.10-rc-alpine3.13

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 tesseract-ocr tesseract-ocr-eng tesseract-ocr-rus

COPY . .
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]
