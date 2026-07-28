---
title: "Dinâmica variacional, linearização e operadores derivados"
status: "teorema estrutural sob hipóteses analíticas declaradas"
---

# Dinâmica variacional, linearização e operadores derivados

## 1. A distinção que precisa ser preservada

A GDQ não começa por um operador quântico. Ela começa pela ação oficial,
definida numa classe de campos admissíveis e num contorno causal. Se reunirmos
os campos em

$$
\Phi=(g,J,H,f),
$$

com

$$
H=d_J^c\omega_g,
$$

o problema fundamental consiste em encontrar as configurações admissíveis
para as quais

$$
\delta\mathcal S_{\rm GDQ}[\Phi]=0.
$$

Essa é uma equação para a geometria completa. Ela existe antes da escolha de
uma base espectral, antes da reconstrução de um espaço de Hilbert e antes da
introdução de operadores de criação e aniquilação.

Os três níveis da construção são:

$$
\boxed{
\text{dinâmica variacional}
\longrightarrow
\text{linearização na sela}
\longrightarrow
\text{restrição ao setor físico}.
}
$$

Confundir esses níveis faria uma ferramenta de análise linear parecer uma lei
fundamental adicional.

## 2. Equação variacional não projetada

Seja $\mathcal V$ o espaço real de variações de uma família admissível
$\Phi(u)$, com $u\in\mathcal V$, e defina

$$
S(u)=\operatorname{Re}\mathcal S_{\rm GDQ}[\Phi(u)].
$$

Suponha que a primeira variação seja contínua e admita representante de
Riesz. Existe então um campo

$$
\mathcal E(u)\in\mathcal V
$$

tal que

$$
DS(u)[v]
=
\langle\mathcal E(u),v\rangle
$$

para toda direção $v\in\mathcal V$. O campo $\mathcal E$ reúne as equações
de Euler--Lagrange de bulk e, depois de fixado o domínio variacional, os
momentos de interface.

Se todas as direções de $\mathcal V$ são permitidas, a estacionariedade

$$
DS(u_*)[v]=0
\qquad
\forall v\in\mathcal V
$$

equivale a

$$
\mathcal E(u_*)=0.
$$

A demonstração é imediata, mas importante. Escolhendo
$v=\mathcal E(u_*)$,

$$
0
=
DS(u_*)[\mathcal E(u_*)]
=
\|\mathcal E(u_*)\|^2,
$$

logo $\mathcal E(u_*)=0$. A recíproca segue diretamente do pareamento.

Essa é a dinâmica lagrangiana geral. Nenhum projetor aparece nessa etapa.

## 3. Vínculos e estacionariedade física

Na presença de normalização, cargas fixadas e redundâncias de gauge, nem toda
direção de $\mathcal V$ é física. Seja

$$
\mathcal V_{\rm phys}
=
\ker D\mathcal C(u_*)\cap\mathcal G^\perp
$$

o espaço tangente que preserva os vínculos linearizados e é ortogonal às
direções de gauge. Se esse subespaço é fechado, existe o projetor ortogonal

$$
P_{\rm phys}:\mathcal V\longrightarrow\mathcal V_{\rm phys}.
$$

A estacionariedade restrita significa

$$
DS(u_*)[v]=0
\qquad
\forall v\in\mathcal V_{\rm phys}.
$$

Usando a autoadjunticidade de $P_{\rm phys}$,

$$
\langle\mathcal E(u_*),v\rangle
=
\langle P_{\rm phys}\mathcal E(u_*),v\rangle
$$

para todo $v\in\mathcal V_{\rm phys}$. Portanto,

$$
\boxed{
DS(u_*)|_{\mathcal V_{\rm phys}}=0
\quad\Longleftrightarrow\quad
P_{\rm phys}\mathcal E(u_*)=0.
}
$$

O projetor não altera a ação e não cria uma nova equação. Ele expressa que
somente a componente tangente ao espaço físico precisa se anular. A componente
normal é equilibrada pelos multiplicadores dos vínculos.

## 4. A Hessiana como derivada da dinâmica

Suponha agora que $\mathcal E$ seja diferenciável em $u_*$. Sua derivada é

$$
\mathbb H_*
=
D\mathcal E(u_*)
=
D^2S(u_*).
$$

Para uma perturbação pequena $\eta$,

$$
\mathcal E(u_*+\eta)
=
\mathcal E(u_*)
+\mathbb H_*\eta
+o(\|\eta\|).
$$

Assim, a equação linearizada

$$
\mathbb H_*\eta=0
$$

não é uma lei adicionada à GDQ. Ela é a aproximação tangente da equação
variacional geral ao redor de um background estacionário.

Quando há vínculos implementados por multiplicadores, $\mathbb H_*$ deve ser
a Hessiana do funcional aumentado:

$$
\mathbb H_*
=
D_X^2
\left[
S(X)-\langle\lambda,\mathcal C(X)\rangle
\right]_{(X_*,\lambda_*)}.
$$

Isso impede que a curvatura da própria folha de vínculos seja descartada.

## 5. Restrição da linearização

O operador tangente observado no setor físico é

$$
K_{\rm phys}
=
P_{\rm phys}\mathbb H_*P_{\rm phys}.
$$

Para uma direção física $\eta$, temos $P_{\rm phys}\eta=\eta$, logo

$$
K_{\rm phys}\eta
=
P_{\rm phys}\mathbb H_*\eta.
$$

Portanto, a projeção de entrada não modifica a perturbação física; a projeção
de saída apenas remove componentes normais aos vínculos ou componentes de
gauge produzidas por uma representação redundante.

Se a Hessiana preserva o setor físico,

$$
P_{\rm phys}\mathbb H_*\eta
=
\mathbb H_*\eta,
$$

então

$$
K_{\rm phys}\eta
=
\mathbb H_*\eta.
$$

Nesse caso, a compressão nem sequer modifica o operador sobre o seu domínio
físico: ela apenas torna explícita a restrição.

## 6. Onde aparecem os operadores quânticos

Se $K_{\rm phys}$ possui uma realização autoadjunta, condições de contorno
fixadas e espectro estável, podemos procurar modos normais

$$
K_{\rm phys}u_j=\lambda_j u_j.
$$

Uma perturbação linear pode ser expandida nesses modos. Depois da reconstrução
do setor de Hilbert, uma representação por operadores escreve

$$
\widehat{\delta\Phi}
=
\sum_j
\left(
a_j u_j+a_j^\dagger\overline{u_j}
\right).
$$

Os operadores $a_j$ e $a_j^\dagger$ codificam as amplitudes dos modos normais
na representação espectral escolhida. Eles não substituem:

- o background não linear;
- a equação variacional completa;
- a formação ou cirurgia de defeitos;
- a mudança física das condições de contorno;
- a interação não linear entre objeto e aparelho.

Consequentemente, a mecânica de operadores é uma redução linear e espectral
da dinâmica GDQ, não sua origem ontológica.

## 7. O que foi certificado em Lean

O módulo
[VariationalDynamics.lean](../../../formal/GDQ/VariationalDynamics.lean)
certifica:

1. que a primeira variação é o pareamento com a equação variacional;
2. que estacionariedade irrestrita equivale ao gradiente nulo;
3. que estacionariedade física equivale ao gradiente projetado nulo;
4. que a Hessiana é a derivada de Fréchet da equação variacional;
5. que a linearização restrita é $P_{\rm phys}\mathbb H_*P_{\rm phys}$;
6. que, em direções físicas invariantes pela Hessiana, a compressão coincide
   com a dinâmica linear bruta.

A certificação é abstrata e funcional-analítica. Para cada background
concreto ainda é necessário fornecer:

- o domínio das variações;
- a regularidade da ação;
- a diferenciação sob as integrais;
- os vínculos e o gauge;
- as condições de contorno;
- a autoadjunticidade e o gap, quando usados.

Essas são condições de aplicação do teorema, não alterações da ação oficial.

## 8. Significado físico

A formulação permite duas estratégias complementares:

1. resolver diretamente as equações variacionais não lineares para estudar
   backgrounds, sólitons, interfaces e transições;
2. linearizar uma solução e usar Hessianas, projetores e operadores para
   estudar estabilidade, espectros e observáveis de laboratório.

A segunda estratégia é frequentemente mais econômica, mas permanece um caso
particular controlado da primeira.
