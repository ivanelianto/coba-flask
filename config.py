import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  HOST = str(os.environ.get("DB_HOST"))
  DATABASE= str(os.environ.get("DB_DATABASE"))
  USERNAME= str(os.environ.get("DB_USERNAME"))
  PASSWORD= str(os.environ.get("DB_PASSWORD"))
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, PASSWORD)
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True
