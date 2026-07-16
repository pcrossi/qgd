# Ponte global--local — pullback da estatística da Questão 16

## 1. Pergunta

Determinar se a difusão espacial já fixada na Questão 16 produz uma
covariância física no espaço de campos capaz de sustentar a sela
bulk--interface.

A difusão conhecida é

$$
D^{ij}=\nu_0\Omega^{-1}h^{ij}.
$$

## 2. Levantamento da difusão para os campos

Se $\xi$ é o incremento estocástico de coordenadas, sua ação infinitesimal nos
campos oficiais é

$$
\delta_\xi g=\mathcal L_\xi g,
$$

$$
\delta_\xi J=\mathcal L_\xi J,
$$

$$
\delta_\xi f=\mathcal L_\xi f=\xi^A\partial_Af.
$$

Defina o gerador de difeomorfismos

$$
R\xi=
(\mathcal L_\xi g,\mathcal L_\xi J,\mathcal L_\xi f).
$$

O pullback direto da covariância de coordenadas para o espaço de campos é,
portanto,

$$
\mathbb D_X^{\rm coord}=RDR^\dagger.
$$

Essa identidade não usa uma teoria externa: é a ação tensorial de uma mudança
infinitesimal de coordenadas sobre $(g,J,f)$.

## 3. Projeção física

Para geradores de gauge admissíveis com traço físico nulo na interface, o
projetor já derivado satisfaz

$$
P^{\rm phys}R=0,
$$

pois remove exatamente as órbitas de difeomorfismo. Logo

$$
\boxed{
\mathbb D^{\rm phys}_{\rm coord}
=P^{\rm phys}RDR^\dagger P^{\rm phys\dagger}=0.
}
$$

Consequentemente, a componente interior longitudinal da difusão browniana
transporta o representante geométrico, mas não excita uma deformação física.

Para não eliminar indevidamente modos de borda, decomponha

$$
\xi=\xi_0+E_\partial\zeta,
$$

onde $\xi_0|_Y=0$ e $E_\partial\zeta$ estende o deslocamento de interface
$\zeta$. Em geral,

$$
B_\partial\zeta:=P^{\rm phys}RE_\partial\zeta\ne0,
$$

e a covariância física possível é

$$
\boxed{
\mathbb D^{\rm phys}
=B_\partial D_\partial B_\partial^\dagger.
}
$$

## 4. Consequência para a equação média

A correção estatística de segunda ordem no setor físico seria

$$
\frac12D^3\mathcal S_{\rm aug}:C^{\rm phys}.
$$

Para a parte interior de gauge da covariância,

$$
C^{\rm phys}_{\rm coord}=0,
$$

e portanto

$$
\frac12D^3\mathcal S_{\rm aug}:C^{\rm phys}_{\rm coord}=0.
$$

Assim, a componente interior não desloca o mapa físico. A componente de
interface pode deslocá-lo, mas exige calcular $E_\partial$, o operador DtN e
$D_\partial$.

## 5. O ruído que seria necessário

Para sustentar uma sela estatística seria necessário um operador intrínseco
de ruído no espaço de campos,

$$
\mathbb B_\perp:
\mathcal K\longrightarrow\mathcal H^{\rm phys},
\qquad
P^{\rm phys}\mathbb B_\perp=\mathbb B_\perp,
$$

com

$$
\mathbb D_\perp=\mathbb B_\perp\mathbb B_\perp^\dagger\ge0.
$$

A ação oficial e a Questão 16 não fornecem atualmente um ruído transversal de
bulk independente. Porém a Q16 fornece uma candidata não ad hoc pelo traço de
bordo da difusão espacial. Falta derivar sua extensão elíptica e seu pullback
DtN. O símbolo $\sigma(g)$ do apêndice histórico continua sendo uma hipótese,
não devendo substituir esse cálculo.

Introduzir $\mathbb B_\perp$ agora seria acrescentar um novo dado estocástico.
Ele só seria legítimo se derivado da integração causal dos graus internos ou
de uma redução explícita da medida oficial.

## 6. Verificação algébrica

O script `ponte_global_local_pullback_estocastico.py` testa, para uma métrica
positiva, vínculos e geradores de posto genérico,

$$
P^{\rm phys}R\simeq0
$$

e

$$
P^{\rm phys}(RDR^\dagger)P^{\rm phys\dagger}\simeq0.
$$

É um teste da implementação do projetor, não uma simulação física.

## 7. Veredito

$$
\boxed{
\begin{gathered}
\text{a componente interior da estatística da Q16 é longitudinal/gauge;}\\
\text{a única componente física possível é o modo de borda,}\\
\text{cujo pullback DtN ainda precisa ser calculado.}
\end{gathered}
}
$$

A rota estatística continua aberta pelo operador
$B_\partial=P^{\rm phys}RE_\partial$, sem postular ruído de bulk. Se essa
componente não fechar a equação média, resta a sela determinística ou uma
nova derivação de ruído transversal intrínseco.

## 8. Teste do modo homogêneo de borda

O script `ponte_global_local_teste_covariancia_borda.py` identificou os dois
log-comprimentos de colar como os deslocamentos homogêneos explícitos das
interfaces e calculou o jato quadrático completo das onze equações nessas duas
direções. A minimização foi restrita a

$$
C_\partial=LL^T\ge0.
$$

O ótimo retornou

$$
C_\partial\simeq4{,}25\times10^{-18}I,
$$

isto é, covariância numericamente nula, e não reduziu o resíduo:

$$
\frac{\|F_{\rm médio}\|_2}{\|F\|_2}
=1+1{,}33\times10^{-12}.
$$

Portanto o deslocamento browniano homogêneo dos dois colares também não
sustenta a sela no ansatz atual. O teste não alcança deformações angulares da
interface, harmônicos não homogêneos ou variações de sua impedância DtN.

Classificação: teste de viabilidade por engenharia inversa com restrição de
positividade; resultado negativo, não derivação da covariância física.
