import grpc
from concurrent import futures
from handlers.grpc import ocr, ocr_pb2_grpc


class Server:
    def __init__(self, port, max_workers):
        self.port = port
        self.max_workers = max_workers

    def run(self):
        server = grpc.server(futures.ThreadPoolExecutor(
            max_workers=self.max_workers))
        ocr_pb2_grpc.add_OcrServiceServicer_to_server(ocr.OcrHandler(), server)
        server.add_insecure_port("[::]:"+str(self.port))
        server.start()

        return server.wait_for_termination()
