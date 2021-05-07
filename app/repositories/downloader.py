import cv2
import numpy as np
import requests


class Downloader:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def download(self, path: str):
        response = requests.get(self.base_url + path)

        if not response.ok:
            return None

        arr = np.asarray(bytearray(response.raw.read()), dtype=np.uint8)
        image = cv2.imdecode(arr, cv2.THRESH_BINARY)

        return image
