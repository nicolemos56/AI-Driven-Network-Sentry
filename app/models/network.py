import os
from pyzabbix import ZabbixAPI
from pydantic import BaseModel

class AccessPoint(BaseModel):
    id: str
    name: str
    ip: str
    zabbix_status: str
    portal_status: str
    cpu_load: str

class NetworkModel:
    def __init__(self):
        self.zapi = ZabbixAPI("http://192.168.0.82")
        try:
            self.zapi.login("Admin", "zabbix")
            print("[MODEL] Zabbix Online")
        except:
            self.zapi = None

    def get_telemetry(self):
        """Retorna status real do Zabbix filtrando ruídos"""
        if not self.zapi: return "DOWN", "0%", 0.0
        try:
            # HostID do MikroTik: 10683
            ping = self.zapi.item.get(hostids='10683', search={"name": "ICMP ping"}, output=["lastvalue"])[0]
            cpu = self.zapi.item.get(hostids='10683', search={"name": "#1: CPU utilization"}, output=["lastvalue"])[0]
            traff = self.zapi.item.get(itemids='50829', output=["lastvalue"])[0]
            
            status = "UP" if ping['lastvalue'] == "1" else "DOWN"
            if status == "DOWN": return "DOWN", "0.0% (OFF)", 0.0
            return "UP", f"{float(cpu['lastvalue']):.1f}%", float(traff['lastvalue'])
        except:
            return "DOWN", "0%", 0.0