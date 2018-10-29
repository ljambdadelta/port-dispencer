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

def log_preambule():
  msg="user with ip "+server.currentSessionClientAddress
  logi.write_to_log(msg)

def formAnswer(rawrequest):
  instruction = parser(rawrequest,"INST")
  argument = parser(rawrequest,"ARG")
  if instruction is "REG":
    log_preambule()
    logi.write_to_log("registration requested")
    mdb.add_new_port(argument)
    logi.write_to_log("registration done")
  elif instruction is "GET":
      logi.write_to_log(('(?) is requesting its port', argument))
      po = mdb.get_port_by_id(argument)
      logi.write_to_log(('It is (?)',po))
  else:
    logi.write_to_log(("It's sending garbage: (?)", rawrequest))

def main():
  print("Server wait")
  server.waitForConnection()
  mdb.reset()
  #mdb.add_new_port('mid5')
  print(mdb.get_port_by_id('mid4'))
  print("end")
main()