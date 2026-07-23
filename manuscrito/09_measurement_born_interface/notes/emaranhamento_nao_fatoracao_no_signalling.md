---
title: "Emaranhamento, não fatoração e no-signalling"
---

# Emaranhamento, não fatoração e no-signalling

## 1. Enunciado

No setor multipartido, o erro conceitual a evitar é imaginar duas partículas
pontuais trocando sinal no espaço físico reconstruído. Na GDQ, o estado
conjunto é uma seção geométrica no espaço de configuração:

$$
Q_{AB}
=
M_A\times M_B.
$$

Uma configuração separável exige simultaneamente:

$$
\rho_{AB}(x_A,x_B)
=
\rho_A(x_A)\rho_B(x_B),
$$

e:

$$
S_{AB}(x_A,x_B)
=
S_A(x_A)+S_B(x_B).
$$

Emaranhamento significa falha de pelo menos uma dessas fatorações:

$$
\rho_{AB}\ne\rho_A\rho_B
\quad
\text{ou}
\quad
S_{AB}\ne S_A+S_B.
$$

Essa falha é geométrica: ela pertence à seção global em $Q_{AB}$, não a um
sinal propagando de $A$ para $B$.

## 2. Colagem por Mayer--Vietoris

Considere uma cobertura:

$$
Q_{AB}=U_A\cup U_B.
$$

As fases locais são 1-formas:

$$
\theta_A=dS_A,
\qquad
\theta_B=dS_B.
$$

Na interseção:

$$
\theta_A|_{U_A\cap U_B}
-
\theta_B|_{U_A\cap U_B}
=
d\chi.
$$

A sequência de Mayer--Vietoris organiza a obstrução global:

$$
\cdots
\to
H^1(Q_{AB})
\to
H^1(U_A)\oplus H^1(U_B)
\to
H^1(U_A\cap U_B)
\xrightarrow{\delta}
H^2(Q_{AB})
\to
\cdots .
$$

Quando a classe de colagem é não trivial, a seção global não pode ser escrita
como produto de duas seções independentes. Esse é o conteúdo topológico da
correlação.

## 3. Condição operacional de causalidade

A correlação global só é fisicamente admissível se não permitir sinalização
operacional. Para escolhas de aparelho $x$ e $y$, e registros $a$ e $b$, exige-se:

$$
P(a|x,y)
=
\sum_b P(a,b|x,y)
=
P(a|x),
$$

e:

$$
P(b|x,y)
=
\sum_a P(a,b|x,y)
=
P(b|y).
$$

Portanto:

$$
\text{correlação global}
\ne
\text{canal de comunicação}.
$$

## 4. Alvo operacional reduzido

No setor projetivo reconstruído, o alvo ideal de dois canais spinoriais é o
singlete. Para eixos unitários $\boldsymbol a$ e $\boldsymbol b$:

$$
E(\boldsymbol a,\boldsymbol b)
=
-
\boldsymbol a\cdot\boldsymbol b.
$$

As probabilidades conjuntas podem ser escritas como:

$$
P(s,t|\boldsymbol a,\boldsymbol b)
=
\frac14
\left(
1
-
st\,\boldsymbol a\cdot\boldsymbol b
\right),
\qquad
s,t\in\{-1,+1\}.
$$

As marginais são:

$$
P(s|\boldsymbol a,\boldsymbol b)
=
\sum_t
P(s,t|\boldsymbol a,\boldsymbol b)
=
\frac12,
$$

e:

$$
P(t|\boldsymbol a,\boldsymbol b)
=
\sum_s
P(s,t|\boldsymbol a,\boldsymbol b)
=
\frac12.
$$

Assim, a correlação depende de ambos os eixos, mas cada marginal local não
depende da escolha distante.

## 5. Como isso entra na GDQ

A cadeia estrutural é:

$$
\mathcal S_{\rm GDQ}
\to
(\rho,S_R)_{AB}
\to
\mathsf R_A(\boldsymbol a)
\oplus
\mathsf R_B(\boldsymbol b)
\to
P(s,t|\boldsymbol a,\boldsymbol b)
\to
E(\boldsymbol a,\boldsymbol b).
$$

O capítulo demonstra a forma geométrica e a compatibilidade operacional no
setor reduzido. O fechamento metrológico forte ainda exige calcular, para
aparelhos reais:

$$
K_{AB}^{\rm phys},
\qquad
\mathsf R_A(\boldsymbol a),
\qquad
\mathsf R_B(\boldsymbol b),
\qquad
\Delta_{\rm gap}.
$$

## 6. Critério de proteção contra ruído

Robustez não é imunidade absoluta. A afirmação correta é espectral:

$$
\Delta_{\rm gap}
=
\lambda_1(K_{AB}^{\rm phys})
-
\lambda_0(K_{AB}^{\rm phys})
>
0.
$$

Perturbações ambientais locais são pequenas se:

$$
\|\delta K_{\rm env}\|
\ll
\Delta_{\rm gap}.
$$

Sem esse cálculo, a formulação permanece estrutural e condicional no nível
metrológico.
