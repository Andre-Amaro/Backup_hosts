from datetime import datetime
from Mikrotik_Connector import MikrotikDevice
import os

class mikrotik():

    def __init__(self,backup_directory) -> None:
        self.backups = os.path.join(os.path.dirname(os.path.realpath(__file__)), backup_directory)
        self.data = datetime.today().strftime('%d-%m-%Y')
        self.month = datetime.today().strftime('%B')
        self.year = datetime.today().strftime('%Y')
        self.MK = MikrotikDevice()

    def host_connect(self,ip,user,password,port):
        try:
            self.MK.connect(ip_address=ip,username=user,password=password,port=port)
            self.backup_generation_mk(self.MK.get_identity(),self.MK.get_export_configuration())
            self.MK.disconnect()
            
            return True
        except  Exception as e:
            return False

    def backup_generation_mk(self,name,conteudo):
        if not os.path.isfile(f'{name}.rsc'):
            f = open(f'{self.backups}/{self.year}/{self.month}/{self.data}/{name}.rsc','x')
            f.write(conteudo)
            f.close()