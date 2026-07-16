# Resultado negativo do modo homogêneo de $J$ e próxima arquitetura

## 1. Modo homogêneo $\chi(s)$

O bloco Hamiltoniano correspondente às fórmulas de
`ponte_global_local_modo_J.md` foi implementado isoladamente em
`ponte_global_local_modo_J_hamiltoniano.py`.

As identidades canônicas passaram:

$$
\|\dot q_{\rm inv}-\dot q\|
=1{,}23\times10^{-16},
$$

$$
\|p_{\rm num}-p_{\rm exato}\|
=1{,}26\times10^{-10},
$$

e a regressão completa em $\chi=0$ reproduziu o RHS causal anterior com erro

$$
5{,}90\times10^{-16}.
$$

Esses testes mostram que a redução algébrica era internamente consistente.
Eles não superam, porém, a condição geométrica fundamental: o teste do tensor
de Nijenhuis excluiu a família $J_\chi$ homogênea do domínio integrável da ação
oficial.

Portanto:

$$
\boxed{
\text{o modo }\chi(s)\text{ não é admissível e não participa da Porta B.}
}
$$

O código é preservado como teste negativo e regressão; a classe correspondente
no motor extensível agora aborta explicitamente qualquer tentativa de uso.

## 2. Template Beltrami complexo

A próxima extensão deve ser um modo não homogêneo pertencente ao subespaço
integrável. Para um harmônico Beltrami fixo, escreva a amplitude e o momento
como pares complexos:

$$
A_B=A_1+iA_2,
\qquad
P_B=P_1+iP_2.
$$

Isso acrescenta quatro componentes reais ao estado canônico. Duas amplitudes
complexas regulares nas gargantas acrescentam quatro parâmetros de tiro, e o
matching de amplitude e momento fornece quatro equações reais.

`BeltramiCanonicalModelTemplate`, em
`ponte_global_local_solver_extensivel.py`, reserva essa estrutura sem atribuir:

1. autovalor ou normalização ao harmônico;
2. termo cinético;
3. potencial;
4. backreaction métrico--dilatônica;
5. condição regular;
6. adaptador ou matching.

Cada método permanece bloqueado até que o operador e sua contribuição à ação
oficial sejam derivados. O solver base permanece inalterado e sua regressão
continua exata.
