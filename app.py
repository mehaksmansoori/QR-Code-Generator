import streamlit as st
import qrcode
from PIL import Image
import io

# Title
st.title("QR Code Generator")

# User Input
data = st.text_input("Enter data for the QR Code:")

# Generate QR Code
if st.button("Generate QR Code"):
    if data:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert image to BytesIO buffer
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)

        # Convert BytesIO to a format st.image() can display
        img_display = Image.open(img_buffer)

        # Display the QR code
        st.image(img_display, caption="Here is your QR Code!", use_container_width=True)

        # Download button
        st.download_button(
            label="Download QR Code",
            data=img_buffer,
            file_name="qrcode.png",
            mime="image/png",
        )
    else:
        st.error("Please enter valid data!")

