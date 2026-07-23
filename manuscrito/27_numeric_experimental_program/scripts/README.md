---
title: "Scripts — Capítulo 27"
---

# Scripts — Capítulo 27

Scripts de protocolo para padronizar novos cálculos GDQ.

| Script | Saída | Função |
|---|---|---|
| `gerar_manifesto_exemplo.py` | `saida_manifesto_exemplo.md` | exemplo de manifesto mínimo |
| `classificar_resultado.py` | `saida_classificacao_resultado.md` | classificador simples de status numérico |
| `tabela_status_numerico.py` | `saida_tabela_status_numerico.md` | status dos blocos numéricos principais |
| `bloco_hessiana_projetor_schur.py` | `saida_bloco_hessiana_projetor_schur.md` | exemplo autocontido de projetor físico e complemento de Schur |
| `gdq_reduced.py` | módulo importável | biblioteca reduzida DtN/Schur/resposta/coerência |
| `verificar_gdq_reduced.py` | `saida_verificar_gdq_reduced.md` | teste autocontido dos blocos reduzidos |

## Execução

```bash
python3 manuscrito/27_numeric_experimental_program/scripts/gerar_manifesto_exemplo.py
python3 manuscrito/27_numeric_experimental_program/scripts/classificar_resultado.py
python3 manuscrito/27_numeric_experimental_program/scripts/tabela_status_numerico.py
python3 manuscrito/27_numeric_experimental_program/scripts/bloco_hessiana_projetor_schur.py
python3 manuscrito/27_numeric_experimental_program/scripts/verificar_gdq_reduced.py
```
