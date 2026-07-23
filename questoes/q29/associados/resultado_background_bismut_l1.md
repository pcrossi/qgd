# Q29 — Dressing eletromagnético do perfil de Bismut $\ell=1$

## 1. Perfil utilizado

Foi usado o perfil zonal já construído na Q29:

$$
B
=
\left(b_0+\beta\cos\chi\right)
\operatorname{vol}_{S^3},
$$

com

$$
b_0=\frac1{\pi R^3}
=0{,}0398837120568,
$$

de modo que o harmônico $\ell=1$ não altera a classe primitiva

$$
\frac1{2\pi}\int_{S^3}B=1.
$$

O termo torsional foi inserido na redução da ação oficial como

$$
-\frac1{12}|B|^2
=
-\frac12
\left(b_0+\beta\cos\chi\right)^2.
$$

As equações não lineares de $A$ e $F$, a normalização da medida e as condições
de regularidade foram resolvidas simultaneamente por continuação em $\beta$.

## 2. Resultado

Para a amplitude estabilizada anteriormente,

$$
\beta_*=0{,}0108937431,
$$

a norma radial de Hopf passa de

$$
K_Q(0)/C
=41{,}588060281
$$

para

$$
K_Q(\beta_*)/C
=41{,}594825709.
$$

Portanto,

$$
\boxed{
\frac{K_Q(\beta_*)}{K_Q(0)}
=1{,}0001626772.
}
$$

O dressing produzido pelo modo torsional não homogêneo é

$$
\boxed{
\frac{\Delta K_Q}{K_Q}
=1{,}626772\times10^{-4}
=0{,}01626772\%.
}
$$

O solver permaneceu convergente em toda a continuação, com resíduo máximo
aproximadamente $1{,}87\times10^{-5}$.

## 3. Interpretação

O cálculo confirma que a densidade torsional não homogênea veste a rigidez
eletromagnética pela ação oficial. Contudo, o efeito é pequeno e tem sinal
positivo para a orientação escolhida. Ele não produz o fator

$$
0{,}966590303
$$

da construção condicional anterior.

Isso também mostra que a grande susceptibilidade do modelo dilatônico com
fonte delta não representa o perfil suave de Bismut $\ell=1$. São fontes
fisicamente diferentes.

## 4. Circularidade da amplitude usada

A amplitude $\beta_*$ não é independente de $\alpha$ no fechamento atual. A
quártica de interface usada para estabilizá-la contém

$$
S_\partial
=
\alpha
\left(
\frac{3\pi}{2}+\frac{3}{4\pi^3}
\right).
$$

Logo, o resultado acima é um teste de consistência dado o background
eletrofraco previamente calibrado; não pode ser invertido diretamente para
ser anunciado como derivação de $\alpha$.

## 5. Equação de autoconsistência necessária

Para remover a circularidade, deve-se substituir a ocorrência de $\alpha$ na
rigidez de interface pela própria norma geométrica calculada:

$$
\alpha(\beta)
=
\frac{1}{\mathcal C_{\rm em}K_Q(\beta)},
$$

onde $\mathcal C_{\rm em}$ é o fator dimensional e de normalização do gerador
obtido da redução de Hopf. Simultaneamente,

$$
\beta^2
=
-\frac{a_2}
{a_4^{\rm bulk}
+\dfrac{5}{32b_0^4}
\left(
\dfrac{3\pi}{2}+\dfrac{3}{4\pi^3}
\right)\alpha(\beta)}.
$$

Essas duas equações definem o ponto fixo $(\alpha,\beta)$ sem inserir o valor
experimental. O fator $\mathcal C_{\rm em}$ ainda precisa ser fixado pela
normalização absoluta da ação oficial, incluindo $\hbar/\Lambda_C^2$, o
comprimento da curva causal e a normalização do gerador de Hopf.

## 6. Veredito

O perfil de Bismut $\ell=1$ foi inserido e seu dressing foi calculado. Ele é
real, estável e pequeno. A pendência não está mais na resposta torsional, mas
na normalização absoluta $\mathcal C_{\rm em}$ da redução para quatro
dimensões.

O cálculo reproduzível está em `questoes/q29/associados/solve_background_bismut_l1_q29.py`.
