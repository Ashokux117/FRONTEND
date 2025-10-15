import streamlit as st

st.title("My First Streamlit App")
st.write("Hello Ashok 👋, welcome to Streamlit!")

number = st.slider("Pick a number", 1, 100)
st.write("You selected:", number)
