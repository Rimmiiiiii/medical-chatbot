import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit UI
st.title("English to Deustch Translator")

# User input
text = st.text_area("Enter text in English:", "")

if st.button("Translate"):
    if text.strip():
        translated_text = GoogleTranslator(source="en", target="de").translate(text)
        st.success(f"**Translation:** {translated_text}")
    else:
        st.warning("Please enter some text to translate.")
