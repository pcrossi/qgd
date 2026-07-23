---
title: "Saída — poço e oscilador como redução"
---

# Saída — poço e oscilador como redução

Classificação: teste de correspondência da Hessiana reduzida plana.

## Parâmetros numéricos

- poço: `2400` pontos internos, $L=1$, $\hbar^2/(2mL^2)=1$;
- oscilador: `3200` pontos internos em $[-8,8]$, $\hbar=m=\omega=1$;
- nenhum valor experimental é usado.

## poço infinito

| modo | numérico | analítico | erro relativo |
|---:|---:|---:|---:|
| 1 | `9.869602995677` | `9.869604401089` | `1.424e-07` |
| 2 | `39.478395074621` | `39.478417604357` | `5.707e-07` |
| 3 | `88.826325556091` | `88.826439609804` | `1.284e-06` |
| 4 | `157.913309945731` | `157.913670417430` | `2.283e-06` |
| 5 | `246.739229966292` | `246.740110027234` | `3.567e-06` |

## oscilador harmônico

| modo | numérico | analítico | erro relativo |
|---:|---:|---:|---:|
| 0 | `0.499999219240` | `0.500000000000` | `1.562e-06` |
| 1 | `1.499996096173` | `1.500000000000` | `2.603e-06` |
| 2 | `2.499989850052` | `2.500000000000` | `4.060e-06` |
| 3 | `3.499980480839` | `3.500000000000` | `5.577e-06` |
| 4 | `4.499967988532` | `4.500000000000` | `7.114e-06` |

## Índices de Morse reduzidos

| modo | poço ideal | oscilador |
|---:|---:|---:|
| 1 / 0 | `0` | `0` |
| 2 / 1 | `1` | `1` |
| 3 / 2 | `2` | `2` |
| 4 / 3 | `3` | `3` |
| 5 / 4 | `4` | `4` |

## Leitura

- o poço recupera $E_n=(n\pi)^2$ no contorno ideal;
- o oscilador recupera $E_n=n+1/2$ no fundo plano;
- os erros restantes são de discretização/truncamento;
- a Hessiana reduzida tem índice de Morse igual ao número de níveis abaixo do estado escolhido;
- o cálculo verifica correspondência, não uma previsão metrológica nova.
