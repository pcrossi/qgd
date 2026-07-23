# Ponte global--local — teste numérico mínimo da catástrofe estocástica

## 1. Enunciado

No melhor candidato preservado antes da perda do ramo energético, testar

$$
F_{\rm red}(q)=r+bq^2+O(q^3)
$$

e o sinal de

$$
\sigma_{\rm req}^2=-\frac rb.
$$

## 2. Ponto e normalização

O teste usa $K_\gamma=1$, o candidato em $h=0{,}18$ da homotopia energética,
integração estrita e os vetores singulares normalizados $(\psi,\phi)$ da
Jacobiana variacional. A normalização é euclidiana nas coordenadas do tiro.
$h$ é auxiliar, não parâmetro físico.

## 3. Resultado

$$
\|\mathfrak F\|_\infty
=1{,}2899213809\times10^{-4},
$$

$$
\sigma_{\min}(D\mathfrak F)
=5{,}2457964783\times10^{-5},
$$

$$
r=\langle\psi,\mathfrak F\rangle
=4{,}4977387416\times10^{-5}.
$$

A segunda diferença central ao longo de $\phi$ forneceu, em seis passos,

$$
b\simeq-3{,}43326\times10^{-5}.
$$

Nos três passos centrais, a dispersão relativa de $b$ foi
$4{,}51\times10^{-5}$. Consequentemente,

$$
\boxed{
\sigma_{\rm req}^2=-\frac rb\simeq1{,}31005>0.
}
$$

## 4. Interpretação e limite

O sinal é favorável: uma covariância positiva do modo mole pode cancelar o
residual projetado na aproximação de dobra. Isso não prova a existência da
sela estatística.

O número $1{,}31005$ ainda não é variância física da GDQ, porque $q$ foi
normalizado na métrica euclidiana do tiro. Falta normalizar $\phi$ pela
métrica física e calcular

$$
\sigma_{\rm GDQ}^2
=\mathfrak P_\gamma
\left[
\langle\phi,(K^{\rm phys}-i0_\gamma)^{-1}\phi\rangle
\right].
$$

Também é necessário retirar a dependência do parâmetro auxiliar $h$.

Classificação: teste numérico de consistência e sinal; não é ajuste, sela,
prova de existência ou demonstração de estabilidade.

Script: `ponte_global_local_teste_catastrofe_simples.py`.
