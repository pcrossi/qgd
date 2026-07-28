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

Teorema condicional/redução efetiva. Para uma dinâmica geral, a conclusão
exige:

1. bacias macroscópicas estáveis;
2. ruído microscópico regular;
3. fronteiras de bacia de medida nula;
4. transporte dos pesos de entrada para as medidas das bacias;
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

A correspondência a demonstrar é:

$$
\mu_{\rm micro}(\mathcal B_i)=|c_i|^2.
$$

No setor QND gaussiano, ela foi demonstrada a partir do filtro martingal e da
captura por informação acumulada:

$$
dp_i
=
p_i\sum_a(s_i^a-\bar s^a)d\widetilde W^a,
\qquad
p_i(\infty)=\mathbf1_{\{I_\infty=i\}}.
$$

Logo:

$$
\mu_{\rm path}(\mathcal B_i)
=
|c_i|^2.
$$

Veja
[[teorema_born_bacias_qnd_gaussiano|Teorema Born–bacias para aparelhos QND gaussianos]].

## O que permanece condicional

Para aparelhos reais, é necessário calcular a Hessiana, a resposta de
interface, os sinais e a informação acumulada. O teorema cobre aparelhos QND
gaussianos; outras classes exigem nova análise. Nenhuma dessas condições é um
postulado novo da ação oficial.
