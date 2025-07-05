import streamlit as st
from modules.session_tracker import SessionTracker
from modules.utils.firebase_utils import upload_session_data, retrieve_session_data

def initialize_session():
    if "tracker" not in st.session_state:
        tracker = SessionTracker()
        stored_data = retrieve_session_data(user_id="default")
        if stored_data:
            for result in stored_data:
                tracker.add_result(result)
        st.session_state.tracker = tracker

def update_session_with_result(result):
    if "tracker" in st.session_state:
        tracker = st.session_state.tracker
        tracker.add_result(result)
        upload_session_data(user_id="default", session_data=tracker.get_session_results())