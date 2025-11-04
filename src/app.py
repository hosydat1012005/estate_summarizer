import streamlit as st
import os
from PyPDF2 import PdfReader
from summarize import summarize_text

st.set_page_config(page_title="Estate Summarizer", page_icon="📄")

st.title("📄 Estate Document Summarizer")
st.caption("Upload a PDF to get a short summary and extracted information.")

uploaded_file = st.file_uploader("Select a PDF", type="pdf")

if uploaded_file:
    # Save uploaded file
    uploads_dir = "data/uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    file_path = os.path.join(uploads_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text
    reader = PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in reader.pages])

    # Summarize
    with st.spinner("Summarizing..."):
        summary = summarize_text(text)

    # Show output
    st.subheader("Summarizing Finished")
    st.write(summary)

    # Save result
    outputs_dir = "data/outputs"
    os.makedirs(outputs_dir, exist_ok=True)
    with open(os.path.join(outputs_dir, f"{uploaded_file.name}_summary.txt"), "w") as f:
        f.write(summary)

    st.success("Done")
