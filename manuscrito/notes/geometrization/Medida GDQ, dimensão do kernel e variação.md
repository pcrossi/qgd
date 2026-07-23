---
title: "Medida GDQ, dimensão do kernel e variação"
tipo: derivacao
status: identidade-exata
---

# Medida GDQ, dimensão do kernel e variação

Em dimensão real $d$, o kernel plano do calor possui o prefator

$$
(4\pi\tau)^{-d/2}.
$$

Como $d=2n$, ele se torna $(4\pi\tau)^{-n}$; com $n=4$,
$(4\pi\tau)^{-4}$.

A medida complexificada é

$$
\mathcal U
=(4\pi z_\tau)^{-n}e^{-(f+\bar f)/2}.
$$

Como a densidade material é definida por

$$
\rho=e^{-(f+\bar f)/2},
$$

a relação correta entre a medida da ação e a densidade é

$$
\boxed{
\mathcal U
=\frac{\rho}{(4\pi z_\tau)^n}.
}
$$

Portanto a frase curta “$\mathcal U=\rho$” só é correta se o fator de kernel
tiver sido removido por definição. Definindo

$$
\widetilde{\mathcal U}
:=(4\pi z_\tau)^n\mathcal U,
$$

temos

$$
\boxed{
\widetilde{\mathcal U}=\rho.
}
$$

Esse ponto é importante porque $\mathcal U$ e $\rho$ não são dois campos
independentes que precisariam ser identificados por uma equação dinâmica. Ambos
vêm do mesmo campo fundamental $f$; $\mathcal U$ é a densidade $\rho$
acompanhada do peso de kernel geométrico.

Com $z_\tau$ fixo,

$$
\delta\mathcal U
=-\frac12\mathcal U(\delta f+\delta\bar f).
$$

Se a métrica varia, o elemento de volume contribui separadamente:

$$
\delta\sqrt{\det g}
=\frac12\sqrt{\det g}\,g^{AB}\delta g_{AB}
$$

em coordenadas reais, com a forma Hermitiana correspondente.

## Rota secundária por unicidade

Embora a GDQ não precise provar $\widetilde{\mathcal U}=\rho$ por evolução,
podemos registrar a rota dinâmica para evitar ambiguidade lógica.

Suponha que duas funções $u_1$ e $u_2$ satisfaçam a mesma equação de transporte
no mesmo domínio:

$$
\partial_\tau u+\nabla_A(uv^A)=0,
$$

em

$$
M=\mathbb R^4\times T^4,
$$

com $v$ suficientemente regular, por exemplo

$$
v\in L^1([0,T];W^{1,\infty}_{\rm loc}(M)),
$$

e

$$
u_1,u_2\in L^\infty([0,T];L^1(M)).
$$

Assuma ainda periodicidade no setor $T^4$, decaimento suficiente no setor
$\mathbb R^4$ e nenhum fluxo de bordo não contabilizado pelo contorno causal
$\gamma$. Se

$$
u_1(\tau_0,x)=u_2(\tau_0,x),
$$

então $w=u_1-u_2$ satisfaz

$$
\partial_\tau w+\nabla_A(wv^A)=0,
\qquad
w(\tau_0,x)=0.
$$

Pela unicidade da equação linear de transporte nessa classe,

$$
w(\tau,x)=0.
$$

Aplicando isso a

$$
u_1=\widetilde{\mathcal U},
\qquad
u_2=\rho,
$$

obteríamos novamente

$$
\widetilde{\mathcal U}=\rho.
$$

Mas essa prova é secundária: ela exige as mesmas condições iniciais e de
contorno. A identidade usada na ação oficial é mais forte, pois é
constitutiva.

## Relação com Born

No setor projetivo de Madelung, escreve-se

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Então

$$
|\Psi|^2=\rho.
$$

Logo a densidade probabilística local da camada efetiva é $\rho$, enquanto
$\mathcal U\,dV_g$ é a medida ponderada da ação:

$$
\mathcal U\,dV_g
=\frac{\rho}{(4\pi z_\tau)^n}dV_g.
$$

O fator $(4\pi z_\tau)^{-n}$ pertence ao kernel geométrico; ele não redefine a
densidade constitutiva $\rho$.
