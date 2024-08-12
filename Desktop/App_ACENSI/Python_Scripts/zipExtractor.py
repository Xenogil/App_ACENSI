import zipfile
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ZipExtractor:
    def __init__(self, zip_path, exzip_path):
        self.zip_path = zip_path
        self.exzip_path = exzip_path

    def unzip_file(self):
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.exzip_path)
        logging.info(f"Les fichiers ont été extraits dans le dossier : {self.exzip_path}")
