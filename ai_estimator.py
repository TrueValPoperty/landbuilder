def estimate_units(area_m2):
    usable_area = area_m2 * 0.7
    unit_size = 90  # m2 average
    price_per_m2 = 3200
    build_cost_per_m2 = 2000

    units = int(usable_area / unit_size)
    gdv = units * unit_size * price_per_m2
    build_cost = units * unit_size * build_cost_per_m2
    profit = gdv - build_cost

    return {
        "land_area_m2": area_m2,
        "estimated_units": units,
        "avg_unit_size_m2": unit_size,
        "GDV": f"£{gdv:,.0f}",
        "build_cost": f"£{build_cost:,.0f}",
        "estimated_profit": f"£{profit:,.0f}"
    }