# Utility-Based Smart Home Energy Management Agent 🏡⚡

An intelligent multi-agent system and simulation framework deployed on **Vercel** that schedules household appliances (Washing Machines, Water Heaters, EV Chargers) to minimize electricity costs and peak grid loads while guaranteeing occupant comfort and honoring deadline constraints.

---

## 🚀 One-Click Vercel Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/smart-home-energy-agent)

---

## 📂 Project Structure

```text
smart-home-energy-agent/
│
├── backend/                  # Python FastAPI & Agent Optimization
│   ├── __init__.py
│   ├── agent.py              # Utility optimization logic & API endpoints
│   ├── environment.py        # Smart home tariffs & solar PV forecasting
│   └── appliances.py         # Device models (Washing Machine, Water Heater, EV)
│
├── frontend/                 # Interactive Web Dashboard
│   ├── index.html            # Main UI & 24-hour simulation dashboard
│   ├── style.css             # Tailwind CSS & custom styling
│   └── app.js                # Chart.js visualizations & weight controls
│
├── vercel.json               # Vercel routing and build configuration
└── package.json              # Node/Python dependency manifest
```
