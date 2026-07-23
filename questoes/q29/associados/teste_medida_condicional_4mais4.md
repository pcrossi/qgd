# Q29 — Teste da medida condicional na redução $8=4+4$

## 1. Coordenadas físicas

Separe coordenadas externas e internas físicas:

$$
X^\mu=\ell_Cx^\mu,
\qquad
Y^a=\ell_Cy^a,
$$

e escreva

$$
\tau=\ell_C^2\widehat\tau,
\qquad
r_H=\ell_CR_H.
$$

O campo eletromagnético físico satisfaz

$$
[A_\mu]=L^{-1},
\qquad
[F_{\mu\nu}]=L^{-2}.
$$

## 2. Redução de O'Neill

A curvatura oito-dimensional contém

$$
\mathcal R_8
\supset
-\frac{r_H^2}{4}|F|^2.
$$

Dimensionalmente,

$$
[r_H^2|F|^2]=L^{-2},
$$

e portanto

$$
\tau r_H^2|F|^2
=
\ell_C^4\widehat\tau R_H^2|F|^2
$$

é adimensional, como deve ser dentro do funcional de Perelman.

## 3. Medida condicional

A proposta correta para não normalizar o espaço-tempo é

$$
d\mu_8(X,Y)
\longrightarrow
dV_4(X)\,d\mu_{\rm int}(Y\mid X),
$$

com

$$
\int_{K_4}d\mu_{\rm int}(Y\mid X)=1.
$$

Assim, o termo eletromagnético reduzido antes do prefator é

$$
-\frac14
\int_{M_4}dV_4,|F|^2
\left[
\tau
\int_{K_4}r_H^2d\mu_{\rm int}
\right].
$$

Como

$$
\left[
\int dV_4|F|^2
\right]=1
$$

e

$$
[\tau r_H^2]=L^4,
$$

o colchete interno que multiplica a ação Maxwell possui dimensão $L^4$.

## 4. Prefator exigido

Para que o coeficiente de Maxwell seja adimensional, o prefator extensivo
necessário é

$$
\boxed{
C_8^{\rm ext}
=
\frac{\hbar}{\ell_C^4}
}
$$

ou, escrevendo $E_C=\hbar c/\ell_C$,

$$
C_8^{\rm ext}
=
\hbar
\left(
\frac{E_C}{\hbar c}
\right)^4.
$$

O prefator oficial escrito como $\hbar/\Lambda_C^2$ não possui essa potência,
quer $\Lambda_C$ seja interpretado como energia, quer como comprimento.

## 5. Teorema de incompatibilidade

Considere simultaneamente:

1. funcional de Perelman com $\tau\mathcal R$ adimensional;
2. medida interna condicional normalizada;
3. medida externa física não normalizada $dV_4$;
4. ação Maxwell padrão.

Então a análise acima impõe unicamente uma densidade global proporcional a
$\ell_C^{-4}$. Portanto,

$$
\boxed{
\text{a medida condicional não pode produzir }Z_C
\text{ a partir de }\hbar/\Lambda_C^2
\text{ sem uma regra dimensional adicional.}
}
$$

Isso é um resultado de no-go dimensional, não uma falha numérica.

## 6. Forma mínima dimensionalmente consistente

Mantendo intacto o funcional geométrico $\mathcal W_{\rm GDQ}$ e todas as
suas equações, a reconstrução extensiva deve ser escrita como

$$
\mathcal S_{\rm phys}
=
\frac{\hbar}{\ell_C^4}
\int_{M_4}dV_4\,
\mathfrak P_\gamma
\left[
\int_{K_4}\mathscr W_8d\mu_{\rm int}
\right].
$$

Essa expressão não altera a dinâmica adimensional já derivada, mas corrige a
regra de reconstrução de uma ação extensiva em quatro dimensões.

Para o setor de Hopf,

$$
\frac1{e^2}
=
\frac{\tau r_H^2}{\ell_C^4}
\left\langle e^{3A}\right\rangle_{\mu_{\rm int}}
=
\widehat\tau R_H^2
\left\langle e^{3A}\right\rangle.
$$

Na notação numérica anterior, isso é justamente

$$
\frac1{e^2}=\mathcal K_Q
$$

se $\widehat\tau=1$. O resultado continua

$$
\alpha^{-1}=4\pi\mathcal K_Q\simeq522{,}697,
$$

mostrando que a correção dimensional remove unidades incorretas, mas não gera
o fator numérico $Z_C\simeq0{,}253412$.

## 7. Consequência física

A diferença não pode vir de Weyl, pois Maxwell é conforme em quatro
dimensões. Ela precisa vir de uma destas estruturas ainda não calculadas:

1. a projeção correta do modo de Hopf sobre o fóton canônico depois da mistura
   $W^3$--$Y$;
2. a distinção entre o raio $R_H$ usado no solver radial e o comprimento da
   órbita eletromagnética na métrica de Berger;
3. uma normalização condicional do gerador após a quebra, diferente da norma
   topológica inteira mas derivada da matriz cinética $W/Y$.

Esses três itens pertencem ao mesmo cálculo: diagonalizar a matriz cinética
eletrofraca on-shell e ler a norma do autovetor fotônico. Não se deve procurar
o fator restante no jacobiano dimensional.
