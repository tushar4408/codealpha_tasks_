# app.py

import streamlit as st
from deep_translator import GoogleTranslator

# Set page title
st.set_page_config(page_title="Language Translator", page_icon="🌐")

# App Header
st.title("🌍 Language Translation Tool")

# Instructions
st.markdown("Type something, choose languages, and get the translated result!")

# User Input
text = st.text_area("🔤 Enter text to translate:")

# Language Dropdowns
languages = [
    "english", "hindi", "spanish", "french", "german", "italian", "chinese", "japanese", "korean", "russian",
    "portuguese", "arabic", "bengali", "turkish", "urdu"
]

source_lang = st.selectbox("🗣️ Select source language:", languages, index=languages.index("english"))
target_lang = st.selectbox("🎯 Select target language:", languages, index=languages.index("hindi"))

# Translate Button
if st.button("Translate"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            st.success("✅ Translated Text:")
            st.write(translated)
        except Exception as e:
            st.error(f"❌ Error: {e}")
