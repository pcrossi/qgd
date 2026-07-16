# Ponte global--local — fechamento do fator causal

## 1. Questão avaliada

Era necessário decidir se o vínculo energético continha um fator causal livre
$K_\gamma$ ou se esse fator já estava fixado pela prescrição causal vigente.

## 2. Resultado canônico reaproveitado

O documento `q29/projetor_causal_cauchy_normalizado.md`, compatível com as
Questões 4 e 9, define

$$
\mathfrak P_\gamma[F]
=\frac{1}{2\pi i w_\gamma}
\oint_\gamma F(z_\tau)\frac{dz_\tau}{z_\tau}.
$$

Esse operador extrai o coeficiente de Laurent físico:

$$
\mathfrak P_\gamma[F]=F_0.
$$

O fator $1/(2\pi i w_\gamma)$ não altera a ação oficial. Ele pertence ao mapa
de reconstrução física já usado implicitamente quando a variação da ação
impõe $E_0=0$ nas Questões 4 e 9.

Para um coeficiente hermitiano independente de $z_\tau$,

$$
\mathfrak P_\gamma[1]=1.
$$

Logo, no setor estacionário da ponte,

$$
\boxed{K_\gamma=1.}
$$

Esse valor não foi obtido pelo condicionamento do solver nem por comparação
com uma raiz desejada.

## 3. Vínculo energético

Sob os dados globais já fixados pelo problema — $R_H=1$, $\beta_E=2\pi$,
$E_H=1$ e a conversão de Einstein associada a $\alpha$ — o vínculo reduzido é

$$
\boxed{
\mathcal C_E
=\frac{p_0^{\rm red}e^{-x_0}}{Z_0}-1=0.
}
$$

Se o background final possuir dependência causal não trivial, não se deve
substituí-la por uma constante. Nesse caso, aplica-se o mesmo projetor ao
integrando completo:

$$
\mathcal C_E
=\mathfrak P_\gamma\!\left[
\frac{p_0^{\rm red}(z_\tau)e^{-x_0(z_\tau)}}{Z_0(z_\tau)}
\right]-1.
$$

Portanto $K_\gamma=1$ fecha o background estacionário, mas não apaga uma
dependência causal que venha a surgir da solução.

## 4. Verificação numérica

O script `ponte_global_local_tau_causal.py` verifica por quadratura em círculos
com winding $1$, $2$ e $-1$ que o projetor normalizado extrai o coeficiente
constante de uma série de Laurent e que

$$
\mathfrak P_\gamma[1]=1
$$

até precisão de máquina.

Classificação: identidade analítica acompanhada por teste de consistência
numérico. Não é ajuste, calibração nem previsão fenomenológica.
