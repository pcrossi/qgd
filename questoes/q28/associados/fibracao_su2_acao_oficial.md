# Q28 — Conexão global derivada da ação oficial

## 1. Ponto de partida

Mantemos integralmente a ação oficial:

$$
\mathcal S_{\rm GDQ}
=\int_\gamma
\left[
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left{
\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n
\right}
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
$$

Nenhum termo fundamental de Yang--Mills é acrescentado. A conexão abaixo é
uma componente fora da diagonal da própria métrica global.

## 2. Ansatz não produto

Escreva localmente o espaço interno como uma fibração

$$
S^3\simeq SU(2)
\longrightarrow K_8
\longrightarrow T^5.
$$

Se $\sigma^a$ são as formas invariantes à esquerda de $SU(2)$, defina

$$
\eta^a
=\sigma^a+A_i^{\ a}(\theta)d\theta^i.
$$

A métrica Hermitiana real subjacente pode ser escrita, no setor interno, como

$$
ds_K^2
=G_{ij}(\theta)d\theta^id\theta^j
+r^2(\theta)\delta_{ab}\eta^a\eta^b.
$$

Quando

$$
A_i^{\ a}=0,
$$

recupera-se o produto $T^5\times S^3$. Para $A\ne0$, a métrica é globalmente
não produto e sua curvatura contém

$$
F^a
=dA^a+\frac12\epsilon^a{}_{bc}A^b\wedge A^c.
$$

## 3. Redução do escalar de curvatura

Para raio constante no primeiro passo, a fórmula de submersão de O'Neill
fornece

$$
\mathcal R_K
=\mathcal R_{T^5}
+\frac{6}{r^2}
-\frac{r^2}{4}F^a_{ij}F_a^{ij}
+\mathcal R_{\rm mod},
$$

onde $\mathcal R_{\rm mod}$ reúne derivadas de $r$, deformações da métrica de
base e termos de drift do dilatão. O termo quadrático em $F$ não foi
postulado: ele é uma componente da curvatura escalar $\mathcal R$ que já
aparece na ação oficial.

Após integrar a fibra, o setor dependente de $A$ é proporcional a

$$
\mathcal S_A
=-\frac{\hbar}{\Lambda_C^2}
\int_\gamma d\tau
\int_{T^5}
\frac{r^5}{4}
\mathcal U_B
F^a_{ij}F_a^{ij}
\sqrt{G}\,d^5\theta,
$$

até a convenção global euclidiana da ação e fatores constantes do volume da
fibra. Para a equação estacionária, apenas o peso positivo

$$
w(\theta,\tau)=r^5\mathcal U_B\sqrt G
$$

é relevante.

## 4. Equação variacional da conexão métrica

Como

$$
\delta F_{ij}=D_i\delta A_j-D_j\delta A_i,
$$

a variação, com os termos de contorno mantidos explicitamente, dá

$$
\delta\mathcal S_A
\propto
\int_{T^5}
\operatorname{tr}
\left[
D_i(wF^{ij})\,\delta A_j
\right]d^5\theta
-\int_{\partial T^5}
w\operatorname{tr}(F^{ij}\delta A_j)n_i.
$$

No toro sem bordo, a equação estacionária derivada da ação oficial é

$$
\boxed{
D_i\left(r^5\mathcal U_BF^{ij}\right)=0.
}
$$

Essa é a equação geométrica para as componentes mistas da métrica GDQ.

## 5. Soluções e setores topológicos

No background homogêneo,

$$
r=\text{constante},
\qquad
\mathcal U_B=\text{constante no toro},
$$

a equação reduz-se a

$$
D_iF^{ij}=0.
$$

Conexões de curvatura covariantemente constante satisfazem essa equação. Sua
classe integral é

$$
a_4
=-\frac{1}{8\pi^2}
\operatorname{tr}(F_T\wedge F_T)
=Ae^{1234}.
$$

Portanto, a ação oficial admite setores estacionários com

$$
A\in\mathbb Z.
$$

Entretanto, a variação é realizada dentro de um setor topológico fixo. Uma
deformação suave de $A_i^{\ a}$ não altera

$$
A
=-\frac{1}{8\pi^2}
\int_{T^4}\operatorname{tr}(F_T\wedge F_T).
$$

Logo, a equação de Euler--Lagrange determina o representante estacionário de
cada setor, mas não escolhe o inteiro topológico entre setores desconectados.

## 6. Relação com o índice geracional

A colagem previamente calculada no ciclo restante fornece

$$
\nu(g)=1.
$$

Assim,

$$
N_{ab}=A\nu(g)=A,
$$

e

$$
N_G=\frac{A}{6}.
$$

Consequentemente,

$$
N_G=3
$$

se e somente se o setor global da métrica satisfizer

$$
\boxed{A=18.}
$$

## 7. O que a ação oficial resolve e o que ela não resolve sozinha

A ação oficial resolve agora três pontos:

1. produz a conexão $A_i^{\ a}$ como parte da métrica;
2. produz sua equação estacionária sem acrescentar outra ação;
3. permite $\mathcal F\ne0$, $a_4\ne0$ e $N_{ab}\ne0$ em backgrounds não
   produto.

Mas a ação local, variada em um setor conexo, não seleciona sozinha o inteiro
$A$. Esse inteiro é uma condição topológica global do domínio, análoga à
escolha do número de circulação de um sóliton. Para derivar $A=18$, é
necessário mostrar que as condições globais já assumidas pela GDQ — colagem
$\mathbb Z_6$, regularidade do estômato e orientação de $S^3$ — admitem um
único setor estável, ou que setores diferentes possuem ações on-shell e a
dinâmica causal seleciona o mínimo admissível.

## 8. Próximo cálculo definido

Para cada inteiro admissível $A$, deve-se resolver

$$
D_i\left(r^5\mathcal U_BF^{ij}\right)=0
$$

e avaliar

$$
\mathcal S_{\rm GDQ}^{\rm on\mbox{-}shell}(A).
$$

O problema das três gerações fica então reduzido à seleção variacional
discreta

$$
\boxed{
A_*
=\operatorname*{argmin}_{A\in\mathcal A_{\mathbb Z_6}}
\mathcal S_{\rm GDQ}^{\rm on\mbox{-}shell}(A),
}
$$

onde $\mathcal A_{\mathbb Z_6}$ é o conjunto de setores compatíveis com a
colagem global e com as condições de regularidade.
