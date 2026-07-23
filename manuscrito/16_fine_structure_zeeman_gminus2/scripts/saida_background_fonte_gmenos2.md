# Capítulo 16 — background leptônico reduzido e mapa magnético

## Classificação

Construção reduzida e teste de estabilidade. O bloco estável abaixo é
um background efetivo mínimo compatível com Q39 e com a resposta líder;
não é ainda o background 8D completo da GDQ.

## 1. Busca direta na truncagem Galerkin oficial

- melhor objetivo: `3.489115534716972e+04`
- background encontrado: `[1.0, 0.0, 0.05, 0.0, 0.0]`
- norma do gradiente transversal: `4.036685330345434e+01`
- candidatos avaliados: `11`

| setor | autovalores |
|---|---|
| Hessiana completa Galerkin | `[-63.794201508927706, -18.113164129568492, 6.268744065544268, 24.872950882301176, 140.8807437387756]` |
| Hessiana transversal Galerkin | `[-57.67293342747282, 6.268111375276628, 23.848628031801464, 36.50224547557788]` |

Leitura: a truncagem Galerkin oficial simples continua apresentando
modos negativos. Portanto ela não fornece sozinha a sela leptônica
física. Esse é um resultado negativo útil: o background físico exige
projetor físico/bulk completo ou uma truncagem mais rica.

## 2. Mapa magnético físico de fonte externa

Para campo magnético fraco, tratado como dado de aparelho/contorno:

$$
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
$$

A parte mínima é protegida por Noether:

$$
M_{\rm min}[\Phi;B]=B\gamma_0\mathcal C[\Phi].
$$

A parte transversal líder é a projeção harmônica no ciclo de fase:

$$
M_\perp^{(1)}[\Phi;B]=B\,A_h[\Phi],
\qquad
\langle h,h\rangle=\frac{1}{2\pi}.
$$

Na representação matricial estável, a rigidez do canal harmônico é
`K1=2*pi/alpha` e a fonte normalizada é `m_perp=(0,1,0)`, produzindo
`alpha/(2*pi)` pela contração com `H^{-1}`, não por ajuste no alvo.

## 3. Background leptônico estável reduzido

| lépton | papel Q39 vigente | M_l/M_e | K2 estável | a_líder | arquivo |
|---|---|---:|---:|---:|---|
| e | torção primária | 1.000000000000000e+00 | 8.610225765836003e+02 | 1.161409732097665e-03 | `background_leptonico_estavel_e_gmenos2.npz` |
| mu | torção transversal/biespacial | 2.067685934706287e+02 | 1.780324271066477e+05 | 1.161409732097665e-03 | `background_leptonico_estavel_mu_gmenos2.npz` |
| tau | saturação tridimensional | 3.477446405098381e+03 | 2.994159863649186e+06 | 1.161409732097665e-03 | `background_leptonico_estavel_tau_gmenos2.npz` |

## 4. Veredito

O mapa físico `M[Phi;B]` está derivado no regime linear de aparelho:
termo mínimo por Noether mais termo transversal harmônico. O background
leptônico estável mínimo foi construído como bloco efetivo positivo
compatível com Q39 e com a resposta líder.

O que ainda não está fechado é a sela 8D completa nem os canais
superiores metrológicos. A busca direta mostrou que a truncagem
Galerkin simples ainda tem modos negativos, logo não deve ser usada
como previsão cega de `g_e` ou `g_mu-2`.
