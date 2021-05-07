from .proto.ocr_pb2 import PlayerStat, PlayerStats
from .proto.ocr_pb2_grpc import OcrService


class OcrHandler(OcrService):

    def GetStatsByImage(self, request, context):
        link = request.link
        player_stats = PlayerStats()
        player_stats.stats.append(PlayerStat(
            name="Anton"+link, surname="Chetverov", score=71))

        return player_stats
