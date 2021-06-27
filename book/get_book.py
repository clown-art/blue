from unicodedata import name
import pymysql
import requests
from requests.exceptions import URLRequired
from bs4 import BeautifulSoup
import logging
import retry
import os
import datetime

logger = logging.Logger(name='Logger', level=logging.INFO)
config = {
    "host": os.environ.get('mysql_host', ''),
    "user": os.environ.get('mysql_user',''),
    "password": os.environ.get('mysql_password', ''),
    "database": os.environ.get('mysql_database', ''), 
    "port":3306
}


class MysqlAPI():
    def __init__(self) -> None:
        self.db = self._connect_mysqlgit 
        self.cursor = self.db.cursor()
    
    @retry
    def _connect_mysql(self):
        try:
            db = pymysql.connect(**config)
        except Exception as err:
            logger.error(err)   
        return  db
    
    def write_book_category(self):
        sql = "insert table category () values() "
    
    def time(self):
        return 
        


class Book():
    def __init__(self):
        self.url = "http://www.xinshu123.vip/"
        self.request = requests
        self.book_mysql = MysqlAPI()

    def get_category(self):
        response = self.request.get(self.url)
        charset_format = response.apparent_encoding
        soup  =  BeautifulSoup((response.content.decode(charset_format)), 'html.parser')
        categorys = soup.find('div', "nav").find_all('a')
        categorys_col = {}
        for category in categorys:
            if category.get_text() == '首页':
                continue
            categorys_col[category.get_text()] = category['href']
        self.book_mysql.cursor.execute("")

if __name__ == '__main__':
    Book().main()
    
        




    
        

        


if __name__ == '__main__': 

    book = Book()
    book.get_category()