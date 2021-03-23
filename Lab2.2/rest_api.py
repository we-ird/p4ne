import glob
import re
from ipaddress import IPv4Network
import json

from flask import Flask

def parse_val(val):
    ipRegex = r'((\d){1,3}\.){3}(\d){1,3}\/(\d){1,3}' #подглядел в гугле
  #  ipRegex = r'((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})'

    ip = re.search(ipRegex, val)
    if ip:
        return{'ip': IPv4Network(tuple(ip.group().split('/')), strict=False)}
    elif val.find('interface ') != -1 and val.split('interface ')[1].strip() != 'resets':
        return({'int':val.split('interface ')[1].strip()})
    elif val.find('hostname') != -1 and not val.split('hostname')[1].strip().startswith(')'):
        return ({'host': val.split('hostname')[1].strip()})
    return {}

def create_host_ip_list():
    hosts_list = []
    host_ip_list = []
    host = {'name': None, 'ip': []}
    for name in glob.glob("../config_files/*.txt"):
        with open(name) as f:
            for line in f:
                result = parse_val(line)
                if result and result.get('host') and result['host'] not in hosts_list:
                    if host['name']:
                        host_ip_list.append(host)
                        host = {'name': None, 'ip': []}
                    hosts_list.append(result['host'])
                    host = {'name': result['host'], 'ip': []}
                elif result and result.get('ip'):
                    host['ip'].append(str(result['ip']))
    host_ip_list.append(host)
    return(host_ip_list)


#a = create_host_ip_list()

#print(a)
#print(list(filter(lambda x: x['name'] == 'cod-oldserv-cat3750', host_lists)))


app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return """
    Справка: <br>
    При обращении по “/configs” — выдаёт сведения об именах всех хостов, для которых есть кофигурационные файлы <br>
    При обращении по “/config/hostname” выдает сведения о всех IP-адресах этого хоста
    """
@app.route('/configs')
def configs():
    hostnames = [d['name'] for d in hosts_lists]
    return(
        json.dumps(hostnames)
    )

@app.route('/configs/<hostname>')
def hostname_ip(hostname):
    host = [d for d in hosts_lists if hostname == d['name']]
    if len(host) > 0:
        return("IP's of " + hostname + ":<br>" + json.dumps(host[0]['ip']))
    else:
        return("device "+hostname+" does not exists")

#print(create_host_ip_list())

if __name__ == '__main__':
    hosts_lists = create_host_ip_list()
    app.run(debug=True)