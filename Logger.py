class Logger:
  def __init__(self):
    self.logfile = "log.log"
    self.logfile_inst = None

  def open_file_for_write(self):
    self.logfile_inst = open(self.logfile,'w')

  def write_to_log(self, text):
    self.open_file_for_write()
    self.logfile_inst.write(text)
    self.logfile_inst.close()
