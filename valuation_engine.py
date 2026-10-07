import numpy as np
import pandas as pd

class CorporateValuationEngine:
    """
    Advanced FP&A Automation Engine for Tech/SaaS Corporate Valuation.
    Computes dynamic WACC, Free Cash Flow to Firm (FCFF) projections, 
    and DCF Terminal Value under multiple macro scenarios.
    """
    def __init__(self, company_name: str, current_arr: float, ebitda_margin: float, capex_intensity: float):
        self.company_name = company_name
        self.current_arr = current_arr
        self.ebitda_margin = ebitda_margin
        self.capex_intensity = capex_intensity
        
    def calculate_wacc(self, cost_of_equity: float, cost_of_debt: float, tax_rate: float, debt_ratio: float) -> float:
        """Computes the Weighted Average Cost of Capital (WACC) using CAPM frameworks."""
        equity_ratio = 1.0 - debt_ratio
        after_tax_debt = cost_of_debt * (1.0 - tax_rate)
        wacc = (equity_ratio * cost_of_equity) + (debt_ratio * after_tax_debt)
        return wacc

    def run_scenario(self, growth_rate: float, years: int = 5) -> pd.DataFrame:
        """Generates dynamic FCFF projections based on strategic operational inputs."""
        years_list = [f"Year {i+1}" for i in range(years)]
        revenue_proj = []
        ebitda_proj = []
        fcff_proj = []
        
        current_rev = self.current_arr
        for _ in range(years):
            current_rev *= (1.0 + growth_rate)
            ebitda = current_rev * self.ebitda_margin
            capex = current_rev * self.capex_intensity
            # Standard FCFF Approximation: EBITDA - CAPEX (Assuming Net Working Capital changes net out for tech profiles)
            fcff = ebitda - capex
            
            revenue_proj.append(round(current_rev, 2))
            ebitda_proj.append(round(ebitda, 2))
            fcff_proj.append(round(fcff, 2))
            
        df = pd.DataFrame({
            'Revenue (ARR)': revenue_proj,
            'EBITDA': ebitda_proj,
            'FCFF': fcff_proj
        }, index=years_list)
        return df

    def perform_dcf(self, fcff_df: pd.DataFrame, wacc: float, terminal_growth: float) -> dict:
        """Executes Enterprise Valuation via Discounted Cash Flows (DCF) and Terminal Value."""
        discount_factors = [(1.0 + wacc) ** (i + 1) for i in range(len(fcff_df))]
        pv_of_fcff = fcff_df['FCFF'].values / discount_factors
        sum_pv_fcff = np.sum(pv_of_fcff)
        
        # Terminal Value via Gordon Growth Model
        final_fcff = fcff_df['FCFF'].iloc[-1]
        terminal_value = (final_fcff * (1.0 + terminal_growth)) / (wacc - terminal_growth)
        pv_terminal_value = terminal_value / discount_factors[-1]
        
        enterprise_value = sum_pv_fcff + pv_terminal_value
        
        return {
            "PV of Explicit Flows": round(sum_pv_fcff, 2),
            "PV of Terminal Value": round(pv_terminal_value, 2),
            "Enterprise Value": round(enterprise_value, 2)
        }

# Execution Block for Senior FP&A Demo Validation
if __name__ == "__main__":
    print(f"=== Initializing Valuation Engine for Tech Corp ===")
    # Inputs: $50M ARR, 25% EBITDA Margin, 5% CAPEX Intensity
    saas_firm = CorporateValuationEngine("CloudScale Tech", 50000000, 0.25, 0.05)
    
    # Capital Structure & Cost assumptions
    wacc_computed = saas_firm.calculate_wacc(cost_of_equity=0.11, cost_of_debt=0.06, tax_rate=0.25, debt_ratio=0.20)
    print(f"Calculated Corporate WACC: {wacc_computed * 100:.2f}%")
    
    # Scenario: High Growth Base Case (20% Revenue growth YoY)
    projections = saas_firm.run_scenario(growth_rate=0.20, years=5)
    print("\n--- 5-Year Financial & FCFF Projections ---")
    print(projections)
    
    # Valuation Results
    valuation = saas_firm.perform_dcf(projections, wacc=wacc_computed, terminal_growth=0.03)
    print("\n--- Valuation Summary Outputs ---")
    for metric, val in valuation.items():
        print(f"{metric}: ${val:,.2f}")
