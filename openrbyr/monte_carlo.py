# monte_carlo.py

import numpy as np

class MonteCarloSimulation:
    def __init__(self, num_particles=10000, detector_distance=50):
        self.num_particles = num_particles
        self.detector_distance = detector_distance

    def run_simulation(self):
        """Simulates X-ray particle interactions using a simple Monte Carlo model."""
        interactions = np.random.rand(self.num_particles, 2) * self.detector_distance
        return interactions

    def analyze_results(self, interactions):
        absorption_ratio = np.mean(interactions[:, 0] < self.detector_distance / 2)
        return {
            "total_particles": self.num_particles,
            "absorbed_ratio": absorption_ratio
        }

if __name__ == "__main__":
    mc = MonteCarloSimulation()
    results = mc.run_simulation()
    analysis = mc.analyze_results(results)
    print("Monte Carlo Simulation Results:", analysis)
