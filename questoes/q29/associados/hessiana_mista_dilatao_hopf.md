# Q29 — Hessiana mista entre dilatão e modo eletromagnético de Hopf

## 1. Objetivo

Verificar diretamente, a partir da ação oficial da GDQ, se a resposta
dilatônica localizada pode vestir o termo cinético eletromagnético mediante
um complemento de Schur quadrático.

Não se acrescenta uma ação de Yang--Mills. O campo eletromagnético é a
flutuação da conexão da fibra de Hopf na métrica:

$$
\eta
\longmapsto
\eta+\kappa_Q A_Q,
\qquad
F_Q=dA_Q.
$$

## 2. Termo produzido pela curvatura oficial

A fórmula de O'Neill fornece

$$
\mathcal R[g(f,A_Q)]
=
\mathcal R[g(f,0)]
-\frac{R^2\kappa_Q^2}{4}|F_Q|^2
+O(F_Q^4).
$$

Após a redução interna, a parcela quadrática tem a forma

$$
\mathcal S_Q^{(2)}[f,A_Q]
=
\frac14K_Q[f]
\int_{M_4}|F_Q|^2dV_4,
$$

com

$$
K_Q[f]
=
C_{\rm GDQ}\tau\kappa_Q^2
\int_{K_\epsilon}
\Phi_Q(y)\,d\mu_f(y),
$$

onde, na redução radial já calculada,

$$
\Phi_Q(\chi)=R^2e^{3A(\chi)}.
$$

## 3. Expansão normalizada da medida

Escreva

$$
f=f_*+t c,
\qquad
\langle c\rangle_{\mu_*}=0.
$$

Para a medida normalizada,

$$
d\mu_{f_*+tc}
=
d\mu_*
\left[
1-tc
+\frac{t^2}{2}
\left(c^2-\langle c^2\rangle_{\mu_*}\right)
+O(t^3)
\right].
$$

Logo,

$$
\frac{dK_Q}{dt}\bigg|_{t=0}
=
-C_{\rm GDQ}\tau\kappa_Q^2
\operatorname{Cov}_{\mu_*}(\Phi_Q,c).
$$

O solver forneceu

$$
\operatorname{Cov}_{\mu_*}(\Phi_Q,c)
=-17{,}1214968064.
$$

Portanto, o acoplamento entre a resposta localizada e a rigidez de Hopf é
real e não nulo.

## 4. Ordem variacional correta

Parametrize a flutuação eletromagnética por

$$
F_Q=q\,\mathcal F,
\qquad
\int_{M_4}|\mathcal F|^2dV_4=1.
$$

Então

$$
\mathcal S_Q[f_*+tc,q]
=
\frac14
\left[K_Q[f_*]+tK_Q'[c]+O(t^2)\right]q^2.
$$

Consequentemente,

$$
\frac{\partial^2\mathcal S_Q}
{\partial t\,\partial q}
\bigg|_{t=q=0}
=0.
$$

O bloco misto da Hessiana quadrática é, portanto,

$$
\boxed{
\mathcal J_{Qf}=0
}
$$

no background sem campo eletromagnético. Isso é consequência da invariância
por reversão da conexão,

$$
F_Q\longmapsto-F_Q,
$$

que proíbe um termo bilinear $cF_Q$.

O primeiro vértice não nulo é de terceira ordem:

$$
\boxed{
\Gamma_{fQQ}[c,\mathcal F,\mathcal F]
=
-\frac12C_{\rm GDQ}\tau\kappa_Q^2
\operatorname{Cov}_{\mu_*}(\Phi_Q,c).
}
$$

Assim, a covariância espectral calculada anteriormente mede o vértice
$fF_Q^2$, não um bloco bilinear da Hessiana.

## 5. Eliminação do dilatão

Se o dilatão responder somente ao próprio campo eletromagnético, sua equação
linearizada é esquematicamente

$$
\mathcal K_f c
+\frac14K_Q'[\,\cdot\,]|F_Q|^2
=0.
$$

Logo,

$$
c
=
-\frac14\mathcal K_f^{-1}K_Q'[\,\cdot\,]|F_Q|^2
+O(F_Q^4).
$$

Ao reinseri-lo na ação, a primeira correção é quártica:

$$
\Delta\mathcal S_{\rm eff}
=
-\frac1{32}
\left\langle
K_Q'|F_Q|^2,
\mathcal K_f^{-1}K_Q'|F_Q|^2
\right\rangle
+O(F_Q^6).
$$

Ela não altera o coeficiente quadrático que define $\alpha$.

## 6. Caso de uma fonte topológica independente

Se o estômato produz um background dilatônico estacionário $c_{\rm stoma}$
independentemente do campo de prova, então

$$
\mathcal K_f c_{\rm stoma}=kJ_{\rm stoma},
\qquad
k\in\mathbb Z,
$$

e o coeficiente quadrático observado é

$$
K_Q^{\rm obs}
=
K_Q[f_*+c_{\rm stoma}].
$$

Nesse caso há um dressing legítimo de $F_Q^2$, mas ele é uma avaliação da
rigidez sobre o background topológico correto, não um complemento de Schur da
Hessiana em $F_Q=0$. Para $k=1$, a resposta linear relativa calculada é

$$
\frac{\delta K_Q}{K_Q}
=
-\frac{\operatorname{Cov}_{\mu_*}(\Phi_Q,c)}
{\langle\Phi_Q\rangle_{\mu_*}}
=0{,}4118891133,
$$

com o sinal final dependente da orientação escolhida para o fluxo.

Como essa correção é grande, a aproximação linear não basta para extrair uma
constante metrológica. É necessário resolver novamente o background
não-linear com a condição de fluxo topológico unitário e só então avaliar
$K_Q[f_{k=1}]$.

## 7. Veredito

O cálculo direto produz um resultado negativo e um positivo:

1. **Negativo:** não existe o vértice bilinear $\mathcal J_{Qf}$ necessário ao
   complemento de Schur proposto no background neutro.
2. **Positivo:** existe um vértice cúbico $fF_Q^2$ quantitativamente não nulo,
   reconstruído pelos resíduos espectrais.
3. **Rota correta:** incorporar $k=1$ como condição de contorno do background
   GDQ, resolver o sistema warped--dilatônico não-linear e calcular a norma do
   modo de Hopf nesse background.

Isso preserva a ação oficial e todos os cálculos anteriores, mas impede usar
a soma de resíduos como fator multiplicativo de $\alpha$ antes de resolver o
background topológico completo.

O background completo foi posteriormente resolvido para fluxo radial
normalizado $k=1$. Encontrou-se

$$
K_Q(1)/K_Q(0)=0{,}993668694,
$$

confirmando o dressing, mas não o fator eletromagnético condicional
$0{,}966590303$. Ver `questoes/q29/associados/resultado_background_fluxo_topologico.md`.
