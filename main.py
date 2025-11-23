# falsification/runner.py

import random
import json
from llm_simulator.simulator import run_scenario
from falsification.distances import signed_distance
from falsification.evolution import mutate, crossover
from falsification.archive import add_to_archive
import config


def scenario_braking():
    return {
        "car_speed": random.uniform(0, 120),
        "pedestrian_distance": random.uniform(0, 50),
        "road_condition": random.choice(["dry", "wet"])
    }


def scenario_lane_change():
    return {
        "car_speed": random.uniform(0, 120),
        # "pedestrian_distance": None,  # not used
        # "road_condition": None,       # not used
        # # Example extra params (if needed)
        "lane_occupied": random.choice([True, False]),
        "indicator": random.choice([True, False])
    }


def scenario_speed_control():
    return {
        "current_speed": random.uniform(0, 120),
        "speed_limit": random.choice([30, 50, 80, 120]),
        "weather": random.choice(["clear", "rain", "fog"])
    }


SCENARIO_FUNCS = [
    ("Braking", scenario_braking),
    ("LaneChange", scenario_lane_change),
    ("SpeedControl", scenario_speed_control),
]


def main():
    all_archives = {}

    for name, scen_func in SCENARIO_FUNCS:
        print(f"=== Running falsification for scenario type: {name} ===")
        population = [scen_func() for _ in range(config.POP_SIZE)]
        archive = []

        for gen in range(config.GENERATIONS):
            print(f"Generation {gen + 1}/{config.GENERATIONS} for {name}")
            for scen in population:
                failures, total = run_scenario(scen, config.RUNS_PER_SCENARIO)
                prob_fail = failures / total
                dist = signed_distance(prob_fail, config.SAFE_UPPER)
                print(
                    f"  Scenario {scen} → p_fail={prob_fail:.3f}, dist={dist:.3f}")
                if dist < 0:
                    add_to_archive(archive, scen, prob_fail, dist)

            # Evolve for next generation
            new_pop = []
            for _ in range(config.POP_SIZE):
                p1, p2 = random.sample(population, 2)
                child = crossover(p1, p2)
                child = mutate(child)
                new_pop.append(child)
            population = new_pop

        all_archives[name] = archive

        # Save archive for this scenario type
        with open(f"experiments/archive_{name}.json", "w") as f:
            json.dump(archive, f, indent=2)

    # Optionally print summary
    for scenario_name, archive in all_archives.items():
        print(
            f"\nArchive for {scenario_name}, total violations: {len(archive)}")


if __name__ == "__main__":
    main()
