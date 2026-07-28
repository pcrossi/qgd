---
title: "Formalização Lean da camada gravitacional e cosmológica"
---

# Formalização Lean da camada gravitacional e cosmológica

Esta nota separa o que foi certificado como identidade matemática exata do que
continua dependendo da solução cosmológica da ação oficial.

O módulo canônico é
[GravityCosmology.lean](../../../../formal/GDQ/GravityCosmology.lean).

## 1. Grupo adimensional e resposta de horizonte

Definimos:

$$
\Pi_G
=
\frac{GM^2}{\hbar c},
$$

e:

$$
G_{\rm rec}
=
\frac{\hbar c}{M^2}\Pi_G.
$$

Sob $M\neq0$, $\hbar\neq0$ e $c\neq0$, a substituição direta fornece:

$$
G_{\rm rec}=G.
$$

Esse resultado certifica a reconstrução dimensional. Ele não calcula
$\Pi_G$.

Do mesmo modo, se o contorno global satisfaz:

$$
R_H
=
\frac{2GE_H}{c^4},
$$

então, para $c\neq0$ e $E_H\neq0$:

$$
\frac{c^4R_H}{2E_H}
=
G.
$$

O teorema reconstrói a resposta depois que $R_H$ e $E_H$ foram dados pelo
problema cosmológico. Ele não os transforma em números universais sem
contorno.

## 2. Saddle térmico e colagem axial

O período euclidiano:

$$
\beta_E=2\pi R_H
$$

produz exatamente:

$$
\tau_\ast
=
\frac{\beta_E^2}{16}
=
\frac{\pi^2R_H^2}{4}.
$$

Com:

$$
\lambda_{\rm ax}
=
\frac{2}{R^2},
$$

o custo relativo é:

$$
\Delta u_v
=
\tau_\ast\pi^2\lambda_{\rm ax}
=
\frac{\pi^4}{2}\frac{R_H^2}{R^2}.
$$

O módulo prova então o teorema condicional:

$$
R
=
\pi^2\sqrt{\alpha}\,R_H
\quad\Longrightarrow\quad
\Delta u_v
=
\frac{1}{2\alpha},
$$

para $\alpha>0$ e $R_H\neq0$.

Essa formulação é deliberada. A álgebra do expoente está fechada, mas a
condição de colagem permanece um dado geométrico a ser obtido do background
cosmológico completo.

## 3. Diluição e canais antissimétricos

A contagem:

$$
\dim\Lambda^2(\mathbb R^8)
=
\binom82
=
28
$$

é certificada diretamente.

Para o peso $e^{-f}=r_p/r$, a razão radial exata é:

$$
\frac{
\frac{r_p}{2}(R_H^2-r_p^2)
}{
\frac13R_H^3
}
=
\frac32\frac{r_p}{R_H}
\left(
1-\frac{r_p^2}{R_H^2}
\right).
$$

Portanto, no limite $R_H\gg r_p$, a dependência dominante é linear em
$r_p/R_H$. O fator $3/2$ não desaparece por álgebra: sua absorção pertence à
normalização do projetor cosmológico adotado no modelo reduzido.

## 4. Densidade cosmológica e equações de estado

Partindo de:

$$
\rho_{\rm UV}^{p}
=
\frac{M_pc^2}{V_p},
\qquad
V_p
=
\frac{4\pi}{3}r_p^3,
$$

o módulo prova, para $c\neq0$:

$$
\alpha^2N
\rho_{\rm UV}^{p}
\frac{r_p}{R_H}
\frac1{c^2}
=
\alpha^2N
\frac{M_p}{V_p}
\frac{r_p}{R_H}.
$$

Assim, o cancelamento de $c^2$ e a dimensão final de densidade de massa são
exatos. A escolha de $N=28$, do perfil global e da normalização $\alpha^2$
permanece identificada no corpo do capítulo.

Também foram certificados:

$$
p_\Lambda=-\rho_\Lambda c^2
\quad\Longrightarrow\quad
w=-1,
$$

e, separadamente, que uma 3-forma homogênea livre com
$\dot\rho=-6H\rho$ e continuidade de fluido perfeito satisfaz:

$$
p=\rho,
\qquad
w=1,
$$

quando $H\neq0$. Isso impede confundir torção homogênea livre com energia
escura.

## 5. Aceleração crítica

Sob:

$$
R_H=\frac{c}{H_0},
$$

o módulo prova:

$$
\frac{c^2}{2\pi R_H}
=
\frac{cH_0}{2\pi},
$$

para $c\neq0$ e $H_0\neq0$.

Essa identidade certifica a passagem entre raio de Hubble e escala de
aceleração. A comparação com a escala fenomenológica galáctica continua uma
avaliação externa, registrada nos scripts do capítulo.

## 6. Alcance lógico

O módulo Lean não afirma:

1. ter resolvido o background $\Phi_\ast^{\rm cos}$;
2. ter diagonalizado $K_{\rm cos}^{\rm phys}$;
3. ter derivado espectralmente o prefator reduzido de $G$;
4. ter calculado CMB, BAO, supernovas ou crescimento de estrutura;
5. que a concordância numérica substitua a cadeia variacional ausente.

Ele certifica a camada algébrica que será usada quando esses dados
cosmológicos forem construídos.
