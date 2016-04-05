from pyzabbix import ZabbixAPI

# pip install py-zabbix
# pip install openpyxl

import openpyxl

wb = openpyxl.load_workbook('hosts.xlsx')
sheet = wb.get_sheet_by_name('HostList')

for row in range(2,100):
        print sheet['A' + str(row)].value


#zapi = ZabbixAPI(url='http://monit.mainroute.com.br/',user='zabbix.api',password='zabbix.api')
#result = zapi.host.get(status=1)
#zapi.host.create(
#{"host": "Linux server",
        #"interfaces": [
#            {
#                "type": 1,
#                "main": 1,
#                "useip": 1,
                #"ip": "192.168.3.1",
                #"dns": "",
#                "port": "10050"
#            }
#        ],
#        "groups": [
#            {
#                "groupid": "33"
#            }
#        ],
#        "templates": [
#            {
#                "templateid": "10001"
#            }
#            ]
#})
