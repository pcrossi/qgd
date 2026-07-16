# Q28 — Protótipo mínimo do setor $U(1)$ em um estômato

## 1. Objetivo

Construir o primeiro exemplo calculado da linha abeliana sem inserir uma
hipercarga experimental. O elo local do estômato é

$$
S^3\subset\mathbb C^2,
$$

com projeção de Hopf

$$
S^1\hookrightarrow S^3\xrightarrow{\pi_H}S^2.
$$

O cálculo deve responder onde vive $c_1(L_Y)$ e qual índice ele produz.

## 2. Obstrução em $S^3$

Para a 3-esfera,

$$
H^2(S^3,\mathbb Z)=0.
$$

Consequentemente, toda linha complexa sobre $S^3$ possui

$$
\boxed{c_1(L\to S^3)=0.}
$$

Portanto, uma hipercarga não nula não pode ser identificada com um primeiro
número de Chern calculado diretamente no elo tridimensional. A conexão de Hopf
pode ter holonomia e Chern--Simons não triviais, mas o fibrado de linha
subjacente sobre $S^3$ é topologicamente trivial.

## 3. Linha de Hopf sobre $S^2$

Cubra $S^2$ por cartas norte e sul. Para um inteiro $m$, defina

$$
A_N=\frac m2(1-\cos\theta)d\phi,
$$

$$
A_S=-\frac m2(1+\cos\theta)d\phi.
$$

No overlap,

$$
A_N-A_S=m\,d\phi.
$$

A função de transição é

$$
g_{NS}(\phi)=e^{im\phi}.
$$

Ela é univalorada se e somente se

$$
\boxed{m\in\mathbb Z.}
$$

A curvatura é

$$
F=dA_N=dA_S
=\frac m2\sin\theta\,d\theta\wedge d\phi.
$$

Logo,

$$
\boxed{
c_1(L_m)
=\frac1{2\pi}\int_{S^2}F
=m.
}
$$

O setor elementar é selecionado por

$$
|m|=1,
$$

sem usar os valores de hipercarga do Modelo Padrão.

## 4. Pullback para o elo

Se

$$
\eta=d\psi+\cos\theta\,d\phi
$$

é a 1-forma global de Hopf em $S^3$, então

$$
d\eta=-\sin\theta\,d\theta\wedge d\phi.
$$

O pullback da curvatura é

$$
\pi_H^*F
=-\frac m2d\eta
=d\left(-\frac m2\eta\right).
$$

Assim, a curvatura puxada para $S^3$ é exata. Isso confirma simultaneamente:

$$
c_1(\pi_H^*L_m)=0
$$

e a existência de uma conexão global de Hopf no elo.

## 5. Operador mínimo calculável

O operador elementar que detecta $c_1(L_m)$ é o Dirac de spin$^c$ sobre a
base $S^2_a$, de raio $a$, torcido por $L_m$:

$$
D_m
=i\sigma^\alpha e_\alpha{}^j
\left(
\nabla_j^{\rm spin}-iA_j
\right).
$$

Seu índice é

$$
\boxed{
\operatorname{ind}D_m^+
=\int_{S^2}\operatorname{ch}(L_m)\widehat A(TS^2)
=\frac1{2\pi}\int_{S^2}F
=m.
}
$$

Para $m>0$, existem $m$ modos zero de uma quiralidade e nenhum da oposta. Para
$m<0$, a quiralidade é invertida.

O espectro não nulo pode ser organizado por $n=1,2,\ldots$:

$$
\lambda_{n,\pm}
=\pm\frac1a\sqrt{n(n+|m|)},
$$

com degenerescência

$$
d_n=|m|+2n.
$$

O espectro não nulo é simétrico, mas os modos zero carregam o índice.

## 6. O que este protótipo prova

O cálculo estabelece, sem usar a tabela fenomenológica:

1. a quantização integral do fluxo abeliano;
2. a existência de um setor mínimo $|m|=1$;
3. a produção de um modo zero quiral por unidade de fluxo;
4. a compatibilidade entre Hopf, $c_1$ e índice de Dirac;
5. a impossibilidade de localizar $c_1\ne0$ diretamente em $S^3$.

## 7. O que ele não prova

Este resultado ainda não determina as hipercargas fracionárias

$$
\frac16,
\quad
-\frac23,
\quad
\frac13,
\quad
-\frac12,
\quad
1.
$$

Essas frações só podem surgir depois da combinação global entre:

$$
SU(3),
\qquad
SU(2),
\qquad
U(1),
\qquad
\Gamma\subseteq\mathbb Z_6.
$$

Também não calcula o $\eta$-invariante do operador tridimensional de borda.
Para isso será necessário levantar a conexão para $S^3$, incluir a torção de
Bismut e diagonalizar

$$
\mathcal D_{\partial,B,A}
=\slashed D_{S^3}
+\frac18B_{ijk}\gamma^{ijk}
-iA_i\gamma^i.
$$

## 8. Status

$$
\boxed{
\text{protótipo }U(1)\text{ fechado: }c_1=m\text{ em }S^2,
\quad
\operatorname{ind}D_m^+=m.
}
$$

O próximo passo é calcular o operador tangencial em $S^3$ com a conexão de
Hopf puxada e determinar sua assimetria espectral.
