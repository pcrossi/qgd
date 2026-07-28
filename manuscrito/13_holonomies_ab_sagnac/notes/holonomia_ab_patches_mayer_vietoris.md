---
title: "Holonomia AB por patches e Mayer-Vietoris"
---

# Holonomia AB por patches e Mayer-Vietoris

## Enunciado

No exterior do solenoide ideal, $dA=0$ localmente, mas a holonomia em laço que
envolve o solenoide pode ser não trivial.

## Prova

O domínio exterior tem:

$$
\pi_1(M_{\rm ext})\simeq\mathbb Z.
$$

Cubra:

$$
M_{\rm ext}=U_N\cup U_S.
$$

Em cada aberto:

$$
A_N=d\chi_N,
\qquad
A_S=d\chi_S.
$$

Na interseção:

$$
A_N-A_S=d(\chi_N-\chi_S).
$$

A função de transição:

$$
g_{NS}
=
\exp\left[
\frac{iq}{\hbar c}
(\chi_N-\chi_S)
\right]
$$

pode ter enrolamento não trivial. Para um laço que envolve o solenoide:

$$
\oint_\gamma A=\Phi.
$$

Logo:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left(\frac{iq\Phi}{\hbar c}\right).
$$

## Representante explícito

Um representante harmônico da classe é:

$$
A_{\rm harm}
=
\frac{\Phi}{2\pi}\,d\theta.
$$

Ele é fechado no exterior:

$$
dA_{\rm harm}=0,
$$

mas não é globalmente exato em $M_{\rm ext}$, pois:

$$
\oint_\gamma A_{\rm harm}
=
\Phi.
$$

Essa igualdade é a forma elementar da obstrução global.

## Certificação formal do núcleo de colagem

O arquivo
[HolonomyPatchingStokes.lean](../../../formal/GDQ/HolonomyPatchingStokes.lean)
formaliza três passos desta construção:

- a holonomia transforma soma de fases em produto de holonomias;
- a troca do levantamento
  $\chi_N-\chi_S\mapsto\chi_N-\chi_S+2\pi n$ não muda a função de transição;
- se os incrementos angulares de uma decomposição finita somam $2\pi$, a
  circulação de $\Phi\,d\theta/(2\pi)$ é exatamente $\Phi$.

O arquivo também prova uma versão celular de Stokes. Nela, as arestas
internas aparecem com orientações opostas e se cancelam; a soma da curvatura
nas faces coincide com a circulação restante no bordo. Esse resultado
certifica o mecanismo algébrico da passagem fluxo--circulação. Para o
solenoide suave, ainda se usa o teorema de Stokes no domínio regular
apropriado, com o interior confinado tratado pela colagem dos patches.

## Comparação numérica exata

Antes do cálculo numérico, a verificação simbólica preservada em
[[../scripts/saida_ab_holonomia_simbolica|saida_ab_holonomia_simbolica]]
confirma:

$$
dA_{\rm harm}=0,
\qquad
\oint_\gamma A_{\rm harm}=\Phi.
$$

Usando:

$$
\Phi_0=\frac{h}{e},
$$

temos:

$$
\frac{e\Phi}{\hbar}
=
2\pi\frac{\Phi}{\Phi_0}
$$

em convenção SI sem o fator $c$ explícito na definição de potencial. Para
$\Phi/\Phi_0=1/2$, a holonomia é:

$$
\exp(i\pi)=-1.
$$

O cálculo preservado em
[[../scripts/saida_ab_fase_ideal|saida_ab_fase_ideal]]
confirma:

$$
\Phi_0
=
4.135667696924\times10^{-15}\,{\rm Wb}.
$$

## Alcance

Isso prova o AB ideal como holonomia. Não calcula correções de solenoide real.
