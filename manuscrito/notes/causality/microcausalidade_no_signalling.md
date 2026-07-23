---
title: "Microcausalidade e no-signalling operacional"
---

# Microcausalidade e no-signalling operacional

Esta nota registra o fechamento seguro da causalidade operacional. A GDQ não
usa o ramo avançado como canal de mensagem para o passado. A resposta
controlável de aparelhos clássicos é retardada, enquanto setores avançados
podem aparecer como condições globais de contorno.

## 1. Cone causal

Na folha física reconstruída, a causalidade é definida pela métrica
lorentziana $h$:

$$
\mathcal C_h(p)
=
\{v\in T_pN:h_p(v,v)\le0\}.
$$

No setor plano,

$$
h=-dt^2+d\mathbf x^2.
$$

Logo,

$$
h(v,v)\le0
\quad
\Longleftrightarrow
\quad
|\mathbf v|\le |v^0|.
$$

## 2. Propagadores

Se $P_h$ é o operador hiperbólico efetivo do setor, com símbolo principal
$h^{\mu\nu}k_\mu k_\nu$, os propagadores fundamentais satisfazem

$$
P_hG_{\rm ret}(x,y)=\delta_h(x,y),
\qquad
\operatorname{supp}G_{\rm ret}(\cdot,y)\subset J_h^+(y),
$$

e

$$
P_hG_{\rm adv}(x,y)=\delta_h(x,y),
\qquad
\operatorname{supp}G_{\rm adv}(\cdot,y)\subset J_h^-(y).
$$

O propagador de Feynman organiza amplitudes ordenadas no tempo:

$$
G_F(x,y)
=
\langle\Omega|
T\{\Phi(x)\Phi(y)\}
|\Omega\rangle.
$$

No setor plano,

$$
G_F(k)
=
\frac{i}{k_h^2-m^2+i0},
\qquad
k_h^2=h^{\mu\nu}k_\mu k_\nu.
$$

## 3. Comutador e suporte causal

Define-se a função de Pauli--Jordan:

$$
\Delta(x,y)
=
G_{\rm ret}(x,y)-G_{\rm adv}(x,y).
$$

Para um campo escalar reconstruído,

$$
[\Phi(x),\Phi(y)]
=
i\hbar\,\Delta(x,y).
$$

Como o suporte de $\Delta$ está contido no cone causal,

$$
x\perp_h y
\quad
\Longrightarrow
\quad
\Delta(x,y)=0.
$$

Portanto,

$$
x\perp_h y
\quad
\Longrightarrow
\quad
[\Phi(x),\Phi(y)]=0.
$$

Para observáveis locais, o enunciado operacional é:

$$
O_A\perp_h O_B
\quad
\Longrightarrow
\quad
[\mathcal A(O_A),\mathcal A(O_B)]=0.
$$

## 4. Por que Sudarshan não sinaliza ao passado

A combinação simétrica

$$
G_{\rm sym}
=
\frac12
\left(
G_{\rm ret}+G_{\rm adv}
\right)
$$

é uma solução global de contorno. Ela pode codificar fase, fechamento,
normalização, polos e restrições de borda.

A resposta física controlável a uma fonte clássica local $J_{\rm app}$ é
retardada:

$$
\delta\Phi(x)
=
\int_N
G_{\rm ret}(x,y)
J_{\rm app}(y)
dV_h(y).
$$

Assim,

$$
x\notin J_h^+(\operatorname{supp}J_{\rm app})
\quad
\Longrightarrow
\quad
\delta\Phi(x)=0.
$$

O ramo avançado é parte da solução condicionada, não um grau de liberdade que
um agente possa modular para transmitir bits ao passado.

## 5. No-signalling em álgebras separadas

Na camada operacional reconstruída, considere duas regiões espacialmente
separadas $O_A$ e $O_B$. Se

$$
[\mathcal A(O_A),\mathcal A(O_B)]=0,
$$

uma operação local não seletiva em $O_B$, descrita por operadores
$M_\alpha\in\mathcal A(O_B)$ com

$$
\sum_\alpha M_\alpha^\dagger M_\alpha=1,
$$

não altera a estatística de um observável $A\in\mathcal A(O_A)$:

$$
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
\left(
M_\alpha\rho M_\alpha^\dagger A
\right).
$$

Usando a comutação espacial,

$$
\langle A\rangle'
=
\sum_\alpha
\operatorname{Tr}
\left(
\rho A M_\alpha^\dagger M_\alpha
\right)
=
\operatorname{Tr}(\rho A)
=
\langle A\rangle.
$$

Logo, operações locais em $O_B$ não mudam marginais locais em $O_A$.

## 6. Escolha retardada

Na escolha retardada, o aparelho altera tardiamente o problema de contorno.
Isso pode mudar correlações finais:

$$
P(a,b|x,y).
$$

Mas não pode mudar a marginal local anterior se a escolha $y$ está fora do
passado causal do registro $a$:

$$
P(a|x,y)=P(a|x,y').
$$

Portanto, a leitura correta é:

$$
\boxed{
\text{mudança global de contorno}
+
\text{no-signalling local},
\text{ não retrocausalidade operacional.}
}
$$

## 7. Status

Este fechamento depende da reconstrução operacional do setor: operadores
locais, domínios, produto interno positivo e álgebra física devem estar
definidos. Quando essa camada existe, microcausalidade implica no-signalling.
