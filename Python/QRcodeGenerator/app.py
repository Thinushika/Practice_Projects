import qrcode
import image

qr = qrcode.QRCode(
    version = 15, #version of the qr code
    box_size=10,
    border=5,
)

data = input("Enter your URL here: ")
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")