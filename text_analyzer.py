import streamlit as st

def text_analyzer():
    st.subheader("📝 Text Analyzer")

    text = st.text_area("Enter text")

    if st.button("Analyze"):
        if not text.strip():
            st.warning("Please enter some text")
            return

        words = text.split()
        characters = len(text)
        unique_words = len(set(words))

        st.write(f"🔹 Words: {len(words)}")
        st.write(f"🔹 Characters: {characters}")
        st.write(f"🔹 Unique words: {unique_words}")
