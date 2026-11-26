def is_budget_sufficient(one_way_km,budget):
    total_km = one_way_km * 2
    litres_needed = total_km / 10
    total_cost = litres_needed * 2
    return total_cost <= budget