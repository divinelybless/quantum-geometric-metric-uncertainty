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
- `benchmarks/tfim_4to8_local_scaling.py` — reproducible 4–8-qubit transverse-longitudinal Ising-chain local scaling benchmark.
- `results/tfim_4to8_scaling.csv` — numerical scaling data used for the larger-system benchmark.
- `figures/ising_preconditioned_spectrum.svg` — preconditioned-curvature spectrum for the Ising benchmark.
- `figures/ising_uncertainty_threshold.svg` — theorem-bound/threshold visualization for the Ising benchmark.
- `references/core_references.bib` — core verified references supporting the reproducibility package.
- `REPRODUCIBILITY.md` — instructions for reproducing the numerical results.
- `requirements.txt` and `environment.yml` — Python environment information.
- `CITATION.cff` — repository citation metadata.
- `LICENSE` — MIT License.

The full journal manuscript and complete submission bibliography will be added once the scientific version is frozen for public release.

## Validation hierarchy

The numerical evidence is intentionally structured around complementary tests:

1. **Diagonal saturation test:** demonstrates sharpness of the deterministic condition-number bound.
2. **Noncommuting entangled stress test:** verifies the result beyond simultaneously diagonalizable metric–Hessian pairs.
3. **Transverse-longitudinal Ising dimer:** demonstrates evaluation of the certificate on a recognizable interacting VQE Hamiltonian.
4. **Finite-shot Monte Carlo:** tests the derived high-probability metric-error radius under the specified centered fidelity estimator.
5. **4–8-qubit Ising-chain local scaling:** evaluates how `g_min`, `W/Delta`, the Euclidean active-Hessian condition number, the exact geometrically preconditioned condition number, and `epsilon_crit` behave as the active dimension grows from 7 to 15.

The 4–8-qubit study is intentionally a **local theorem diagnostic** centered at the exact ground state. It is not presented as evidence of efficient ground-state preparation, global VQE convergence, or favorable asymptotic scaling.

## Reproduction status

The original four notebook code paths were independently re-executed on **10 September 2026** from fresh Python processes in an isolated working directory and reproduced the manuscript-level certificate values. The additional 4–8-qubit scaling benchmark has also been independently executed and its internal certificate assertions passed. See `REPRODUCIBILITY.md` and `results/tfim_4to8_scaling.csv` for the documented values.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Run the notebooks in numerical order. The larger local-scaling benchmark may be reproduced with:

```bash
python benchmarks/tfim_4to8_local_scaling.py
```

## Reproducibility policy

No numerical table or figure is intended to enter the manuscript unless it is reproducible from one documented code path. The repository therefore keeps the analytical stress tests, finite-shot simulation, physical dimer benchmark, and larger local-scaling benchmark in documented code paths with explicit constants and assumptions.

## Citation

If you use this repository, please cite the accompanying manuscript and this software repository. See `CITATION.cff` for the current citation metadata. A DOI will be added after archival deposition.

## License

This repository is released under the **MIT License**. See `LICENSE` for the full terms.

## Author

**Dorcas Attuabea Addo**  
GitHub: [@divinelybless](https://github.com/divinelybless)
