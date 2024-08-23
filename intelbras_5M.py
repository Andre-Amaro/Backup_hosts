import paramiko as pm
from time import sleep
import os
from datetime import datetime

class apc_5m():
        def __init__(self,backup_directory) -> None:
                self.backups = os.path.join(os.path.dirname(os.path.realpath(__file__)), backup_directory)
                self.data = datetime.today().strftime('%d-%m-%Y')
                self.month = datetime.today().strftime('%B')
                self.year = datetime.today().strftime('%Y')
                self.ssh = pm.SSHClient()
                self.ssh.set_missing_host_key_policy(pm.AutoAddPolicy)


        def host_connect(self,host,port,username,password):
                try:
                        self.ssh.connect(port=port,hostname=host,username=username,password=password)
                        stdin, stdout, stderr = self.ssh.exec_command('cat /tmp/system.cfg')
                        sleep(2)
                        self.output = stdout.read()
                        self.output = self.output.decode().strip()
                        self.ssh.close()
                        self.generate_BKP_APC5M()
                        return True
                
                except Exception as e :
                        print(e)
                        return False
                
        def generate_BKP_APC5M(self):
                for i in self.output.splitlines():
                        if 'snmpd.name' in i:
                                name = (i[11:])
                                name = name.replace(' ','')
                                name = name.replace('/','-')
                                if not os.path.isfile(f'{self.backups}/{self.year}/{self.month}/{self.data}/{name}.cfg'):
                                        f = open(f"{self.backups}/{self.year}/{self.month}/{self.data}/{name}.cfg","x")
                                        f.write(self.output)
                                        f.close()

