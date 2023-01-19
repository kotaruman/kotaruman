
 import wifi-qrcode_generator as qr
 form PIL import Image
 
 img = qr.wifi_qrcode ('ชื่อ WIFI',False,'WAP','รหัสผ่าน')
 img.save("Outputwifiqr.jpg","JPEG")
 Image.open('outputwifiqr.jpg')
