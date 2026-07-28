---
title: "Impedância coletiva de superfície"
---

# Impedância coletiva de superfície

## 1. Por que a impedância entra

O perfil torsional $H_n$ fornece a densidade interna líder do nêutron. O
observável de espalhamento, porém, não mede essa densidade nua. Ele mede a
resposta da superfície bariônica ao campo de sonda.

Na GDQ, essa resposta deve vir da Hessiana física de superfície, não de um novo
termo fundamental.

## 2. Forma de Schur

Separe as flutuações de superfície em:

$$
\delta\Phi_\Sigma
=
\delta\Phi_{\rm obs}
\oplus
\Psi.
$$

Aqui $\delta\Phi_{\rm obs}$ é o canal diretamente sondado e $\Psi$ são modos
coletivos relaxáveis. A forma quadrática é:

$$
Q_\Sigma
=
\langle\delta\Phi_{\rm obs},K_{oo}\delta\Phi_{\rm obs}\rangle
+
2\operatorname{Re}
\langle\delta\Phi_{\rm obs},J_\Sigma\Psi\rangle
+
\langle\Psi,K_{\Sigma}\Psi\rangle.
$$

Eliminando variacionalmente os modos coletivos:

$$
K_\Sigma\Psi+J_\Sigma^\dagger\delta\Phi_{\rm obs}=0,
$$

portanto:

$$
\Psi
=
-K_\Sigma^{-1}J_\Sigma^\dagger\delta\Phi_{\rm obs}.
$$

Substituindo:

$$
\mathcal I_\Sigma(q)
=
-J_\Sigma^\dagger(q)
K_\Sigma^{-1}(q)
J_\Sigma(q).
$$

## 3. Três modos mínimos

No modelo reduzido de superfície, usa-se:

$$
x=\frac{q^2}{\Lambda_E^2},
\qquad
\Lambda_E=\frac{\sqrt{12}}{r_p}.
$$

O vetor de acoplamento mínimo é:

$$
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix}.
$$

Os modos são:

1. $j_0$: deslocamento normal da casca;
2. $j_1$: cisalhamento/magnetização;
3. $j_2$: torção não local.

Logo:

$$
\mathcal I_\Sigma(q)
=
-j_0^2\frac{x^2}{1+x}
-j_1^2\frac{x^2}{(1+x)^2}
-j_2^2\frac{x^3}{(1+x)^2}.
$$

Como todos os termos começam em $q^4$, a impedância não altera:

$$
G_E^n(0),
\qquad
\left.
\frac{dG_E^n}{dq^2}
\right|_0.
$$

Ela corrige a forma em $q$ intermediário.

## 4. Status

O cálculo reduzido ajusta os acoplamentos por mínimos quadrados para reproduzir
a forma de Galster. Portanto ele demonstra capacidade de representação do
ansatz de Schur, não uma derivação dos coeficientes físicos.

Para uma predição, os mesmos $j_i$ devem ser extraídos
diretamente da Hessiana bariônica física completa.

Script:

[[../../scripts/modos_coletivos_superficie|modos_coletivos_superficie.py]]

Saída:

[[../../scripts/saida_modos_coletivos_superficie|Saída — modos coletivos de superfície]].
