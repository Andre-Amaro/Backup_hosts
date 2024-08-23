import os
from datetime import datetime

class files():

    def __init__(self,backup_directory) -> None:
        self.backups = os.path.join(os.path.dirname(os.path.realpath(__file__)), backup_directory)
        self.data = datetime.today().strftime('%d-%m-%Y')
        self.month = datetime.today().strftime('%B')
        self.year = datetime.today().strftime('%Y')

    def create_directory(self):
        if not os.path.exists(f'{self.backups}/{self.year}'):
            os.mkdir(f'{self.backups}/{self.year}')
        if not os.path.exists(f'{self.backups}/{self.year}/{self.month}'):
            os.mkdir(f'{self.backups}/{self.year}/{self.month}')
        if not os.path.exists(f'{self.backups}/{self.year}/{self.month}/{self.data}'):
            os.mkdir(f'{self.backups}/{self.year}/{self.month}/{self.data}')
    


    