# Q39 — previsão da terceira ressonância pela condição Koide-GDQ

## Classificação

Avaliação direta da identidade geométrica reduzida. O valor de tau
não entra como alvo.

## Entradas

- `alpha_inv = 137.035999177000`
- `R_e = 1.000000000000000`
- `R_mu = 3/(2 alpha)+6/5+2 alpha = 206.768593470628673`

## Fórmula

Dados `x=sqrt(R1)` e `y=sqrt(R2)`:

$$
R_{3,\pm}
=
\left[
2(x+y)\pm\sqrt{3x^2+12xy+3y^2}
\right]^2.
$$

## Saída

- ramo leve/sombra `R_3_minus = 6.491919023876940`
- ramo pesado/físico `R_3_plus = 3477.446405098382002`
- `Q(R_e,R_mu,R_3_plus) = 0.666666666666667`

## Leitura GDQ

O ramo pesado é o tau no setor leptônico carregado. O ramo leve é uma
solução matemática da mesma condição angular e não deve ser promovido a
partícula sem estabilidade e interpretação pela Hessiana física.
