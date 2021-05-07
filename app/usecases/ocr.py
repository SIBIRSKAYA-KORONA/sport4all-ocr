from app.repositories.downloader import Downloader


class OcrUseCase:
    def __init__(self, downloader: Downloader):
        self.downloader = downloader

    def extract(self, url: str):
        image = self.downloader.download(url)
        return image.shape
