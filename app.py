import streamlit as st
import qrcode
from PIL import Image

# Title
st.title("QR Code Generator")

# User Input
data = st.text_input("Enter data for the QR Code:")

# Generate QR Code
if st.button("Generate QR Code"):
    if data:
        # Generate the QR code
        qr = qrcode.make(data)
        qr.save("qrcode.png")  # Save the QR code image
        st.image("qrcode.png", caption="Here is your QR Code!")  # Display the image
    else:
        st.error("Please enter valid data!")
