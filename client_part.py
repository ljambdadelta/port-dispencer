import mClient

def main():
    my_az_port=None
    boss="10.78.0.10"
    boss_port="12921"
    cli=mClient.mClient(boss,boss_port)
    cli.connect()
    my_az_port=cli.give_azport()
    print(my_az_port)
    
main()