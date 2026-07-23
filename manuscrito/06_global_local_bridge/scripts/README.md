---
title: "Scripts opcionais — Capítulo 6"
---

# Scripts opcionais — Capítulo 6

Estes scripts são verificações didáticas autocontidas para o Capítulo 6.
Eles ilustram etapas da ponte global--local, mas não substituem os lemas do
texto.

Classificação geral:

- verificação de consistência;
- toy model numérico;
- sem ajuste a dado experimental;
- sem alteração da ação oficial.

## Scripts

| Script | Saída | Função |
|---|---|---|
| `verificar_limite_apontado_torus_esfera.py` | `saida_verificar_limite_apontado_torus_esfera.md` | Verifica a planificação local de $S^1_R$ e $S^3_R$ quando $R\to\infty$. |
| `verificar_transporte_medida_ponderada.py` | `saida_verificar_transporte_medida_ponderada.md` | Testa transporte de densidade ponderada com jacobiano correto. |
| `verificar_gap_localizacao_toy.py` | `saida_verificar_gap_localizacao_toy.md` | Mostra um modo ligado localizado preservando gap enquanto o domínio cresce. |
| `verificar_resolvente_riesz_toy.py` | `saida_verificar_resolvente_riesz_toy.md` | Compara projetores de Riesz em uma família finita de operadores. |
| `verificar_homomorfismo_relogio.py` | `saida_verificar_homomorfismo_relogio.md` | Verifica $\tau_\gamma(t)=\tau_0e^{\kappa t}$ a partir do homomorfismo causal. |

## Uso

Executar a partir da raiz do projeto:

```bash
python3 manuscrito/06_global_local_bridge/scripts/verificar_limite_apontado_torus_esfera.py
python3 manuscrito/06_global_local_bridge/scripts/verificar_transporte_medida_ponderada.py
python3 manuscrito/06_global_local_bridge/scripts/verificar_gap_localizacao_toy.py
python3 manuscrito/06_global_local_bridge/scripts/verificar_resolvente_riesz_toy.py
python3 manuscrito/06_global_local_bridge/scripts/verificar_homomorfismo_relogio.py
```

