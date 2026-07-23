---
title: "Hessiana CP e susceptibilidade topológica"
---

# Hessiana CP e susceptibilidade topológica

O parâmetro que mede a rigidez do vácuo contra deslocamentos de CP é a
susceptibilidade topológica. Na formulação efetiva:

$$
\chi_{\rm top}^{\rm GDQ}
=
\left.
\frac{\partial^2E_{\rm vac}(\theta)}
{\partial\theta^2}
\right|_{\theta=0}.
$$

Como a energia depende da carga topológica:

$$
Q_C
=
\int_N q_C,
$$

a mesma quantidade pode ser escrita como função de correlação:

$$
\chi_{\rm top}^{\rm GDQ}
=
\int d^4x\,
\langle q_C(x)q_C(0)\rangle_{\rm GDQ}.
$$

Na linguagem da ação oficial, essa é a curvatura do funcional efetivo depois
de projetar a segunda variação no modo angular torsional. Se
$\Phi_\ast=(g_\ast,J_\ast,H_\ast,f_\ast,\mathcal U_\ast)$ é o background
admissível, o operador físico relevante é:

$$
K_{\rm CP}^{\rm phys}
=
P_{\rm phys}
\delta^2\mathcal S_{\rm GDQ}[\Phi_\ast]
P_{\rm phys}.
$$

O modo angular normalizado é representado por uma direção $\eta_B$ no espaço de
flutuações torsionais:

$$
\delta H
=
\eta_B\,\delta\vartheta_B.
$$

A susceptibilidade direta da GDQ é então a forma quadrática:

$$
\chi_{\rm top}^{\rm GDQ}
=
\langle
\eta_B,
K_{\rm CP}^{\rm phys}
\eta_B
\rangle_{\mathcal U_\ast}.
$$

Esse enunciado separa três níveis:

1. a periodicidade, que é topológica;
2. a relaxação, que depende de $\chi_{\rm top}^{\rm GDQ}>0$;
3. a metrologia, que exige avaliar $K_{\rm CP}^{\rm phys}$ no background forte.

Para o potencial periódico:

$$
V(\theta)
=
\chi_{\rm top}^{\rm GDQ}
(1-\cos\theta),
$$

a Hessiana angular reduzida é:

$$
\frac{d^2V}{d\theta^2}
=
\chi_{\rm top}^{\rm GDQ}\cos\theta.
$$

No mínimo CP:

$$
\left.
\frac{d^2V}{d\theta^2}
\right|_{\theta=0}
=
\chi_{\rm top}^{\rm GDQ}
>
0.
$$

No máximo instável:

$$
\left.
\frac{d^2V}{d\theta^2}
\right|_{\theta=\pi}
=
-
\chi_{\rm top}^{\rm GDQ}
<
0.
$$

Portanto, a positividade da Hessiana física no canal torsional é exatamente a
condição matemática que torna $\theta=0\pmod{2\pi}$ um atrator estável.
