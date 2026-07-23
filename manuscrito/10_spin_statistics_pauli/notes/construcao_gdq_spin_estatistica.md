---
title: "Construção GDQ do spin, estatística e Pauli"
---

# Construção GDQ do spin, estatística e Pauli

## 1. Enunciado

Spin na GDQ começa como circulação e torção do defeito, mas precisa ser
realizado por estrutura spinorial no setor efetivo.

A cadeia é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm estômato}
\to
\text{fatia normal }\mathbb C^2
\to
S^3
\to
\operatorname{Spin}
\to
D_{B,A}
\to
\text{CAR}
\to
\text{Pauli}.
$$

## 2. Background do estômato

O estômato é um defeito de codimensão compatível com uma fatia normal complexa:

$$
N_{\rm normal}\simeq\mathbb C^2.
$$

O elo de uma pequena bola normal é:

$$
\partial B_\epsilon(\mathbb C^2)
\simeq
S^3.
$$

Esse $S^3$ carrega a geometria de Hopf usada para circulação e orientação.

## 3. Hessiana angular e setor físico

A Hessiana da ação oficial ao redor do estômato separa modos radiais, angulares
e de calibre. O setor físico é:

$$
K_{\rm phys}^{\rm spin}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}^{\rm estômato}
P_{\rm phys}.
$$

As flutuações angulares não triviais do elo $S^3$ produzem o setor spinorial
efetivo.

Mais explicitamente, escrevemos uma perturbação admissível do background como:

$$
\Phi
=
\Phi_\ast
+
\delta\Phi,
\qquad
\delta\Phi
=
\delta\Phi_{\rm phys}
+
\delta\Phi_{\rm gauge}
+
\delta\Phi_{\rm constr}.
$$

A segunda variação define a forma quadrática:

$$
\left.\delta^2\mathcal S_{\rm GDQ}\right|_{\Phi_\ast}
(\delta\Phi,\delta\Phi)
=
\langle \delta\Phi,K_{\rm GDQ}^{\rm estômato}\delta\Phi\rangle.
$$

O projetor $P_{\rm phys}$ remove modos de gauge, variações de normalização e
direções que violam os vínculos de carga e fluxo. Assim:

$$
\delta\Phi_{\rm phys}
=
P_{\rm phys}\delta\Phi,
$$

e somente a forma quadrática reduzida:

$$
\langle \delta\Phi_{\rm phys},
K_{\rm phys}^{\rm spin}\delta\Phi_{\rm phys}\rangle
$$

é usada para identificar graus de liberdade observáveis. O operador spinorial
abaixo é, portanto, o operador efetivo que representa a ação de
$K_{\rm phys}^{\rm spin}$ no subespaço angular de meia-monodromia. Ele não é
postulado como nova dinâmica fundamental.

## 4. Operador espinorial efetivo

O operador que aparece não é uma nova ação fundamental. Ele é a linearização
spinorial da Hessiana projetada:

$$
D_{B,A}
=
\gamma^a
\left(
\nabla_a
+
\frac18H_{abc}\gamma^{bc}
+
A_a
\right).
$$

Ele atua em:

$$
\psi\in\Gamma(S\otimes E).
$$

## 5. Rotação e troca

A estrutura spin fornece o recobrimento:

$$
SU(2)\to SO(3).
$$

Uma rotação de $2\pi$ atua como:

$$
U(2\pi)=-I.
$$

A troca de dois férmions é uma holonomia no espaço de configuração reduzido.
No setor Lorentziano positivo e local graduado, ela impõe estatística
fermiônica.

## 6. CAR e Pauli

Os operadores efetivos obedecem:

$$
\{a_i,a_j^\dagger\}
=
\delta_{ij},
\qquad
\{a_i^\dagger,a_j^\dagger\}=0.
$$

Daí:

$$
(a_i^\dagger)^2=0.
$$

Esse é Pauli. A barreira de Bohm é a manifestação geométrica da exclusão no
fluido, não a prova algébrica primária.

## 7. Limitação

A seleção dinâmica completa de qual setor spinorial aparece em todo background
material é programa posterior. O fechamento atual é estrutural no setor local
regular.

## 8. Verificação computacional preservada

Os testes computacionais do capítulo não calculam um espectro material novo.
Eles verificam, de modo autocontido, três identidades estruturais usadas no
texto:

1. o levantamento $SU(2)$ de rotações espaciais dá $U(2\pi)=-I$ e
   $U(4\pi)=I$;
2. uma circulação ímpar de $\pi\hbar$ produz holonomia $-1$;
3. a álgebra exterior finita realiza a CAR e implica
   $(a_i^\dagger)^2=0$.

As saídas ficam registradas em `scripts/saida_*.md` e servem como verificação
simbólica, não como ajuste fenomenológico.
