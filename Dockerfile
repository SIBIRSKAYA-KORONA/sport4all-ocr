FROM python:3.9.5-alpine

WORKDIR /app

RUN apk update && apk upgrade && apk --update add gcc g++ make cmake openssl-dev linux-headers
RUN apk add tesseract-ocr tesseract-ocr-data-rus

COPY . .

RUN pip3 install -r requirements.txt

CMD make start
