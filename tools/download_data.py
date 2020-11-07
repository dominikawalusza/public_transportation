from urllib.request import urlopen
from zipfile import ZipFile

import os
import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level="INFO")

URL = "http://otwartedane.metropoliagzm.pl/dataset/90259e73-6600-48e8-8b5b-acc35231f13e/resource/fea68b17-0664-40cb-9bc0-1a261bd16f5b/download/gps_20201019.zip"
TARGET_PATH = "C:\\Users\\Waldi\\Desktop\\Dominika\\GZM\\baza"
TARGET_FILE_NAME = "gps_20201019.zip"
UNPACKED = "unpacked"

ZIP_TARGET_FILE_PATH = os.path.join(TARGET_PATH, TARGET_FILE_NAME)
UNPACKED_FILE_PATH = os.path.join(TARGET_PATH, UNPACKED)

def download(file_url, target_path, file_name):
    logging.info("Starting downloading")
    
    zipresp = urlopen(file_url)
    file_path = os.path.join(target_path, file_name)
    tempzip = open(file_path, "wb")
    tempzip.write(zipresp.read())
    tempzip.close()
    logging.info("Correctly downloaded")
    return True

def unpack(file_path, target_dir):
    logging.info("Starting unpacking")
    zf = ZipFile(file_path)
    zf.extractall(path = target_dir)
    zf.close()
    logging.info("Correctly unpacked")
    return True

if __name__ == "__main__":
    try:
        download(URL, TARGET_PATH, TARGET_FILE_NAME)
    except Exception as e:
        logging.error(e)

    try:
        unpack(ZIP_TARGET_FILE_PATH, UNPACKED_FILE_PATH)
    except Exception as e:
        logging.error(e)