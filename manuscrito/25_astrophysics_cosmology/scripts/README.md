---
title: "Scripts — Capítulo 25"
---

# Scripts — Capítulo 25

Os scripts desta pasta são autocontidos e servem para reproduzir as reduções
numéricas preservadas no capítulo.

| Script | Saída | Classificação |
|---|---|---|
| `buraco_negro_reduzido.py` | `saida_buraco_negro_reduzido.md` | teste de consistência de redução |
| `buraco_negro_pipeline_reduzido.py` | `saida_buraco_negro_pipeline_reduzido.md` | avaliação reduzida / trilha de validação |
| `cosmologia_escalas_gdq.py` | `saida_cosmologia_escalas_gdq.md` | avaliação direta de fórmulas estruturais |
| `contrato_cosmologia_integrada.py` | `saida_contrato_cosmologia_integrada.md` | verificação estrutural do contrato de solver cosmológico único |
| `escala_eletrofraca_global.py` | `saida_escala_eletrofraca_global.md` | auditoria de $v_K$, cálculo de $\beta_\ast$, $v_{\rm GDQ}$ e W/Z condicional |
| `eletrofraca_raio_proton.py` | `saida_eletrofraca_raio_proton.md` | avaliação direta e comparação fenomenológica |
| `raio_proton_superficie.py` | `saida_raio_proton_superficie.md` | correção aritmética legada, cálculo de $r_p^{\rm surf}$ e resposta por sonda |

## Execução

Na raiz do projeto:

```bash
python3 manuscrito/25_astrophysics_cosmology/scripts/buraco_negro_reduzido.py
python3 manuscrito/25_astrophysics_cosmology/scripts/buraco_negro_pipeline_reduzido.py
python3 manuscrito/25_astrophysics_cosmology/scripts/cosmologia_escalas_gdq.py
python3 manuscrito/25_astrophysics_cosmology/scripts/contrato_cosmologia_integrada.py
python3 manuscrito/25_astrophysics_cosmology/scripts/escala_eletrofraca_global.py
python3 manuscrito/25_astrophysics_cosmology/scripts/eletrofraca_raio_proton.py
python3 manuscrito/25_astrophysics_cosmology/scripts/raio_proton_superficie.py
```
