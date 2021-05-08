from app.service.config import Config
from app.repositories.ocr import TextExtractor
from app.repositories.downloader import Downloader
from app.usecases.ocr import OcrUseCase


downloader = Downloader(Config.base_url)
text_extractor = TextExtractor()
use_case = OcrUseCase(downloader, text_extractor)

print(use_case.extract('DCm8ED3ZAip3AqP3i4Ddt2GCqRAKJpG9', 1, 21))
