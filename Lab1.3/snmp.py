from pysnmp.hlapi import *

snmp_object_mib_name = ObjectIdentity('SNMPv2-MIB','sysDescr',0)

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmp_object_mib_name)
                )




for errorIndication, errorStatus, errorIndex, varBinds in result:
    for message in varBinds:
        print(message)
