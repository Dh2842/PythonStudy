import qrcode

qr_data = 'https://www.roblox.com/home'
qr_img = qrcode.make(qr_data)

save_path = 'myqr.png'
qr_img.save(save_path)