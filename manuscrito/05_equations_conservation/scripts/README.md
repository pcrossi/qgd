---
title: "Scripts — Capítulo 5"
---

# Scripts — Capítulo 5

Estes scripts são verificações simbólicas ou ilustrações pedagógicas ligadas ao
Capítulo 5. Eles não substituem as derivações do texto.

## Scripts

1. `verificar_corrente_fase_1d.py`
   - Classificação: ilustração de conservação de corrente.
   - Mostra que divergência nula preserva carga integrada e que fluxo de bordo
     altera a carga.
   - Saída: `saida_verificar_corrente_fase_1d.md`.

2. `verificar_bohm_fisher_variacao.py`
   - Classificação: teste numérico/simbólico de variação.
   - Compara a derivada variacional da energia de Fisher com o operador de
     Bohm em uma malha 1D.
   - Saída: `saida_verificar_bohm_fisher_variacao.md`.

3. `verificar_noether_shift_fase.py`
   - Classificação: ilustração de simetria contínua.
   - Verifica que uma densidade que depende apenas de $\partial S_R$ é
     invariante sob deslocamento global da fase.
   - Saída: `saida_verificar_noether_shift_fase.md`.

4. `verificar_polarizacao_canonica_toy.py`
   - Classificação: ilustração de Routh/Cauchy--Schwarz.
   - Mostra que, a carga e normalização fixas, o minimizador satisfaz
     $\Pi=(Q_S/N_\rho)\rho$.
   - Saída: `saida_verificar_polarizacao_canonica_toy.md`.

5. `verificar_simbolo_parabolico_gdq.py`
   - Classificação: verificação simbólico-numérica de parabolicidade forte.
   - Ilustra que, após gauge, o símbolo principal tem a forma
     $\sigma_{\rm pr}(\xi)=|\xi|_g^2I$ em métrica positiva.
   - Saída: `saida_verificar_simbolo_parabolico_gdq.md`.

## Uso

```bash
python3 verificar_corrente_fase_1d.py
python3 verificar_bohm_fisher_variacao.py
python3 verificar_noether_shift_fase.py
python3 verificar_polarizacao_canonica_toy.py
python3 verificar_simbolo_parabolico_gdq.py
```
