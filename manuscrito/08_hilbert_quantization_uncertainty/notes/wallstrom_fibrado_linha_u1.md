---
title: "Prova da quantização de circulação por fibrado U(1)"
---

# Prova da quantização de circulação por fibrado $U(1)$

Esta nota registra a prova técnica usada nas Seções 08.5 e 08.6.

O objetivo é mostrar que a integralidade da circulação não é um postulado
externo de Madelung/Nelson e não vem da soma de Poisson. Ela vem da existência
global da fase física como seção de um fibrado de linha hermitiano.

## 1. Dados do setor regular

Considere um setor regular da GDQ no qual:

1. a densidade é positiva fora do conjunto nodal;
2. a fase local $S_R$ é suave em cada carta;
3. o estado reconstruído é admissível como seção global do setor físico;
4. o domínio físico remove os nós da densidade.

Definimos:

$$
Z_\rho=\{x:\rho(x)=0\},
\qquad
M^\ast=M\setminus Z_\rho.
$$

Em $M^\ast$, a amplitude $\sqrt\rho$ é não nula. Portanto a fase é bem
definida como variável angular:

$$
\chi=\frac{S_R}{\hbar}.
$$

A função física de fase não é $\chi:M^\ast\to\mathbb R$ como função real
global arbitrária. A função física é:

$$
e^{i\chi}:M^\ast\to S^1.
$$

Essa diferença é o ponto central.

## 2. Forma local do estado

Se $L\to M^\ast$ é um fibrado de linha hermitiano, em cada carta
$U_a\subset M^\ast$ escolhemos uma seção local unitária $s_a$ e escrevemos:

$$
\Psi_a
=
\sqrt\rho\,e^{i\chi_a}s_a.
$$

Em uma interseção $U_a\cap U_b$, as seções locais se relacionam por uma função
de transição:

$$
s_a=g_{ab}s_b,
\qquad
g_{ab}:U_a\cap U_b\to U(1).
$$

Como $\Psi$ é seção global, deve valer:

$$
\Psi_a=\Psi_b.
$$

Logo:

$$
\sqrt\rho\,e^{i\chi_a}s_a
=
\sqrt\rho\,e^{i\chi_b}s_b.
$$

Como $\rho>0$ em $M^\ast$:

$$
e^{i\chi_a}g_{ab}
=
e^{i\chi_b}.
$$

Escrevendo:

$$
g_{ab}=e^{i\lambda_{ab}},
$$

temos:

$$
\chi_b-\chi_a
=
\lambda_{ab}
\pmod{2\pi}.
$$

Portanto, a fase local pode mudar de carta por funções angulares, mas o objeto
global $e^{i\chi}$ permanece bem definido.

## 3. Cociclo e integralidade

Em uma tripla interseção $U_a\cap U_b\cap U_c$, as funções de transição devem
satisfazer a condição de cociclo:

$$
g_{ab}g_{bc}g_{ca}=1.
$$

Em fases:

$$
\lambda_{ab}+\lambda_{bc}+\lambda_{ca}
=
2\pi n_{abc},
\qquad
n_{abc}\in\mathbb Z.
$$

Os inteiros $n_{abc}$ representam a obstrução topológica global. Eles definem
a primeira classe de Chern:

$$
c_1(L)\in H^2(M^\ast,\mathbb Z).
$$

É importante verificar que essa classe não depende da escolha dos
levantamentos reais $\lambda_{ab}$. Podemos escolher:

$$
\lambda_{ab}'
=
\lambda_{ab}+2\pi k_{ab},
\qquad
k_{ab}\in\mathbb Z,
$$

sem alterar $g_{ab}$. Na interseção tripla:

$$
\begin{aligned}
\lambda_{ab}'+\lambda_{bc}'+\lambda_{ca}'
&=
\lambda_{ab}+\lambda_{bc}+\lambda_{ca}
+2\pi(k_{ab}+k_{bc}+k_{ca})
\\
&=
2\pi
\left(
n_{abc}+k_{ab}+k_{bc}+k_{ca}
\right).
\end{aligned}
$$

Portanto:

$$
n_{abc}'
=
n_{abc}+k_{ab}+k_{bc}+k_{ca}.
$$

A diferença é o cobordo inteiro da 1-cochain $k$. Assim, embora o
representante $n_{abc}$ dependa dos levantamentos, sua classe não depende:

$$
[n']=[n]
\quad\text{em}\quad
\check H^2(M^\ast,\mathbb Z).
$$

É essa classe, e não um representante isolado, que define $c_1(L)$.

Se $A$ é uma conexão unitária em $L$ e $F_A=dA$ sua curvatura local, então:

$$
c_1(L)
=
\left[
\frac{F_A}{2\pi}
\right]
\in
H^2(M^\ast,\mathbb Z).
$$

Consequentemente, para qualquer 2-ciclo fechado $\Sigma$:

$$
\frac1{2\pi}
\int_\Sigma F_A
\in
\mathbb Z.
$$

Essa é a forma global da quantização.

## 4. Circulação em um ciclo fechado

Considere agora um ciclo fechado $C\subset M^\ast$.

Parametrize o ciclo por $\theta\in[0,2\pi]$. Pela propriedade de levantamento
da cobertura $\mathbb R\to U(1)$, a fase física ao longo desse intervalo
admite um levantamento real contínuo $\chi(\theta)$. Não é necessário supor
que $\chi$ seja linear.

$$
\oint_C d\chi
=
\chi(2\pi)-\chi(0).
$$

Como a quantidade física é $e^{i\chi}$, ao completar o ciclo devemos ter:

$$
e^{i\chi(2\pi)}
=
e^{i\chi(0)}.
$$

Logo:

$$
\chi(2\pi)-\chi(0)=2\pi N,
\qquad
N\in\mathbb Z.
$$

Algebricamente, isso decorre da equivalência:

$$
e^{ix}=e^{iy}
\quad\Longleftrightarrow\quad
x-y\in2\pi\mathbb Z.
$$

Portanto:

$$
\frac1{2\pi}\oint_Cd\chi=N.
$$

Multiplicando por $\hbar$:

$$
\oint_CdS_R
=
2\pi\hbar N
=
Nh.
$$

Essa é exatamente a condição quântica de circulação.

Esse argumento separa duas afirmações:

1. a propriedade de cobertura fornece o levantamento contínuo ao longo do
   intervalo;
2. o fechamento da fase física no ciclo força o incremento inteiro.

A primeira é topológica; a segunda é a periodicidade exata de $U(1)$.

## 5. Por que circulação não inteira não é estado global

Suponha que se tente escrever:

$$
\chi(\theta)=\alpha\theta
$$

em um ciclo angular $\theta\sim\theta+2\pi$.

Então:

$$
e^{i\chi(\theta+2\pi)}
=
e^{i\alpha(\theta+2\pi)}
=
e^{i\alpha\theta}e^{i2\pi\alpha}.
$$

Para que isso represente o mesmo ponto físico de $S^1$ após uma volta:

$$
e^{i2\pi\alpha}=1.
$$

Isso implica:

$$
\alpha\in\mathbb Z.
$$

Se $\alpha\notin\mathbb Z$, a expressão não define um mapa global regular
$S^1\to S^1$. Ela pode ser escrita localmente em um intervalo aberto, mas não
fecha no ciclo.

Logo, a circulação não inteira não é um estado físico global do setor. Ela é
uma expressão local que falha na condição de colagem.

## 6. Papel correto da soma de Poisson

A identidade:

$$
\sum_{m\in\mathbb Z}e^{im\epsilon}
=
2\pi
\sum_{n\in\mathbb Z}\delta(\epsilon-2\pi n)
$$

é verdadeira como distribuição.

Mas ela já pressupõe:

$$
m\in\mathbb Z.
$$

Portanto, ela não prova que os setores são inteiros. Ela apenas expressa a
análise harmônica depois que o grupo de fases já foi identificado como $S^1$.

O fundamento é:

$$
\text{fase global }S^1
\quad\Longrightarrow\quad
\text{caracteres inteiros}
\quad\Longrightarrow\quad
\text{soma de Poisson}.
$$

Não o inverso.

Uma forma regularizada que evita interpretar a série divergente
pontualmente é:

$$
D_\varepsilon(\theta)
=
\sum_{m\in\mathbb Z}
e^{-\varepsilon m^2}e^{im\theta},
\qquad
\varepsilon>0.
$$

Pela soma de Poisson:

$$
D_\varepsilon(\theta)
=
\sqrt{\frac{\pi}{\varepsilon}}
\sum_{n\in\mathbb Z}
\exp\left[
-\frac{(\theta-2\pi n)^2}{4\varepsilon}
\right].
$$

No limite $\varepsilon\downarrow0$, essa família converge no sentido de
distribuições para o pente periódico:

$$
2\pi\sum_{n\in\mathbb Z}\delta(\theta-2\pi n).
$$

Assim, o pente é uma representação distribucional rigorosa dos setores já
inteiros. Ele não é uma função ordinária e não seleciona sozinho a topologia
da fase.

## 7. Relação com a GDQ

Na GDQ, a fase vem de:

$$
S_R
=
\frac{\hbar}{2i}(f-\bar f).
$$

Localmente, as equações de Madelung usam $S_R$ como potencial de fase. Porém,
globalmente, o setor físico admissível exige que:

$$
e^{iS_R/\hbar}
$$

seja uma seção global bem definida.

Assim, a GDQ não precisa acrescentar uma condição externa de univocidade da
função de onda. Ela exige admissibilidade geométrica global do estado
reconstruído.

A condição:

$$
\oint_CdS_R=Nh
$$

é consequência dessa admissibilidade.

Essa passagem também foi certificada formalmente. A reconstrução usada é:

$$
\Psi(f)
=
\sqrt{e^{-\operatorname{Re}f}}\,
e^{i\operatorname{Im}f}.
$$

Logo:

$$
|\Psi(f)|^2
=
e^{-\operatorname{Re}f}
=
\rho(f).
$$

Para um deslocamento imaginário constante:

$$
f\longmapsto f+ic,
$$

a densidade permanece inalterada e a fase sofre a rotação $e^{ic}$. Para
$c=2\pi k$, $k\in\mathbb Z$, o próprio estado reconstruído é idêntico:

$$
\Psi(f+2\pi k i)=\Psi(f).
$$

Se $f:[0,1]\to\mathbb C$ é um laço físico contínuo cuja fase reconstruída
fecha, então:

$$
e^{i\operatorname{Im}f(1)}
=
e^{i\operatorname{Im}f(0)}
$$

implica:

$$
\hbar
\left[
\operatorname{Im}f(1)-\operatorname{Im}f(0)
\right]
=
nh.
$$

Assim, o elo entre o potencial oficial e a circulação não é apenas uma
analogia com a função de onda: ele é uma identidade constitutiva seguida de
um teorema global de levantamento.

É necessário manter a classificação correta. A expressão pontual da ação não
escolhe sozinha a topologia, o domínio excisado ou a cobertura. Esses são
dados globais do problema variacional da GDQ. Uma vez adotada a
admissibilidade global já definida pela teoria, a circulação inteira é
deduzida e não constitui um axioma adicional.

## 8. Limitações da prova

Esta prova fecha Wallstrom no setor escalar regular com fase $U(1)$.

Ela não substitui:

- a construção de setores spinoriais antiperiódicos;
- a prova de spin como circulação/Hopf;
- a estatística fermiônica;
- a resposta de spin a aparelhos;
- a análise de estados com nós singulares além da remoção de $Z_\rho$.

Esses temas exigem estruturas próprias.

## 9. Conclusão

A quantização de circulação segue da cadeia:

$$
\rho>0\text{ em }M^\ast
\to
e^{iS_R/\hbar}:M^\ast\to S^1
\to
\Psi\in\Gamma(L)
\to
g_{ab}:U_a\cap U_b\to U(1)
\to
c_1(L)\in H^2(M^\ast,\mathbb Z)
\to
\frac1{2\pi}\oint_C d(S_R/\hbar)\in\mathbb Z.
$$

Portanto:

$$
\boxed{
\oint_CdS_R=Nh,
\qquad
N\in\mathbb Z.
}
$$
