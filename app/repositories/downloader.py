import cv2
import numpy as np
import requests
from app.common.logger import log


class Downloader:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def download(self, path: str):
        response = requests.get(self.base_url + path)

        if not response.ok:
            return None

        arr = np.asarray(bytearray(response.content), dtype=np.uint8)
        try:
            return cv2.imdecode(arr, cv2.THRESH_BINARY)
        except Exception as e:
            log.error('error while decode image: %s', e)
            return None
