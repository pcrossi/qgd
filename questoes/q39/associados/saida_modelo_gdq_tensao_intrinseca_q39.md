# Q39 — saída do modelo GDQ intrínseco reduzido

## Classificação

Modelo reduzido GDQ intrínseco. Não usa $n_\tau=17$, não usa
Rosen--Morse como seleção de geração e não ajusta $M_\mu$ ou
$M_\tau$ como alvo. A derivação dos cinco pontos está documentada
em `derivacao_gdq_intrinseca_1a5_q39.md`; a elevação 8D completa
permanece condicional.

## 1. Entrada

- `alpha_inv = 137.035999177000`
- `alpha = 7.297352564331424e-03`

## 2. Múon como setor biespacial

Fórmula reduzida:

$$
R_\mu
=
\frac32\alpha^{-1}+\frac65+2\alpha.
$$

- termo dominante `3/(2 alpha) = 205.553998765500012`
- impedância/interface `6/5 = 1.200000000000000`
- autoenergia `2 alpha = 0.014594705128663`
- `R_mu = 206.768593470628673`

## 3. Tau como saturação tridimensional

Condição reduzida:

$$
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23.
$$

- raiz pequena descartada: `6.491919023876937`
- raiz física saturada: `R_tau = 3477.446405098381092`
- amplitude tau `sqrt(R_tau) = 58.969877099230764`
- verificação `Q = 0.666666666666667`

## 4. Comparação

| razão | GDQ reduzido | experimento | erro relativo | Rosen--Morse benchmark |
|---|---:|---:|---:|---:|
| `M_mu/M_e` | 206.768593471 | 206.768282700 | +1.503e-06 | 206.767857700 |
| `M_tau/M_e` | 3477.446405098 | 3477.150000000 | +8.524e-05 | 3477.146514900 |

## 5. Veredito

A rota reduzida por tensão/topologia reproduz os números sem usar
`n_tau=17`. Ela também explica por que existem apenas três setores
físicos no modelo reduzido.

Os cinco pontos foram derivados no modelo reduzido intrínseco em
`derivacao_gdq_intrinseca_1a5_q39.md`. A elevação 8D foi fechada
no background estacionário produto/bloco em
`calcula_background_8d_estacionario_q39.py`, com:

1. `a_W=a_f=a_H=epsilon=0`; 
2. `lambda_B_gap=1/2`; 
3. `m_perp^2=1`, `j_mix=0`, `Delta_Schur=0`; 
4. `R_l^(8)=R_l^(0)` no produto estacionário.

Backgrounds warped/mistos reais permanecem como setores condicionais
a avaliar pelo mesmo critério de Schur, sem pós-ajuste.
