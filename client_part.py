#!/bin/python3
import mClient

def main():
    my_az_port=None
    boss="192.168.1.142"
    boss_port=12921
    cli=mClient.mClient(str.encode(boss),boss_port)
    #cli.connect()
    my_az_port=cli.give_azport()
    print(my_az_port)
    
main()
