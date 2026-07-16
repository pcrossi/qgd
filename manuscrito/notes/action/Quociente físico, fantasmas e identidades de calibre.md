---
title: "Quociente físico, fantasmas e identidades de calibre"
---

# Quociente físico, fantasmas e identidades de calibre

## 1. O problema geométrico

Se $\eta$ é uma flutuação e $R\epsilon$ é uma direção infinitesimal de gauge,

$$
\eta\sim\eta+R\epsilon.
$$

A Hessiana bruta possui modos nulos ao longo da órbita. O espaço físico é o
quociente

$$
\mathcal V_{\rm phys}
=\ker C\cap\mathcal D_{\rm bordo}\big/\operatorname{Im}R,
$$

onde $C$ reúne os vínculos lineares. Escolhido o produto interno ponderado da
ação, pode-se representar esse quociente por um projetor ortogonal
$P_{\rm phys}$ e definir

$$
\mathbb H_{\rm phys}
=P_{\rm phys}\mathbb HP_{\rm phys}.
$$

Esse é o operador intrínseco. Nenhum campo fantasma foi introduzido.

## 2. Coordenadas de gauge e jacobiano

Uma condição $F[A]=0$ escolhe localmente uma seção da órbita. Inserir essa
seção na integral funcional produz

$$
1
=\Delta_{\rm FP}[A]
\int\mathcal Dg\,\delta(F[A^g]),
$$

com

$$
\Delta_{\rm FP}[A]
=\det M_A,
\qquad
M_A
=\left.\frac{\delta F[A^g]}{\delta\epsilon}\right|_{\epsilon=0}.
$$

O determinante é o jacobiano da mudança de coordenadas entre o espaço total e
o produto local “seção vezes órbita”. A identidade

$$
\det M_A
=\int\mathcal D\bar c\,\mathcal Dc\,
e^{-\langle\bar c,M_Ac\rangle}
$$

é uma representação algébrica desse jacobiano. Ela não transforma $c$ e
$\bar c$ em excitações materiais.

No setor $U(1)$, com $F[A]=\partial^\mu A_\mu$,

$$
M_A=-\partial^2,
$$

independente de $A$. Seu determinante é uma constante comum às configurações
e não contribui para a polarização.

## 3. Identidade de Ward sem fantasmas dinâmicos

Se

$$
L_{A^g}=g^{-1}L_Ag,
$$

então, por cálculo funcional,

$$
F_\tau(L_{A^g})
=g^{-1}F_\tau(L_A)g.
$$

A ciclicidade do traço fornece

$$
\Gamma_\tau[A^g]
=\operatorname{Tr}F_\tau(L_{A^g})
=\operatorname{Tr}F_\tau(L_A)
=\Gamma_\tau[A].
$$

Para $U(1)$, $\delta A_\mu=\partial_\mu\varepsilon$. Logo

$$
0=\delta_\varepsilon\Gamma_\tau
=\int d^dx\,
\frac{\delta\Gamma_\tau}{\delta A_\mu}
\partial_\mu\varepsilon.
$$

Integrando por partes e usando $\varepsilon$ arbitrário,

$$
\partial_\mu
\frac{\delta\Gamma_\tau}{\delta A_\mu}=0.
$$

Uma nova derivada funcional em relação a $A_\nu$ e a transformada de Fourier
dão

$$
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
$$

## 4. Extensão não abeliana

No caso não abeliano, a órbita, a condição de gauge e o jacobiano são
covariantes em relação ao background. A invariância do funcional efetivo é
codificada pela identidade

$$
\mathcal S(\Gamma_\tau)=0.
$$

Sua forma expandida é a identidade de Slavnov--Taylor. BRST fornece uma
notação cohomológica conveniente para demonstrá-la; a construção GDQ pode
igualmente mantê-la como identidade geométrica do quociente e do operador
covariante.

## 5. Conclusão lógica

O resultado demonstrado não é que “um determinante cancela magicamente todos
os modos”. É mais preciso:

1. os modos de gauge são removidos por quociente ou projetor físico;
2. uma seção de gauge introduz um jacobiano geométrico;
3. fantasmas são uma representação opcional desse jacobiano;
4. a covariância espectral produz Ward e Slavnov--Taylor;
5. portanto fantasmas não são ontologia fundamental da GDQ.

O fechamento vale nos setores e domínios em que o operador covariante e o
quociente físico foram construídos. Não é uma afirmação indiscriminada sobre
qualquer background singular.
