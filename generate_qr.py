import qrcode

# Portfolio link
data = "https://portifolio-five-gilt.vercel.app/"

# Generate QR code
qr = qrcode.make(data)

# Save image
qr.save("portfolio_qr.png")

print(" QR code saved as 'portfolio_qr.png'")
