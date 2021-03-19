import glob

ipList = []

for name in glob.glob("./config_files/*.txt"):
    with open(name) as f:
        for line in f:
            if line.find('ip address ') != -1:
                ip = line.split("address")[1].strip()
                try:
                    int(ip[0])
                    if ip not in ipList:
                        ipList.append(ip)
                except:
                    pass
print(ipList)
print(len(ipList))
