import streamlit as st

st.title("Streamlit Text Input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:", 0, 100, 25)

if name:
    st.write(f"Hello, {name}")