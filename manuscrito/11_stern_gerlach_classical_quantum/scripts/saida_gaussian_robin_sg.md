# Espectro axial no background gaussiano — Capítulo 11

- x_c=sqrt(6): `2.449489742783e+00`
- beta_B: `5.000000000000e-02`
- pontos: `2400`
- potencial algébrico: `V_H=0` (teste mínimo);

| modo | lambda+ | lambda- | diferença |
|---:|---:|---:|---:|
| 1 | 3.562212208e-02 | -3.790647948e-02 | 7.352860155e-02 |
| 2 | 1.483932311e+00 | 1.453844714e+00 | 3.008759683e-02 |
| 3 | 2.769494342e+00 | 2.747455415e+00 | 2.203892742e-02 |
| 4 | 3.998773220e+00 | 3.980591638e+00 | 1.818158268e-02 |
| 5 | 5.196537552e+00 | 5.180701274e+00 | 1.583627777e-02 |
| 6 | 6.380664232e+00 | 6.366236804e+00 | 1.442742757e-02 |
| 7 | 7.600617006e+00 | 7.586425710e+00 | 1.419129580e-02 |
| 8 | 8.954306620e+00 | 8.939289475e+00 | 1.501714575e-02 |

- menor lambda+ positivo: `True`;
- menor lambda- positivo: `False`;

O canal antiparalelo pode adquirir modo negativo porque é máximo
da energia Zeeman. Isso não invalida os dois canais unitários, mas
impede usar sua Hessiana estática como dois mínimos dissipativos.
