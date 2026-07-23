# Capítulo 16 — derivação do canal superior físico

## Classificação

Avaliação direta da regra de seleção do mapa magnético linear. Não usa
valor experimental de `g_e` nem de `g_mu-2`.

## 1. Mapa magnético linear

Para campo magnético uniforme no ciclo de Noether, o acoplamento linear
seleciona apenas a componente harmônica de Hodge:

$$
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
$$

O canal superior direto seria uma projeção de $M_\perp$ sobre modos
exatos superiores $d\sin(k\vartheta)$.

## 2. Regra de seleção

$$
h=\frac{d\vartheta}{2\pi},
\qquad
e_k\propto d\sin(k\vartheta).
$$

Como o campo uniforme é constante no ciclo,

$$
\langle h,e_k\rangle=0
\qquad
(k\ge1).
$$

Numericamente:

- `||h||^2 = 1.591549430918953e-01`
- `<h,e_1> = -4.359835622510790e-17`
- `<h,e_2> = -2.724897264069244e-17`
- `<e_1,e_2> = -6.539753433766185e-17`

Portanto:

$$
\boxed{\mu_{2,\ell}^{\rm direto}=0.}
$$

## 3. Blocos estáveis com regra de seleção

| lépton | papel Q39 | M_l/M_e | K2 | mu2 direto | a obtido | arquivo |
|---|---|---:|---:|---:|---:|---|
| e | torção primária | 1.000000000000000e+00 | 8.610225765836003e+02 | 0.0 | 1.161409732097665e-03 | `background_leptonico_selecao_e_gmenos2.npz` |
| mu | torção transversal/biespacial | 2.067685934706287e+02 | 1.780324271066477e+05 | 0.0 | 1.161409732097665e-03 | `background_leptonico_selecao_mu_gmenos2.npz` |
| tau | saturação tridimensional | 3.477446405098381e+03 | 2.994159863649186e+06 | 0.0 | 1.161409732097665e-03 | `background_leptonico_selecao_tau_gmenos2.npz` |

## 4. Consequência

O primeiro canal superior não é uma nova fonte linear direta para campo
magnético uniforme. Assim, substituir os blocos `required` por uma
fonte direta derivada dá `mu2=0`, não o valor metrológico observado.

Logo, os resíduos superiores de `g-2` devem vir de outro elo interno:

1. correção da Hessiana física `H_C=H_0+alpha H_1+...`;
2. mistura Hessiana entre o canal líder e modos superiores;
3. mapa eletrogeométrico interno não uniforme, se derivado do bulk;
4. ou fonte de aparelho não uniforme, que não é universal.

Para a anomalia universal de campo uniforme, a rota correta é a
correção de Hessiana, não uma nova `mu2` direta.
