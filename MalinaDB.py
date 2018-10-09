import sqlite3
import os.path

class MalinaDB: 
  def __init__(self):
    self.db_conn = sqlite3.connect('Malina.db')
    self.cursor = self.db_conn.cursor()
  def clean(self):
    if os.path.isfile('Malina.db') is True:
      self.cursor.execute("DROP TABLE rel")
    self.cursor.execute("CREATE TABLE rel (malina-id INTEGER, port INTEGER, ipaddr TEXT)")
  def test(self):
    self.cursor.execute("INSERT INTO rel VALUES 42, 5009, 192.1.1.1")
    