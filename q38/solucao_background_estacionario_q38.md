# Q38 — Solução explícita do background estacionário de Einstein–Bismut

## 1. Geometria

Use a decomposição compatível com o fundo cosmológico já adotado:

\[
\mathcal K_8=S^3_R\times T^5
=\underbrace{(S^3_R\times S^1_R)}_{\text{superfície de Hopf}}\times T^4.
\]

O fator \(S^3\times S^1\) admite uma estrutura Hermitiana de superfície de
Hopf. Escolha um coframe ortonormal \(e^1,e^2,e^3\) em \(S^3_R\), com

\[
\operatorname{Ric}_{ab}=\frac{2}{R^2}\delta_{ab},
\qquad a,b=1,2,3,
\]

e coframes paralelos nos cinco ciclos toroidais.

## 2. Torção e dilaton

Na convenção do Capítulo 17, escolha

\[
\boxed{H_*=\frac{2}{R}\,e^1\wedge e^2\wedge e^3.}
\]

Essa é a torção canônica da superfície de Hopf, com orientação escolhida para
que \(H_*=d^c\omega_*\). Como a forma de volume de \(S^3\) é harmônica,

\[
dH_*=0,\qquad d^\dagger H_*=0.
\]

Escolha \(f_*\) espacialmente constante. Como a ação oficial contém

\[
\mathcal U_*=
\frac{e^{-f_*}}{(4\pi z_\tau)^n},
\]

a normalização em cada folha do fluxo fixa

\[
\boxed{
f_*(z_\tau)
=\log\!\left[
\frac{2\pi^2R^3\prod_{A=1}^{5}(2\pi L_A)}
{(4\pi z_\tau)^n}
\right],
\qquad
\int_{S^3_R\times T^5}\mathcal U_*dV=1.
}
\]

Assim, \(f_*\) é constante nas coordenadas internas, mas pode depender do
parâmetro complexo do fluxo. A expressão antiga sem
\((4\pi z_\tau)^n\) normalizava \(e^{-f}dV\), e não a medida oficial
\(\mathcal U dV\).

## 3. Verificação da equação métrica

Para \(H_{abc}=h\epsilon_{abc}\), com \(h=2/R\),

\[
H_{a mn}H_b{}^{mn}=2h^2\delta_{ab}=\frac8{R^2}\delta_{ab}.
\]

Então, nas direções de \(S^3\),

\[
R_{ab}-\frac14H_{a mn}H_b{}^{mn}
=\frac2{R^2}\delta_{ab}-\frac14\frac8{R^2}\delta_{ab}=0.
\]

Nas direções toroidais, \(R_{AB}=H_{A mn}=0\), e, como a dependência em
\(z_\tau\) não é uma dependência espacial interna,
\(\nabla_i\nabla_jf_*=0\). Portanto

\[
\boxed{
R_{ij}-\frac14H_{ikm}H_j{}^{km}+\nabla_i\nabla_jf_*=0.
}
\]

Esta é uma sela **steady** do fluxo generalizado, isto é,
\(1/(2\sigma)=0\). Um toro compacto plano não poderia satisfazer a versão
shrinking com lado direito estritamente positivo e dilaton constante.

## 4. Equação torsional e regularidade

A segunda equação estacionária é

\[
d_f^\dagger H=d^\dagger H+i_{\nabla f}H=0.
\]

Como \(d^\dagger H_*=0\) e \(\nabla_K f_*=0\),

\[
\boxed{d_{f_*}^\dagger H_*=0.}
\]

A densidade espacial \(\rho_*=e^{-f_*}>0\) é globalmente regular e não possui os zeros
do ansatz FLRW antigo.

## 5. Relação com `src/solve_dilaton.py`

O script antigo testa um ansatz diferente: insere a evolução cosmológica na
equação dilatônica e fixa \(b(t)=1\), obtendo
\(\ddot u+3u/2=0\). Aqui resolve-se primeiro o setor interno compacto
estacionário; o parâmetro do fluxo não é tratado como coordenada lorentziana
do fator interno. Assim, \(f_*\) espacialmente constante resolve as equações
elípticas internas; sua dependência de normalização em \(z_\tau\) pertence ao
problema causal externo.

O diagnóstico antigo continua válido para seu ansatz, mas aquele ansatz não é
o background interno apropriado ao determinante de Q38.

## 6. Background assintótico e par para o determinante

O background homogêneo resolvido é
\(\mathfrak B_*=(g_*,f_*,H_*)\). Os dois setores devem tender a ele na borda,
mas não podem ter exatamente o mesmo \((g,H)\) em todo o interior: a conexão
de Bismut é determinada pela estrutura Hermitiana. Portanto, escrevemos

\[
\mathfrak B_{\rm inst}=(g_*+\delta g_{\rm inst},
f_*+\delta f_{\rm inst},H_*+\delta H_{\rm inst}),
\qquad
\mathfrak B_0=(g_*,f_*,H_*),
\]

\[
\delta H_{\rm inst}=d^c\delta\omega_{\rm inst},
\qquad
Q_{\rm rel}(\nabla_B[g_*+\delta g_{\rm inst},J_*+\delta J_{\rm inst}])
-Q_{\rm rel}(\nabla_B[g_*,J_*])=\frac12.
\]

Na borda, \(\delta g_{\rm inst}=\delta f_{\rm inst}
=\delta H_{\rm inst}=0\), de modo que volume, temperatura, normalização e
condições assintóticas são idênticos. A retroação no interior deve ser obtida
das equações de sela; não é permitido variar \(\mathcal A_B\) como campo
independente.

## 7. Jacobiano \(\alpha^4\)

No setor de Hopf, a equação estacionária demonstrou

\[
\frac14H_{a mn}H_b{}^{mn}=R_{ab}.
\]

Após normalização pela curvatura do background, o tensor quadrático é a
métrica no subespaço Hermitiano transmitido. Uma amplitude de conexão
\(\alpha\) produz resposta quadrática \(\alpha^2\) em cada uma das duas
direções complexas internas. Portanto

\[
D_{\rm tr}=\alpha^2I_2,
\qquad
\boxed{J_{\rm tr}=\det_{\mathbb C}D_{\rm tr}=\alpha^4.}
\]

Isso deriva a quarta potência sem confundir a dimensão global complexa quatro
com a fibra interna complexa dois.

## 8. Status

Ficam resolvidos o background interno assintótico regular, a normalização do
dilaton, o cancelamento Ricci--torção e o jacobiano \(\alpha^4\) no canal
homogêneo. Antes de diagonalizar, falta resolver a retroação local
\((\delta g_{\rm inst},\delta f_{\rm inst},\delta H_{\rm inst})\) que realiza
a carga relativa. Depois disso, o cálculo é diagonalizar

\[
K_{\rm eff}=K_H-JK_T^{-1}J^\dagger
\]

nos setores relativo e trivial, usando a mesma extensão auto-adjunta.
