from llama_index.core import SimpleDirectoryReader
from logger import logging
from exception import CustomException
import sys

def load_data(data):
  """
  Load PDF from specific directory
  
  Parameters :
  - data (str) : The Path directory container PDF Files

  Return :
  - A list of loaded PDF documents
  """
  try:
    logging.info("load data dimulai...")
    loader = SimpleDirectoryReader(data)
    doc = loader.load_data()
    logging.info("load data selesai ...")
    return doc
  except Exception as e:
    raise CustomException(e, sys)  