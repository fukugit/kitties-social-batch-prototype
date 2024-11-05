import logging

from app import engine, SessionLocal
from app.model import Cat
from app import Base

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
  db = SessionLocal()

  # cat = Cat(name='test_cat', breed='test_breed')
  # db.add(cat)
  # db.flush()
  # db.commit()
  cats = db.query(Cat).all()
  logger.info("hello world!")
  logger.info(cats)

