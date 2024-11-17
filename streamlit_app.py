import streamlit as st
from ultralytics import solutions

solutions.inference()

### Make sure to run the file using command `streamlit run <file-name.py>`
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


#sudo apt-get install python3-opencv
#pip install ultralytics
# (not required) pip install lapx
