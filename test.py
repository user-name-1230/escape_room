#!/usr/bin/env python3

from adventurelib import start, when
import pyqrcode
from PIL import Image


@when("hallo")
def hello_world():
    print("Hallo Welt")


@when("show qr code")
def qr():
    url = pyqrcode.create(
        "https://itty.bitty.site/#/?XQAAAAJsAAAAAAAAAAAeGQknmB2KhEriTBmhNCMxxyBfQwODwNmbNQRMJDZWhnDaOrDrqvEQI0ujHcri43qiRCODRphUfmBlZ/vEkNRL825ItDDbWmyaXYeb4i98hzSM3/5VkUA=")
    url.png("qr.png", scale=4)
    img = Image.open("qr.png")
    img.show()


start()
