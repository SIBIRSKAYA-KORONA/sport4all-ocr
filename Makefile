
gen_proto:
	python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./handlers/grpc/ocr.proto

fmt:
	autopep8 -ir .

start:
	python3 main.py
