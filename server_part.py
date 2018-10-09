import Server
import Logger
import MalinaDB 

server = Server.Server()
log = Logger.Logger()

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
      log.write_to_log("user with ip"+server.l)
    elif isinstance(argument, int) is True:
      print
    else:   
      print 
  elif instruction is "PORT":
    if argument is "GET"
    else:
def main():
  server.waitForConnection()