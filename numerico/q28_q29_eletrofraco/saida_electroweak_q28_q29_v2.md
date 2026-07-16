# Relatório de Simulação Eletrofraca V2 (Diferenças Finitas)

Este documento registra a execução do solver variacional eletrofraco de segunda geração (`solve_electroweak_q28_q29_v2.py`).

## 1. Algoritmo Utilizado
1. **Fibrados de Killing:** A integração numérica dos geradores $\\xi_W$ e $\\xi_Y$ sobre a medida de $S^3$ ($d\\mu = \\sin^2 y \\, dy$) forneceu os acoplamentos discretos.
2. **Diferenças Finitas:** O campo $\\Phi(r)$ foi resolvido em uma malha radial de $200$ pontos, aproximando a derivada radial $\\frac{d\\Phi}{dr}$ e minimizando o funcional de ação variacional por L-BFGS-B.

## 2. Resultados Numéricos Obtidos
* **Acoplamento $g$ (SU(2)):** `0.65147`
* **Acoplamento $g'$ (U(1)):** `1.12838`
* **$\\sin^2 \\theta_W$:** `0.75000`
* **VEV ($v$) na Borda:** `168.9825` GeV (Erro vs CODATA: `31.3692%`)
* **Massa Bóson W:** `55.0435` GeV (Erro vs CODATA: `31.5200%`)
* **Massa Bóson Z:** `110.0870` GeV (Erro vs CODATA: `20.7259%`)
