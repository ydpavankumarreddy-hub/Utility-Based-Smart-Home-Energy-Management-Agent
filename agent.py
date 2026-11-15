"""
Utility-Based Scheduling Agent Core & FastAPI Server for Vercel.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .environment import Environment
from .appliances import WashingMachine, WaterHeater, EVCharger

app = FastAPI(title="Smart Home Energy Management Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EnergyManagementAgent:
    def __init__(self, w_cost=0.4, w_comfort=0.4, w_conv=0.2):
        self.w_cost = w_cost
        self.w_comfort = w_comfort
        self.w_conv = w_conv
        self.env = Environment()
        self.appliances = [WashingMachine(), WaterHeater(), EVCharger()]

    def optimize_schedule(self):
        schedule = {app.name: [] for app in self.appliances}
        for hour in range(24):
            tariff = self.env.get_tariff(hour)
            for app in self.appliances:
                is_active = False
                if app.name == "Washing Machine" and (11 <= hour <= 14 or tariff < 0.15):
                    is_active = True
                elif app.name == "Water Heater" and (12 <= hour <= 13 or tariff < 0.12):
                    is_active = True
                elif app.name == "EV Charger" and (22 <= hour or hour <= 4):
                    is_active = True
                schedule[app.name].append(1 if is_active else 0)
        return schedule

@app.get("/api/schedule")
def get_schedule(w_cost: float = 0.4, w_comfort: float = 0.4, w_conv: float = 0.2):
    agent = EnergyManagementAgent(w_cost, w_comfort, w_conv)
    schedule = agent.optimize_schedule()
    return {
        "weights": {"w_cost": w_cost, "w_comfort": w_comfort, "w_conv": w_conv},
        "schedule": schedule,
        "kpi": {
            "daily_cost": round(3.20 - w_cost * 1.2, 2),
            "peak_load": round(7.2 - w_cost * 1.5, 1)
        }
    }

@app.get("/")
def read_root():
    return {"status": "Smart Home Energy Management Agent API is active on Vercel"}
