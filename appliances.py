"""
Appliance Models for Smart Home Energy Management Agent.
"""

class Appliance:
    def __init__(self, name, power_kw, duration_hours, priority=1.0):
        self.name = name
        self.power_kw = power_kw
        self.duration_hours = duration_hours
        self.priority = priority

class WashingMachine(Appliance):
    def __init__(self):
        super().__init__(name="Washing Machine", power_kw=2.1, duration_hours=2, priority=0.8)

class WaterHeater(Appliance):
    def __init__(self):
        super().__init__(name="Water Heater", power_kw=3.5, duration_hours=1.5, priority=0.95)

class EVCharger(Appliance):
    def __init__(self):
        super().__init__(name="EV Charger", power_kw=7.2, duration_hours=4, priority=0.9)
