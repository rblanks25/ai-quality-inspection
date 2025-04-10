import streamlit as st
import random
from pathlib import Path

# --- Simulated AI logic placeholder ---
def inspect_image(image_name):
    """Simulate inspection outcome based on image name."""
    if "label" in image_name.lower():
        return "Label detected: Sirloin Steak", "label"
    elif "shrimp" in image_name.lower():
        return random.choice(["Pass", "Fail", "Needs Review"]), "shrimp"
    elif "broc" in image_name.lower():
        return random.choice(["Pass", "Fail", "Needs Review"]), "broccoli"
    else:
        return random.choice(["Pass", "Fail", "Needs Review"]), "unknown"

# --- Streamlit UI ---
st.set_page_config(page_title="AI Quality Inspection", layout="wide")
st.title("🛠️ AI Quality Inspection")

uploaded_files = st.file_uploader(
    "Upload images (labels, products, etc.)", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

# Sidebar counters
pass_count = 0
fail_count = 0
review_count = 0

if uploaded_files:
    st.sidebar.header("✨ Summary")
    for uploaded_file in uploaded_files:
        # Image metadata and result
        image_name = Path(uploaded_file.name).name
        result, category = inspect_image(image_name)

        # Update counters
        if result == "Pass":
            pass_count += 1
        elif result == "Fail":
            fail_count += 1
        else:
            review_count += 1

        # Display results per image
        st.subheader(f"{image_name}")
        if result == "Pass":
            st.success(f"✅ Result: {result}")
        elif result == "Fail":
            st.error(f"❌ Result: {result}")
        else:
            st.warning(f"🔶 Result: {result}")

        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        st.markdown("---")

    # Final summary sidebar
    st.sidebar.metric("✅ Pass", pass_count)
    st.sidebar.metric("❌ Fail", fail_count)
    st.sidebar.metric("🔶 Needs Review", review_count)
