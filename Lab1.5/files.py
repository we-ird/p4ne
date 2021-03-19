import glob

ipList = []

for name in glob.glob("./config_files/*.txt"):
    with open(name) as f:
        for line in f:
            if line.find('IP address') > 0:
                ip = line.split(":")[1].strip()
                if ip not in ipList:
                    ipList.append(ip)

print(ipList)
