---
title: "Quantização relativa, ação exponenciada e termo de extremidade"
---

# Quantização relativa, ação exponenciada e termo de extremidade

## 1. O problema

A prova por fibrado $U(1)$ mostra que uma fase circular global possui
circulação inteira. Resta uma pergunta mais refinada: seria possível obter a
integralidade diretamente da ação oficial, sem usar previamente o fechamento
da fase?

A resposta exige separar o que é local do que é global. A ação oficial
fornece uma corrente contínua. A integralidade surge apenas quando essa
corrente é combinada com uma identificação global dos extremos da história.

## 2. Domínio regular e seus bordos

Seja

$$
M^\circ
=
\mathcal M_{\mathbb C}\setminus Z,
$$

onde $Z$ contém os defeitos ou pontos nos quais a descrição geométrica deixa
de ser regular. Depois da reconstrução global--local, considere uma região
$\Omega$ entre duas folhas físicas $\Sigma_1$ e $\Sigma_2$:

$$
\partial\Omega
=
\Sigma_2
\sqcup(-\Sigma_1)
\sqcup\mathcal B_\infty
\sqcup\mathcal B_{\rm st}
\sqcup\mathcal B_{\rm app}.
$$

Os três bordos laterais representam, respectivamente, o infinito, a
interface do estômato e a interface com o aparelho.

As condições variacionais admissíveis são:

1. fixar $S_R$ no bordo;
2. impor fluxo normal nulo;
3. equilibrar os fluxos dos dois lados de uma interface;
4. contabilizar no aparelho o fluxo que deixa o objeto.

## 3. Corrente derivada da ação oficial

Usamos

$$
f=-\ln\rho+\frac{i}{\hbar}S_R,
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
$$

As derivadas são

$$
\partial_\mu f
=
-\partial_\mu\ln\rho
+\frac{i}{\hbar}\partial_\mu S_R
$$

e

$$
\partial_{\bar\nu}\bar f
=
-\partial_{\bar\nu}\ln\rho
-\frac{i}{\hbar}\partial_{\bar\nu}S_R.
$$

Consequentemente,

$$
\begin{aligned}
g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
={}&
g^{\mu\bar\nu}
\partial_\mu\ln\rho
\partial_{\bar\nu}\ln\rho
\\
&+
\frac{1}{\hbar^2}
g^{\mu\bar\nu}
\partial_\mu S_R
\partial_{\bar\nu}S_R
\\
&+
\frac{i}{\hbar}
g^{\mu\bar\nu}
\left(
\partial_\mu\ln\rho\,
\partial_{\bar\nu}S_R
-
\partial_\mu S_R\,
\partial_{\bar\nu}\ln\rho
\right).
\end{aligned}
$$

No funcional real admissível, o último termo é cancelado por sua parcela
conjugada. A contribuição quadrática real da fase é, portanto, o segundo
termo.

Mantendo $\rho$, $g$, $z_\tau$ e o contorno fixos, a parcela da ação que
depende de $S_R$ é

$$
\mathcal S_S
=
\int_\gamma\int_{M^\circ}
\frac{\tau}{\hbar\Lambda_C^2}
\mathcal U\,
g^{\mu\bar\nu}
\partial_\mu S_R
\partial_{\bar\nu}S_R
\,dV_g\,\frac{d\tau}{\tau}.
$$

Para

$$
S_R\longmapsto S_R+\varepsilon\eta,
$$

a primeira variação é

$$
\delta\mathcal S_S
=
\int_\gamma\int_{M^\circ}
\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,
g^{\mu\bar\nu}
\partial_\mu\eta
\partial_{\bar\nu}S_R
\,dV_g\,\frac{d\tau}{\tau}.
$$

Definimos

$$
\widehat J_S^\mu
=
\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,
g^{\mu\bar\nu}
\partial_{\bar\nu}S_R.
$$

Integrando por partes,

$$
\begin{aligned}
\delta\mathcal S_S
={}&
-\int_\gamma\int_{M^\circ}
\eta\,\nabla_\mu\widehat J_S^\mu
\,dV_g\,\frac{d\tau}{\tau}
\\
&+
\int_\gamma\int_{\partial M^\circ}
\eta\,n_\mu\widehat J_S^\mu
\,d\Sigma\,\frac{d\tau}{\tau}.
\end{aligned}
$$

No interior:

$$
\boxed{
\nabla_\mu\widehat J_S^\mu=0.
}
$$

Essa é a corrente de Noether da simetria contínua
$S_R\mapsto S_R+S_0$.

## 4. Momento normal, carga e forma pré-simplética

O termo de bordo identifica

$$
\Pi_{S_R}
=
n_\mu\widehat J_S^\mu.
$$

Numa folha:

$$
\Theta_{\Sigma,S}
=
\int_\Sigma
\Pi_{S_R}\,\delta S_R\,d\Sigma,
$$

e

$$
\Omega_{\Sigma,S}
=
\int_\Sigma
\delta\Pi_{S_R}\wedge\delta S_R\,d\Sigma.
$$

Como

$$
\Pi_{S_R}
=
\rho\,
\frac{2\tau}{\hbar\Lambda_C^2(4\pi z_\tau)^n}
n_\mu g^{\mu\bar\nu}
\partial_{\bar\nu}S_R,
$$

temos, em geral,

$$
\boxed{
\Pi_{S_R}\ne\rho
\quad\text{off shell}.
}
$$

A carga usada nesta prova é a carga de Noether:

$$
Q_S[\Sigma]
=
\int_\Sigma\Pi_{S_R}\,d\Sigma.
$$

Ela não é substituída pela normalização de $\rho$.

## 5. Conservação e fluxo de interface

Stokes fornece

$$
Q_S[\Sigma_2]-Q_S[\Sigma_1]
=
-\left(
\Phi_\infty+\Phi_{\rm st}+\Phi_{\rm app}
\right).
$$

Para um sistema fechado:

$$
\Phi_\infty+\Phi_{\rm st}+\Phi_{\rm app}=0
$$

e, portanto,

$$
Q_S[\Sigma_2]=Q_S[\Sigma_1].
$$

Num experimento aberto, a carga do objeto pode mudar. A quantidade conservada
é a carga do sistema objeto--aparelho, pois o fluxo que sai de um lado entra
no outro com orientação oposta.

## 6. O no-go da simetria local

Considere um deslocamento constante durante toda a história:

$$
S_R'(t,x)=S_R(t,x)+c,
\qquad c\in\mathbb R.
$$

Como

$$
dS_R'=dS_R,
\qquad
\partial_tS_R'=\partial_tS_R,
$$

temos exatamente

$$
\mathcal S_{\rm GDQ}[S_R+c]
=
\mathcal S_{\rm GDQ}[S_R]
$$

e

$$
I_{\rm red}[S_R+c]
=
I_{\rm red}[S_R].
$$

Isso vale para qualquer $c$ real. Logo:

$$
\boxed{
\text{a simetria contínua local não seleciona }h\mathbb Z.
}
$$

## 7. Interpolação canônica e termo de extremidade

Agora considere

$$
S_R'(t,x)
=
S_R(t,x)+a(t)\Delta S_R.
$$

A forma canônica da ação reduzida é

$$
I_{\rm red}
=
\int_{t_1}^{t_2}dt
\left[
\int_{\Sigma_t}
\Pi_{S_R}\partial_tS_R\,d\Sigma
-H_{\rm red}
\right].
$$

Se:

1. $H_{\rm red}$ depende de $\Pi_{S_R}$ e dos gradientes espaciais de $S_R$,
   mas não de seu valor absoluto;
2. $\Pi_{S_R}$ não é alterado;
3. $Q_S$ é conservada;

então

$$
\begin{aligned}
\Delta I_{\rm red}
&=
\int_{t_1}^{t_2}
Q_S\dot a\,\Delta S_R\,dt
\\
&=
Q_S\Delta S_R
\left[a(t_2)-a(t_1)\right].
\end{aligned}
$$

Para

$$
a(t_1)=0,
\qquad
a(t_2)=1,
$$

resulta

$$
\boxed{
\Delta I_{\rm red}=Q_S\Delta S_R.
}
$$

Esse termo pertence à interpolação dependente do tempo. Ele não deve ser
atribuído ao deslocamento constante da história, cuja mudança é zero.

## 8. Teorema de quantização relativa

Suponha agora:

1. reconstrução de uma ação lorentziana real $I_{\rm phys}$;
2. peso físico $\exp(iI_{\rm phys}/\hbar)$;
3. identificação global dos dois extremos;
4. ausência de outros termos na mudança da ação.

A independência da amplitude em relação ao representante exige

$$
\exp\left(
\frac{iQ_S\Delta S_R}{\hbar}
\right)=1.
$$

Como

$$
e^{ix}=1
\quad\Longleftrightarrow\quad
x=2\pi n,
\qquad n\in\mathbb Z,
$$

obtemos

$$
\boxed{
Q_S\Delta S_R
=
2\pi\hbar n
=
nh.
}
$$

Esse é o resultado geral. Se o setor primitivo foi selecionado
independentemente como

$$
Q_S=1,
$$

então

$$
\boxed{
\Delta S_R=nh.
}
$$

## 9. O que significa “setor primitivo”

Suponha que as cargas admissíveis formem

$$
\Gamma_Q=q_0\mathbb Z,
\qquad q_0>0.
$$

O setor primitivo positivo possui $Q_S=q_0$. Escolher unidades em que
$q_0=1$ permite escrever $Q_S=1$.

Para que isso seja uma seleção física, e não uma normalização escolhida pelo
resultado, é preciso demonstrar:

1. discreção de $\Gamma_Q$;
2. existência de um menor gerador positivo;
3. orientação do gerador;
4. ausência de uma cobertura múltipla não resolvida.

A simetria local contínua não prova esses itens. Eles vêm da topologia global,
do fibrado ou do contorno admissível.

## 10. Relação com a prova por $U(1)$

As duas provas não competem:

1. a prova por fibrado $U(1)$ mostra diretamente
   $\Delta S_R\in h\mathbb Z$ para uma fase circular admissível;
2. a prova pela ação exponenciada mostra a forma mais geral
   $Q_S\Delta S_R\in h\mathbb Z$ num problema relativo de bordo.

No setor primitivo circular, ambas coincidem. Em sistemas com interface ou
carga relativa, a segunda forma conserva a informação de $Q_S$.

## 11. Classes de background

| Classe | Hipótese global | Conclusão |
|---|---|---|
| circular | fase $U(1)$ global | $\Delta S_R\in h\mathbb Z$ |
| relativa/de bordo | extremos identificados e $Q_S$ conservada | $Q_S\Delta S_R\in h\mathbb Z$ |
| trivial | fase real global sem defeito | $\Delta S_R=0$ |
| spinorial/Hopf | cobertura dupla | meia-monodromia |
| aberta | fuga não contabilizada | não há carga global do objeto |
| obstruída | sem folha ou ação física real | teorema inaplicável |

## 12. Verificação mecânica

A camada algébrica foi formalizada em Lean 4 no módulo canônico
[BoundaryPhaseQuantization.lean](../../../formal/GDQ/BoundaryPhaseQuantization.lean).

O módulo certifica:

1. conservação sob fluxo lateral nulo;
2. conservação do sistema objeto--aparelho;
3. mudança nula para o deslocamento constante;
4. termo $Q_S\Delta S_R$ na interpolação;
5. quantização relativa;
6. redução ao setor primitivo;
7. classificação conservadora dos backgrounds.

A formalização não substitui as hipóteses geométricas declaradas nesta nota.
Ela verifica que, uma vez fornecidas, a conclusão algébrica segue sem etapas
ocultas.
