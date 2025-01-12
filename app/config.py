import os

basedir = os.path.abspath(os.path.dirname(__file__))

# SQL Server 连接字符串
DATABASE_URI = 'mssql+pyodbc://sa:123456@localhost/menzhen?driver=ODBC+Driver+17+for+SQL+Server'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mssql+pyodbc://sa:123456@localhost/menzhen?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False