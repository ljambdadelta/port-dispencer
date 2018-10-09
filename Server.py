import socket

class Server:
  def __init__(self, sock=None):
    self.refresh()
    self.sock=sock

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

  def restart(self):
    self.refresh()
    self.sock.bind((socket.gethostname(), 911))
    self.sock.listen()

  def waitForConnection(self):
    self.restart()
    self.currentSession, self.currentSessionClientAddress = self.sock.accept()
    self.currentSession.setblocking(True) # Needed for treating socket as file
 
  def getIncomingDataContent(self):
    if self.currentSession is None:
      return None
    if self.currentSessionContent is not None:
      return self.currentSessionContent
    self.currentSessionfile = self.currentSession.makefile()
    self.currentSessionContent = self.currentSessionfile.read()
    self.currentSessionfile.close()
    return self.currentSessionContent

