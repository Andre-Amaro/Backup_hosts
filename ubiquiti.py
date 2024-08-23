import paramiko as pm
from scp import SCPClient
import os
from datetime import datetime
from time import sleep

class unif():

    def __init__(self,backup_directory) -> None:
        self.backups = os.path.join(os.path.dirname(os.path.realpath(__file__)), backup_directory)
        self.data = datetime.today().strftime('%d-%m-%Y')
        self.month = datetime.today().strftime('%B')
        self.year = datetime.today().strftime('%Y')

    def host_connect(self,host,port,user,password):
        self.ssh = pm.SSHClient()
        self.ssh.set_missing_host_key_policy(pm.AutoAddPolicy)
        try:
            self.ssh.connect(port=port,hostname=host,username=user,password=password)
            stdin, stdout, stderr = self.ssh.exec_command("uname -n")
            output = stdout.read()
            output = output.decode().strip()

            self.download_bkp()
            sleep(1)
            self.create_file_unif(output)
            self.ssh.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def download_bkp(self):
        try:
            scp = SCPClient(self.ssh.get_transport())
            scp.get('/tmp/system.cfg',f'{self.backups}/{self.year}/{self.month}/{self.data}')
        except Exception as f :
            print('erro download file')
    
    def create_file_unif(self,name):
        if os.path.isfile(f'{self.backups}/{self.year}/{self.month}/{self.data}/{name}.cfg'):
            pass
        else:
            os.rename(f'{self.backups}/{self.year}/{self.month}/{self.data}/system.cfg', f'{self.backups}/{self.year}/{self.month}/{self.data}/{name}.cfg')
