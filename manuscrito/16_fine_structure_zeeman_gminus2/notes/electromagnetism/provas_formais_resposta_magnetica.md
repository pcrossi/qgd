---
title: "Provas formais da resposta magnética reduzida"
---

# Provas formais da resposta magnética reduzida

Esta nota separa as identidades certificadas da parte ainda dependente do
background físico.

## 1. Normalização mínima

Defina a convenção operacional:

$$
g
=
\frac{2mc}{q}\gamma.
$$

Para o mapa magnético mínimo:

$$
\gamma_0
=
\frac{q}{mc},
$$

temos, para $qmc\ne0$:

$$
g_0
=
\frac{2mc}{q}
\frac{q}{mc}
=
2.
$$

Lean certifica essa identidade em
`magneticGFactor_minimal_eq_two`. A hipótese $\gamma_0=q/(mc)$ permanece
visível: Noether conserva a circulação, enquanto o mapa de fonte fixa a razão
giromagnética mínima.

## 2. Norma do ciclo de fase

No ciclo de comprimento $2\pi$, o representante constante de período unitário
é:

$$
h
=
\frac{d\vartheta}{2\pi}.
$$

Logo:

$$
\lVert h\rVert^2
=
(2\pi)
\left(
\frac{1}{2\pi}
\right)^2
=
\frac{1}{2\pi}.
$$

Assim, no modelo em que o canal transversal líder é $\alpha h$:

$$
a^{(1)}
=
\alpha\lVert h\rVert^2
=
\frac{\alpha}{2\pi}.
$$

Lean certifica a norma e essa composição em
`unitHarmonicCircleNormSq_eq` e `leadingMagneticAnomaly_eq`. A formalização
não afirma que todo background físico seleciona esse canal.

## 3. Multiplicador da circulação

No espaço físico gauge-fixado, mas ainda contendo o modo $c_\ell$, a equação
linearizada é:

$$
K_{\ell,\rm phys}\eta
=
B\,m_\ell+\delta\lambda\,c_\ell.
$$

Aplicando a pseudoinversa e impondo:

$$
\langle c_\ell,\eta\rangle=0,
$$

obtemos:

$$
\delta\lambda
=
-B
\frac{
\langle c_\ell,K_{\ell,\rm phys}^{+}m_\ell\rangle
}{
\langle c_\ell,K_{\ell,\rm phys}^{+}c_\ell\rangle
}.
$$

Portanto:

$$
\gamma_{\rm eff,\ell}
=
-\left.
\frac{\partial\lambda}{\partial B}
\right|_{B=0}
=
\frac{
\langle c_\ell,K_{\ell,\rm phys}^{+}m_\ell\rangle
}{
\langle c_\ell,K_{\ell,\rm phys}^{+}c_\ell\rangle
}.
$$

Com:

$$
m_\ell
=
\gamma_{0,\ell}c_\ell+m_{\perp,\ell},
$$

a linearidade fornece:

$$
\gamma_{\rm eff,\ell}
=
\gamma_{0,\ell}
+
\frac{
\langle c_\ell,K_{\ell,\rm phys}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,K_{\ell,\rm phys}^{+}c_\ell\rangle
}.
$$

O núcleo escalar dessa decomposição está certificado por
`noetherZeemanEffectiveRatio_decomposition` e
`effectiveMagneticRatio_eq_minimal_plus_anomaly`.

## 4. Bloco líder como verificador

Considere:

$$
H_{\rm lead}
=
\begin{pmatrix}
1&-1\\
-1&K
\end{pmatrix},
\qquad
K=\frac{2\pi}{\alpha}.
$$

Para:

$$
c=(1,0)^T,
\qquad
m_\perp=(0,1)^T,
$$

a inversa é:

$$
H_{\rm lead}^{-1}
=
\frac{1}{K-1}
\begin{pmatrix}
K&1\\
1&1
\end{pmatrix}.
$$

Então:

$$
\frac{
\langle c,H_{\rm lead}^{-1}m_\perp\rangle
}{
\langle c,H_{\rm lead}^{-1}c\rangle
}
=
\frac{1/(K-1)}{K/(K-1)}
=
\frac1K
=
\frac{\alpha}{2\pi}.
$$

Lean certifica a identidade em `leadingBlockResponse_eq`, sob
$\alpha\ne0$ e $K\ne1$.

Esse cálculo verifica a realização reduzida do termo líder. Ele não deriva a
matriz $H_{\rm lead}$ de uma sela leptônica 8D.

## 5. Canal direto ortogonal

Se um modo superior exato $e_k$ é ortogonal ao representante harmônico:

$$
\langle h,e_k\rangle=0,
$$

qualquer fonte linear proporcional a esse overlap fornece:

$$
\mu_k^{\rm direto}=0.
$$

Lean certifica a implicação algébrica em
`directOrthogonalChannel_vanishes`. A prova analítica da ortogonalidade no
ciclo está na decomposição de Hodge do capítulo e é verificada pelos scripts.

## 6. Alcance

Arquivo Lean:
[MagneticResponse.lean](../../../../formal/GDQ/MagneticResponse.lean).

Certificado:

1. $g_0=2$ dado o mapa magnético mínimo;
2. $\lVert h\rVert^2=1/(2\pi)$;
3. $a^{(1)}=\alpha/(2\pi)$ no canal líder reduzido;
4. decomposição da resposta protegida e transversal;
5. identidade do bloco Hessiano líder;
6. anulação de um canal linear diretamente ortogonal.

Não certificado por essas identidades:

1. a derivação universal de $\alpha$ para toda classe cosmológica;
2. a existência da sela leptônica 8D adequada;
3. a seleção de todos os canais superiores;
4. os valores metrológicos completos de $g_e$ e $g_\mu-2$.
