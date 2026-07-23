# Q30 — Limite espectral da medida suavizada GDQ

## 1. Covariância

Seja $L$ a Hessiana física positiva no complemento dos modos zero,
$L\phi_j=\lambda_j\phi_j$. A covariância GDQ é

$$
\boxed{C_\tau=e^{-\tau L}L^{-1},\qquad \tau>0.}
$$

Seus autovalores são $c_j=e^{-\tau\lambda_j}/\lambda_j$.

## 2. Propriedade de traço

Em domínio compacto de dimensão $d$, a lei de Weyl dá
$\lambda_j\sim Cj^{2/d}$. Logo,

$$
\sum_{j=1}^\infty c_j
\lesssim
\sum_{j=1}^\infty
\frac{e^{-\tau Cj^{2/d}}}{j^{2/d}}<\infty.
$$

Portanto,

$$
\boxed{C_\tau\text{ é operador de traço}.}
$$

Isso define uma medida gaussiana de Radon $\mu_{C_\tau}$ no espaço de Hilbert
das flutuações físicas. $\tau$ não é regulador a remover: é resolução
geométrica da GDQ.

## 3. Limite dos cortes

Para

$$
C_{\tau,N}=\sum_{j=1}^N c_j|\phi_j\rangle\langle\phi_j|,
$$

temos

$$
\|C_\tau-C_{\tau,N}\|_1=\sum_{j>N}c_j\to0.
$$

As medidas gaussianas truncadas convergem fracamente para $\mu_{C_\tau}$ e

$$
\mathbb E\|\Phi-\Phi_N\|^2=\sum_{j>N}c_j\to0.
$$

Assim, o limite $N\to\infty$ está construído no setor quadrático.

## 4. Interação

Escreva na thimble

$$
\operatorname{Re}S[q_*+\Phi]
=S_*+\frac12\langle\Phi,L\Phi\rangle+V_{\rm int}(\Phi).
$$

A medida candidata é

$$
d\nu_\tau
=Z_\tau^{-1}e^{-V_{\rm int}/\hbar}d\mu_{C_\tau}.
$$

Uma condição suficiente para existência e convergência uniforme é

$$
\boxed{
V_{\rm int}(\Phi)\ge-a\|\Phi\|^2-b,
\qquad
a<\frac{1}{2\|C_\tau\|}.
}
$$

Sob essa cota, dominância gaussiana/Fernique fornece integrabilidade e
convergência dos observáveis cilíndricos limitados.

## 5. Determinantes relativos

Se $L_C=L_0+K$ e
$C_{\tau,0}^{1/2}KC_{\tau,0}^{1/2}$ é de traço, o quociente é definido por

$$
\boxed{
\frac{\det{}'L_C}{\det{}'L_0}
=\det_F(I+C_{\tau,0}^{1/2}KC_{\tau,0}^{1/2}).
}
$$

Isso substitui o produto infinito formal do termo de um loop.

## 6. Thimble global

O controle espectral não resolve sozinho o ciclo complexo. Uma condição
suficiente seria convexidade forte global no setor topológico:

$$
\boxed{
\operatorname{Hess}\operatorname{Re}S\ge m^2I>0.
}
$$

Ela implicaria único ponto crítico, fluxo de gradiente completo e ausência de
Stokes entre selas. O corpus prova estabilidade local, não essa estimativa
global.

## 7. Veredito

$$
\boxed{
\text{limite gaussiano }N\to\infty\text{ resolvido para }\tau>0;
\text{interação e thimble global dependem de coercividade não provada.}
}
$$

## 8. Classificação

- propriedade de traço e medida gaussiana: teorema;
- convergência quadrática: teorema;
- medida interagente: condicional à cota de coercividade;
- thimble global: aberta.

A auditoria `questoes/q30/associados/obstrucao_coercividade_contorno_causal.md` mostrou que a
coercividade depende dos momentos $\mathfrak c_0,\mathfrak c_1$ e do
coeficiente torsional projetado. O corpus ainda não fixa parametrização,
orientação e ramo de $(\gamma,z_\tau)$ necessários para seus sinais.
