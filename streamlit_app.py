import streamlit as st
import os

if os.getenv("HOSTNAME") == "streamlit":
  st.write("welcome to the cloud")

st.write(os.environ)
