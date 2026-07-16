# Q38 — Fechamento da auditoria pela ação GDQ pura

## 1. Variação com normalização

Defina
\[
\sigma=\frac{f+\bar f}{2},\qquad
\mathcal U=\frac{e^{-\sigma}}{(4\pi z_\tau)^n},
\qquad
\int_{\mathcal M_{\mathbb C}}\mathcal U\,dV_g=1.
\]

A restrição deve ser imposta por um multiplicador \(\lambda\). No setor real,
a variação dilatônica tem a estrutura
\[
-4\tau\frac{\Delta\sqrt{\mathcal U}}{\sqrt{\mathcal U}}
+\tau\mathcal R+\sigma-n-1=\lambda.
\]

Para \(\sigma\) constante,
\[
\boxed{\tau\mathcal R_*+\sigma_*-n-1=\lambda.}
\]

Logo, a equação local não fixa isoladamente \(\sigma_*\). O multiplicador é
determinado pela normalização global.

## 2. Valor constante do dilaton

Se o background compacto possui volume \(V_*\) e \(\mathcal U_*\) é constante,
\[
1=\frac{e^{-\sigma_*}}{(4\pi z_\tau)^n}V_*.
\]
Portanto
\[
\boxed{
\sigma_*=\log\left[\frac{V_*}{(4\pi z_\tau)^n}\right].
}
\]

Obter \(\sigma_*=1/(2\alpha)\) equivale a demonstrar
\[
\boxed{
\frac{V_*}{(4\pi z_\tau)^n}
=e^{1/(2\alpha)}.
}
\]
Essa é uma relação global entre volume e escala de difusão, não uma ação
instantônica.

## 3. Cancelamento pela normalização

No modo interno constante e sem warp dependente de \(y\),
\[
\int_K\mathcal U_*\sqrt q\,d^{2n-4}y=1
\]
quando a medida é normalizada no próprio setor interno. Assim,
\[
e^{-\sigma_*}
\]
é cancelado pelo volume usado para normalizá-lo. Ele não pode ser contado
novamente como supressão independente em \(C_R\).

O coeficiente correto continua sendo
\[
C_R^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}\operatorname{Re}
\int_\gamma d\tau\int_K
\eta_R e^{2A}\mathcal U_*\sqrt q\,d^{2n-4}y.
\]

Um exponencial residual só pode sobreviver se a projeção gravitacional não
coincidir com o modo normalizado total, por exemplo devido a warp não
constante ou projeção modal. Nesse caso ele deve ser calculado dentro da
integral, não multiplicado externamente.

## 4. Equação métrica estacionária

A variação métrica do funcional normalizado de Perelman produz, no setor
Hermitiano real,
\[
\boxed{
\operatorname{Ric}_{\mathcal R}
+\nabla\nabla\sigma
=\frac{1}{2\tau}g
}
\]
na convenção shrinking. Se \(\mathcal R\) inclui a torção constitutiva, usa-se
o tensor de Ricci generalizado correspondente.

## 5. Teste de \(T^5\times S^3\)

Considere \(T^5\) plano, \(S^3\) redondo e \(\sigma\) constante. Nas direções
toroidais,
\[
\operatorname{Ric}_{AB}=0,\qquad
\nabla_A\nabla_B\sigma=0.
\]
A equação exigiria
\[
0=\frac{1}{2\tau}g_{AB},
\]
o que é impossível para \(\tau<\infty\).

Portanto
\[
\boxed{
T^5_{\rm plano}\times S^3
\text{ com dilaton constante não é um ponto crítico shrinking da ação oficial.}
}
\]

Ele pode representar um limite steady \(\tau\to\infty\), uma compactificação
auxiliar ou uma aproximação cosmológica, mas não o background estacionário
finito usado para avaliar \(C_R\) sem warp adicional.

## 6. O que seria necessário para uma solução

A ação GDQ permite três rotas internas:

1. \(\sigma(y,\tau)\) não constante;
2. warp \(A(y,\tau)\) que torne o tensor interno não plano;
3. limite steady \(\tau\to\infty\).

No toro compacto estritamente plano, uma Hessiana periódica não pode ser uma
constante positiva em todas as direções, pois sua integral é zero. Portanto a
primeira rota isolada não resolve a equação. É necessário warp/curvatura
interna ou o limite steady.

## 7. Consequência para a fórmula numérica

A expressão
\[
\Pi_1=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)}
\]
continua sendo uma parametrização numericamente próxima, mas não foi obtida
pela avaliação da ação oficial:

1. o exponencial é cancelado no modo totalmente normalizado;
2. o background plano \(T^5\times S^3\) não satisfaz o ponto crítico shrinking;
3. o warp que poderia gerar uma projeção residual não foi resolvido;
4. \(\alpha^4(1+\alpha)/\chi_{\rm Fano}\) ainda não foi obtido da integral.

## 8. Veredito rigoroso

A derivação formal
\[
\mathcal S_{\rm GDQ}\longrightarrow
C_R^{\rm GDQ}\longrightarrow
G=\frac{c^4}{16\pi C_R^{\rm GDQ}}
\]
está correta.

Entretanto,
\[
\boxed{
\text{a previsão numérica específica de Q38 não está derivada da ação oficial.}
}
\]

Assim, Q38 fica encerrada como auditoria com resultado negativo: a fórmula
proposta ainda é uma conjectura de avaliação do volume efetivo. Para convertê-la
em teorema, deve-se fornecer e resolver o warp estacionário completo.
