---
title: "Bacias dinâmicas e resultado único"
---

# Bacias dinâmicas e resultado único

## Enunciado

A regra de Born fornece a distribuição operacional de registros. Um evento
individual exige uma dinâmica real do aparelho e do ambiente que selecione uma
bacia macroscópica:

$$
\Phi_{A+E}(t)\to\mathcal B_i.
$$

## Status

Teorema condicional/redução efetiva. A conclusão exige:

1. bacias macroscópicas estáveis;
2. ruído microscópico regular;
3. fronteiras de bacia de medida nula;
4. compatibilidade dos pesos de entrada com a medida de Born;
5. isolamento suficiente dos registros finais.

## Argumento

Após o acoplamento $S+A+E$, a distribuição reduzida torna-se diagonal:

$$
\rho_{SA}
\simeq
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
$$

Essa diagonalização fornece probabilidades de registros, mas não escolhe um
ramo individual. Para um aparelho real, cada registro corresponde a uma região
atratora:

$$
\mathcal B_i
=
\{\Phi_{A+E}:\Phi_{A+E}(t\to\infty)\to R_i\}.
$$

Se as fronteiras entre bacias têm medida nula, então quase toda
microconfiguração inicial termina em uma única bacia. A frequência observada
em muitas repetições é:

$$
p_i
=
\mu_{\rm micro}(\mathcal B_i).
$$

A compatibilidade Born exige:

$$
\mu_{\rm micro}(\mathcal B_i)=|c_i|^2.
$$

Quando essa compatibilidade é satisfeita pelo aparelho, a teoria produz
resultado único e distribuição Born.

## O que permanece condicional

Para aparelhos reais, é necessário calcular a Hessiana, a resposta de
interface, a dissipação e as bacias. Sem esse cálculo, o resultado único fica
como hipótese dinâmica real, não como postulado novo da ação oficial.
