import os, sys 
import Logger
if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess

class mPorts:
    def __init__(self):
        #self.update_file()
        self.сooked_file = None

    def update_file(self):
        subprocess.run("az network lb inbound-nat-rule list -g FLVDI --lb-name LBforVMSS | grep frontendPort | awk '{print $2}' | sed 's/,//g' > raw.ports")
        subprocess.run("cp raw.ports cooked.ports -f")

    def extract_port(self):
        all_ports = self.get_list_ports_from_file("cooked.ports")
        if len(all_ports) > 0:
            self.trim_first_port_out_of_file("cooked.ports", all_ports)
        else:
            l = Logger()
            l.write_to_log("Error: no port left!")
            all_ports[0]=0
        return all_ports[0]
    
    def get_list_ports_from_file(self, filename):
        self.cooked_file = open(filename, os.O_RDONLY)
        payload = self.cooked_file.read()
        array_of_words_of_payload = payload.rsplit()
        return array_of_words_of_payload

    def trim_first_port_out_of_file(self, filename, all_ports):
        self.cooked_file = open(filename, os.O_WRONLY)
        self.cooked_file.write( all_ports[1:] )
        self.cooked_file.close()
        

    



