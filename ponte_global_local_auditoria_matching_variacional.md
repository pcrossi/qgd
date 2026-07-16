# Auditoria do matching variacional da ponte global--local

## 1. Pergunta

Verificou-se se o solver usa apenas a continuidade dos momentos bare ou a
condição variacional completa, incluindo:

1. multiplicador da carga strong-KT;
2. fluxo de fase fixado;
3. resposta DtN exterior e canal compensador;
4. vínculos globais usados no problema de sela.

## 2. Momento vinculado do colar

O funcional interno aumentado contém

$$
\beta\left[2c(a\dot a-c)-h_0\right].
$$

Logo o momento correto é

$$
\widetilde\Pi_a
=\Pi_a+2\beta ac.
$$

Em `ponte_global_local_integrador.py`, a variável denominada `pa` já é
precisamente $\widetilde\Pi_a$. Isso é confirmado pela fórmula eliminada

$$
\beta
=\frac{ap_ae^u+4c^2\tau+4h_0\tau+2p_ue^u}
{2a^2ce^u},
$$

implementada em `beta_value`.

O adaptador usa

$$
p_y=a\,p_a,
$$

portanto cola $a\widetilde\Pi_a$, e não $a\Pi_a$ bare. Nenhum termo
$2\beta ac$ deve ser somado novamente: isso produziria dupla contagem.

Na semente histórica, o deslocamento é numericamente não nulo:

$$
2\beta ac=-3{,}9973\times10^{-3}
$$

na esquerda e

$$
2\beta ac=-4{,}3951\times10^{-3}
$$

na direita. Assim, a distinção foi efetivamente testada; não se trata de uma
coincidência causada por $\beta=0$.

## 3. DtN exterior

`ponte_global_local_dtn_exterior.md` define

$$
\widetilde{\mathcal N}_-
+\mathcal N_+^{\rm eff}=0.
$$

O complemento de Schur $\mathcal N_+^{\rm eff}$ é necessário quando os canais
compensadores são eliminados. O solver vigente não os elimina: integra
explicitamente dois colares independentes e todo o exterior causal entre as
duas interfaces. Ele impõe os traços nas duas pontas e os balanços orientados
dos momentos.

Resolver simultaneamente o canal antipodal é a realização não linear antes do
complemento de Schur. Acrescentar também $\mathcal N_+^{\rm eff}$ aos resíduos
duplicaria a resposta exterior.

## 4. Cargas, fluxos e multiplicadores globais

- a carga relativa entra por $h_0$ e pelo multiplicador eliminado $\beta$;
- a circulação angular física está em $m=1$ no potencial do colar;
- o fluxo radial estacionário é fixado por $p_v=0$;
- a fase constante e sua equação redundante foram removidas do sistema;
- a normalização entra por $Z=\int\mathscr Vds$;
- raio e energia são impostos por $\mathcal C_R$ e $\mathcal C_E$;
- o comprimento exterior é um dado do domínio reduzido;
- momento espacial e angular macroscópicos são nulos no ansatz homogêneo.

Os multiplicadores desses vínculos ainda devem aparecer na Hessiana do
funcional aumentado da Porta C. Eles não geram um deslocamento adicional no
matching de background além dos momentos vinculados já usados.

## 5. Limitação real

O matching de background está completo dentro do ansatz estacionário
cohomogeneidade--1. O que permanece não avaliado é o DtN linearizado físico
com todos os modos não homogêneos e o complemento de Schur harmônico. Essa é
uma pendência da Hessiana/Porta C, não um termo conhecido omitido na Porta B.

## 6. Veredito

$$
\boxed{
\text{não foi encontrado termo variacional já derivado e omitido no matching.}
}
$$

O resíduo de momento do solver é continuidade do momento vinculado completo.
Não foi feita correção numérica, pois somar qualquer termo adicional agora
seria dupla contagem ou introdução de uma fonte Robin não derivada.
