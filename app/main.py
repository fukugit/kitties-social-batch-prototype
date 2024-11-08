import logging

from app import engine, SessionLocal
from app.model import Cat
from app import Base
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

def run():
  """
  This is the main function.

   Args:
     None

   Returns:
     None
   """
  logger.info("=============== main start =================")
  db = SessionLocal()
  cats = db.query(Cat).all()

  cats_dict = [cat.__dict__ for cat in cats]
  for cat in cats_dict:
    cat.pop('_sa_instance_state', None)

  df = pd.DataFrame(cats_dict)
  df.to_csv("./csv/cats_data.csv", index=False)

  logger.info("See the file below. It contains cats data.")
  logger.info("File: ./csv/cats_data.csv")
  logger.info("=============== main end =================")

