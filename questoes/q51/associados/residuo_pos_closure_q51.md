# Q51 — Resíduo após o fechamento reduzido `closure_mobility`

## 1. Objetivo

Depois de gerar os fechamentos de camada pelo espectro angular spin--torção e
executar a variante `closure_mobility`, resta medir o erro que ainda precisa
ser explicado pela Hessiana nuclear completa.

O cálculo está em:

- `diagnostico_residuo_pos_closure_q51.py`;
- `saida_diagnostico_residuo_pos_closure_q51.md`.

## 2. Quantidade diagnosticada

Se:

$$
\Delta_i
=
\log_{10}T_{1/2,i}^{\rm GDQ,red}
-
\log_{10}T_{1/2,i}^{\rm exp},
$$

então:

$$
\frac{T_{\rm model}}{T_{\rm exp}}
=
10^{\Delta_i}.
$$

A correção de ação que faltaria, apenas como diagnóstico, é:

$$
\Delta W_i^{\rm falt}
=
-\ln(10)\,\Delta_i.
$$

Ela não é usada para ajustar o modelo.

## 3. Resultado

Na variante `closure_mobility`, o RMS é:

$$
{\rm RMS}=0{,}067894
\quad\text{décadas}.
$$

Todos os casos do dataset diagnóstico ficam com resíduo menor que \(0{,}1\)
década. O caso Po-212 deixa de ser anomalia dominante quando o filho Pb-208,
duplamente fechado, ativa a mobilidade de determinante do canal alfa.

## 4. Interpretação GDQ

O resíduo restante não sugere uma nova barreira universal. Ele aponta para
refinamentos da Hessiana nuclear completa e do dataset:

$$
K_\partial^{\rm phys}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Os termos a refinar devem aparecer em:

1. \(K_{\partial\partial}\), como rigidez local da camada fechada;
2. ou no complemento de Schur, como menor acoplamento entre superfície alfa e
   modos internos do filho fechado;
3. no operador radial completo \(g_{rr}^{\rm eff}\), hoje ainda reduzido;
4. na substituição do dataset diagnóstico por NUBASE/AME/ENSDF auditado.

## 5. Status

$$
\boxed{
\text{o resíduo pós-closure_mobility está abaixo de 0,1 década na série diagnóstica.}
}
$$

Esse resultado autoriza classificar a Q51 como prova de conceito fechada. A
classificação não deve ser confundida com fechamento metrológico final, que
exigirá Hessiana nuclear completa e dataset amplo.
