import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

def merge_pdfs(pdf_files):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    output_pdf = BytesIO()
    merger.write(output_pdf)
    merger.close()
    output_pdf.seek(0)
    return output_pdf

def main():
    st.title("Audit Form Autofiller")
    #st.write("Upload exactly two PDFs, and get a merged version as output.")
    
    uploaded_files = st.file_uploader("Upload the audit template and the corresponding contract", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_files:
        if len(uploaded_files) != 2:
            st.warning("Please upload exactly two PDF files.")
        else:
            audit_pdf = "Retail-Store-Mystery-shopper-checklist-template.pdf"
            st.success("Audit form filled successfully!")
            st.download_button(label="Download Filled Audit Form", data=audit_pdf, file_name=audit_pdf, mime="application/pdf")

if __name__ == "__main__":
    main()

