from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

from logger import logging
from exception import CustomException
import sys


def download_gemini_index(model, embed_model, documents):
  """
  Download and Initialize a Gemini Embedding
  """
  try:
    logging.info("load index dimulai...")
    index = VectorStoreIndex.from_documents(documents=documents, embed_model=embed_model)
    index.storage_context.persist()
    query_engine = index.as_query_engine(llm=model)
    logging.info("load index selesai ...")
    return query_engine
  except Exception as e:
    raise CustomException(e, sys)

