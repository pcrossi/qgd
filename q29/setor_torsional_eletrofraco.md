# Q29 — Teste do setor torsional como modo eletrofraco

## 1. Redução ao modo carregado

Na extensão Perelman--Bismut usada pelo manuscrito,

$$
\mathcal W_T
\supset
-\frac{\tau}{12}
\int |B|^2d\mu.
$$

Considere um modo normalizado

$$
B=\beta\,\Xi_{\rm EW},
\qquad
\int|\Xi_{\rm EW}|^2d\mu=1,
$$

com $\Xi_{\rm EW}$ projetado no setor $(1,2)_{1/2}$. Então

$$
\boxed{
V_B^{(2)}(\beta)
=-\frac{\tau}{12}|\beta|^2.
}
$$

Logo, na convenção da expansão

$$
V=\frac12a_2|\beta|^2+\frac14a_4|\beta|^4+\cdots,
$$

temos

$$
\boxed{a_2=-\frac\tau6<0.}
$$

O setor torsional fornece o sinal necessário à quebra.

## 2. Ausência de quártica direta

O funcional escrito contém apenas $|B|^2$. Portanto,

$$
\delta_B^4\mathcal W_T=0
$$

com métrica e dilatão congelados. Assim,

$$
a_4^{\rm direto}=0.
$$

## 3. Retroação métrico--dilatônica

Se $x=(h,\varphi)$ reúne os modos estáveis e $K>0$ é sua Hessiana, a expansão
mais geral até a ordem necessária é

$$
V(\beta,x)
=-\frac\tau{12}|\beta|^2
+\frac12\langle x,Kx\rangle
+\langle x,C\rangle|\beta|^2
+V_4^{\rm intr}|\beta|^4+cdots.
$$

A equação de resposta linear fornece

$$
x_*=-K^{-1}C|\beta|^2.
$$

Substituindo de volta,

$$
V_{\rm eff}(\beta)
=-\frac\tau{12}|\beta|^2
+\left(
V_4^{\rm intr}
-\frac12\langle C,K^{-1}C\rangle
\right)|\beta|^4+cdots.
$$

Portanto, a eliminação de um setor estável contribui com sinal não positivo:

$$
\boxed{
\Delta V_4^{\rm backreaction}
=-\frac12\langle C,K^{-1}C\rangle\leq0.
}
$$

Ela não pode, sozinha, produzir a quártica positiva necessária. É obrigatório
existir uma contribuição intrínseca

$$
V_4^{\rm intr}
>\frac12\langle C,K^{-1}C\rangle.
$$

## 4. Vínculo de fluxo como alternativa

Se a magnitude torsional é fixada por uma classe integral,

$$
\frac1{2\pi}\int_{\Sigma_3}B=n_B\in\mathbb Z,
$$

então $|\beta|$ não é determinado por uma quártica de Landau: ele é um módulo
de norma fixa. A quebra passa a ser descrita por um modelo sigma não linear,

$$
\Phi_{\rm EW}^\dagger\Phi_{\rm EW}=\frac{v^2}{2},
$$

com multiplicador de Lagrange. Essa rota pode gerar massas para $W$ e $Z$ sem
postular um potencial fundamental, mas a excitação radial observada exigiria
a elasticidade finita do vínculo.

## 5. Resultado

O setor torsional resolve apenas metade do problema:

$$
\boxed{a_2=-\tau/6<0.}
$$

Ele não determina $a_4>0$. A ação atualmente escrita precisa fornecer uma das
duas estruturas:

1. quarta variação intrínseca positiva da curvatura de Bismut completa; ou
2. vínculo topológico de fluxo com elasticidade calculável.

Sem uma dessas estruturas, o potencial eletrofraco fica ilimitado na direção
torsional e a Q29 não está matematicamente fechada.
