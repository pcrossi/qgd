# Q29 — Resposta localizada do dilatão no estômato

## 1. Objetivo

Preservar o background e todas as derivações anteriores, acrescentando apenas
o setor linear causado por um defeito causal localizado. Escreva

$$
f(y;z)=f_*(y)+c(y)\log(z-z_*)+\cdots.
$$

A normalização da medida exige retirar o modo constante:

$$
\langle c\rangle_{\mathcal U_*}=0.
$$

## 2. Fonte compatível

Na redução radial principal, use o operador ponderado

$$
L_f^{(0)}c
=-\frac1\mu\frac{d}{d\chi}
\left(p\frac{dc}{d\chi}\right),
\qquad
p=\frac\mu{R^2},
$$

com

$$
\mu(\chi)
\propto e^{-F(\chi)}\sin^2\chi,
\qquad
\int_\epsilon^\pi\mu d\chi=1.
$$

A fonte unitária no estômato deve ser compensada para obedecer à condição de
solvabilidade de Neumann:

$$
J_{\rm stoma}
=\delta_{\chi=\epsilon}-\mu(\chi).
$$

Equivalentemente,

$$
p(\epsilon)c'(\epsilon)=-1,
\qquad
p(\pi)c'(\pi)=0,
$$

e o termo distribuído preserva a carga total zero.

## 3. Resíduo projetado

A inserção eletromagnética radial, salvo fatores constantes, é

$$
\Phi_Q(\chi)=R^2e^{3A(\chi)}.
$$

Ao normalizar a medida perturbada, o coeficiente do logaritmo em $F_Q(z)$ é a
covariância

$$
\boxed{
\operatorname{Res}_{z_*}F_Q
=-m\,\operatorname{Cov}_{\mu}(\Phi_Q,c),
}
$$

onde $m$ é a amplitude topológica/causal da monodromia.

## 4. Resultado numérico por fonte unitária

O solver principal encontrou

$$
\langle c\rangle_\mu\simeq0,
\qquad
p(\epsilon)c'(\epsilon)\simeq-1,
$$

e uma covariância não nula. Portanto, o cancelamento do setor homogêneo é
quebrado por uma resposta espacialmente localizada:

$$
\boxed{
\operatorname{Cov}_{\mu}(\Phi_Q,c)\ne0.
}
$$

Esse é o primeiro requisito para gerar um resíduo eletromagnético sem alterar
a ação oficial nem os resultados espectrais anteriores.

Numericamente,

$$
\langle\Phi_Q\rangle=41{,}5682188582,
$$

$$
\operatorname{Cov}_\mu(\Phi_Q,c)
=-17{,}1214968064,
$$

e

$$
\boxed{
\frac{\operatorname{Cov}_\mu(\Phi_Q,c)}
{\langle\Phi_Q\rangle}
=-0{,}4118891133.
}
$$

### Convergência

| pontos | covariância | susceptibilidade relativa |
|---:|---:|---:|
| 5000 | $-17{,}121503393$ | $-0{,}4118892151$ |
| 10000 | $-17{,}121498123$ | $-0{,}4118891336$ |
| 20000 | $-17{,}121496806$ | $-0{,}4118891133$ |
| 40000 | $-17{,}121496477$ | $-0{,}4118891082$ |

A resposta está numericamente convergida.

## 5. Alcance e próximo bloco

O cálculo usa a parte principal ponderada de $L_f$. Para fechamento, ainda é
necessário:

1. acrescentar o potencial completo $V_{\rm eff}$ da Hessiana dilatônica Q32;
2. derivar a fonte $J_{\rm stoma}$ da condição de salto, em vez de fixar sua
   amplitude como unidade;
3. determinar $m$ pela monodromia admissível ($\mathbb Z$, $\mathbb Z_6$ ou
   circulação de Hopf);
4. inserir o resíduo na integral causal e calcular $K_Q$.

O resultado atual é uma susceptibilidade do background, não um ajuste de
$\alpha$.

Correção posterior: essa susceptibilidade não é diretamente um resíduo de uma
função logarítmica. Ela foi reconstruída como soma $\sum Res_n/\lambda_n$ do
resolvente físico; ver `q29/resolvente_e_residuos_dilaton.md`.
