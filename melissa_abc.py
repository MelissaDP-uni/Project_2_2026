# This script performs ABC inventory classification: it ranks SKUs by their
# annual usage value and assigns each one to Tier A, B, or C based on its
# cumulative contribution to total inventory value.

skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
]


def usage_value(demand, cost):
    return demand * cost


def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"


def classify_inventory(items):
    """Takes a list of SKU dicts (with demand & cost) and returns them
    sorted by value, with cum_pct and tier added to each."""
    for item in items:
        item["value"] = usage_value(item["demand"], item["cost"])

    items_sorted = sorted(items, key=lambda item: item["value"], reverse=True)

    total_value = sum(item["value"] for item in items_sorted)
    running_total = 0
    for item in items_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100
        item["tier"] = assign_tier(item["cum_pct"])

    return items_sorted


if __name__ == "__main__":
    classified = classify_inventory(skus)

    for item in classified:
        print(item["sku"], "| value:", item["value"],
              "| cum %:", round(item["cum_pct"], 1),
              "| tier:", item["tier"])

    tier_counts = {"A": 0, "B": 0, "C": 0}
    for item in classified:
        tier_counts[item["tier"]] += 1
    print(tier_counts)

# --- Try It Yourself ---
# TODO 1: Add two more SKUs of your own to the 'skus' list above. Re-run and
#         see if the tier split changes much.
# TODO 2: Try changing the assign_tier thresholds to 70 / 90 instead of 80 / 95.
