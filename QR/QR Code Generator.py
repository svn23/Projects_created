import pyqrcode
import png
link = "https://www.linkedin.com/in/sovan-sen-40a873217/"
qr_code = pyqrcode.create(link)
qr_code.png("linkedin.png", scale=5)