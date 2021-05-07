default: fmt start

gen_proto:
	python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./app/handlers/grpc/proto/ocr.proto

fmt:
	autopep8 -ir .

start:
	python3 main.py

image:
	docker build -t sport-ocr -f Dockerfile .
