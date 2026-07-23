---
title: "Difusão variável de Nelson na GDQ"
---

# Difusão variável de Nelson na GDQ

Esta nota registra a derivação canônica da difusão variável de Nelson na GDQ.
Ela não altera a ação oficial: descreve a redução estocástica na folha física
depois da reconstrução global--local.

## 1. Dados e domínio

Seja $(\Sigma,h)$ uma folha espacial riemanniana cuja métrica é mantida fixa
durante o passo estocástico local, e seja $\rho>0$ uma densidade normalizada
em relação a $dV_h$. Se $h$ depender explicitamente de $t$, a conservação deve
incluir também $\partial_t dV_h$; essa contribuição não pode ser escondida na
deriva. Definimos

$$
\nu_0=\frac{\hbar}{2m_0},
\qquad
\Omega(x,t)=\frac{m(x,t)}{m_0}>0.
$$

Definimos

$$
D^{ij}(x,t)=\nu_0\Omega^{-1}(x,t)h^{ij}(x).
$$

O processo de Itô forward é

$$
dX_t^i=b_+^i\,dt+\sigma^i{}_a\,dW_t^a,
\qquad
\sigma^i{}_a\sigma^j{}_a=2D^{ij}.
$$

## 2. Gerador e adjunto

Para uma função teste suave $\varphi$, o gerador forward é

$$
\mathcal L_+\varphi
=b_+^i\nabla_i\varphi+D^{ij}\nabla_i\nabla_j\varphi.
$$

O adjunto em relação a $dV_h$ fornece

$$
\partial_t\rho
=\mathcal L_+^*\rho
=-\nabla_i(b_+^i\rho)
+\nabla_i\nabla_j(D^{ij}\rho).
$$

Substituindo $D^{ij}=\nu_0\Omega^{-1}h^{ij}$ e usando compatibilidade métrica,

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\nu_0\Delta_h(\Omega^{-1}\rho).
$$

A regra do produto dá

$$
\begin{aligned}
\Delta_h(\Omega^{-1}\rho)={}&
\Omega^{-1}\Delta_h\rho
+2\nabla^i\Omega^{-1}\nabla_i\rho\\
&+\rho\,\Delta_h\Omega^{-1}.
\end{aligned}
$$

Essa é a origem precisa dos termos de Itô omitidos quando se trata
incorretamente a difusão variável como constante.

## 3. Evolução backward e velocidade osmótica

A descrição backward compatível usa uma deriva $b_-^i$. Igualando as duas
equações de Fokker--Planck para a mesma densidade e impondo corrente física
única, sem acrescentar uma parcela solenoidal independente, obtém-se

$$
b_+^i-b_-^i
=2D^{ij}\nabla_j\ln\rho+2\nabla_jD^{ij}.
$$

Definindo

$$
v^i=\frac{b_+^i+b_-^i}{2},
\qquad
u^i=\frac{b_+^i-b_-^i}{2},
$$

segue, no caso isotrópico,

$$
u^i
=\nu_0\Omega^{-1}\nabla^i\ln\rho
+\nu_0\nabla^i\Omega^{-1}.
$$

Como

$$
\nabla^i\Omega^{-1}
=-\Omega^{-1}\nabla^i\ln\Omega,
$$

temos

$$
\boxed{
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
}
$$

## 4. Limite homogêneo

Se $\Omega$ é constante em um setor de massa $m$,

$$
\nabla\Omega=0,
\qquad
\nu_0\Omega^{-1}=\frac{\hbar}{2m}.
$$

Logo

$$
\partial_t\rho
=-\nabla_i(b_+^i\rho)
+\frac{\hbar}{2m}\Delta_h\rho,
$$

e

$$
u^i=\frac{\hbar}{2m}\nabla^i\ln\rho.
$$

Assim, Nelson é recuperado exatamente no setor homogêneo. O que permanece
condicional não é a conta estocástica, mas a derivação de $\Omega[g,f,\bar f]$
e da escala $m_0$ para cada background material a partir da ação oficial.

## 5. Classificação

- equação de Itô e Fokker--Planck: derivação exata na redução física;
- correções por $\nabla\Omega$: derivação exata;
- recuperação de $\hbar/(2m)$ para $\Omega$ constante: identidade exata;
- origem geométrica de $\Omega$ e seleção de $m_0$: problema solitônico e
  espectral posterior.
