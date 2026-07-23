---
title: "Índice local APS, Hopf e Bismut"
---

# Índice local APS, Hopf e Bismut

Esta nota registra a parte local da construção geracional. Ela não usa o
Modelo Padrão como entrada. O objetivo é mostrar que um estômato primitivo
coorientado carrega uma unidade de índice quiral.

## 1. O elo local do estômato

Um estômato isolado é modelado localmente por uma vizinhança normal complexa.
Depois da excisão do núcleo, o bordo normal é:

$$
\partial B^4\simeq S^3.
$$

Como:

$$
H^2(S^3,\mathbb Z)=0,
$$

o primeiro Chern de uma linha abeliana não mora literalmente em $S^3$. Ele é
lido pela fibration de Hopf:

$$
S^1\longrightarrow S^3\longrightarrow S^2.
$$

Na base $S^2$, um fluxo primitivo é descrito por:

$$
A_N=\frac m2(1-\cos\theta)d\varphi,
$$

$$
A_S=-\frac m2(1+\cos\theta)d\varphi.
$$

No equador:

$$
A_N-A_S=m\,d\varphi,
$$

logo a função de transição é:

$$
g_{NS}=e^{im\varphi}.
$$

A curvatura é:

$$
F=dA_N=\frac m2\sin\theta\,d\theta\wedge d\varphi.
$$

Portanto:

$$
c_1(L_m)
=
\frac{1}{2\pi}\int_{S^2}F
=
m.
$$

O estômato primitivo corresponde a:

$$
|m|=1.
$$

## 2. Operador tangencial no elo $S^3$

No elo redondo de raio $a$, o operador de Dirac tangencial sem torção possui
espectro simétrico:

$$
\lambda_n^\pm
=
\pm\frac{n+\frac32}{a},
\qquad
d_n=(n+1)(n+2).
$$

A conexão de Hopf pode ser escrita, em uma base de formas invariantes
$\sigma_i$, como:

$$
A_m=-\frac m2\sigma_3.
$$

A contribuição topológica que importa para a condição APS é a transgressão:

$$
\frac{1}{4\pi^2}\int_{S^3}A_m\wedge dA_m
=
-m^2.
$$

Assim, a eta reduzida tem parte fracionária:

$$
\bar\eta(A_m)
\equiv
-\frac{m^2}{2}
\pmod{\mathbb Z}.
$$

Para $|m|=1$:

$$
-\bar\eta(A_m)\equiv\frac12\pmod{\mathbb Z}.
$$

Esse meio-termo é a assinatura espectral do fluxo Hopf primitivo no bordo.

## 3. Papel da torção de Bismut

A GDQ não usa o operador de Dirac nu como ação fundamental. O operador
spinorial aparece como operador reconstruído ou efetivo da Hessiana no setor
local. A conexão correta é a conexão Hermitiana com torção de Bismut.

No bordo $S^3$, a torção paralelizante desloca o operador tangencial. Na
normalização usada nesta construção, o acoplamento torsional físico é:

$$
\beta=-\frac32
$$

para a orientação escolhida.

Um modelo espectral reduzido do setor tangencial é:

$$
D_{m,B}^{(j)}
=
\frac1a
\left(
2\,\boldsymbol\sigma\cdot\mathbf L^{(j)}
-m\sigma_3
\right).
$$

O kernel torsional associado ao fluxo primitivo tem dimensão:

$$
h_m=|m|+1.
$$

Logo:

$$
h_1=2.
$$

Esses dois modos são o duplo grau de liberdade interno que depois é separado
por contorno/aparelho ou por escolha de setor quiral efetivo.

## 4. Preenchimento APS e unidade de índice

Considere um preenchimento $X^4=B^4$ com bordo $S^3$ e uma extensão suave:

$$
A=f(r)A_m.
$$

Pelo termo de Chern:

$$
\int_{X^4}{\rm ch}_2(L_m)
=
\frac{1}{8\pi^2}\int_{X^4}F\wedge F
=
-\frac{m^2}{2}.
$$

Sem torção, a parte fracionária do termo de volume e a eta de bordo se
cancelam. A quiralidade local não aparece automaticamente.

Com a torção de Bismut ligada adiabaticamente, o operador tangencial sofre
fluxo espectral. Para o setor primitivo $m=1$, há uma travessia simples de
autovalor no caminho físico de Bismut. Com a convenção APS:

$$
\Delta{\rm ind}_{\rm APS}
=
-{\rm SF}.
$$

Como o fluxo espectral físico tem:

$$
{\rm SF}=-1,
$$

segue:

$$
{\rm ind}_{\rm APS}D_{1,B}^+=1.
$$

Esta é a unidade local de geração:

$$
\boxed{
{\rm ind}_{\rm estômato}=1
}.
$$

## 5. O que esta unidade não significa

Ela não é:

- uma hipercarga;
- uma fração de Chern;
- uma geração inserida por tabela;
- uma partícula já massiva.

Ela é uma unidade local de índice quiral. As hipercargas pertencem à linha
$L_Y$ e ao quociente global $\mathbb Z_6$. As massas e misturas pertencem aos
capítulos posteriores, onde a Hessiana física do background material é
diagonalizada.

## 6. Verificação computacional

O script:

$$
{\tt scripts/indice\_aps\_hopf\_bismut.py}
$$

verifica os invariantes discretos usados nesta nota: fluxo $c_1=m$, parte
fracionária de $\bar\eta$, dimensão do kernel torsional e unidade APS
primitiva.
