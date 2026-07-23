---
title: "Teorema spin-estatística condicional na GDQ"
---

# Teorema spin-estatística condicional na GDQ

## 1. Enunciado

No setor físico efetivo da GDQ, campos de spin semi-inteiro obedecem
estatística fermiônica quando as hipóteses locais do teorema spin--estatística
são satisfeitas.

O enunciado usado no manuscrito é condicional:

$$
\boxed{
\text{setor Lorentziano, spinorial, positivo e graduadamente local}
\Longrightarrow
\text{CAR}.
}
$$

Isso significa que a GDQ não postula Pauli nem importa o Modelo Padrão como
ontologia. Ela reconstrói o setor operacional onde o teorema se aplica.

## 2. Hipóteses necessárias

As hipóteses usadas são:

| Hipótese | Forma na GDQ |
|---|---|
| Espaço-tempo Lorentziano | métrica física reconstruída $(N,h)$ |
| Estrutura spin | $P_{\rm Spin}(N)\to N$ |
| Campo semi-inteiro | $\psi\in\Gamma(S\otimes E)$ |
| Clifford | $\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu}$ |
| Cone causal comum | símbolo principal $(\gamma^\mu k_\mu)^2=h^{\mu\nu}k_\mu k_\nu$ |
| Produto interno positivo | reconstrução física por quociente de normas nulas |
| Energia positiva | $H\ge0$ no setor físico reconstruído |
| Localidade | observáveis pares comutam em separação tipo-espaço |
| Localidade graduada | campos fermiônicos ímpares anticomutam em separação tipo-espaço |

O teorema não é afirmado fora desse domínio.

## 3. Campo spinorial efetivo

A partir do setor spinorial,

$$
\psi\in\Gamma(S\otimes E),
$$

o operador efetivo de primeira ordem tem símbolo principal

$$
\sigma(D)(k)=\gamma^\mu k_\mu.
$$

Pela álgebra de Clifford,

$$
\sigma(D)(k)^2
=
(\gamma^\mu k_\mu)^2
=
h^{\mu\nu}k_\mu k_\nu.
$$

Logo a propagação frontal do setor spinorial usa o mesmo cone causal da métrica
física $h$. Essa é a condição que impede que a estatística seja escolhida
livremente sem afetar causalidade ou positividade.

## 4. Por que CAR

Se um campo de spin semi-inteiro fosse quantizado por comutadores bosônicos no
setor Lorentziano positivo, uma das condições físicas teria de falhar:

1. positividade de norma;
2. positividade de energia;
3. localidade relativística;
4. covariância spinorial.

Para preservar simultaneamente essas condições, a álgebra correta é a CAR:

$$
\{a(f),a^\dagger(g)\}
=
\langle f,g\rangle_{\mathcal H_1},
$$

$$
\{a(f),a(g)\}=0,
\qquad
\{a^\dagger(f),a^\dagger(g)\}=0.
$$

O espaço de muitos corpos é a álgebra exterior:

$$
\mathcal F_-(\mathcal H_1)
=
\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H_1.
$$

## 5. Localidade graduada

Campos fermiônicos ímpares não são observáveis diretamente mensuráveis. A
condição local correta é graduada.

Para regiões tipo-espaço separadas $O_1\perp_h O_2$:

$$
\{\psi(O_1),\psi(O_2)\}=0.
$$

Observáveis físicos pares, construídos com número par de campos fermiônicos,
comutam:

$$
[A_{\rm even}(O_1),B_{\rm even}(O_2)]=0.
$$

Assim a causalidade observável é preservada.

## 6. Energia positiva

No setor físico reconstruído, o semigrupo euclidiano define

$$
T_E(a)=e^{-aH/\hbar},
\qquad
a\ge0.
$$

O gerador é

$$
H
=
-\hbar
\left.
\frac{d}{da}T_E(a)
\right|_{a=0^+}.
$$

Sob reflexão positiva e quociente por normas nulas:

$$
H=H^\dagger,
\qquad
H\ge0.
$$

Na Fock fermiônica:

$$
d\Gamma(H_1)\ge0
$$

quando $H_1\ge0$ no setor de uma partícula física.

## 7. Pauli como consequência

Das CAR:

$$
\{a_i^\dagger,a_j^\dagger\}=0.
$$

Tomando $i=j$:

$$
2(a_i^\dagger)^2=0.
$$

Logo:

$$
(a_i^\dagger)^2=0.
$$

Esse é o princípio de exclusão de Pauli no setor CAR.

Na linguagem de funções de onda, a antissimetria implica:

$$
\Psi(x_1,x_2)
=
-\Psi(x_2,x_1).
$$

Em $x_1=x_2$:

$$
\Psi(x,x)=0.
$$

Na GDQ, esse nó aparece geometricamente porque, com $R=\sqrt\rho$,

$$
R\to0
$$

faz o termo de Bohm

$$
Q
=
-\frac{\hbar^2}{2m}\frac{\nabla^2R}{R}
$$

tornar-se singular se o numerador não cancelar a anulação de $R$.

## 8. Relação com holonomia

A GDQ oferece uma leitura geométrica adicional. A troca de dois solítons
idênticos define um laço no espaço de configurações reduzido. Se

$$
\oint_\gamma dS_R
=
(2k+1)\pi\hbar,
$$

então

$$
\operatorname{Hol}_\gamma
=
\exp\left(
\frac{i}{\hbar}\oint_\gamma dS_R
\right)
=
-1.
$$

Assim:

$$
\Psi(x_2,x_1)=-\Psi(x_1,x_2).
$$

A ordem lógica preservada é:

$$
\boxed{
\text{estrutura spinorial + positividade + localidade}
\Rightarrow
\text{CAR}
\Rightarrow
\text{Pauli}.
}
$$

A holonomia $-1$ é a forma geométrica da mesma antissimetria; ela não substitui
o teorema.

## 9. Status

O resultado está fechado estruturalmente no setor efetivo local da GDQ.

Permanece condicional porque depende da reconstrução do setor físico
Lorentziano positivo e local graduado. Essa condicionalidade não é fraqueza
ad-hoc: é exatamente o domínio matemático de validade do teorema
spin--estatística.
