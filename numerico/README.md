# Pacote Numérico da Geometrodinâmica Quântica (GDQ)

Este diretório contém os códigos e rotinas computacionais para a validação numérica e fenomenológica do formalismo da Geometrodinâmica Quântica.

## Arquitetura de Diretórios

* **`comum/`**: Bibliotecas compartilhadas contendo solvers de autovalores, rotinas de quadratura e aplicação de condições de contorno.
* **`q39_leptons/`**: Solvers para o espectro de massas leptônicas (e, múon, tau), incluindo estudo de contornos e correções térmicas.
* **`q40_barions/`**: Rotinas para cálculo de fatores de forma, momentos magnéticos e raios de carga de próton/nêutron.
* **`q30_confinamento/`**: Discretização e simulação de Wilson Loops para cálculo da tensão de string.
* **`q31_cp_forte/`**: Cálculo da suscetibilidade topológica e do momento de dipolo elétrico do nêutron.
* **`q28_q29_eletrofraco/`**: Cálculo das Killing-normas e massas dos bósons de gauge eletrofracos.
* **`q28_tres_estomatos/`**: Seleção numérica do junction torsional, comparação
  de $N=2,\ldots,8$, Hessiana angular e modos zero internos.

## Protocolo de Validação

Todas as rotinas numéricas devem obedecer ao seguinte protocolo de 3 níveis:
1. **Nível 1 (Analítico):** Testar o solver numérico contra limites analíticos fechados (ex.: Rosen-Morse regularizado).
2. **Nível 2 (Convergência):** Rodar simulações com malhas progressivas ($N \in \{800, 1600, 3200, 6400\}$) para garantir convergência assintótica.
3. **Nível 3 (Físico):** Comparar os resultados finais com valores experimentais (CODATA/PDG).
