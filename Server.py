import socket

# Класс-интерфейс с малинами. Соединяемся/парсим.
# __init__/refresh: Создаём сокет(пустой) и сразу его инициализируем, ожидаем tcp-поток
# Инициализируем ничем все переменные.

# rebuildSocket: убиваем старый сокет и создаём новый.

# restart: пересоздаём сокет и привязываем его к порту из аргумента

# waitForConnection: рестартим сокет. Собственно здесь мы и ждём подключений. С полученными
# запросами работаем как с файлами

# getIncomingDataContent: Как-то считывает пейлоад из сессии. Написано давно и забыто
# Если работает, лучше не трогать
#TODO: вспомнить, что я писал и зачем

class Server:
  def __init__(self, sock=None):
    self.sock=sock
    self.refresh()
    

  def refresh(self):
    self.rebuildSocket()
    self.currentSessionClientAddress=None
    self.currentSession=None
    self.currentSessionfile=None
    self.currentSessionContent=None

  def rebuildSocket(self):
    if self.sock is not None:
      self.sock.close()
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def restart(self, port):
    self.refresh()
    self.sock.bind((socket.gethostname(), port))
    self.sock.listen()

  def waitForConnection(self,port):
    self.restart(port)
    self.currentSession, self.currentSessionClientAddress = self.sock.accept()
    #self.currentSession.setblocking(True) # Needed for treating socket as file
 
  def getIncomingDataContent(self):
    if self.currentSession is None:
      return None
    if self.currentSessionContent is not None:
      return self.currentSessionContent
    self.currentSessionfile = self.currentSession.makefile()
    self.currentSessionContent = self.currentSessionfile.read()
    self.currentSessionfile.close()
    return self.currentSessionContent

  def sendAnswerToMalina(self,answer):
    self.currentSession.sendall(answer)
    self.endSession()
  
  def endSession(self):
    self.currentSession.shutdown(socket.SHUT_RDWR)
    self.currentSession.close()
