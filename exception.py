import sys

class CustomException(Exception):
  def __init__(self, error_message, error_detail:sys):
    self.error_message = error_message
    _,_,exc_tb = error_detail.exc_info()
    print(exc_tb)

    self.lineno = exc_tb.tb_lineno
    self.file_name = exc_tb.tb_frame.f_code.co_filename
  def __str__(self):
    return f"Error occured in python script name [{self.file_name}] linenumber [{self.lineno}] error message [{self.error_message}]"

if __name__=="__main__":
  try :
    a = 1/0
  except Exception as e:
    raise CustomException(e, sys)