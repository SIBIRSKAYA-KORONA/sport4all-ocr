from app.usecases.ocr import OcrUseCase
from app.common.logger import log
from .proto.ocr_pb2 import PlayerStats
from .proto.ocr_pb2_grpc import OcrService


class OcrHandler(OcrService):
    def __init__(self, ocr: OcrUseCase):
        self.ocr = ocr

    def GetStatsByImage(self, request, context):
        log.info('received request: %s', request)
        stats = self.ocr.extract(
            request.path, request.player_column, request.score_column)
        log.info('extracted %d records', len(stats))

        proto_stats = PlayerStats()
        for stat in stats:
            proto_stat = proto_stats.stats.add()
            proto_stat.name = stat['name']
            proto_stat.surname = stat['surname']
            proto_stat.score = stat['score']

        return proto_stats
