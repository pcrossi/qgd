---
title: "Scripts — Capítulo 24"
---

# Scripts — Capítulo 24

Os scripts desta pasta são verificadores autocontidos. Eles não dependem dos
arquivos de auditoria históricos nem de documentos externos ao capítulo.

## Scripts

| Script | O que verifica | Saída |
|---|---|---|
| `decaimento_alfa_reduzido.py` | tabela alfa reduzida, resíduos e RMS | `saida_decaimento_alfa_reduzido.md` |
| `alfa_pipeline_schur_riesz_reduzido.py` | construção reduzida completa do canal alfa: Schur, Riesz, mobilidade de determinante, taxa e RMS | `saida_alfa_pipeline_schur_riesz_reduzido.md` |
| `camadas_spin_torcao.py` | fechamentos de camada por contagem spin--torção | `saida_camadas_spin_torcao.md` |
| `klein_nishina_reduzido.py` | fator angular e limite Thomson | `saida_klein_nishina_reduzido.md` |
| `klein_nishina_total_e_fluxo.py` | raio clássico, Thomson, integração angular e seção total Klein--Nishina | `saida_klein_nishina_total_e_fluxo.md` |
| `pares_eletromagneticos_reduzidos.py` | limiares, Ward, vidas de positrônio, produção nuclear e opacidade magnética | `saida_pares_eletromagneticos_reduzidos.md` |
| `neutrinos_torsionais_reduzido.py` | massas neutras candidatas e comparação | `saida_neutrinos_torsionais_reduzido.md` |
| `oscilacoes_neutrinos_folha_modo.py` | reconstrução reduzida de $K^\nu$, mistura folha--modo e probabilidades de oscilação | `saida_oscilacoes_neutrinos_folha_modo.md` |

## Execução

Na raiz do projeto:

```bash
python3 manuscrito/24_nuclear_phenomenology/scripts/decaimento_alfa_reduzido.py
python3 manuscrito/24_nuclear_phenomenology/scripts/alfa_pipeline_schur_riesz_reduzido.py
python3 manuscrito/24_nuclear_phenomenology/scripts/camadas_spin_torcao.py
python3 manuscrito/24_nuclear_phenomenology/scripts/klein_nishina_reduzido.py
python3 manuscrito/24_nuclear_phenomenology/scripts/klein_nishina_total_e_fluxo.py
python3 manuscrito/24_nuclear_phenomenology/scripts/pares_eletromagneticos_reduzidos.py
python3 manuscrito/24_nuclear_phenomenology/scripts/neutrinos_torsionais_reduzido.py
python3 manuscrito/24_nuclear_phenomenology/scripts/oscilacoes_neutrinos_folha_modo.py
```

Classificação geral: verificações reduzidas e testes de consistência. Elas não
substituem a avaliação metrológica direta da Hessiana completa.
