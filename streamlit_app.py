import streamlit as st
import os
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model
from QAWithPDF.embedding import download_gemini_index
from tempfile import TemporaryDirectory

def main():
  st.set_page_config("QA With Documents")
  docs = st.file_uploader("Upload Your Document", accept_multiple_files=True)
  st.header("QA with document (Document Retrieval)")
  user_question = st.text_input("ask your question")
  if st.button('submit & process'):
    with st.spinner("Processing ..."):
      # print(doc)
      upload_dir = "data"
      for uploaded_file in docs:
          file_path = os.path.join(upload_dir, uploaded_file.name)
          with open(file_path, "wb") as f:
              f.write(uploaded_file.read())
      document = load_data(upload_dir)
      setting = load_model(model_name='models/gemini-pro', embed_model="models/text-embedding-004")
      query_engine = download_gemini_index(setting.llm, setting.embed_model, document)
      response = query_engine.query(user_question)
      st.write(response.response)

if __name__=="__main__":
  main()