

import pyqrcode

qr_code = pyqrcode.create("https://parseltongue.co.in")
qr_code.svg('qrcode.svg', scale=5)

