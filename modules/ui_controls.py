import streamlit as st
from prediction_engine import get_prediction_display, handle_result_submission
from material_data import get_material_input_fields

def display_ui():
    st.title("Aureus Engine Pattern Predictor")

    # Display Prediction
    prediction_text, confidence, color = get_prediction_display()
    st.markdown(
        f"<div style='border:3px solid {color};padding:10px;margin:10px 0;text-align:center;font-size:24px;'>"
        f"<strong>Next Prediction: {prediction_text}</strong><br><small>Confidence: {confidence*100:.1f}%</small></div>",
        unsafe_allow_html=True
    )

    # Crafted Result Input
    st.subheader("Enter Crafted Result")
    cols = st.columns([1, 1, 1])
    with cols[0]:
        if st.button("✅ W", key="win"):
            handle_result_submission("W")
    with cols[1]:
        if st.button("❌ L", key="loss"):
            handle_result_submission("L")
    with cols[2]:
        if st.button("➖ M", key="mid"):
            st.session_state["awaiting_mid_input"] = True

    if st.session_state.get("awaiting_mid_input", False):
        quality = st.selectbox("Select Crafted Quality", ["P", "C", "R", "X", "E", "Y"], key="mid_quality")
        if st.button("Submit Quality", key="submit_quality"):
            handle_result_submission(quality)
            st.session_state["awaiting_mid_input"] = False

    # Material Input Section
    st.subheader("Crafting Materials")
    get_material_input_fields()
