from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.network import NetworkModel
from app.controllers.ai_engine import AIAgent
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Instâncias
net_model = NetworkModel()
agent = AIAgent()

# --- ESTADOS GLOBAIS DE SIMULAÇÃO (DEFINIDOS AQUI PARA EVITAR NAMEERROR) ---
sim_portal_down = False
sim_apn_down = False
sim_unknown = False

@app.get("/aps")
async def get_aps():
    net_status, cpu, _ = net_model.get_telemetry()
    
    # Lógica de prioridade de status
    final_net = "DOWN" if (sim_apn_down or net_status == "DOWN") else "UP"
    final_portal = "DOWN" if (sim_portal_down or sim_unknown or final_net == "DOWN") else "OK"
    
    return [{
        "id": "2", "name": "MikroTik-AP-Virtual", "ip": "192.168.0.103",
        "zabbix_status": final_net,
        "portal_status": final_portal,
        "cpu_load": cpu
    }]

@app.get("/agent/decision")
async def agent_decision():
    net_status, cpu, traffic = net_model.get_telemetry()
    
    telemetry = {
        "network": "DOWN" if (sim_apn_down or net_status == "DOWN") else "UP",
        "portal": "DOWN" if (sim_portal_down or sim_unknown) else "OK",
        "cpu": cpu,
        "traffic_kbps": round(traffic/1000, 2),
        "unknown": sim_unknown
    }
    
    return await agent.analyze_and_decide(telemetry)

@app.get("/network-stats/2")
async def stats():
    _, _, t = net_model.get_telemetry()
    # Retorna dado real para o gráfico
    return {"data": [round(t/1000, 2) for _ in range(20)]}

@app.post("/simulate/{type}")
async def simulate(type: str):
    global sim_portal_down, sim_apn_down, sim_unknown
    if type == "portal": sim_portal_down = True
    elif type == "apn": sim_apn_down = True
    elif type == "unknown": sim_unknown = True
    return {"status": "injected"}

@app.post("/action/execute/{id}")
async def execute(id: str):
    global sim_portal_down, sim_apn_down, sim_unknown
    sim_portal_down = False
    sim_apn_down = False
    sim_unknown = False
    return {"message": "Sucesso"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)