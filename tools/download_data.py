from urllib.request import urlopen
from zipfile import ZipFile

zipurl = "https://otwartedane.metropoliagzm.pl/dataset/90259e73-6600-48e8-8b5b-acc35231f13e/resource/fea68b17-0664-40cb-9bc0-1a261bd16f5b/download/gps_20201019.zip"
zipresp = urlopen(zipurl)
tempzip = open("C:/Users/Waldi/Desktop/Dominika/GZM/baza/gps_20201019.zip", "wb")
tempzip.write(zipresp.read())
tempzip.close()
zf = ZipFile("C:/Users/Waldi/Desktop/Dominika/GZM/baza/gps_20201019.zip")
zf.extractall(path = "C:/Users/Waldi/Desktop/Dominika/GZM/baza/unpacked")
zf.close()