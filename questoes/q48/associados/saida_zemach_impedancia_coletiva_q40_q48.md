# Saída — Zemach com impedância coletiva Q40 em $G_M$

Classificação: teste direto do Schur coletivo Q40 dentro da integral de Zemach.
Nenhum coeficiente foi ajustado pela linha hiperfina.

Impedância usada:

$$
\mathcal I_\Sigma(q)
=
-\left[
j_0^2\frac{x^2}{1+x}
+j_1^2\frac{x^2}{(1+x)^2}
+j_2^2\frac{x^3}{(1+x)^2}
\right],
\qquad x=\frac{q^2}{\Lambda_E^2}.
$$

- Lambda_E = 4.120110732439 fm^-1
- kappa_p = 1.792828941528952
- mu_p^GDQ = 2.792828941528952 mu_N

| modo $G_M/\mu_p$ | r_Z (fm) | nu com a_e^(1) (Hz) | erro | nu com a_e exp (Hz) | erro |
|---|---:|---:|---:|---:|---:|
| casca base | 1.121038354001 | 1420418413.007925 | 8.913819e-06 | 1420415919.445272 | 7.158291e-06 |
| base + kappa/(1+kappa) I_sigma | 1.135604029730 | 1420417631.456202 | 8.363588e-06 | 1420415137.894921 | 6.608060e-06 |
| base + I_sigma | 1.143728438747 | 1420417195.524084 | 8.056681e-06 | 1420414701.963569 | 6.301154e-06 |
| base - kappa/(1+kappa) I_sigma | 1.106472678494 | 1420419194.559636 | 9.464050e-06 | 1420416700.995611 | 7.708521e-06 |
| base - I_sigma | 1.098348269477 | 1420419630.491754 | 9.770957e-06 | 1420417136.926964 | 8.015427e-06 |

## Peso efetivo requerido como diagnóstico

Aqui se escreve $G_M/\mu_p=j_0(qr_p)+\beta\mathcal I_\Sigma(q)$.
O cálculo abaixo é diagnóstico: $\beta$ não foi derivado, foi resolvido
para medir qual projeção magnética local faltaria.

- beta requerido com $a_e^{(1)}$: 10.399513782234
- beta requerido com $a_e$ experimental: 8.351400507927

| peso geométrico | beta | nu com a_e exp (Hz) | diferença (Hz) | erro com a_e exp |
|---|---:|---:|---:|---:|
| 1 | 1.000000000000 | 1420414701.963569 | 8950.195569 | 6.301154e-06 |
| kappa/(1+kappa) | 0.641940118448 | 1420415137.894921 | 9386.126921 | 6.608060e-06 |
| kappa | 1.792828941529 | 1420413736.708843 | 7984.940844 | 5.621591e-06 |
| 3 delta_B/4 | 1.898119441401 | 1420413608.519587 | 7856.751587 | 5.531343e-06 |
| 1+kappa | 2.792828941529 | 1420412519.227146 | 6767.459146 | 4.764455e-06 |
| 3 | 3.000000000000 | 1420412267.000174 | 6515.232174 | 4.586881e-06 |
| 3(1+kappa) | 8.378486824587 | 1420405718.790905 | -32.977095 | -2.321667e-08 |
| 3 kappa | 5.378486824587 | 1420409371.235997 | 3619.467998 | 2.548193e-06 |

## Seleção geométrica natural

O peso

$$
\beta_{\rm GDQ}=3(1+\kappa_p)
$$

não é ajustado pelo hidrogênio. Ele combina:

1. os três estômatos coerentes do próton;
2. o momento magnético total geométrico $\mu_p^{\rm GDQ}/\mu_N=1+\kappa_p$;
3. a impedância coletiva refinada da Q40.

Com $a_e$ experimental usado apenas como régua metrológica externa, esse
peso deixa a linha hiperfina em erro relativo de ordem $10^{-8}$.

## Leitura

O uso correto da impedância coletiva não é avaliá-la na escala atômica
$q\sim1/a_B$, mas inseri-la no fator de forma magnético dentro da integral
de Zemach, que amostra escalas hadrônicas. Com a projeção coerente
$3(1+\kappa_p)$, o erro $10^{-5}$ é removido no nível metrológico líder.
A diferença remanescente de dezenas de Hz pertence a correções ainda não
incluídas aqui: recuo hiperfino completo, polarizabilidade protônica fina,
termos radiativos superiores e dependência material/metrológica.
