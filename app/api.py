import logging

from app import engine, SessionLocal
from app.model import Cat
from app import Base
import pandas as pd
from app.logger_setup import setup_logger
from app.utils.csv_util import CsvUtil

from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    page = {
        'ping': "success",
    }
    logger = setup_logger()
    logger.info("=============== / start =================")
    logger.info("=============== / end =================")
    return jsonify(page)

@main_bp.route('/cat')
def get_cat():
  """
  This is the main function.

   Args:
     None

   Returns:
     None
   """
  logger = setup_logger()
  logger.info("=============== main start =================")
  db = SessionLocal()
  cats = db.query(Cat).all()

  cats_dict = [cat.__dict__ for cat in cats]
  for cat in cats_dict:
    cat.pop('_sa_instance_state', None)

  df = pd.DataFrame(cats_dict)
  csv_util = CsvUtil("./csv/cats_data.csv", df)
  csv_util.remove()
  csv_util.write_to_csv()


  logger.info("See the file below. It contains cats data.")
  logger.info("File: ./csv/cats_data.csv")
  logger.info("=============== main end =================")
  page = {
      'result': "success"
  }
  return jsonify(page)
