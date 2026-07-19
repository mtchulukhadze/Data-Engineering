import qrcode

url = input("Enter URL:").strip()
file_path = "D:\Data\Data Engineering\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("generated")