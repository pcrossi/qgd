# Refinamento do gap exterior de referência

## 1. Escopo

Este documento executa o refinamento solicitado em raio cosmológico e
truncamento harmônico para o operador de referência

$$
K_\ell^{(0)}
=-\partial_s^2+\mu^2+\frac{\ell(\ell+2)}{R^2}.
$$

Ele não substitui o potencial matricial da Hessiana oficial no background
warped ainda desconhecido.

## 2. DtN exato

Para $L=\pi R$,

$$
\kappa_{\ell,R}
=\sqrt{\mu^2+\frac{\ell(\ell+2)}{R^2}},
$$

$$
\Lambda_{\ell,R}^{\rm eff,(0)}
=\kappa_{\ell,R}
\tanh(\pi R\kappa_{\ell,R}).
$$

O script `ponte_global_local_gap_referencia.py` avaliou

$$
R=1,10,100,1000
$$

e

$$
\ell_{\max}=4,8,16,32,64.
$$

## 3. Resultado para setor sem limiar

Se $\mu=0$, o modo constante é removido por normalização. O menor modo físico
é $\ell=1$:

$$
\Delta_R^{(0)}
=\frac{\sqrt3}{R}\tanh(\pi\sqrt3).
$$

Portanto,

$$
\boxed{
\Delta_R^{(0)}\sim\frac{\sqrt3}{R}\longrightarrow0.
}
$$

O aumento de $\ell_{\max}$ não altera esse menor autovalor. Logo o espectro
angular global, sozinho, não fornece gap uniforme na descompactificação.

## 4. Resultado com limiar local

Se o background bulk--interface produzir

$$
\mu^2\geq\mu_*^2>0,
$$

então

$$
\Lambda_{\ell,R}^{\rm eff,(0)}
\geq\mu\tanh(\pi R\mu),
$$

e

$$
\boxed{
\lim_{R\to\infty}\Delta_R^{(0)}=\mu.
}
$$

Assim, a uniformidade do gap não pode vir apenas da compactação global. Ela
deve vir do potencial local da Hessiana física do estômato.

## 5. Convergência harmônica

O mínimo estabiliza assim que o menor harmônico físico está incluído. O
truncamento harmônico controla os modos altos e o DtN completo, mas não cria
um gap ausente nos modos baixos.

Para coeficientes suaves, a convergência do DtN truncado deve ser medida em
normas de Sobolev de traço. A tabela numérica do script confirma a monotonia
dos autovalores altos e a invariância do mínimo sob aumento de
$\ell_{\max}$.

## 6. Conclusão

O refinamento do modelo de referência está concluído. Ele produz um critério
necessário inequívoco:

$$
\boxed{
\text{gap uniforme global--local}
\Longrightarrow
\text{limiar local }\mu_*^2>0
\text{ na Hessiana do background BI.}
}
$$

Calcular esse $\mu_*^2$ exige o background global warped. O produto homogêneo
não pode fornecê-lo porque não é ponto crítico da ação normalizada na direção
toroidal.

