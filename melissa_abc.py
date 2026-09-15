# This program sorts a list of products by how much value they contribute
# overall, and groups them into A, B, or C categories based on that.

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


