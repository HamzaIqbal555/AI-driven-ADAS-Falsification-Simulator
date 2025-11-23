# falsification/distances.py

def signed_distance(fail_prob, safe_upper):
    """
    Compute the signed distance to safe region, adapted from PF concept.
    In the original PF, they compare parameter estimates to safe intervals.
    Here, we compare failure probability.
    """
    if fail_prob <= safe_upper:
        # Inside safe region → positive distance
        return safe_upper - fail_prob
    else:
        # Violation → negative distance
        return -(fail_prob - safe_upper)
