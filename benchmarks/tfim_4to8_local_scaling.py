import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron_all(ops):
    out = np.array([[1.0]], dtype=complex)
    for op in ops:
        out = np.kron(out, op)
    return out


def pauli_string(n, mapping):
    return kron_all([mapping.get(i, I) for i in range(n)])


def tfim_hamiltonian(n, J=1.0, hx=0.8, hz=0.3):
    H = np.zeros((2**n, 2**n), dtype=complex)
    for i in range(n - 1):
        H -= J * pauli_string(n, {i: Z, i + 1: Z})
    for i in range(n):
        H -= hx * pauli_string(n, {i: X})
        H -= hz * pauli_string(n, {i: Z})
    return H


def local_tfim_certificate(n, J=1.0, hx=0.8, hz=0.3):
    H = tfim_hamiltonian(n, J, hx, hz)
    evals, evecs = np.linalg.eigh(H)
    psi0 = evecs[:, 0]
    E0 = float(evals[0])
    eye = np.eye(2**n, dtype=complex)

    generators = [pauli_string(n, {i: Y}) for i in range(n)]
    generators += [pauli_string(n, {i: Z, i + 1: Z}) for i in range(n - 1)]

    dpsi = []
    for P in generators:
        mean = float(np.real(np.vdot(psi0, P @ psi0)))
        dpsi.append((-0.5j) * (P - mean * eye) @ psi0)

    p = len(dpsi)
    A = H - E0 * eye
    G = np.array([[np.real(np.vdot(di, dj)) for dj in dpsi] for di in dpsi])
    Hess = np.array([[2.0 * np.real(np.vdot(di, A @ dj)) for dj in dpsi] for di in dpsi])

    ew, U = np.linalg.eigh(G)
    Uact = U[:, ew > 1e-10]
    Gact = Uact.T @ G @ Uact
    Hact = Uact.T @ Hess @ Uact

    gvals, Q = np.linalg.eigh(Gact)
    Gmhalf = Q @ np.diag(1.0 / np.sqrt(gvals)) @ Q.T
    S0 = Gmhalf @ Hact @ Gmhalf

    hvals = np.linalg.eigvalsh(Hact)
    svals = np.linalg.eigvalsh(S0)
    gap = float(evals[1] - evals[0])
    width = float(evals[-1] - evals[0])
    ratio = width / gap
    kappa_H = float(hvals[-1] / hvals[0])
    kappa_S0 = float(svals[-1] / svals[0])
    gmin = float(gvals[0])
    gmax = float(gvals[-1])
    epscrit = 0.5 * gmin * ((gap / width) * kappa_H - 1.0)
    epshalf = 0.5 * epscrit
    Khalf = ratio * (1.0 + 2.0 * epshalf / gmin)

    return {
        "n_qubits": n,
        "p_parameters": p,
        "active_rank": len(gvals),
        "gap": gap,
        "width": width,
        "W_over_Delta": ratio,
        "g_min": gmin,
        "g_max": gmax,
        "kappa_H": kappa_H,
        "kappa_S0": kappa_S0,
        "epsilon_crit": epscrit,
        "epsilon_halfcrit": epshalf,
        "K_at_halfcrit": Khalf,
        "commutator_norm": float(np.linalg.norm(Gact @ Hact - Hact @ Gact, 2)),
    }


def main():
    df = pd.DataFrame([local_tfim_certificate(n) for n in range(4, 9)])
    assert np.all(df["epsilon_crit"] > 0)
    assert np.all(df["K_at_halfcrit"] < df["kappa_H"])
    assert np.all(df["kappa_S0"] <= df["W_over_Delta"] + 1e-10)

    df.to_csv("tfim_4to8_scaling.csv", index=False)

    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(df["n_qubits"], df["W_over_Delta"], marker="o", label=r"$W/\Delta$")
    ax.plot(df["n_qubits"], df["kappa_H"], marker="s", label=r"$\kappa(H_{\rm act})$")
    ax.plot(df["n_qubits"], df["kappa_S0"], marker="^", label=r"$\kappa(S_0)$")
    ax.set_xlabel("Number of qubits")
    ax.set_ylabel("Conditioning / spectral ratio")
    ax.set_xticks(df["n_qubits"])
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("tfim_4to8_conditioning_scaling.png", dpi=300, bbox_inches="tight")

    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    ax.plot(df["n_qubits"], df["epsilon_crit"], marker="o", label=r"$\varepsilon_{\rm crit}$")
    ax.set_xlabel("Number of qubits")
    ax.set_ylabel(r"Critical metric-error radius $\varepsilon_{\rm crit}$")
    ax.set_xticks(df["n_qubits"])
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("tfim_4to8_epsilon_crit_scaling.png", dpi=300, bbox_inches="tight")

    print(df.round(8).to_string(index=False))
    print("All scaling-certificate checks passed.")


if __name__ == "__main__":
    main()
