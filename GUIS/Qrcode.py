import qrcode
qr = qrcode.QRCode(box_size=10,border=4)
data = 'https://deworldr.github.io/Map14/'
qr.add_data(data)
qr_img = qrcode.make(data)
qr_img.save("D:\งาน\project\GUIS\Image\Qrcode\img14.png")