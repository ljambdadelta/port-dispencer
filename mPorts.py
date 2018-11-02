import os, sys 
import Logger

# Класс для взаимодействия с 'базой' портов из ажуры. Получить их, выделить их
#TODO: заресторить, если кто-то отказывается/добавлен по ошибке
# В __init__ ничего особенного, только явное обнуление переменной
# файла из которого грабятся имена

# update_file: работает только под линуксом. Перезапрашивает у ажуры список портов

# extract_port: вычленяет из списка портов самый первый длядальнейшего использования. 
# Подчищает его из списка. Если свободных портов нет -- сыпет в лог об этом, возвращает ноль

# get_list_ports_from_file: получая аргументом имя файла, берёт из него список портов

# trim_first_port_out_of_file: получая аргументы имя файла и список портов, перезаписывает в
# файл весь список, за исключением первого порта

# Магия чуть ниже взята с гайда. Якобы ускоряет работу для *nix. Нужен тест.
if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess
import MalinaDB

class mPorts:
    def __init__(self):
        self.сooked_file = None

    def update_file(self):
        subprocess.run("./azure.sh")

    def cleanup(self):
        md=MalinaDB.MalinaDB('Malina.db')
        md.reset()	

    def extract_port(self):
        all_ports = self.get_list_ports_from_file("cooked.ports")
        if len(all_ports) > 0:
            self.trim_first_port_out_of_file("cooked.ports", all_ports)
        else:
            l = Logger.Logger()
            l.write_to_log("Error: no port left!")
            all_ports.append('0')
        return all_ports[0]
    
    def get_list_ports_from_file(self, filename):
        self.cooked_file = open(filename, 'r')
        payload = self.cooked_file.read()
        array_of_words_of_payload = payload.rsplit()
        return array_of_words_of_payload

    def trim_first_port_out_of_file(self, filename, all_ports):
        self.cooked_file = open(filename, 'w')
        self.cooked_file.write( '\n'.join(all_ports[1:]) )
        self.cooked_file.close()
        

    



