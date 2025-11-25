import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image
import streamlit as st


load_dotenv()

gemini_api_key=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

st.header("Image Analyser")
upload_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if upload_file is not None:
    st.image(Image.open(upload_file))
prompt = st.text_input("Enter the text")

if st.button("GET RESPONSE"):
    img = Image.open(upload_file)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content([prompt, img])
    st.markdown(response.text)