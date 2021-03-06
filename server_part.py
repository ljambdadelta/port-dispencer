#!/bin/python3
import Server
import Logger
import MalinaDB
import os,sys 
if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess

server = Server.Server()
logi = Logger.Logger()
mdb=MalinaDB.MalinaDB('Malina.db')

# сервер, логи и мдб -- должны быть видны глобально
# parser: вычленяет из пейлоада либо инструкцию, либо аргумент. Кому-то не хватает дефайнов

# formAnswer: пилим ответ на полученный аргумнетом запрос


def parser(instructionWithArgument, position):
  print("\n instruction is: %s" % instructionWithArgument)
  if position is "INST":
    position=0
    print("\n instr: %s " % instructionWithArgument.split(" ")[position] )
  elif position is "ARG":
    position=1
    print("\n arg is: %s" % instructionWithArgument.split(" ")[position])
  else:
    position=-1 # невозможеое состояние
  return instructionWithArgument.split(" ")[position]

def log_preambule():
  msg="user with ip "+server.currentSessionClientAddress[0]
  logi.write_to_log(msg)

def doAnswer(rawrequest):
  srawrequest=rawrequest.decode()
  instruction = parser(srawrequest,"INST")
  argument = parser(srawrequest,"ARG")
  if instruction == 'REG':
    log_preambule()
    logi.write_to_log("registration requested")
    mdb.add_new_port(argument)
    po = mdb.get_port_by_id(argument)
    logi.write_to_log("registration done")
    sendAnswer(po)
  elif instruction == "GET":
      logi.write_to_log('%s is requesting its port'% argument)
      po = mdb.get_port_by_id(argument)
      logi.write_to_log('It is %s'% po)
      sendAnswer(po)
  else:
    logi.write_to_log("It's sending garbage: %s"% rawrequest)
  

def sendAnswer(answer):
  print(answer)
  server.sendAnswerToMalina(str(answer).encode())

def main():
  mypid=int(os.getpid())
  print("I am server, my pid is %s"% mypid) 
  pidlist=str.split(subprocess.run("ps aux|grep server_part| awk '{print $2}'", capture_output=True, text=True, shell=True).stdout) 
  for pid in pidlist:
    pid=int(pid)
    print("pid of server: %s"% pid)
    if pid < mypid:
      print("%s != %s#" %(pid, mypid))
      print("it's not me, killing active clone")
      os.kill(pid, 9)
    else:
      print("Oh, it's one of mine pids, won't kill it")
  counter=0
  while True:
    counter+=1
    print("Server Wait. Attempt %i" % counter)
    server.waitForConnection(12921)
    doAnswer(server.getIncomingDataContent())
  
  #mdb.reset()
  #mdb.add_new_port('mid5')
  #print(mdb.get_port_by_id('mid4'))
  print("end")
main()
