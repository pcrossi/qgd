# Q37 — teste da impedância DtN global

## 1. Hipótese testada

Depois da canonicalização do setor neutro radial, o kernel fotônico possui

$$
K_0
=\frac{\mathcal K_Q}{2}(1+\delta_B)
=15{,}1626057586\ldots.
$$

Se o modo observado precisa atravessar a interface entre o setor global e a
resposta local do mesmo estômato, a composição variacional de duas
impedâncias fornece

$$
K_{\rm eff}
=\frac{K_0K_\partial}{K_0+K_\partial}.
$$

Não se escolhe $K_\partial$ pelo valor de $\alpha$. O primeiro teste usa o
operador DtN do primeiro harmônico de uma extensão regular pela 4-bola cujo
bordo é $S^3_R$.

## 2. Rigidez DtN sem ajuste

Para o primeiro harmônico,

$$
\lambda_{\rm DtN}=\frac1R.
$$

Cada lado da interface contribui

$$
K_\partial^{(1)}
=\lambda_{\rm DtN}
\operatorname{Area}(S^3_R)
\langle|T|^2\rangle,
$$

com

$$
\operatorname{Area}(S^3_R)=2\pi^2R^3,
\qquad
\langle|T|^2\rangle=\frac14.
$$

Somando as duas extensões,

$$
\boxed{
K_\partial^{\rm DtN}=\pi^2R^2.
}
$$

Para o raio já fixado no background numérico,

$$
R=1{,}998411184770,
$$

obtém-se

$$
K_\partial^{\rm DtN}=39{,}4157186074\ldots.
$$

## 3. Resultado

O complemento de Schur dá

$$
K_{\rm eff}^{\rm DtN}
=\frac{K_0K_\partial^{\rm DtN}}
{K_0+K_\partial^{\rm DtN}},
$$

e portanto uma estimativa inteiramente congelada de

$$
\alpha_{\rm DtN}^{-1}
=4\pi K_{\rm eff}^{\rm DtN}.
$$

Numericamente,

$$
K_{\rm eff}^{\rm DtN}=10{,}9502262826\ldots,
$$

$$
\boxed{
\alpha_{\rm DtN}^{-1}=137{,}604601779\ldots.
}
$$

O desvio relativo em $Z_Q$ diante da fórmula cosmológica é $0{,}414868\%$.

O script `teste_schur_dtn_global.py` executa essa avaliação e verifica que a
Hessiana de interface permanece positiva.

Para reproduzir exatamente a fórmula cosmológica seria necessário

$$
K_\partial=38{,}8357712279\ldots.
$$

Esse número não foi usado no teste; serve apenas como diagnóstico posterior.
A proximidade entre ele e $\pi^2R^2$ mostra que a escala e o sinal do termo
faltante são os de uma impedância DtN do elo $S^3$, não os de um prefator
dimensional arbitrário.

## 4. Estatuto

O teste é uma **estimativa geométrica sem ajuste**, não uma prova final. Para
fechar a identidade é necessário substituir o DtN da 4-bola redonda pelo DtN
da Hessiana Hermitiano--Bismut no background warped real, com as condições de
bordo oficiais. O operador completo deverá decidir se a pequena diferença
restante é produzida pela torção, pelo warp e pelo raio finito do estômato.

O resultado exclui duas rotas:

1. não falta uma potência dimensional de $\ell_C$;
2. não se deve inserir um fator escalar escolhido pela discrepância.

Ele seleciona uma rota concreta:

$$
\boxed{
\text{matriz neutra canonizada}
+\text{DtN global da Hessiana oficial}
\longrightarrow Z_Q^E.
}
$$

## 5. Tentativa de usar o operador warped já existente

Foram auditados `q29/problema_sturm_liouville_wz.md` e
`q29/solve_sturm_liouville_wz_q29.py`. Esse operador tem variável
$\chi\in[\epsilon,\pi]$ e descreve perfis **tangenciais** dentro do
$S^3$ de Hopf:

$$
-\frac{d}{d\chi}
\left(p(\chi)\frac{d\Psi}{d\chi}\right)
+q(\chi)\Psi
=\lambda w(\chi)\Psi.
$$

O DtN necessário nesta rota é diferente. Ele deve propagar o primeiro
harmônico na direção normal $r$ da fatia

$$
\mathbb C^2\supset B^4_R,
\qquad
\partial B^4_R=S^3_R.
$$

Logo sua forma é um operador normal $L_r$ cujo traço e derivada normal são
avaliados em $r=R$. Substituir $r$ por $\chi$ confundiria a normal ao estômato
com uma coordenada angular do próprio elo.

Além disso, o solver eletrofraco existente calcula $g$ e $g'$ a partir de
`ALPHA_INV`; ele é adequado para comparação fenomenológica de $W/Z$, mas não
pode ser invertido para derivar $\alpha$.

Portanto a tentativa não produziu uma correção warped independente. O
resultado redondo de $137{,}6046$ permanece a estimativa não circular válida.
O refinamento legítimo exige derivar da Hessiana oficial o operador normal

$$
L_r^{\rm phys}
=-\frac1{w_r}
\partial_r(p_r\partial_r)+V_r
$$

na vizinhança $B^4_R$, com regularidade no centro, e então calcular

$$
\Lambda_{\rm DtN}^{\rm WB}phi
=p_r(R)\partial_r\Psi_\phi(R).
$$

Essa EDP/EDO normal ainda não está presente nos arquivos atuais.

## 6. No-go do refinamento puramente conformal

Na dimensão normal quatro, com métrica induzida fixa, a forma
$\int F\wedge\star F$ é conformalmente invariante. Assim, para
$g_{\rm WB}=e^{2A}g_{\rm red}$, o warp escalar cancela entre $\sqrt g$ e
$F^{ab}F_{ab}$ e não modifica a rigidez DtN integrada. Na truncagem conformal
disponível, $Z(\eta)F^2$ também não produz bloco bilinear em $A_Q=0$. Portanto
esse background mantém

$$
K_\partial=\pi^2R^2=39{,}415718607388\ldots.
$$

Ward, sozinho, não exclui mistura de $F$ com uma 2-forma torsional de
background. Portanto apenas o refinamento conformal direto está encerrado
negativamente. O deslocamento
até $38{,}835771227928\ldots$ só pode vir de anisotropia Hermitiana, mistura
cinética interna ou interface transversal efetivamente derivada.
