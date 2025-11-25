import random
import numpy as np


def mutate(scenario):
    child = scenario.copy()
    # handle each field only if not None
    if "car_speed" in child and child["car_speed"] is not None:
        child["car_speed"] = np.clip(
            child["car_speed"] + np.random.uniform(-10, 10), 0, 120)
    if "pedestrian_distance" in child and child["pedestrian_distance"] is not None:
        child["pedestrian_distance"] = np.clip(
            child["pedestrian_distance"] + np.random.uniform(-5, 5), 0, 50
        )
    if "road_condition" in child and child["road_condition"] is not None:
        child["road_condition"] = random.choice(["dry", "wet"])
    if "lane_occupied" in child:
        child["lane_occupied"] = random.choice([True, False])
    if "indicator" in child:
        child["indicator"] = random.choice([True, False])
    if "current_speed" in child and child["current_speed"] is not None:
        child["current_speed"] = np.clip(
            child["current_speed"] + np.random.uniform(-5, 5), 0, 120)
    if "speed_limit" in child and child["speed_limit"] is not None:
        child["speed_limit"] = random.choice([30, 50, 80, 120])
    if "weather" in child and child["weather"] is not None:
        child["weather"] = random.choice(["clear", "rain", "fog"])
    return child


def crossover(p1, p2):
    """
    Combine two scenarios p1 and p2 into a child scenario.
    Handles None values by carrying over non-None values or picking one.
    """
    child = {}
    for key in p1.keys():
        v1 = p1.get(key)
        v2 = p2.get(key)
        # If both are None, keep None
        if v1 is None and v2 is None:
            child[key] = None
        # If one is None, pick the one with a value
        elif v1 is None:
            child[key] = v2
        elif v2 is None:
            child[key] = v1
        else:
            # Both not None. Handle numeric or categorical accordingly
            if isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
                child[key] = (v1 + v2) / 2
            else:
                # For non-numeric, choose randomly
                child[key] = random.choice([v1, v2])
    return child
