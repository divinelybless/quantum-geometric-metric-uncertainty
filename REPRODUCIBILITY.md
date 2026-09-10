# Reproducibility Guide

## Scope

These materials reproduce the numerical checks supporting the local metric-uncertainty theory developed in the accompanying manuscript.

The calculations use NumPy/SciPy linear algebra and statevector expressions directly. No cloud quantum hardware or proprietary service is required.

## Environment

Recommended:

- Python 3.11 or newer
- NumPy
- SciPy
- Matplotlib
- JupyterLab / Jupyter Notebook
- nbformat

Install with:

```bash
pip install -r requirements.txt
```

or create the Conda environment with:

```bash
conda env create -f environment.yml
conda activate qgp-metric-uncertainty
```

## Notebook order

### 1. Exact verification

`notebooks/01_exact_verification.ipynb`

Reproduces the exactly solvable diagonal model and verifies the ground-state Hessian–metric sandwich, common metric/Hessian null space, active-space reduction, deterministic operator-norm perturbation bounds, saturation of the condition-number certificate, regularization behavior, and local spectral-rate comparison.

### 2. Finite-shot validation

`notebooks/02_finite_shot_verification.ipynb`

Reproduces the centered fidelity estimator, deterministic finite-difference bias, high-probability operator-norm radius, and the Monte Carlo stress test used in the manuscript.

The documented benchmark uses active dimension `r = 2`, finite-difference spacing `h = 0.1`, `N = 100000` shots per displaced fidelity setting, confidence parameter `delta = 0.05`, and 5000 Monte Carlo metric estimates.

### 3. Cross-model exact validation

`notebooks/03_cross_model_validation.ipynb`

Reproduces the entangled, noncommuting two-qubit stress test. This notebook verifies that the theory does not depend on simultaneous diagonalization of the active Fubini–Study metric and active energy Hessian.

### 4. Ising-dimer physical benchmark

`notebooks/04_ising_dimer_benchmark.ipynb`

Reproduces the transverse-longitudinal Ising dimer with `J = 1`, `h_x = 0.8`, and `h_z = 0.3`. The notebook uses fixed pseudorandom seed `20260910` for the multi-start optimizer and reproduces the active metric, active Hessian, perturbation certificate, and uncertainty-threshold sweep.

## Figures

The `figures/` directory contains manuscript figures generated from these notebooks. Their source calculations should be regarded as authoritative rather than the rendered PNG files themselves.

## Numerical precision

Small differences in the last printed digits may occur across BLAS/LAPACK implementations and SciPy versions. The theorem checks are based on inequalities with numerical tolerances, not exact string matching of floating-point output.

## Manuscript source

`paper/main.tex` is the polished scientific source used when this repository was prepared. `paper/references.bib` is the associated working bibliography. Journal-specific formatting may differ from this repository version.

## Archival release

Before final journal submission, the repository should be archived to a DOI-granting service such as Zenodo. The resulting persistent identifier can then replace the provisional repository citation in the manuscript and `CITATION.cff`.
