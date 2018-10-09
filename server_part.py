import Server
import Logger
import MalinaDB 

server = Server.Server()
logi = Logger.Logger()

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
  argument = parser(rawrequest,"POS")
  if instruction is "ID":
    if argument is "REG":
      msg="user with ip"+server.currentSessionClientAddress
      logi.write_to_log(msg)

    elif isinstance(argument, int) is True:
      print
    else:   
      print 
  elif instruction is "PORT":
    if argument is "GET":
      print
    else:
      print
def __init__():
  print("Server wait")
  server.waitForConnection()
  print("MDB create")
  MDB=MalinaDB.MalinaDB()
  print("MDB clean")
  MDB.clean()
  print("MDB test")
  MDB.test()
  print("end")
