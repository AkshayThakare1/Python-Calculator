import streamlit as st
from calculator import calculator
from text_analyzer import text_analyzer

# Load retro CSS
with open("retro.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🟢 Retro Python Lab █")

menu = st.sidebar.selectbox(
    "Select Tool",
    ["Calculator", "Text Analyzer"]
)

if menu == "Calculator":
    calculator()
else:
    text_analyzer()
