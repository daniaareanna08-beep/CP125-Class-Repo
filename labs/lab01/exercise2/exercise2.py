import math

def calculate_tent_cost(participants, tent_capacity, tent_price):
    tents = math.ceil(participants / tent_capacity)
    return tents * tent_price
