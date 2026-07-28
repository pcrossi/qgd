# Resultado do benchmark Cs — Fein et al. (2022)

## Protocolo

- resposta da bobina congelada: `C/I = 10.3 G m/A`;
- único parâmetro calibrado: gradiente magnético uniforme de fundo;
- treino: índices pares da série nominal de 380 m/s;
- teste interno: índices ímpares da mesma série;
- validação externa ao ajuste: toda a série nominal de 270 m/s;
- domínio declarado: `0.15 A <= I <= 4.5 A`.

## Resultado

Gradiente de fundo obtido: `0.350359 G/m`.

O artigo informa `0.4 G/m`; a diferença é compatível com a
digitização da figura e com a divisão parcial adotada aqui.

| Conjunto | N | RMSE | MAE | Viés |
|---|---:|---:|---:|---:|
| calibração 380 m/s | 15 | 0.022693 | 0.021161 | -0.010751 |
| teste interno 380 m/s | 14 | 0.022753 | 0.020167 | -0.003857 |
| validação cega 270 m/s | 30 | 0.023745 | 0.019905 | -0.000433 |

## Refinamento da quadratura no conjunto cego

| Pontos em velocidade | RMSE | Mudança |
|---:|---:|---:|
| 2000 | 0.023745317 | — |
| 4000 | 0.023745317 | 2.092e-11 |
| 8000 | 0.023745317 | 1.394e-13 |
| 16000 | 0.023745317 | 7.945e-16 |

## Classificação

O benchmark valida o protocolo de calibração e transporte da resposta
do aparelho. Ele não é uma previsão cega exclusiva da GDQ, pois a
resposta magnética atômica usada na fase é a expressão operacional
publicada pelo experimento, e não um canal magnético novamente
derivado da Hessiana oficial.

![Comparação entre dados e resposta congelada](benchmark_cs_fein2022.png)
