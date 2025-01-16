import os
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings
from logger import logging
from exception import CustomException
import sys

load_dotenv(dotenv_path='../.env')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
def load_model(model_name='models/gemini-pro', embed_model="models/text-embedding-004"):
  """
  Load model from gemini api
  
  Parameters :
  - model_name (str) : The Path directory container PDF Files

  Return :
  - A list of loaded PDF documents
  """
  try:
    logging.info("load model dimulai...")
    Settings.llm = Gemini(model=model_name, api_key=GEMINI_API_KEY)
    Settings.embed_model = GeminiEmbedding(model_name=embed_model)
    Settings.chunk_size = 800
    Settings.chunk_overlap = 20
    logging.info("load model selesai ...")
    return Settings
  except Exception as e:
    raise CustomException(e, sys)