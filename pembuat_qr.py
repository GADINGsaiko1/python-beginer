import qrcode

link = input("input link / url: ")
file_name = input("nama file untuk qr nya apa? ")
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(link)
gambar = qr.make_image(fill_color='black', back_color='white')
gambar.save(file_name)
print(f"qr code sudah dibuat dengan nama {file_name}")