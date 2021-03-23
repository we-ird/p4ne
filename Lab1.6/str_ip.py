import glob
import re
from ipaddress import IPv4Network

def parse_val(val):
    ipRegex = r'((\d){1,3}\.){3}(\d){1,3}\/(\d){1,3}' #подглядел в гугле
  #  ipRegex = r'((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})'

    ip = re.search(ipRegex, val)
    if ip:
        return{'ip': IPv4Network(tuple(ip.group().split('/')), strict=False)}
    elif val.find('interface ') != -1 and val.split('interface ')[1].strip() != 'resets':
        return({'int':val.split('interface ')[1].strip()})
    elif val.find('hostname') != -1:
        return ({'host': val.split('hostname')[1].strip()})
    return {}

for name in glob.glob("../config_files/*.txt"):
    with open(name) as f:
        for line in f:
            result = parse_val(line)
            if result:print(result)

