import qrcode

# Replace with your real resume URL
url = "https://yourusername.github.io/assets/MiRuYoun_Resume.pdf"

# Create the QR code
img = qrcode.make(url)

# Save the QR code as an image file
img.save("resume_qr.png")

# Optional: Show the QR code
img.show()