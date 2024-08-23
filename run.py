from files_creation import files
from ubiquiti import unif
from mikrotik import mikrotik
from intelbras_5M import apc_5m
from intelbras_5A import apc_5a
import pandas as pd
import os

def iterator():
    mk_hosts = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/hosts_ip.csv")
    apc_5a_hosts = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/apc_5a_ip.csv")
    unif_hosts = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/hosts_unif_ip.csv")
    users = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/users.csv")
    apc_5m_hosts = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/apc_5m_ip.csv")
    backup = 'arquivos'
    
    #load global user data
    usuarios = pd.read_csv(f'{users}')

    #directories creation
    directory = files(backup_directory=backup)
    directory.create_directory()
 

    #5m backup
    data_5m = pd.read_csv(f'{apc_5m_hosts}')
    apc5m = apc_5m(backup_directory=backup)
    data_5m = data_5m.drop_duplicates()
    for i in data_5m.get('IP'):
        for  index, row in usuarios.iterrows():
            if apc5m.host_connect(host=i,username=row['USUARIO'],password=row['SENHA'],port=row['PORTA']):
                 break
            
    #unif backup
    data_unif = pd.read_csv(f'{unif_hosts}')
    ubqt = unif(backup_directory=backup)
    data_unif = data_unif.drop_duplicates()
    for i in data_unif.get('IP'):
        for  index, row in usuarios.iterrows():
            if ubqt.host_connect(host=i,user=row['USUARIO'],password=row['SENHA'],port=row['PORTA']):
                 break
            
    #apc5A backup
    data_5a = pd.read_csv(f'{apc_5a_hosts}')
    apc5a = apc_5a(backup_directory=backup)
    data_5a = data_5a.drop_duplicates()
    for i in data_5a.get('IP'):
        for  index, row in usuarios.iterrows():
            if apc5a.host_connect(host=i,username=row['USUARIO'],password=row['SENHA'],port=row['PORTA']):
                 break
            
    # mikrotik backup       
    data_mk = pd.read_csv(mk_hosts)
    mk = mikrotik(backup_directory=backup)
    data_mk = data_mk.drop_duplicates()
    usuarios.drop_duplicates()
    for i in data_mk.get('IP'):
        for  index, row in usuarios.iterrows():
            if mk.host_connect(ip=i,user=row['USUARIO'],password=row['SENHA'],port=row['PORTA']):
                 break
            
if __name__ == '__main__':
    iterator()