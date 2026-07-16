# Q30 — Auditoria do sinal do fluxo Perelman--Bismut

## 1. Primeira variação e fluxo

Com a medida ponderada fixada, a primeira variação métrica é

$$
\boxed{
\delta_g\mathcal W_T
=-\tau\int\langle E_T,\delta g\rangle e^{-f}dV,
}
$$

onde, no funcional encolhedor,

$$
E_T=\operatorname{Ric}-\frac14H^2+\nabla^2f-\frac1{2\tau}g.
$$

Logo,

$$
\operatorname{grad}_g\mathcal W_T=-\tau E_T.
$$

O fluxo registrado no Capítulo 17 é

$$
\partial_\tau g=-2E_T
=\frac2\tau\operatorname{grad}_g\mathcal W_T.
$$

Portanto, ele é fluxo de **subida** de $\mathcal W_T$, compatível com

$$
\frac{d\mathcal W_T}{d\tau}\ge0.
$$

Não havia inconsistência nessas duas fórmulas; a inconsistência estava em
chamar um mínimo de atrator desse fluxo ascendente.

## 2. Projeção radial

Como $G_{RR}=12/R^2$, a equação reduzida é

$$
\boxed{
\frac{dR}{d\tau}
=+\frac{2}{\tau G_{RR}}\mathcal W_Q'(R)
=+\frac{R^2}{6\tau}\mathcal W_Q'(R).
}
$$

A mobilidade de subida é

$$
\boxed{\mathsf M_R^{(\mathcal W)}=\frac{R^2}{6\tau}>0.}
$$

Num ponto crítico,

$$
\dot\rho=\mathsf M_R^{(\mathcal W)}K_R\rho.
$$

Logo, $K_R<0$ caracteriza um atrator da subida e $K_R>0$ um repulsor.

## 3. Avaliação

No ramo constitutivo vigente,

$$
K_R=5.32888850629080>0,
$$

$$
\mathsf M_R^{(\mathcal W)}=0.652068126520676,
$$

e

$$
\boxed{
\Gamma_R^{\rm crescimento}
=3.47479834473450>0.
}
$$

O tempo de e-folding no parâmetro auxiliar é

$$
\Gamma_R^{-1}=0.287786484506457.
$$

## 4. Consequência para Q30

$K_R>0$ ainda prova coercividade da ação estática e positividade do operador
de Jacobi. Mas o fluxo de Perelman aumenta uma entropia e repele esse mínimo.
Ele não pode ser usado automaticamente como mobilidade causal da medida
$e^{-\operatorname{Re}S}$.

Uma dinâmica física de descida teria o sinal oposto, mas esse sinal deve vir
da reconstrução causal $z_\tau=\tau+i\nu_0t$, não de uma troca manual.

## 5. Veredito

$$
\boxed{
\text{o ramo }K_R>0\text{ é coercivo estaticamente, mas repulsor do fluxo
ascendente de }\mathcal W_T.
}
$$

O sinal do fluxo auxiliar está resolvido. A mobilidade causal em $t$ continua
aberta.

## 6. Classificação

- sinal da primeira variação: derivação variacional;
- compatibilidade com monotonicidade: exata;
- taxa radial: avaliação direta;
- interpretação anterior como relaxação: corrigida;
- dinâmica causal física: aberta.

