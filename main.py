import streamlit as st
from ui_controls import display_ui
from session_manager import initialize_session

# Set Streamlit page config
st.set_page_config(page_title="Aureus Engine", layout="centered")

# Initialize session variables
initialize_session()

# Display UI
display_ui()
