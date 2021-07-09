import streamlit as st
import os
from streamlit import caching

if os.getenv("HOSTNAME") == "streamlit":
  st.write("welcome to the cloud")

st.write(os.environ)



caching.clear_cache()
