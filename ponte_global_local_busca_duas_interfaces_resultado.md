# Busca condicional com duas interfaces independentes

## Classificação

$$
\boxed{
\text{teste numérico de existência; candidato próximo, raiz não demonstrada}
}
$$

Não foram usados dados experimentais como alvo e o vínculo energético
$\mathcal C_E$ ainda não foi imposto.

## Etapa exploratória

A busca de dez variáveis reduziu o custo de

$$
94{,}507
$$

para

$$
6{,}2161\times10^{-7}.
$$

Contudo, ao reavaliar o candidato com integração precisa, obteve-se

$$
\|\mathfrak F\|=1{,}11499\times10^{-3},
$$

$$
\max|\mathcal C_N^+|
=3{,}21368\times10^{-5}.
$$

As restrições dos dois colares ficaram em

$$
3{,}58\times10^{-18}
$$

e

$$
2{,}82\times10^{-17}.
$$

Logo, a dificuldade residual está na colagem exterior, não nos integradores
internos.

## Refinamento

Uma segunda otimização foi iniciada do candidato usando tolerância de
integração $2\times10^{-8}$. Ela não terminou dentro do limite de 150
segundos e não produziu novo candidato. Esse timeout não é resultado físico.

## Veredito

$$
\boxed{
\text{nenhuma raiz foi ainda aceita.}
}
$$

A redução de três ordens de grandeza do resíduo mostra que a formulação de
duas interfaces é numericamente plausível, mas não autoriza declarar
existência. O próximo refinamento deve usar Jacobiana variacional ou colocação
multidomínio, evitando diferenças finitas sobre dez integrações completas.

A Jacobiana variacional escolhida está especificada em
`ponte_global_local_jacobiana_variacional.md`. A colocação multidomínio será
usada posteriormente como verificação independente da raiz.
