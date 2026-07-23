---
title: "Forma-relógio, sincronização e assinatura lorentziana"
---

# Forma-relógio, sincronização e assinatura lorentziana

Esta nota registra a construção usada no Capítulo 2 para passar do bulk
Riemanniano positivo ao espaço-tempo físico efetivo. A construção não muda a
ação oficial e não altera a assinatura do bulk. Ela define uma métrica física
projetada depois que uma direção-relógio foi selecionada.

## 1. O pullback Riemanniano permanece positivo

Se $X:N^4\to M^8$ é uma imersão e $g$ é positiva no bulk, então

$$
q=X^*g
$$

é positiva em $N$. Para todo vetor não nulo $v\in T_pN$,

$$
q(v,v)=g(dXv,dXv)>0.
$$

Logo, a assinatura lorentziana não pode surgir apenas por restrição de $g$ a
uma subvariedade. É necessário um dado adicional: uma 1-forma relógio.

## 2. Reflexão por uma forma-relógio

Seja $u$ uma 1-forma não nula em $N$ e defina

$$
s=q^{-1}(u,u)>0.
$$

A métrica física efetiva é

$$
h=q-2\frac{u\otimes u}{s}.
$$

Escolha um referencial $q$-ortonormal no qual

$$
u=\sqrt{s}\,e^0.
$$

Então

$$
q=(e^0)^2+(e^1)^2+(e^2)^2+(e^3)^2
$$

e

$$
2\frac{u\otimes u}{s}=2(e^0)^2.
$$

Portanto

$$
h=-(e^0)^2+(e^1)^2+(e^2)^2+(e^3)^2.
$$

Assim,

$$
\operatorname{sign}(h)=(-,+,+,+).
$$

Esse é um resultado algébrico. Ele prova a assinatura uma vez dada a
forma-relógio, mas ainda não seleciona qual forma-relógio é física.

## 3. Seleção por simultaneidade cosmológica

No espaço cosmológico de Einstein usado como domínio global auxiliar,

$$
M_{\rm cos}=T^5\times S^3,
$$

separe o ciclo cosmológico distinguido:

$$
T^5=T^4\times S_E^1.
$$

Se $\Theta_E$ parametriza $S_E^1$ e $R_E$ é seu raio, a 1-forma de comprimento
desse ciclo é

$$
\omega_E=R_Ed\Theta_E.
$$

As hipersuperfícies

$$
\Theta_E=\text{constante}
$$

definem simultaneidade comóvel. No limite local apontado, introduzimos

$$
x^0=R_E\Theta_E.
$$

Logo,

$$
dx^0=R_Ed\Theta_E=\omega_E.
$$

O limite tangente local transporta a forma cosmológica para

$$
\omega_0=dx^0.
$$

No referencial local físico,

$$
u=X^*\omega_0.
$$

A sincronização no evento comum exige

$$
\iota^*\omega_E=u,
$$

onde $\iota$ identifica a folha cosmológica com o referencial tangente local
no ponto-base. Essa condição fixa a direção e a unidade do relógio. Após
normalização,

$$
q^{-1}(u,u)=1.
$$

O contorno causal $\gamma$ fixa a orientação entre $u$ e $-u$.

## 4. Status lógico

O resultado é um teorema condicional:

- dado o background cosmológico de Einstein;
- dada sua foliação comóvel;
- dado o limite tangente local apontado;
- dada a sincronização no evento comum;
- dada a orientação causal;

então a forma-relógio física é selecionada e a métrica projetada tem
assinatura lorentziana.

Não foi postulado um segundo bulk lorentziano. Também não foi alterada a ação
oficial. A construção apenas explica como um observador físico lê uma métrica
efetiva de assinatura $(-,+,+,+)$ a partir de um bulk Riemanniano positivo
quando a direção-relógio é selecionada pela ponte global-local.
