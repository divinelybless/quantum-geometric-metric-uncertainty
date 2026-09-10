# Reproducibility Guide

## Scope

These materials reproduce the numerical checks supporting the local metric-uncertainty theory developed in the accompanying manuscript.

The calculations use NumPy/SciPy linear algebra and statevector expressions directly. No cloud quantum hardware or proprietary service is required.

## Environment

Recommended:

- Python 3.11 or newer
- NumPy
- SciPy
- Pandas
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

## Independent execution check

On 10 September 2026, the four repository notebooks were re-executed sequentially from fresh Python processes in an isolated working directory. All four completed without runtime errors. The execution check did not reuse notebook kernel state between notebooks.

Key reproduced values were:

- Exact verification: `kappa(S0) = 4.0`, `K(lambda,eps) = 7.2`, `epsilon_crit = 1.875`.
- Finite-shot validation: `epsilon_N = 0.7449667286`, empirical violation rate `0.0`, `K = 27.8389353155 < kappa_H = 64`.
- Noncommuting entangled test: `||[G,Hess]||_2 = 1.1384199577`, `kappa(S_lambda) = 4.1123004994`, `K = 8.8973665961`, certificate `True`.
- Ising dimer: active rank `3`, `kappa(S0) = 2.9964256623`, `epsilon_crit = 0.0168084698`, `kappa(S_lambda) = 2.7709346418`, `K = 3.4134587353`, certificate `True`.

A completely new dependency installation was not performed in that check because package installation was not available in the isolated runtime; dependency declarations in `requirements.txt` and `environment.yml` remain the portable setup route for external users.

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

The `figures/` directory contains manuscript figures generated from these notebooks. Their source calculations should be regarded as authoritative rather than any rendered image file alone.

## Numerical precision

Small differences in the last printed digits may occur across BLAS/LAPACK implementations and SciPy versions. The theorem checks are based on inequalities with numerical tolerances, not exact string matching of floating-point output.

## Public-release status

The repository is now suitable as a reproducibility release candidate. Before creating the archival DOI release, the remaining tasks are to choose a software/data license, create a GitHub release/tag (suggested `v0.1.0`), connect the repository to Zenodo, and insert the resulting DOI into `CITATION.cff` and the manuscript.
