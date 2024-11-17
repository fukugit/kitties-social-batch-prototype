from app.utils.csv_util import CsvUtil

def test_get_path():
  csv_util = CsvUtil("./csv/cats_data.csv", None)
  result = csv_util.get_path()
  assert result == "./csv/cats_data.csv"