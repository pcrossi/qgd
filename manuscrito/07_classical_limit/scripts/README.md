---
title: "Scripts opcionais — Capítulo 7"
---

# Scripts opcionais — Capítulo 7

Scripts didáticos autocontidos para verificar etapas do limite clássico.

Classificação geral:

- verificação de consistência;
- toy model numérico;
- sem ajuste experimental;
- sem alteração da ação oficial.

## Scripts

| Script | Saída | Função |
|---|---|---|
| `verificar_bohm_epsilon_cl.py` | `saida_verificar_bohm_epsilon_cl.md` | Confirma a escala $|Q_B|/T_{\rm cl}\sim\varepsilon_{\rm cl}^2$. |
| `verificar_hamilton_newton.py` | `saida_verificar_hamilton_newton.md` | Verifica Hamilton $\to$ Newton em um oscilador harmônico. |
| `verificar_liouville_monocinetico.py` | `saida_verificar_liouville_monocinetico.md` | Testa conservação de norma de uma densidade advectada. |
| `verificar_cotangente_kepler.py` | `saida_verificar_cotangente_kepler.md` | Verifica o limite cotangente global $\to$ Kepler local. |
| `verificar_noether_classico.py` | `saida_verificar_noether_classico.md` | Verifica conservação por simetria em toy models clássicos. |
| `verificar_gravidade_macroscopica.py` | `saida_verificar_gravidade_macroscopica.md` | Verifica trace-reversed $\to$ Einstein, fator $8\pi$ e anulação geodésica da torção antissimétrica. |

## Uso

Executar a partir da raiz do projeto:

```bash
python3 manuscrito/07_classical_limit/scripts/verificar_bohm_epsilon_cl.py
python3 manuscrito/07_classical_limit/scripts/verificar_hamilton_newton.py
python3 manuscrito/07_classical_limit/scripts/verificar_liouville_monocinetico.py
python3 manuscrito/07_classical_limit/scripts/verificar_cotangente_kepler.py
python3 manuscrito/07_classical_limit/scripts/verificar_noether_classico.py
python3 manuscrito/07_classical_limit/scripts/verificar_gravidade_macroscopica.py
```
