---
title: "Output — integrated cosmology contract"
---

# Output — integrated cosmology contract

## Single input

$$
\mathcal P_{\rm cos}=(\Phi_*^{\rm cos},R_H,\eta_b,T_0,\mathcal P_{\rm prim},\mathcal B_{\rm contorno})
$$

| Item | Role |
|---|---|
| `Phi_cos*=(g,J,H,f,U)_cos` | frozen data before comparison |
| `R_H` | frozen data before comparison |
| `eta_b` | frozen data before comparison |
| `T_0` | frozen data before comparison |
| `P_prim` | frozen data before comparison |
| `B_contorno` | frozen data before comparison |

## Common chain

$$
\mathcal S_{\rm GDQ}\to\Phi_*^{\rm cos}\to K_{\rm cos}^{\rm phys}\to\delta\Phi_{\rm cos}\to\text{observables}
$$

$$
K_{\rm cos}^{\rm phys}=P_{\rm cos}^{\rm phys}\operatorname{Hess}\mathcal S_{\rm GDQ}P_{\rm cos}^{\rm phys}
$$

$$
K_{\rm cos}^{\rm phys}\delta\Phi_{\rm cos}=J_{\rm bar}+J_\gamma+J_\nu+J_H
$$

## Mandatory observables

| Observable | Must use |
|---|---|
| `H(z)` | the same `P_cos` and the same background |
| `SN` | the same `P_cos` and the same background |
| `BAO` | the same `P_cos` and the same background |
| `CMB` | the same `P_cos` and the same background |
| `BBN/lithium` | the same `P_cos` and the same background |
| `lensing` | the same `P_cos` and the same background |
| `growth` | the same `P_cos` and the same background |
| `birefringence` | the same `P_cos` and the same background |

## Closure prohibitions

| Prohibition | Reason |
|---|---|
| `independent factor for Hubble` | would break integrated cosmology |
| `independent factor for lithium` | would break integrated cosmology |
| `independent factor for Bullet Cluster` | would break integrated cosmology |
| `independent factor for birefringence` | would break integrated cosmology |
| `changing boundary after comparison` | would break integrated cosmology |

## Classification

Structurally closed formulation. Joint metrological solver remains a future extension.
