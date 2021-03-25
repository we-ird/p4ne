import requests
from flask import render_template,jsonify
import json
from flask import Flask

def get_ticket():

    headers = {"content-type": "application/json"}
    body = {"username": "devnetuser", "password": "Cisco123!"}
    token_url = "https://sandboxapic.cisco.com/api/v1/ticket"
    ticket = None
    r = requests.post(token_url, headers=headers, data=json.dumps(body), verify=False)
    if r.status_code == 200:
        ticket = r.json()['response']['serviceTicket']
    return ticket

def get_topology(token):
    if token:
        topology_url = 'https://sandboxapicem.cisco.com/api/v1/topology/physical-topology'
        topology_headers = {"content-type": "application/json","X-Auth-Token": token}

        r = requests.get(topology_url, headers=topology_headers)
        return(r.json()['response'])
    else:
        return ("No token provided")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("topology.html")

@app.route('/api/topology')
def topology():
    return(jsonify(topology))

if __name__ == '__main__':
    topology = get_topology(get_ticket())
    app.run(debug=True)