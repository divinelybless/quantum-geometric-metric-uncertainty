# v0.1.0 — Reproducibility release candidate

This release candidate contains the reproducibility materials supporting the manuscript **“Metric Uncertainty and Local Linearized Convergence Certificates in Quantum-Geometric Variational Optimization.”**

## Included

- Exact verification of the Hessian–metric sandwich, active-space reduction, deterministic metric perturbation bound, regularization structure, and local spectral-rate certificate.
- Finite-shot centered-fidelity metric estimator and Monte Carlo validation.
- Noncommuting entangled two-qubit stress test.
- Transverse-longitudinal Ising-dimer benchmark and uncertainty-threshold sweep.
- Environment files, citation metadata, reproducibility guide, core references, and MIT License.

## Reproduction status

All four notebook code paths were independently re-executed on 10 September 2026 from fresh Python processes in an isolated working directory. All completed without runtime errors and reproduced the manuscript-level certificate values recorded in `REPRODUCIBILITY.md`.

## Archival plan

After the GitHub release is created, connect the repository to Zenodo and archive this version. Then add the Zenodo DOI to `CITATION.cff`, the README, and the manuscript code/data availability statement.
