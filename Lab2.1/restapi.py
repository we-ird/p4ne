import requests
from pprint import pprint


#https://172.19.153.222/api/v1/auth/token-services -H "Accept:application/json" -u "cisco:cisco" -d "" --insecure -3

ip = '10.31.70.210'
auth_url = 'https://' + ip + ':55443/api/v1/auth/token-services'
int_url = 'https://' + ip + ':55443/api/v1/interfaces'
auth = ('restapi', 'j0sg1280-7@')

r = requests.post(auth_url, auth=auth, verify=False)
if r.status_code == 200:
    token = r.json()['token-id']
    headers = {"content-type": "application/json", "X-Auth-Token": token}
    r = requests.get(int_url, headers=headers, verify=False)

    ints = r.json()['items']
    filtered = []

    for iface in ints:
        if iface.get('if-name', None):
            intStat = requests.get(int_url+'/' + iface.get('if-name', None) + '/statistics', headers=headers, verify=False)
            intsStatJson = intStat.json()
            filtered.append({'int': iface.get('if-name', None), 'packets_out': intsStatJson['out-total-packets'], 'packets_in': intsStatJson['in-total-packets']})

    pprint(filtered)

    #filtered = [{'interface': a.get('if-name', None), 'ip': a.get('ip-address', None)} for a in ints]

    #pprint(filtered)




