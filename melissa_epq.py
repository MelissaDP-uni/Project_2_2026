# This script calculates the Economic Production Quantity (EPQ) for a product
# made in-house, along with production runs per year and maximum inventory level.

import math


def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))


# Inputs
annual_demand = 12000          # units per year
setup_cost = 50                # cost per production run, in Rand
holding_cost = 2                # cost per unit per year, in Rand
daily_demand_rate = 40          # units sold per day
daily_production_rate = 100     # units your process can make per day

# Core calculation
epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                     daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

# --- Try It Yourself ---
# TODO 1: Change daily_production_rate to 150 and re-run. Does EPQ go up or down? Why?
# TODO 2: Set daily_production_rate to 100000 and compare EPQ to plain EOQ
#         (sqrt(2*D*S/H)) with the same D, S, H. Explain why they're nearly identical.
