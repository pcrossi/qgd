# Saída — Q76 toy quase real de estabilidade

Classificação: estimativa fenomenológica parametrizada / engenharia reduzida.

O cálculo não deriva um hardware real. Ele estima quais escalas a Hessiana
GDQ teria que produzir para que o qubit geométrico fosse competitivo.

## Fórmulas usadas

$$
\epsilon_{\rm leak}\simeq\left(\frac{\|J\|}{\Delta_{\rm gap}}\right)^2,
\qquad
\epsilon_{\rm th}\simeq e^{-hf_{\rm gap}/k_BT},
$$

$$
\epsilon_{\rm nonad}\simeq
\left(
\frac{1}{2\pi f_{\rm gap}t_{\rm gate}}
\right)^2,
\qquad
\epsilon_{\rm axis}\simeq\frac{\delta\theta^2}{6}.
$$

$$
\epsilon_\phi\simeq1-e^{-t_{\rm gate}/T_2}.
$$

## Cenários

| cenário | f_gap GHz | T K | J/Delta | gate ns | T2 us | beta_gap | leak | thermal | nonad | axis | dephase | readout | erro total | fidelidade |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| criogenico_controlado | 5 | 0.015 | 0.01 | 40 | 50 | 15.9975 | 1.000e-04 | 1.128e-07 | 6.333e-07 | 4.167e-06 | 7.997e-04 | 1.000e-03 | 1.905e-03 | 0.998095407 |
| spin_frio_gap_maior | 20 | 0.1 | 0.003 | 100 | 1e+03 | 9.59849 | 9.000e-06 | 6.783e-05 | 6.333e-09 | 6.667e-07 | 1.000e-04 | 5.000e-04 | 6.775e-04 | 0.999322501 |
| temperatura_4K_gap_alto | 500 | 4 | 0.001 | 5 | 100 | 5.99905 | 1.000e-06 | 2.481e-03 | 4.053e-09 | 1.667e-07 | 5.000e-05 | 1.000e-04 | 2.632e-03 | 0.997367732 |
| ambiente_exigente_gap_THz | 5e+04 | 300 | 0.0001 | 1 | 1e+06 | 7.99874 | 1.000e-08 | 3.359e-04 | 1.013e-11 | 4.167e-08 | 1.000e-09 | 1.000e-05 | 3.459e-04 | 0.999654061 |

## Leitura dos resultados

1. Em regime criogênico, o erro térmico já pode ser muito pequeno se
   $hf_{\rm gap}\gg k_BT$; os termos dominantes passam a ser readout,
   dephasing e vazamento.
2. Em $4\,{\rm K}$, é necessário gap de centenas de GHz para tornar o termo
   térmico pequeno.
3. Em temperatura ambiente, a escala térmica é aproximadamente
   $k_BT/h\simeq6251\,{\rm GHz}$; por isso o toy exige gap em dezenas de THz
   ou uma proteção topológica que reduza o acoplamento térmico efetivo.
4. O caminho GDQ a testar é produzir grande $\Delta_{\rm gap}$ e pequeno
   $J$ pela Hessiana/contorno, não declarar estabilidade absoluta.

$$
\boxed{
\text{toy quase real: promissor se }\Delta_{\rm gap}\text{ cresce e }J/\Delta\text{ cai; não prova hardware ainda.}
}
$$
