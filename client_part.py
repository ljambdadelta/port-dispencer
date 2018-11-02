#!/bin/python3
import mClient

def main():
    boss="10.78.0.10"
    boss_port=12921
    my_az_port=-1
    while my_az_port <= 1024:
        cli=mClient.mClient(str.encode(boss),boss_port)
        my_az_port=cli.give_azport()
        print(my_az_port)
    
    
    
main()
