# Formalização da meia-monodromia spinorial de Hopf

## Enunciado certificado

O módulo `GDQ/SpinHopfMonodromy.lean` porta para Lean a prova analítica já
registrada no capítulo de spin. O domínio local é uma carta complexa
transversal perfurada ao núcleo do estômato. Fixada a classe spinorial/Hopf,
a seção possui localmente o fator de raiz quadrada

$$
s(z)=z^{1/2}s_0(z),
$$

com $s_0$ holomorfa e não nula. A parcela singular da forma logarítmica é

$$
\Omega_S^{\rm sing}
=
\frac12\frac{dz}{z}.
$$

Lean avalia diretamente a integral de contorno circular de Mathlib:

$$
\oint_{|z|=R}\Omega_S^{\rm sing}
=
\pi i,
\qquad
R\ne0.
$$

Consequentemente,

$$
\frac{1}{2\pi i}
\oint_{|z|=R}\Omega_S^{\rm sing}
=
\frac12.
$$

Não se introduz o valor $1/2$ como resultado desejado: ele segue da integral
exata de $z^{-1}$.

O módulo também prova que uma parcela regular $d\log s_0$ não altera esse
resultado, desde que sejam fornecidas as hipóteses analíticas explícitas de
integrabilidade no círculo e de que a parcela seja a derivada complexa de
$\log s_0$ nesse domínio. Portanto, a formalização cobre a conexão completa
$\Omega_S=(1/2)dz/z+d\log s_0$, e não apenas seu representante singular.

## Conversão física

Com $h=2\pi\hbar$, o módulo prova:

$$
\oint dS_R
=
\frac h2
=
\pi\hbar.
$$

A holonomia correspondente é

$$
\exp\left(
\frac{i}{\hbar}\oint dS_R
\right)
=
-1,
$$

e duas voltas produzem

$$
\exp(2\pi i)=1.
$$

O módulo também certifica diretamente o levantamento angular:

$$
u(2\pi)=-u(0),
\qquad
u(4\pi)=u(0),
$$

e a invariância algébrica do projetor de Hopf sob $u\mapsto-u$.

## Dependência lógica

A cadeia formal é:

$$
\text{classe local spinorial/Hopf}
\Longrightarrow
\Omega_S^{\rm sing}=\frac12\frac{dz}{z}
\Longrightarrow
\operatorname{Res}\Omega_S=\frac12
\Longrightarrow
\oint dS_R=\frac h2
\Longrightarrow
\operatorname{Hol}=-1.
$$

O primeiro elo é um dado geométrico do setor admissível do defeito. Os demais
elos são teoremas verificados.

## O que o módulo não afirma

Ele não afirma que:

1. toda configuração da ação oficial possui meia-monodromia;
2. a expressão pontual da ação escolhe sozinha a estrutura spinorial;
3. a meia-monodromia, isoladamente, prova a estatística fermiônica;
4. o setor material concreto do elétron já foi selecionado dinamicamente.

A seleção do setor pertence ao problema do background admissível e de sua
Hessiana física. A passagem de spin para estatística exige ainda a construção
global tratada separadamente no capítulo. Assim, a formalização preserva o
status de teorema estrutural condicional, sem modificar a ação oficial.
