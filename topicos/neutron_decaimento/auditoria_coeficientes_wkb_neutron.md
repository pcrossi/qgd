# Auditoria da determinação de $A_2,C_4,M_r$ e da meia-vida

## 1. Equações disponíveis

O corpus fornece

$$
A_2=\pi^2(32+12\ell)w_R+A_2^{\rm cola},
$$

$$
C_4=\pi^2\left(\frac83+2\ell\right)w_V+C_4^{\rm cola},
$$

e

$$
M_r
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}G_{r,3}
\right].
$$

Portanto, determinar os três números exige

$$
\ell,quad w_R,quad w_V,quad
A_2^{\rm cola},quad C_4^{\rm cola},quad G_{r,3}.
$$

Nenhum desses seis dados possui valor numérico para a cirurgia do nêutron nos
documentos consolidados.

Além disso,

$$
B_3=\frac{2\kappa_T\tau_T^2\nu_3}{V_0^2}
$$

também não é numérico enquanto $\kappa_T,\tau_T,\nu_3,V_0$ não forem
avaliados no mesmo background.

## 2. Por que o background estático da Q30 não fornece $M_r$

No colar cilíndrico de Q30 existem os números

$$
R=1{,}03707435228632,
\qquad
\tau=0{,}274900522513626.
$$

Com normalização homogênea, eles fornecem aproximadamente

$$
p_R=0{,}155384352526,
\qquad
K_R=5{,}32888850629,
\qquad
\Lambda_R^{\rm DtN}=0{,}909959279437.
$$

Essas quantidades são rigidez de gradiente, curvatura potencial e impedância
**estáticas**. Nenhuma delas é o terceiro jato causal $G_{r,3}$. Logo,

$$
\boxed{M_r\neq p_R,\ K_R,\ \Lambda_R^{\rm DtN}}
$$

sem uma continuação lorentziana derivada. Transplantar esses números seria
misturar Q30 com a cirurgia bariônica.

## 3. Exclusão do benchmark natural ingênuo

Teste apenas diagnóstico:

$$
\ell=w_R=w_V=1,
\qquad
A_2^{\rm cola}=C_4^{\rm cola}=0.
$$

Isso produziria

$$
A_2=44\pi^2=434{,}262593647932,
$$

$$
C_4=\frac{14}{3}\pi^2=46{,}0581538717503.
$$

A condição de bounce exigiria

$$
B_3>2\sqrt{A_2C_4}=282{,}852140589261.
$$

Se também fossem postos ingenuamente
$\kappa_T=\tau_T=\nu_3=V_0=1$, resultaria $B_3=2$, muito abaixo do limiar.
Portanto, o benchmark de parâmetros unitários **não possui ponto de retorno**
e não pode ser usado para calcular uma meia-vida.

Classificação: teste de consistência que exclui um palpite; não é background
físico.

## 4. Vida média e meia-vida já avaliadas

Para uma taxa exponencial,

$$
P(t)=e^{-\Gamma t},
\qquad
\tau_{\rm média}=\Gamma^{-1},
\qquad
t_{1/2}=\frac{\log2}{\Gamma}=\tau_{\rm média}\log2.
$$

A avaliação condicional Q29 com coeficiente torsional externo forneceu

$$
\Gamma^{\rm cond}=1{,}119132143048115\times10^{-3}\ \mathrm{s}^{-1},
$$

portanto

$$
\boxed{t_{1/2}^{\rm cond}=619{,}361337144746\ \mathrm{s}.}
$$

A fórmula histórica $\alpha^{-11}$ forneceu

$$
\Gamma^{(\alpha)}=1{,}137140542406870\times10^{-3}\ \mathrm{s}^{-1},
$$

portanto

$$
\boxed{t_{1/2}^{(\alpha)}=609{,}552781481901\ \mathrm{s}.}
$$

Essas são meias-vidas calculadas, mas não resultam de valores derivados de
$A_2,C_4,M_r$.

## 5. Veredito

Não existe um triplo físico $(A_2,C_4,M_r)$ numericamente determinado no
corpus. Há infinitos triplos compatíveis com as simetrias e, sem
$G_{r,3}$, não existe sequer uma unidade causal para $M_r$.

Logo, uma meia-vida WKB física não pode ser calculada honestamente neste
estágio. O cálculo pode ser fechado de duas maneiras legítimas:

1. fornecer a família causal e o matching, obtendo os seis dados da Seção 1;
2. declarar explicitamente uma calibração fenomenológica, que deixa de ser
   previsão da ação oficial.

Nenhuma conservação adicional gera esses coeficientes locais.

## 6. Reprodutibilidade

Os números desta auditoria estão em
`neutron/auditar_coeficientes_wkb_neutron.py`.
