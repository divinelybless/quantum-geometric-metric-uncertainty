# Quantum-Geometric Metric Uncertainty

Reproducibility materials for the manuscript **“Metric Uncertainty and Local Linearized Convergence Certificates in Quantum-Geometric Variational Optimization.”**

This repository accompanies a theory-centered study of how operator-norm uncertainty in an estimated Fubini–Study metric propagates into the conditioning and local linearized spectral rate of variational quantum optimization.

## Main result chain

The manuscript develops the certification path

`VQE spectral structure → metric-error radius → preconditioned-curvature bound → metric-accuracy threshold → local spectral certification.`

For the fully centered finite-shot metric estimator, the repository also documents the measurement-budget-to-certification chain.

## Repository structure

- `notebooks/01_exact_verification.ipynb` — exact geometry, active-space, perturbation, conditioning and regularization checks.
- `notebooks/02_finite_shot_verification.ipynb` — finite-shot fidelity estimator and Monte Carlo validation.
- `notebooks/03_cross_model_validation.ipynb` — noncommuting entangled synthetic stress test.
- `notebooks/04_ising_dimer_benchmark.ipynb` — transverse-longitudinal Ising-dimer benchmark and uncertainty-threshold sweep.
- `figures/ising_preconditioned_spectrum.svg` — preconditioned-curvature spectrum for the Ising benchmark.
- `figures/ising_uncertainty_threshold.svg` — theorem-bound/threshold visualization for the Ising benchmark.
- `references/core_references.bib` — core verified references supporting the reproducibility package.
- `REPRODUCIBILITY.md` — instructions for reproducing the numerical results.
- `requirements.txt` and `environment.yml` — Python environment information.
- `CITATION.cff` — repository citation metadata.

The full journal manuscript and complete submission bibliography will be added once the scientific version is frozen for public release.

## Validation hierarchy

The numerical evidence is intentionally structured around complementary tests:

1. **Diagonal saturation test:** demonstrates sharpness of the deterministic condition-number bound.
2. **Noncommuting entangled stress test:** verifies the result beyond simultaneously diagonalizable metric–Hessian pairs.
3. **Transverse-longitudinal Ising dimer:** demonstrates evaluation of the certificate on a recognizable interacting VQE Hamiltonian.
4. **Finite-shot Monte Carlo:** tests the derived high-probability metric-error radius under the specified centered fidelity estimator.

## Reproduction status

All four notebook code paths were independently re-executed on **10 September 2026** from fresh Python processes in an isolated working directory. All completed without runtime errors and reproduced the manuscript-level certificate values. See `REPRODUCIBILITY.md` for the recorded values and scope of this check.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Run the notebooks in numerical order. Each notebook is self-contained and uses explicit parameter choices and random seeds where stochastic sampling is involved.

## Reproducibility policy

No numerical table or figure is intended to enter the manuscript unless it is reproducible from one documented code path. The repository therefore keeps the analytical stress tests, finite-shot simulation, and physical benchmark in separate notebooks with explicit constants and seeds.

## Citation

If you use this repository, please cite the accompanying manuscript and this software repository. See `CITATION.cff` for the current citation metadata. A DOI will be added after archival deposition.

## License

A software/data license has not yet been selected. Until a license is added, standard copyright restrictions apply.

## Author

**Dorcas Attuabea Addo**  
GitHub: [@divinelybless](https://github.com/divinelybless)
