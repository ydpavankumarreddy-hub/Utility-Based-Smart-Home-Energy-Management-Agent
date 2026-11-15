"""
Environment Module: Time-varying tariffs and solar PV generation.
"""

class Environment:
    def __init__(self):
        self.tariffs = [
            0.10, 0.10, 0.09, 0.09, 0.10, 0.12,
            0.15, 0.22, 0.25, 0.20, 0.15, 0.12,
            0.10, 0.10, 0.12, 0.14, 0.18, 0.28,
            0.35, 0.38, 0.32, 0.24, 0.18, 0.12
        ]
        self.solar_forecast = [
            0.0, 0.0, 0.0, 0.0, 0.0, 0.1,
            0.4, 1.2, 2.5, 4.0, 5.5, 6.8,
            7.2, 6.9, 5.8, 4.2, 2.3, 0.8,
            0.1, 0.0, 0.0, 0.0, 0.0, 0.0
        ]

    def get_tariff(self, hour):
        return self.tariffs[hour % 24]

    def get_solar(self, hour):
        return self.solar_forecast[hour % 24]
