import streamlit as st

st.set_page_config(page_title="AI Quality Inspection", layout="centered")

st.title("AI Quality Inspection App")

uploaded_file = st.file_uploader("Upload an image for inspection", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("🔍 Running AI checks...")
    # Placeholder for actual model prediction
    st.success("✅ Result: Pass (demo)")
