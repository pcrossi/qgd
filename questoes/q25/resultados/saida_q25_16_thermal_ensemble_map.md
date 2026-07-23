# Q25.16 — Mapa térmico do ensemble GDQ reduzido

Classificação: calibração/inversão fenomenológica do mapa térmico.

O script varre por Monte Carlo reprodutível o ensemble positivo reduzido da GDQ e inverte a curva `C_s(1)(beta_eff)` para os pontos digitizados da Fig. 2D de Parsons.

| kBT/t exp | C_s(1) exp | beta_eff GDQ | T_eff GDQ | C_s(1) GDQ | residual |
|---:|---:|---:|---:|---:|---:|
| 0.000 | -3.50000000e-01 | 7.63442723e-01 | 1.30985596e+00 | -3.50000000e-01 | 0.00000000e+00 |
| 0.450 | -2.10000000e-01 | 5.19445430e-01 | 1.92513004e+00 | -2.10000000e-01 | 0.00000000e+00 |
| 0.550 | -2.40000000e-01 | 5.91747963e-01 | 1.68990865e+00 | -2.40000000e-01 | 2.77555756e-17 |
| 0.900 | -1.10000000e-01 | 2.93897795e-01 | 3.40254340e+00 | -1.10000000e-01 | 1.38777878e-17 |
| 1.500 | -5.00000000e-02 | 1.36273764e-01 | 7.33816966e+00 | -5.00000000e-02 | -6.93889390e-18 |

Ajuste fenomenológico do mapa térmico reduzido:

$$
\beta_{\rm eff} \simeq \frac{0.291786}{k_BT/t+0.050000}
$$

MSE em beta: `4.52656229e-03`.

Interpretação: a curva experimental pode ser representada por uma família de ensembles GDQ reduzidos com `beta_eff` variável. Isto resolve a comparação operacional da curva no modelo reduzido, mas a derivação do mapa térmico a partir da Hessiana completa do aparelho continua pendente.
