import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Set up reproducibility and timeline (90 days)
np.random.seed(42)
random.seed(42)
start_date = datetime(2026, 3, 1)
date_list = [start_date + timedelta(days=x) for x in range(90)]

shifts = ['Shift A', 'Shift B', 'Shift C']
product_lines = ['Feeder Busduct', 'Plug-in Busduct']
amperages = ['800A', '1600A', '2500A', '4000A']
materials = ['Copper', 'Aluminum']

prod_rows = []
down_rows = []

# Station options for root cause analysis
stations_reasons = {
    'CNC Bending': ['Hydraulic Leak', 'Die Wear out', 'Sheet Metal Jam'],
    'Insulation Line': ['Insulation Thickness Defect', 'Oven Temperature Drop', 'Epoxy Fluid Clog'],
    'Enclosure Assembly': ['Welding Machine Calibration', 'Pneumatic Riveter Jam', 'Material Stockout (Screws)'],
    'Testing Rig': ['Dielectric Test Failure', 'Software System Crash', 'Safety Interlock Trip']
}

# 2. Programmatically generate the log entries
for dt in date_list:
    date_str = dt.strftime('%Y-%m-%d')
    for shift in shifts:
        for p_line in product_lines:
            amp = random.choice(amperages)
            mat = random.choice(materials)
            planned_time = 420  # 480 mins minus 60 mins scheduled breaks

            # Injecting hidden data trends for portfolio storytelling
            if shift == 'Shift B' and p_line == 'Feeder Busduct':
                down_time = random.randint(60, 150)
                scrap_pct = random.uniform(0.07, 0.14)
                perf_modifier = random.uniform(0.72, 0.84)
            else:
                down_time = random.randint(10, 45) if random.random() > 0.4 else 0
                scrap_pct = random.uniform(0.01, 0.03)
                perf_modifier = random.uniform(0.90, 0.98)

            actual_run = max(0, planned_time - down_time)
            base_rate = 0.50 if p_line == 'Feeder Busduct' else 0.70

            target_meters = int(planned_time * base_rate)
            total_produced = int(actual_run * base_rate * perf_modifier)

            if total_produced > target_meters: total_produced = target_meters

            scrap_meters = int(total_produced * scrap_pct)
            good_meters = max(0, total_produced - scrap_meters)

            prod_rows.append([
                date_str, shift, p_line, amp, mat,
                planned_time, actual_run, target_meters,
                total_produced, good_meters, scrap_meters
            ])

            # Populate downtime logs based on production drops
            if down_time > 0:
                station = random.choice(list(stations_reasons.keys()))
                reason = random.choice(stations_reasons[station])

                if shift == 'Shift B' and p_line == 'Feeder Busduct' and random.random() > 0.3:
                    station = 'Insulation Line'
                    reason = 'Insulation Thickness Defect'

                down_rows.append([date_str, shift, station, down_time, reason])

# 3. Save directly to Excel files
df_production = pd.DataFrame(prod_rows, columns=[
    'Date', 'Shift', 'Product_Line', 'Amperage_Rating', 'Conductor_Material',
    'Planned_Time_Min', 'Actual_Run_Time', 'Target_Meters',
    'Total_Meters_Produced', 'Good_Meters', 'Scrap_Meters'
])

df_downtime = pd.DataFrame(down_rows, columns=[
    'Date', 'Shift', 'Machine_Station', 'Downtime_Minutes', 'Downtime_Reason'
])

with pd.ExcelWriter('Busduct_Factory_OEE_Data.xlsx') as writer:
    df_production.to_excel(writer, sheet_name='Production_Log', index=False)
    df_downtime.to_excel(writer, sheet_name='Downtime_Details', index=False)

print("Success! Your high-quality Excel data file 'Busduct_Factory_OEE_Data.xlsx' has been created.")
