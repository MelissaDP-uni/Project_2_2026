# This program works out the best batch size to produce at once when making
# your own stock, and shows how many production runs you'd need per year.

import math


def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))



annual_demand = 12000          
setup_cost = 50                
holding_cost = 2                
daily_demand_rate = 40          
daily_production_rate = 100     


epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                     daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))


