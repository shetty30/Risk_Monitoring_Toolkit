# 📊 Risk Management Toolkit

This repository contains three risk monitoring projects implemented in Python using Pandas and SQLite:

1. **FX Risk Monitoring Tool** – Tracks foreign currency exposures and calculates USD-equivalent positions.
2. **Liquidity Risk Dashboard** – Aggregates cash inflows/outflows, computes liquidity metrics, and visualizes results.
3. **Interest Rate Risk Analyzer** – Estimates portfolio duration, reprices instruments under rate shocks, and calculates P&L impact.

---

## 🛠️ Tech Stack
- Python (Pandas, SQLite3, NumPy)
- Jupyter Notebook
- Matplotlib (visualization)
- (Optional) Requests (for live FX rates)

---
## 💱 FX Risk Monitoring Tool
- Stores FX rates (mock or from API) in SQLite
- Stores currency exposures
- Performs SQL `JOIN` to compute USD-equivalent exposures
- Adds simple scenario analysis (e.g. 1% FX move impact)

| Currency | Exposure   | Rate | Exposure_USD | P&L_If_1pct_Move |
|---------|------------|------|-------------|----------------|
| EUR     | 100,000    | 1.08 | 108,000     | 1,080          |
| INR     | 5,000,000  | 0.012| 60,000      | 600            |

---

## 💧 Liquidity Risk Dashboard
- Reads daily cash inflows/outflows
- Aggregates positions by day/week/month
- Calculates:
  - Liquidity Coverage Ratio (LCR)
  - Net Stable Funding Ratio (NSFR)
  - Cumulative maturity gaps
- Visualizes daily cash flows and cumulative positions using Matplotlib

---

## 📈 Interest Rate Risk Analyzer
- Loads mock fixed-income portfolio (bonds, deposits)
- Calculates:
  - Weighted Average Maturity (WAM)
  - Duration & Modified Duration
- Reprices instruments under parallel rate shocks (e.g. +100bps)
- Calculates portfolio P&L impact and sensitivity table

---

## 📦 Installation
```bash
git clone https://github.com/yourusername/risk_management_toolkit.git
cd risk_management_toolkit
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
jupyter notebook

