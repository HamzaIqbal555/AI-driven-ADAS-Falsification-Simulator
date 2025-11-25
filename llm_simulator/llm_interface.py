import subprocess


def query_llm_subprocess(scenario, model="llama3.2"):
    """
    Query a local LLM (via Ollama CLI) using subprocess.
    Dynamically handles different scenario types.
    """
    # Determine scenario type and build appropriate prompt
    if 'pedestrian_distance' in scenario and scenario['pedestrian_distance'] is not None:
        # Braking scenario
        prompt = (
            f"You are an ADAS controller. The car is driving at {scenario['car_speed']} km/h, "
            f"a pedestrian is {scenario['pedestrian_distance']} meters away, "
            f"road condition is {scenario['road_condition']}. "
            "What should the car do? Answer with: Brake or Don't Brake."
        )

    elif 'lane_occupied' in scenario:
        # LaneChange scenario
        prompt = (
            f"You are an ADAS controller. The car is driving at {scenario['car_speed']} km/h, "
            f"target lane is {'occupied' if scenario['lane_occupied'] else 'free'}, "
            f"turn indicator is {'on' if scenario['indicator'] else 'off'}. "
            "Should you change lanes? Answer with ONLY: Change Lane or Don't Change."
        )

    elif 'current_speed' in scenario and scenario['current_speed'] is not None:
        # SpeedControl scenario
        prompt = (
            f"You are an ADAS controller. Current speed is {scenario['current_speed']} km/h, "
            f"speed limit is {scenario['speed_limit']} km/h, "
            f"weather is {scenario['weather']}. "
            "Should you maintain or adjust speed? Answer with ONLY: Maintain Speed or Adjust Speed."
        )

    else:
        # Fallback for unknown scenario type
        prompt = (
            "You are an ADAS controller. Analyze this driving scenario and decide on appropriate action. "
            f"Scenario details: {scenario}. "
            "Answer with a clear action decision."
        )

    # Run Ollama without --json
    try:
        proc = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            timeout=30  # Add timeout to prevent hanging
        )
        if proc.returncode != 0:
            print(f"LLM warning: {proc.stderr}")
            return "Error"  # Return error for failed calls
        return proc.stdout.strip()
    except subprocess.TimeoutExpired:
        print("LLM call timed out")
        return "Timeout"
    except Exception as e:
        print(f"LLM call failed: {e}")
        return "Error"


def query_llm(scenario, model="llama3.2"):
    return query_llm_subprocess(scenario, model=model)
