# OpenRBYR: A Ray-by-Ray CT Simulation Toolkit

![PyPI](https://img.shields.io/pypi/v/openrbyr)
![CI](https://github.com/HussainAther/OpenRBYR/actions/workflows/ci.yml/badge.svg)
![Docs](https://readthedocs.org/projects/openrbyr/badge/?version=latest)


## 📌 Overview
OpenRBYR is an open-source Python package for simulating Ray-by-Ray Computed Tomography (RBYRCT) scan paths. This toolkit enables researchers to explore and develop CT imaging methodologies with a focus on precision and low-dose imaging techniques.

### Features:
- **Simulated ray paths & scan trajectories**: Model different CT setups and beam configurations.
- **Monte Carlo simulation integration**: Example setups for **TOPAS** and **Geant4**.
- **Basic MART-like reconstruction**: Implementations to test reconstruction methods.
- **Synthetic CT phantoms**: Sample datasets for algorithm validation.

## 🛠 Installation
```bash
# Clone the repository
git clone https://github.com/HussainAther/OpenRBYR.git
cd OpenRBYR

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Getting Started
Here’s an example of how to simulate a simple CT scan setup:
```python
from openrbyr import ray_simulation

# Simulate rays for a CT setup
rays = ray_simulation.simulate_rays(num_rays=100, detector_distance=50)
ray_simulation.visualize_rays(rays)
```

## 📂 Project Structure
```
OpenRBYR/
│── examples/            # Sample simulations & reconstructions
│── notebooks/           # Jupyter notebooks for tutorials
│── openrbyr/            # Main package source code
│   │── __init__.py
│   │── ray_simulation.py # Core ray-path simulator
│   │── monte_carlo.py   # Monte Carlo simulation interface
│   │── reconstruction.py # Basic MART-like reconstruction
│── tests/               # Unit tests
│── synthetic_phantoms/  # Sample CT phantoms
│── docs/                # Documentation
│── README.md            # Main project description
│── INSTALL.md           # Installation instructions
│── CONTRIBUTING.md      # Contribution guidelines
│── LICENSE              # License file
│── .gitignore           # Ignore unnecessary files
```

## 🤝 Contributing
We welcome contributions from the community! To get started:
1. Fork the repository.
2. Create a new branch (`feature-name`).
3. Commit and push your changes.
4. Submit a pull request.

## 🔬 Future Roadmap
✅ **Implement GAN-based CT Denoising** (AI-powered artifact reduction)  
✅ **Support cloud-based Monte Carlo simulations**  
✅ **Integrate Web Visualization Tools** (e.g., Three.js for interactive 3D rendering)  
✅ **Develop AI-assisted inpainting for limited-angle CT**  
✅ **Create an API for real-time CT reconstruction**  

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## 📜 License
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## 🌍 Acknowledgments
Special thanks to **Richard Gordon** and the **OREL research team** for their contributions to RBYRCT technology.

