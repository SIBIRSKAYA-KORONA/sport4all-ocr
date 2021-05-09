FROM python:3.9.5

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 libleptonica-dev

RUN wget https://github.com/tesseract-ocr/tesseract/archive/4.1.1.zip && unzip 4.1.1.zip && cd tesseract-4.1.1 && \
	./autogen.sh && ./configure && make && make install && ldconfig && make training && make training install
RUN git clone https://github.com/tesseract-ocr/tessdata_best.git && cd tessdata_best && mv eng.traineddata rus.traineddata /usr/local/share/tessdata/
RUN rm -rf tessdata_best && 4.1.1.zip && tesseract-4.1.1
ENV TESSDATA_PREFIX=/usr/local/share/tessdata/

COPY . .

RUN pip3 install -r requirements.txt

CMD make start
