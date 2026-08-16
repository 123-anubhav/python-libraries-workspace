import streamlit as st
from pip._internal.cli import spinners
import pypdf
#import docx

st.title("Employee Records")
st.header("Employee data")

st.subheader("Employee data subheader")

name=st.text_input("Employee name put here")
review=st.text_area("Employee review put here")

st.markdown("### Employee data")

#chat_msg=st.chat_box("Employee data box put here")

st.selectbox("select someon",
             ["select anyone","JAVA","PYTHON","DEVOPS","AL/ML","AGENTIC AI"])

cv = st.file_uploader("upload your cv : ", type=["pdf","docx","docs"])

if(st.button("Click me")):
    st.success(cv.name)
    st.write(cv)
    st.write(name)
    st.write(review)
    # st.spinners(cv.name)
    """
    if cv is not None:
        # Show basic file details
        st.write("File name:", cv.name)

        # Check file extension and extract text
        if cv.type == "application/pdf" or cv.name.endswith(".pdf"):
            reader = pypdf.PdfReader(cv)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            st.subheader("Extracted PDF Content:")
            st.write(text)

        elif (
                cv.type
                == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                or cv.name.endswith(".docx")
        ):
            doc = docx.Document(cv)
            text = "\n".join([p.text for p in doc.paragraphs])
            st.subheader("Extracted Word Document Content:")
            st.write(text)
        else:
            st.warning("Please upload a valid PDF or DOCX file.")
"""


# 2. Check if the user has uploaded the file
if cv is not None:
  # 3. Read the PDF content using pypdf
  try:
    reader = pypdf.PdfReader(cv)
    extracted_text = ""

    # Loop through each page and extract text
    for page in reader.pages:
      extracted_text += page.extract_text() + "\n"

    # 4. Display the extracted text in the browser
    st.subheader("Parsed CV Data:")
    st.text(extracted_text)  # Preserves layout and spacing

  except Exception as e:
    st.error(f"Error parsing PDF: {e}")