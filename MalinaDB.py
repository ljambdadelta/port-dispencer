import sqlite3
import os.path
import mPorts, Logger

# Класс для взаимодействия с базой данных малин
# __init__: Принимает аргументом имя базы данных в папке со скриптом
# Если не чувствует её, то создаст. Возможно, под линуксом, если не хватает прав, вылетит
# Инициируется курсор относительно этой базы. Ласт_ид -- счётчик подключенных малин. Мпортс -- 
# объект д/взаимодействия с ажурой (файлом с портами из неё)

# reset: Дропает таблицу и создаёт с нуля. Обновляет файл с портами из ажуры!

# check_if_this_malinaid_has_assigned: обращается к таблице с параметром malinaid
# Если находит запись с таким идентификатором, возвращает истину

# get_port_by_id: ищет запись в таблице по malinaid. Возвращает порт того, что нашёл. 
# Если нет такого порта, запрашивает добавление

# add_new_port: Создаёт новую запись в таблице. Порт берёт из копии ажурной базы
# 

# get_last_id: Возвращает счётчик. Когда-то он был нужен.

# run_and_commit: без коммита инсерт не пушится в базу, велосипед для грабли


class MalinaDB: 
  def __init__(self, dbname):
    self.logi = Logger.Logger()
    print("MDB create")
    self.dbname = dbname
    try:
      self.db_conn = sqlite3.connect(self.dbname)
    except sqlite3.Error as ex_fail_connect:
      print("Can't find and create DB", ex_fail_connect[0])
    self.cursor = self.db_conn.cursor()
    self.last_id=0
    self.m_port = mPorts.mPorts()

  def reset(self):
    print("MDB clean")
    if os.path.isfile(self.dbname) is True:
      self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS rel (
        malinaid INTEGER,
        port INTEGER);
      """)
      self.cursor.execute("DROP TABLE rel;")
    self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS rel (
      malinaid INTEGER,
      port INTEGER);
    """)
    self.db_conn.commit()
    self.last_id=0
    self.m_port.update_file()

  def run_and_commit(self,funct,arg):
    funct(*arg)
    self.db_conn.commit()

  def test(self):
    print("MDB test")
    a=42
    b=5009
    #c="192.1.1.1"
    self.cursor.execute("INSERT INTO rel VALUES (?,?);", (a,b))

  def check_if_this_malinaid_has_assigned(self,malinaid):
    self.cursor.execute("SELECT port FROM rel WHERE malinaid=?;", (malinaid,))
    port=self.cursor.fetchone()
    if port is not None:    return True
    else:                   return False

  def get_port_by_id(self, malinaid):
    self.cursor.execute("SELECT port FROM rel WHERE malinaid=?;", (malinaid,))
    try:
      port=self.cursor.fetchone()[0]
    except:
      self.logi.write_to_log("No such ID in DB, adding...")
      self.add_new_port(malinaid)
      return self.get_port_by_id(malinaid)
    return port
  
  def add_new_port(self,malinaid):
    existFlag=self.check_if_this_malinaid_has_assigned(malinaid)
    port = self.m_port.extract_port()
    if existFlag is False:
      self.last_id=self.last_id+1
      args= (malinaid, port)
      self.run_and_commit(self.cursor.execute,('''INSERT INTO rel(malinaid,port) VALUES (?,?);''',args)) 
    else: 
      self.logi.write_to_log(('port already assigned for this malina: (?)', malinaid))

  def get_last_id(self):
    return self.last_id

