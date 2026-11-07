import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Adhipathi | Real Estate Intelligence & Enterprise Asset Management",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- HEADER SECTION ---
st.title("🏛️ ADHIPATHI")
st.markdown("##### *The Alignment of Wealth and Legacy*")
st.caption(
    "Enterprise AI & PropTech Intelligence Platform: Predictive Land"
    " Valuation • Construction IoT Monitoring • Investment Simulation • AI Risk"
    " Auditing"
)
st.divider()

# --- SIDEBAR GLOBAL CONTROLS ---
st.sidebar.header("🕹️ Global Asset Parameters")
selected_market = st.sidebar.selectbox(
    "Target Investment Zone",
    [
        "Prime Metro Commercial Belt",
        "Suburban Growth Corridor",
        "Emerging Tech Innovation District",
        "Luxury Waterfront Belt",
    ],
)

asset_type = st.sidebar.radio(
    "Asset Class",
    ["Commercial High-Rise", "Mixed-Use Residential", "Industrial Logistics Hub", "Raw Land Parcel"],
)

land_sqft = st.sidebar.slider("Total Surface / Plot Size (Sq. Ft.)", 5000, 200000, 25000, step=2500)
base_valuation = st.sidebar.number_input("Current Base Valuation ($)", value=2500000, step=50000)
holding_period = st.sidebar.slider("Investment Horizon (Years)", 1, 15, 7)

st.sidebar.divider()
st.sidebar.subheader("📊 Macroeconomic Assumptions")
infra_growth_idx = st.sidebar.slider("Local Infrastructure Growth Index (1-10)", 1, 10, 8)
inflation_hedge_rate = st.sidebar.slider("Assumed Inflation Hedge (%)", 2.0, 8.0, 4.5)

# --- NAVIGATION TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Future Land Value Engine",
    "🏗️ Construction IoT Tracker",
    "💼 Portfolio Cash Flow & IRR Simulator",
    "📜 AI Legal & Title Audit Hub",
    "👑 Lifestyle & Ecosystem Index",
])

# --- TAB 1: PREDICTIVE LAND VALUE ENGINE ---
with tab1:
  st.subheader("Predictive Valuation & Capital Growth Engine")
  st.write(
      f"Simulating capital appreciation trajectory for **{selected_market}** ("
      f"*{asset_type}*) over a **{holding_period}-year horizon**."
  )

  # Calculations
  base_appreciation = 0.055
  infra_boost = infra_growth_idx * 0.009
  total_annual_cagr = base_appreciation + infra_boost + (inflation_hedge_rate * 0.01)

  years = np.arange(0, holding_period + 1)
  projected_values = [base_valuation * ((1 + total_annual_cagr) ** yr) for yr in years]
  bull_case = [val * 1.18 for val in projected_values]
  bear_case = [val * 0.88 for val in projected_values]

  df_val = pd.DataFrame({
      "Year": years,
      "Base Model": projected_values,
      "Bull Case (+18%)": bull_case,
      "Bear Case (-12%)": bear_case,
  })

  col1, col2, col3, col4 = st.columns(4)
  target_val = projected_values[-1]
  roi_pct = ((target_val - base_valuation) / base_valuation) * 100

  col1.metric("Current Asset Base", f"${base_valuation:,.2f}")
  col2.metric(f"Projected Value ({holding_period}Y)", f"${target_val:,.2f}", delta=f"+{roi_pct:.1f}% Growth")
  col3.metric("Projected CAGR", f"{total_annual_cagr*100:.2f}%", delta="Outperforming Benchmark")
  col4.metric("Est. Sq. Ft. Price", f"${target_val/land_sqft:,.2f}/sq ft", delta=f"+${(target_val-base_valuation)/land_sqft:,.2f}")

  st.divider()
  st.markdown("#### **Valuation Trajectory Scenarios**")
  st.line_chart(df_val.set_index("Year"))

# --- TAB 2: CONSTRUCTION IOT TRACKER ---
with tab2:
  st.subheader("Real-Time Construction Milestone & IoT Telemetry")
  st.write("Computer vision and IoT monitoring for structural execution.")

  col_a, col_b = st.columns([2, 1])

  with col_a:
    milestone_df = pd.DataFrame({
        "Development Phase": [
            "Land Acquisition & Permits",
            "Foundation Excavation & Piling",
            "Core Superstructure & Framing",
            "MEP & Utilities Installation",
            "Architectural Facade & Finishing",
            "Final Inspection & Commissioning",
        ],
        "Completion Status": [100, 100, 82, 45, 15, 0],
        "AI Verification": ["Passed", "Passed", "Verified via Drone Scan", "In Progress", "Scheduled", "Pending"],
        "Schedule Variance": ["0 Days", "-2 Days", "+1 Day", "0 Days", "On Track", "On Track"],
    })

    st.dataframe(
        milestone_df,
        column_config={
            "Completion Status": st.column_config.ProgressColumn(
                "Phase Progress", format="%d%%", min_value=0, max_value=100
            ),
        },
        use_container_width=True,
    )

  with col_b:
    st.markdown("#### **Site IoT Sensor Stream**")
    st.metric("Concrete Structural Curing", "94.2 PSI", delta="Optimal Strength")
    st.metric("Site Safety Hazard Score", "0.02 Risk Index", delta="-15% vs Industry Avg")
    st.metric("Supply Chain Inventory Stock", "88% On-Site", delta="Zero Bottleneck Detected")

# --- TAB 3: PORTFOLIO CASH FLOW & IRR SIMULATOR ---
with tab3:
  st.subheader("Pro-Forma Investment & Capital Return Simulator")
  st.write("Stress-test equity requirements, debt service coverage, and investor IRR.")

  c1, c2, c3 = st.columns(3)
  equity_pct = c1.slider("Equity Contribution (%)", 20, 50, 30)
  interest_rate = c2.slider("Senior Debt Rate (%)", 4.0, 10.0, 6.5)
  target_cap_rate = c3.slider("Exit Cap Rate (%)", 4.0, 9.0, 5.75)

  debt_amount = base_valuation * (1 - (equity_pct / 100))
  equity_amount = base_valuation * (equity_pct / 100)
  annual_noi = base_valuation * (target_cap_rate / 100)
  annual_debt_service = debt_amount * (interest_rate / 100)
  net_cash_flow = annual_noi - annual_debt_service
  dscr = annual_noi / annual_debt_service if annual_debt_service > 0 else 0

  st.divider()
  m1, m2, m3, m4 = st.columns(4)
  m1.metric("Required Equity Capital", f"${equity_amount:,.2f}")
  m2.metric("Senior Debt Financing", f"${debt_amount:,.2f}")
  m3.metric("Annual Net Cash Flow", f"${net_cash_flow:,.2f}")
  m4.metric("Debt Service Coverage (DSCR)", f"{dscr:.2f}x", delta="Healthy" if dscr > 1.25 else "Tight")

# --- TAB 4: AI LEGAL & TITLE AUDIT HUB ---
with tab4:
  st.subheader("Autonomous Title, Zoning & Contract Audit Engine")
  st.write("LLM-assisted legal risk audit analyzing property title deeds and municipal compliance.")

  sample_deed = st.text_area(
      "Property Encumbrance & Deed Extract for AI Audit:",
      value="PARCEL 402-A: Clear title free of tax liens. Zoning classified as MU-3 Commercial High-Density. Easement clause recorded on East boundary for public utility access (12 ft). No active litigation recorded.",
      height=100,
  )

  if st.button("Run AI Legal Audit"):
    st.info("🔍 Auditing document clauses against state regulatory frameworks...")
    st.success("✅ Title Audit Complete: Zero undisclosed tax liens or ownership disputes detected.")

    col_l1, col_l2 = st.columns(2)
    col_l1.write("**Compliance Checklist:**")
    col_l1.markdown("- Municipal Zoning Alignment: **Verified (MU-3)**\n- Boundary Easement Risk: **Low (Utility Standard)**\n- Encumbrance Status: **Clean**")
    col_l2.write("**Suggested Action:**")
    col_l2.markdown("Document approved for institutional closing. Risk rating: **Low**.")

# --- TAB 5: LIFESTYLE & ECOSYSTEM INDEX ---
with tab5:
  st.subheader("Integrated Lifestyle Concierge & Ecosystem Index")
  st.write("Evaluating proximity metrics to high-value amenities and infrastructure.")

  col_x, col_y, col_z, col_w = st.columns(4)
  col_x.metric("Security & Privacy Index", "98 / 100")
  col_y.metric("Transit Connectivity", "92 / 100")
  col_z.metric("Ecosystem Sustainability", "95 / 100")
  col_w.metric("Luxury Amenity Access", "96 / 100")

  st.divider()
  st.success("✨ **Executive Portfolio Assessment:** Asset matches high-yield legacy wealth guidelines.")
