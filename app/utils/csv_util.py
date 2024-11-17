import pandas as pd
import os
from app.logger_setup import setup_logger

class CsvUtil:
  """ CSV utilities class """
  def __init__(self,path, df):
    self.path = path
    self.df = df
    self.logger = setup_logger()

  def write_to_csv(self):
      self.df.to_csv(self.path, index=False)

  def remove(self):
    if os.path.exists(self.path):
        os.remove(self.path)
        self.logger.info(f"{self.path} was removed.")
    else:
        self.logger.info(f"{self.path} does not exist.")

  def get_path(self):
     return self.path