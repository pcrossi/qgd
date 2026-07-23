# Q51 — No-go para modelos escalares simples de superfície

## 1. Pergunta

Depois de identificar o resíduo da Q51 como overlap/preformação de superfície,
testamos se ele poderia ser representado por uma fórmula escalar simples:

$$
E_\partial
=
F(A,Z,Q_\alpha).
$$

Esse teste não é derivação. É auditoria.

## 2. Escalares testados

Foram avaliados:

1. mismatch de contato:

$$
\delta_{\rm touch}
=
\frac{R_{\rm touch}-R_{\rm pai}}{R_{\rm pai}};
$$

2. altura relativa da barreira no raio de contato:

$$
x_{\rm barrier}
=
\frac{V_C(R_{\rm touch})}{Q_\alpha}-1;
$$

3. suavidade de curvatura:

$$
\chi_{\rm curv}
=
\frac{\delta_{\rm touch}^2}{x_{\rm barrier}};
$$

4. fissilidade reduzida:

$$
\frac{Z^2}{A};
$$

5. indicador diagnóstico de filha mágica \(^{208}{\rm Pb}\).

## 3. Resultado

A saída está em:

- `saida_teste_modelos_escalares_superficie_q51.md`.

O resultado mostra que escalares simples carregam alguma informação, mas não
constituem uma lei GDQ. Quando o indicador de camada entra, o ajuste melhora
porque a informação estrutural do espectro nuclear foi inserida externamente.

## 4. Interpretação

Na GDQ, a camada fechada, deformação, impedância e overlap não devem entrar
como etiquetas discretas. Elas devem emergir do operador:

$$
\mathsf R_\partial^{\rm GDQ}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

E do projetor:

$$
P_\perp\Phi_{4N}.
$$

Logo:

$$
E_\partial^{\rm GDQ}
=
\langle
P_\perp\Phi_{4N},
\mathsf R_\partial^{\rm GDQ}
P_\perp\Phi_{4N}
\rangle_\partial.
$$

## 5. Veredito

$$
\boxed{
\text{não devemos fechar Q51 com uma fórmula escalar ajustada.}
}
$$

O fechamento deve vir do operador de superfície. O teste escalar serve apenas
para confirmar que a informação ausente é estrutural.

