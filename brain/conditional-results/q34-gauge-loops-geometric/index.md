---
title: "Q34 — calibre em loops pelo loop geométrico"
status: structural-closed
source: "manuscrito/04_action_consistency/notes/loop_geometrico_calibre_fase_t4.md"
updated: 2026-07-21
---

# Q34 — calibre em loops pelo loop geométrico

## Estado vigente

Q34 está fechada no setor geométrico declarado. O cálculo mínimo de loop não
usa espinor ou Yang--Mills como ação fundamental; ele vem da fase do campo
$f$ em um ciclo toroidal do bulk oficial.

## Cadeia canônica

$$
\mathcal S_{\rm GDQ}
\to
S_\chi^{(2)}
\to
H_n[A]
\to
\operatorname{Tr}\log H_n[A]
\to
\Pi_{\mu\nu}^{(n)}.
$$

Com:

$$
H_n[A]=-(D^{(n)})^2+m_n^2,
\qquad
D_\mu^{(n)}=\partial_\mu-iq_nA_\mu.
$$

## Resultado

O tensor de polarização é transversal:

$$
\Pi_{\mu\nu}^{(n)}
=
(Q_\mu Q_\nu-Q^2\delta_{\mu\nu})\Pi_{n,s_0}(Q^2),
\qquad
Q^\mu\Pi_{\mu\nu}^{(n)}=0.
$$

Além disso, $\Pi(0)=0$ e a resposta satura no ultravioleta para $s_0>0$.
Fantasmas permanecem representação auxiliar do jacobiano de gauge, não
ontologia da GDQ.

## Scripts

1. `manuscrito/04_action_consistency/scripts/verificar_loop_geometrico_fase_t4.py`;
2. `manuscrito/04_action_consistency/scripts/verificar_kernels_covariantes_calibre.py`.

