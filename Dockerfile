FROM python:3.9.5

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 libleptonica-dev

RUN wget https://github.com/tesseract-ocr/tesseract/archive/4.1.1.zip && unzip 4.1.1.zip && cd tesseract-4.1.1 && \
	./autogen.sh && ./configure && make && make install && ldconfig && make training && make training install
RUN rm -rf 4.1.1.zip tesseract-4.1.1

ENV TESSDATA_PREFIX=/usr/local/share/tessdata/
RUN wget https://github.com/tesseract-ocr/tessdata_best/archive/4.1.0.zip && unzip 4.1.0.zip && \
	cd tessdata_best-4.1.0 && mv eng.traineddata rus.traineddata /usr/local/share/tessdata/
RUN rm -rf 4.1.0.zip tessdata_best-4.1.0

COPY . .

RUN pip3 install -r requirements.txt

CMD make start

