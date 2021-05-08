from app.repositories.downloader import Downloader
from app.repositories.ocr import TextExtractor


class OcrUseCase:
    def __init__(self, downloader: Downloader, text_extractor: TextExtractor):
        self.downloader = downloader
        self.text_extractor = text_extractor

    def extract(self, url: str, string_column: int, num_column: int):
        image = self.downloader.download(url)
        if image is None:
            return []

        return self.text_extractor.extract(image, string_column, num_column)
