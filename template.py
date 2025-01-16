import logging
import os
from pathlib import Path

list_of_files = [
  "QAWithPDF/__init__.py",
  "QAWithPDF/data_ingestion.py",
  "QAWithPDF/embedding.py",
  "QAWithPDF/model_api.py",
  "Experiments/experiments.ipynb",
  "streamlit_app.py",
  "logger.py",
  "exception.py",
  "setup.py"
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath)
  if filedir != "" :
    os.makedirs(filedir, exist_ok=True)
    logging.info(f"Membuat Directory : {filedir} untuk file {filename}")
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    with open(filepath, 'w') as file:
      pass
    file.close()
    logging.info(f"Membuat File Kosong : {filepath}")
  else:
    logging.info(f"{filename} sudah ada")