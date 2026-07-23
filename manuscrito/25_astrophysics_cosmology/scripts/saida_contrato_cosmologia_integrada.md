---
title: "Saída — contrato de cosmologia integrada"
---

# Saída — contrato de cosmologia integrada

## Entrada única

$$
\mathcal P_{\rm cos}=(\Phi_*^{\rm cos},R_H,\eta_b,T_0,\mathcal P_{\rm prim},\mathcal B_{\rm contorno})
$$

| Item | Papel |
|---|---|
| `Phi_cos*=(g,J,H,f,U)_cos` | dado congelado antes da comparação |
| `R_H` | dado congelado antes da comparação |
| `eta_b` | dado congelado antes da comparação |
| `T_0` | dado congelado antes da comparação |
| `P_prim` | dado congelado antes da comparação |
| `B_contorno` | dado congelado antes da comparação |

## Cadeia comum

$$
\mathcal S_{\rm GDQ}\to\Phi_*^{\rm cos}\to K_{\rm cos}^{\rm phys}\to\delta\Phi_{\rm cos}\to\text{observáveis}
$$

$$
K_{\rm cos}^{\rm phys}=P_{\rm cos}^{\rm phys}\operatorname{Hess}\mathcal S_{\rm GDQ}P_{\rm cos}^{\rm phys}
$$

$$
K_{\rm cos}^{\rm phys}\delta\Phi_{\rm cos}=J_{\rm bar}+J_\gamma+J_\nu+J_H
$$

## Observáveis obrigatórios

| Observável | Deve usar |
|---|---|
| `H(z)` | o mesmo `P_cos` e o mesmo background |
| `SN` | o mesmo `P_cos` e o mesmo background |
| `BAO` | o mesmo `P_cos` e o mesmo background |
| `CMB` | o mesmo `P_cos` e o mesmo background |
| `BBN/litio` | o mesmo `P_cos` e o mesmo background |
| `lentes` | o mesmo `P_cos` e o mesmo background |
| `crescimento` | o mesmo `P_cos` e o mesmo background |
| `birrefringencia` | o mesmo `P_cos` e o mesmo background |

## Proibições de fechamento

| Proibição | Motivo |
|---|---|
| `fator independente para Hubble` | quebraria a cosmologia integrada |
| `fator independente para litio` | quebraria a cosmologia integrada |
| `fator independente para Bullet Cluster` | quebraria a cosmologia integrada |
| `fator independente para birrefringencia` | quebraria a cosmologia integrada |
| `troca de contorno depois da comparacao` | quebraria a cosmologia integrada |

## Classificação

Formulação estrutural fechada. Solver metrológico conjunto permanece extensão futura.
