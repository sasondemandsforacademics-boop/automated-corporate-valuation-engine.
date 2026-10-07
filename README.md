# Corporate Valuation & FP&A Automation Engine

## 📊 Executive Summary
This repository implements an end-to-end financial intelligence pipeline designed to bridge advanced FP&A forecasting with robust data programming. Built using Python and scalable architecture principles, it automates core corporate valuation workflows—specifically **Weighted Average Cost of Capital (WACC)** computation via CAPM and multi-year **Discounted Cash Flow (DCF)** modeling—to deliver quantitative inputs for M&A, CAPEX allocation, and strategic corporate planning.

## 🛠️ Key Features
- **Dynamic WACC Calculation:** Automates capital structure analysis integrating cost of equity (CAPM), after-tax cost of debt, and financial leverage ratios.
- **Object-Oriented Projections:** Leverages Object-Oriented Programming (OOP) to generate multi-year financial statements and Free Cash Flow to Firm (FCFF) models.
- **Scenario & Stress-Testing Framework:** Built-in capabilities to execute sensitivity analysis across varying revenue growth paths, EBITDA margins, and macroeconomic assumptions.
- **Terminal Value Modeling:** Implements the Gordon Growth Model to derive enterprise values with dynamic terminal growth configurations.

## 💻 Tech Stack & Competencies Demonstrated
- **Programming Languages:** Python (NumPy, Pandas).
- **Core Financial Frameworks:** Corporate Valuation, FP&A Forecasting, Capital Structure Optimization, Scenario Analysis.
- **Architecture Principles:** Object-Oriented Programming (OOP), Data Literacy, and Automation workflows.

## 🚀 Execution & Sample Output
The core engine `valuation_engine.py` validates a baseline Tech/SaaS corporate structure (\$50M ARR, 25% EBITDA Margin) against a target WACC and computes explicit discounted cash flows over a 5-year projection horizon.
