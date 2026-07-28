# Capítulo 9 — Saída da verificação

## 1. Consistência Riccati

- resposta analítica: `1.887922614249`
- resposta RK4: `1.887922614249`
- erro absoluto: `2.220e-15`

## 2. Convergência do complemento de Schur

| elementos | resposta Schur | erro absoluto |
|---:|---:|---:|
| 20 | 1.888375695449 | 4.531e-04 |
| 40 | 1.888035885469 | 1.133e-04 |
| 80 | 1.887950932112 | 2.832e-05 |
| 160 | 1.887929693720 | 7.079e-06 |
| 320 | 1.887924384111 | 1.770e-06 |

## 3. Calibração sintética e validação separada

- lambda verdadeiro do fixture: `0.930000`
- lambda calibrado: `0.930500`
- erro de calibração: `+5.000e-04`
- chi² de calibração: `1.969047`
- informação de Fisher local: `7.085600e+05`
- RMSE no conjunto de teste congelado: `1.566936e-04`

## 4. Classificação

Teste de consistência + convergência + calibração sintética. Não é previsão
física nem comparação experimental.
