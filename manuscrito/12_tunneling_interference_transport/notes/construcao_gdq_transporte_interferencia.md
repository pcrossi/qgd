---
title: "Construção GDQ do transporte e da interferência"
---

# Construção GDQ do transporte e da interferência

## 1. Enunciado

Tunelamento, dupla fenda, detector e escolha retardada são problemas de
domínio, contorno e transporte. Não exigem mudança da ação oficial.

A cadeia geral é:

$$
J_{\rm app}^{\rm clássico}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\rho,S_R
\to
\text{corrente}
\to
\text{registro}.
$$

## 2. Barreira e tunelamento

No modelo reduzido, a barreira especifica um domínio unidimensional e uma
deformação efetiva. O ansatz usado no capítulo é:

$$
g_{xx}\propto\rho.
$$

Ele não é teorema geral da ação oficial. Ele define um setor reduzido
condicional que permite estudar a saturação de distância própria.

## 3. Dupla fenda

A placa com duas fendas define contorno:

$$
\partial M_{\rm placa}
=
\partial M_{\rm aberto}
\cup
\partial M_{\rm fechado}.
$$

No setor Madelung plano, evoluem:

$$
\rho,
\qquad
S_R,
\qquad
J^\mu=\rho\nabla^\mu S_R/m.
$$

As franjas vêm da soma coerente das duas soluções de contorno.

## 4. Detector

Um detector acoplado a uma fenda altera a impedância de interface:

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

A perda de visibilidade é:

$$
\mathcal C_{\rm det}
=
e^{-\Gamma_{\rm det}},
$$

com:

$$
\Gamma_{\rm det}
=
\frac12
\left\langle
\Delta\Phi_\partial,
\mathsf R_{\rm det}
\Delta\Phi_\partial
\right\rangle.
$$

## 5. Escolha retardada

O aparelho dependente do tempo muda o contorno:

$$
\mathsf R_{\rm old}(t)
\to
\mathsf R_{\rm new}(t).
$$

A solução final depende do problema de transporte causal efetivamente
realizado antes do registro. Não há sinal físico enviado para o passado.

## 6. Limitação

Para aparelho real, é necessário calcular $\Phi_\ast$, $K_{\rm phys}$ e
$\mathsf R_{\rm app}$ com geometria, material, perdas e tempos de resposta do
dispositivo concreto.
