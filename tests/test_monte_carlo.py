# tests/test_monte_carlo.py
from openrbyr_core.monte_carlo import simulate_monte_carlo

def test_simulate_monte_carlo_runs():
    output = simulate_monte_carlo(photon_count=1000)
    assert "dose_map" in output
    assert output["dose_map"].shape[0] > 0

