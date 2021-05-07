import grpc
from concurrent import futures

from .config import Config
from app.common.logger import log
from app.repositories.downloader import Downloader
from app.repositories.ocr import TextExtractor
from app.usecases.ocr import OcrUseCase
from app.handlers.grpc.ocr import OcrHandler
from app.handlers.grpc.proto import ocr_pb2_grpc


class Server:
    def __init__(self):
        pass

    def run(self):
        downloader = Downloader(Config.base_url)
        text_extractor = TextExtractor()
        use_case = OcrUseCase(downloader, text_extractor)
        handler = OcrHandler(use_case)

        server = grpc.server(futures.ThreadPoolExecutor(
            max_workers=Config.max_grpc_workers))
        ocr_pb2_grpc.add_OcrServiceServicer_to_server(handler, server)
        server.add_insecure_port("[::]:"+str(Config.port))
        server.start()
        log.info("service is started")

        return server.waitmak_for_termination()
