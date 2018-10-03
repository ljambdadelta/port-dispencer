class Logger:
  def __init__(self):
    self.logfile="TODO:"

class MalinaDB: 
  def __init__(self):
    self.logfile="TODO:"

class Server:
  def __init__(self, sock=None):
    refresh()

  def refresh(self):
    rebuildSocket()
    self.currentSessionClientAddress=None
    self.currentSession=None
    self.currentSessionfile=None
    self.currentSessionContent=None

  def rebuildSocket(self):
    if sock is !None:
      self.sock.close()
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def restart(self):
    refresh()
    self.socket.bind((socket.gethostname(), 911))
    self.socket.listen()

  def waitForConnection(self):
    self.restart()
    self.currentSession, self.currentSessionClientAddress = self.sock.accept()
    self.currentSession.setblocking(True) # Needed for treating socket as file
 
  def getIncomingDataContent(self)
    if self.currentSession is None:
      return None
    if self.currentSessionContent is not None:
      return self.currentSessionContent
    self.currentSessionfile = self.currentSession.makefile()
    self.currentSessionContent = self.currentSessionfile.read()
    self.currentSessionfile.close()
    return self.currentSessionContent
 
def parser(instructionWithArgument, position):
  if position is "INST":
    position=0
  if position is "POS":
    position=1
  else:
    position=-1 # Unsupported argument
  return instructionWithArgument.split(" ")[position]

def formAnswer(rawrequest):
  instruction = parser(rawrequest,"INST")
  argument = paeser(rawrequest,"POS")
  if instruction is "ID":
    if argument is "REG":
    elif isinstance(argument, int) is True:
    else:   
  elif instruction is "PORT":
    if argument is "GET"
    else:
def main():
  server = Server.Server()
  server.waitForConnection()
  
