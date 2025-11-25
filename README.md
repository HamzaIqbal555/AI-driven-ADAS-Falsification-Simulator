# ADAS Simulator with Falsification Testing

This project implements an Advanced Driver Assistance System (ADAS) simulator that uses a locally hosted Large Language Model (LLM) as a backend. The simulator evaluates the LLM's decision-making capabilities in three ADAS scenarios: **Braking**, **Lane Change**, and **Speed Control**. The project also applies a falsification testing approach to identify scenarios where the LLM's decisions violate safety constraints.

---

## Features

- **ADAS Simulator**: Simulates three ADAS scenarios using a local `llama3.2` model.
- **Falsification Testing**: Identifies safety violations by evolving scenarios over multiple generations.
- **Scenario Evolution**: Uses mutation and crossover to generate new scenarios.
- **Graphical Results**: Provides visualizations of failure probabilities and safety distances for each scenario type.

---

## Scenarios

1. **Braking**:
   - Evaluates whether the system decides to brake based on the distance to a pedestrian and road conditions.
   - Safety Constraint: The system should brake if the pedestrian is within 15 meters.

2. **Lane Change**:
   - Evaluates whether the system decides to change lanes based on lane occupancy and turn indicator status.
   - Safety Constraint: The system should not change lanes if the lane is occupied.

3. **Speed Control**:
   - Evaluates whether the system adjusts speed based on the current speed, speed limit, and weather conditions.
   - Safety Constraint: The system should adjust speed if it exceeds the speed limit.

---

## Falsification Testing Approach

The falsification testing approach identifies scenarios where the LLM's decisions violate safety constraints. The process involves:

1. **Scenario Generation**:
   - An initial population of scenarios is generated randomly.

2. **Simulation**:
   - Each scenario is evaluated using the LLM to determine the failure probability and signed distance to the safe region.

3. **Evolution**:
   - New scenarios are generated using mutation and crossover to explore the scenario space.

4. **Archiving Violations**:
   - Scenarios that violate safety constraints are stored in an archive for analysis.

---

## Design Decisions

- **Local LLM**: The `llama3.2` model is used locally via the `ollama` subprocess interface to avoid reliance on paid APIs.
- **Scenario Evolution**: Mutation and crossover are used to systematically explore the scenario space and identify edge cases.
- **Safety Metrics**:
  - **Failure Probability**: The proportion of runs where the LLM's decision violates the safety constraint.
  - **Signed Distance**: A measure of how far the scenario is from the safe region.

---

## Assumptions

- The LLM is capable of understanding and responding to ADAS-related prompts.
- The safety constraints are well-defined and sufficient to evaluate the LLM's performance.
- The `llama3.2` model is hosted locally and accessible via the `ollama` command-line interface.

---

## Limitations

- **LLM Bias**: The LLM's responses may be biased or inconsistent, affecting the reliability of the simulator. Any general LLM cannot be trusted blindly for the rsponses it generate and can be dangerous if not being trained for a specific task.
- **Scalability**: The current implementation is designed for small populations and may not scale well to larger scenario spaces.
- **Simplified Scenarios**: The scenarios are simplified representations of real-world ADAS situations and may not capture all complexities. Note, I intentionally reduced the population and generation size of test cases for fast execution of the simulations.

---

## How to Run the Project

1. **Install Requirements**  
   Ensure you have Python installed. Then, install the required dependencies:
   ```bash
   pip install -r requirements.txt

2. **Trigger command** 
   ```bash
   python main.py

3. **Run below command for updated graphical results** 
   ```bash
   python analysis/results.py
