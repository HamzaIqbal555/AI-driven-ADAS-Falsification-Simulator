import json
import matplotlib.pyplot as plt
import os

# Path to the experiments folder
EXPERIMENTS_FOLDER = "experiments"


def load_archives():
    archives = {}
    for file in os.listdir(EXPERIMENTS_FOLDER):
        if file.startswith("archive_") and file.endswith(".json"):
            scenario_type = file[len("archive_"):-len(".json")]
            with open(os.path.join(EXPERIMENTS_FOLDER, file), "r") as f:
                archives[scenario_type] = json.load(f)
    return archives


def plot_results(archives):
    for scenario_type, data in archives.items():
        fail_probs = [entry["fail_prob"] for entry in data]
        distances = [entry["distance"] for entry in data]

        # Create a figure for the scenario type
        plt.figure(figsize=(12, 6))

        # Subplot 1: Failure probabilities
        plt.subplot(1, 2, 1)
        plt.hist(fail_probs, bins=10, color="skyblue", edgecolor="black")
        plt.title(f"Failure Probabilities for {scenario_type}")
        plt.xlabel("Failure Probability")
        plt.ylabel("Frequency")

        # Subplot 2: Signed distances
        plt.subplot(1, 2, 2)
        plt.hist(distances, bins=10, color="salmon", edgecolor="black")
        plt.title(f"Signed Distances for {scenario_type}")
        plt.xlabel("Signed Distance")
        plt.ylabel("Frequency")

        # Save the plot as an image
        plt.tight_layout()
        plt.savefig(f"results_{scenario_type}.png")
        plt.show()


def main():
    archives = load_archives()
    plot_results(archives)


if __name__ == "__main__":
    main()
