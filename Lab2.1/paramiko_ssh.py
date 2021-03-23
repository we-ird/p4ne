import paramiko
import time
from pprint import pprint

BUF_SIZE = 20000
TIMEOUT = 1
host_ip = '10.31.70.209'
login = 'restapi'
password = 'j0sg1280-7@'

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connection.connect(host_ip, username=login, password=password, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
session.send("show ip interface brief  \n")
time.sleep(TIMEOUT)
ints = session.recv(BUF_SIZE)

time.sleep(TIMEOUT)

session.close()

pprint(ints.decode().strip())


