#!/bin/python3
import mClient
import time
import os, sys 
if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess


def main():
    boss="10.78.0.10"
    boss_port=12921
    my_az_port=-1
    while my_az_port <= 1024:
        try:
            cli=mClient.mClient(str.encode(boss),boss_port)
            my_az_port=cli.give_azport()
            print(my_az_port)
            time.sleep(1)
        except: 
            print("Error Occured. Maybe Server is down? Retrying...")
            continue
    subprocess.run("cat /home/student/cred.lst | sed 's#PORT=\x22.....\x22#PORT=50000#' > /home/student/alt.cred.lst", shell="true" )
    subprocess.run("mv /home/student/alt.cred.lst /home/student/cred.lst", shell="true")
    subprocess.run("cat /home/student/cred.lst | sed 's/PORT=...../PORT=%i/' > /home/student/alt.cred.lst" % my_az_port, shell="true" )
    subprocess.run("mv /home/student/alt.cred.lst /home/student/cred.lst", shell="true")
    subprocess.run("chmod 777 /home/student/cred.lst", shell="true")
    
    
    
main()
