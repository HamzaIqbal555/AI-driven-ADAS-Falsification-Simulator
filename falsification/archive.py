# falsification/archive.py

def add_to_archive(archive, scenario, prob, dist):
    """
    Store violating scenarios into archive, adapted from PF archive storage logic.
    In original PF they store parameter vectors + violation scores.
    Here we store scenario, fail probability, distance.
    """
    archive.append({
        "scenario": scenario,
        "fail_prob": prob,
        "distance": dist
    })
