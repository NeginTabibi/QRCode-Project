import qrcode
import os
import qrcode.image.svg

# 1. Define your folder and file name
folder_name = "generated_qrcodes"
file_name = "custom_qr.png"

# 2. Combine them into a full path safely
full_path = os.path.join(folder_name, file_name)

# 3. Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

# 4. Create a QRCode object
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# 5. Add data
qr.add_data('https://www.wikipedia.org')
qr.make(fit=True)

# 6. Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="lightyellow")

# 7. Save the image
img.save(full_path)

print(f"QR code saved successfully to: {os.path.abspath(full_path)}")

# 8. Generate the SVG (optional)
# factory = qrcode.image.svg.SvgPathImage
# img = qr.make_image(image_factory=factory)
# img.save("generated_qrcodes/custom_qr.svg")
# print("QR code saved successfully!")