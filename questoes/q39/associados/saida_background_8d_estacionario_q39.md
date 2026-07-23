# Q39 — avaliação direta do background leptônico 8D estacionário

## Classificação

Avaliação direta de quantidade já derivada no background estacionário
produto/bloco da GDQ. Não é engenharia inversa e não usa alvo
experimental. A normalização usada é a normalização primitiva comum
`C_gamma=tau=R_max=1`.

## Background avaliado

O background estacionário leptônico produto é:

$$
g_8=g_B\oplus g_K,
\qquad
K=T^5\text{ plano},
$$

$$
A(k)=\text{constante},
\qquad
f_K(k)=\text{constante},
\qquad
H_{BK}=0,
\qquad
\mathcal C_{BK}=0.
$$

Portanto o background não possui warp interno, dilaton interno
não homogêneo, torção mista nem bloco métrico misto.

## Valores físicos extraídos

| quantidade | valor | origem |
|---|---:|---|
| `a_W=||nabla_K A||_infty` | `0` | `A(k)` constante |
| `a_f=||nabla_K f_K||_infty` | `0` | `f_K(k)` constante |
| `a_H=||H_BK||_infty` | `0` | torção sem bloco misto |
| `epsilon=||C_BK||` | `0` | métrica produto |
| `lambda_B_gap` | `0.5` | gap físico conservador `Delta_0=1/2` da ponte C3 |

O gap horizontal/radial reduzido também dá `3/2` em `tau=1`, mas
o critério de Schur deve usar o menor gap físico disponível. Por isso
foi usado o valor conservador:

$$
\lambda_B^{\rm gap}=\Delta_0=\frac12.
$$

## Critério de Schur

$$
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\left(c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\varepsilon^2\right).
$$

$$
j_{\rm mix}=b_Wa_W+b_fa_f+b_Ha_H+b_C\varepsilon.
$$

No background avaliado:

- `m_perp^2 = 1`;
- `j_mix = 0`;
- `Delta_Schur = 0`;
- `Delta_Schur/lambda_B_gap = 0`.

Logo:

$$
\frac{j_{\rm mix}^2}{m_\perp^2}
=
0
<
\frac12.
$$

O setor é subcrítico de forma exata.

## Massas relativas resultantes

Como o complemento de Schur é nulo, as razões 8D coincidem com as
razões reduzidas intrínsecas:

| lépton | razão 8D |
|---|---:|
| `e` | `1.000000000000000` |
| `mu` | `206.768593470628673` |
| `tau` | `3477.446405098381092` |

## Veredito

Para o background leptônico 8D estacionário produto, os valores físicos
pedidos são:

$$
a_W=a_f=a_H=\varepsilon=0,
\qquad
\lambda_B^{\rm gap}=\frac12.
$$

Portanto a expansão 8D fecha sem deslocamento de massa:

$$
R_\ell^{(8)}=R_\ell^{(0)}.
$$

Backgrounds warped/mistos reais, caso sejam introduzidos depois, não
reabrem este resultado; eles devem ser avaliados por este mesmo critério
e só alteram a hierarquia se produzirem `j_mix != 0` sub/supercrítico.
