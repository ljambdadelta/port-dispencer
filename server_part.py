import Server
import Logger
import MalinaDB 


server = Server.Server()
logi = Logger.Logger()
mdb=MalinaDB.MalinaDB('Malina.db')

# сервер, логи и мдб -- должны быть видны глобально
# parser: вычленяет из пейлоада либо инструкцию, либо аргумент. Кому-то не хватает дефайнов

# formAnswer: пилим ответ на полученный аргумнетом запрос
#TODO:

def parser(instructionWithArgument, position):
  if position is "INST":
    position=0
  if position is "ARG":
    position=1
  else:
    position=-1 # невозможеое состояние
  return instructionWithArgument.split(" ")[position]

def formAnswer(rawrequest):
  instruction = parser(rawrequest,"INST")
  argument = parser(rawrequest,"ARG")
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

def main():
  print("Server wait")
  #server.waitForConnection()
  mdb.reset()
  #mdb.add_new_port('mid5')
  print(mdb.get_port_by_id('mid4'))
  print("end")
main()