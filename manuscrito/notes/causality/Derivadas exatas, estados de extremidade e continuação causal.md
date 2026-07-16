---
title: "Derivadas exatas, estados de extremidade e continuação causal"
---

# Derivadas exatas, estados de extremidade e continuação causal

Se

$$
L'=L+\frac{dF(q,t)}{dt},
$$

então

$$
S'[q]=S[q]+F(q_1,t_1)-F(q_0,t_0).
$$

O kernel lorentziano transforma-se como

$$
K'(q_1,t_1;q_0,t_0)
=e^{iF(q_1,t_1)/\hbar}
K(q_1,t_1;q_0,t_0)
e^{-iF(q_0,t_0)/\hbar}.
$$

Logo, a equivalência não consiste em ignorar o termo: os vetores de borda
devem sofrer a transformação conjugada. Em notação de operadores,

$$
U'(t_1,t_0)
=V(t_1)U(t_1,t_0)V(t_0)^{-1},
$$

com

$$
V(t)=e^{iF(t)/\hbar}.
$$

Depois da continuação para um parâmetro euclidiano, os fatores podem deixar de
ser unitários. Isso torna indispensável transportar também o domínio, os
estados e a condição de reflexão. Concluir apenas que “o fator tornou-se real”
não basta para provar quebra de calibre.

