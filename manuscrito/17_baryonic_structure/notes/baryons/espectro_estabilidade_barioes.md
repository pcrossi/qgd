---
title: "Espectro líder e estabilidade bariônica"
---

# Espectro líder e estabilidade bariônica

## 1. Hessiana bariônica

A estabilidade de um bárion é avaliada pela Hessiana física:

$$
K_B^{\rm phys}
=
P_{\rm phys}^\dagger
\left.
\delta^2\mathcal S_{\rm GDQ}
\right|_{\Phi_B}
P_{\rm phys}.
$$

O projetor $P_{\rm phys}$ remove:

1. difeomorfismos redundantes;
2. variações que violam a normalização de $\mathcal U$;
3. variações que mudam a carga/resíduo;
4. variações que mudam a classe topológica do bárion;
5. modos incompatíveis com o contorno do estômato.

No setor preservado, o próton não possui caminho contínuo para o vácuo sem
violar carga de Cauchy, fluxo de Noether ou a classe trimodal.

## 2. Momento de inércia

Para a casca de superfície reduzida:

$$
\langle r^2\rangle_{\rm surf}
=
\frac35r_p^2.
$$

O momento de inércia líder é:

$$
I_{\rm rot}
=
\frac12M_p\langle r^2\rangle_{\rm surf}
=
\frac{3}{10}M_pr_p^2.
$$

## 3. Escala rotacional

A energia rotacional líder é:

$$
E_{\rm rot}
=
\frac{5(\hbar c)^2}{M_pr_p^2}.
$$

Essa escala fornece o primeiro teste contra o canal $\Delta(1232)$:

$$
M_\Delta^{\rm lead}
=
M_p+E_{\rm rot}.
$$

Ela deve ser lida como aproximação líder, pois ainda não diagonaliza os modos
radiais, torsionais e de garganta da Hessiana completa.

## 4. Nêutron livre

O nêutron preserva número bariônico, mas a orientação torsional antiparalela
abre um canal neutro de cisalhamento. Isso torna o nêutron livre
dinamicamente instável sem tornar o próton instável.

O ponto essencial é:

$$
B_{\rm top}=1
$$

para próton e nêutron, mas:

$$
Q_p=1,
\qquad
Q_n=0.
$$

O decaimento beta do nêutron é então uma cirurgia dinâmica em setor neutro,
não perda contínua da classe bariônica.

Script:

[[../../scripts/espectro_estabilidade_barioes|espectro_estabilidade_barioes.py]]

Saída:

[[../../scripts/saida_espectro_estabilidade_barioes|Saída — espectro e estabilidade bariônica]].
