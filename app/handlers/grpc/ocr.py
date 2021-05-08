from app.usecases.ocr import OcrUseCase
from app.common.logger import log
from .proto.ocr_pb2 import PlayerStats
from .proto.ocr_pb2_grpc import OcrService


class OcrHandler(OcrService):
    def __init__(self, ocr: OcrUseCase):
        self.ocr = ocr

    def GetStatsByImage(self, request, context):
        log.info('received request: %s', request)
        result = self.ocr.extract(
            request.path, request.player_column, request.score_column)
        log.info('extracted data: %s', result)

        return PlayerStats(**result)
