---
title: "Difusão universal e inércia geométrica — análise condicional"
tipo: derivacao
status: derivacao-estocastica-com-origem-geometrica-condicional
---

# Difusão universal e inércia geométrica — análise condicional

## 1. Hipótese de escala

A proposta original introduz uma difusão universal

$$
\nu_0=\frac{\hbar}{2m_0}
$$

e um fator geométrico positivo

$$
\Omega=\frac{m}{m_0}.
$$

Se o gerador local contiver o coeficiente efetivo

$$
\nu_{\rm eff}=\frac{\nu_0}{\Omega},
$$

então, algebricamente,

$$
\nu_{\rm eff}
=\frac{\hbar}{2m_0}\frac{m_0}{m}
=\frac{\hbar}{2m}.
$$

Essa identidade mostra que a dependência $1/m$ pode ser representada por uma
escala geométrica. Ela não demonstra que a ação oficial produz $\Omega$.

## 2. Correção necessária para difusão variável

Para o processo de Itô

$$
dX_t=b\,dt+\sqrt{2D(X_t,t)}\,dW_t,
$$

a equação de Fokker--Planck é

$$
\partial_t\rho
=-\nabla\cdot(b\rho)+\Delta(D\rho),
$$

e não simplesmente

$$
\partial_t\rho
=-\nabla\cdot(b\rho)+D\Delta\rho.
$$

Como

$$
\Delta(D\rho)
=D\Delta\rho
+2\nabla D\cdot\nabla\rho
+\rho\Delta D,
$$

uma função $D=\nu_0\Omega^{-1}$ gera termos adicionais com derivadas de
$\Omega$. O texto original os omitia.

Uma formulação geométrica alternativa pode escolher o gerador em forma de
divergência,

$$
\mathcal L\rho=\nabla\cdot(D\nabla\rho),
$$

mas isso corresponde a uma escolha específica de deriva, medida e convenção
estocástica. Essa escolha precisa ser derivada ou declarada.

## 3. Velocidade osmótica e recuperação de Nelson

As duas equações forward e backward compatíveis fornecem

$$
u^i
=\nu_0\Omega^{-1}
\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
$$

Portanto a dinâmica estocástica variável está fechada sem cancelar
artificialmente $\nabla\Omega$. No setor em que $\Omega$ é constante,

$$
u^i=\frac{\hbar}{2m}\nabla^i\ln\rho,
$$

e recupera-se exatamente Nelson. A derivação covariante detalhada está em
[[Difusão variável de Nelson na GDQ]].

## 4. O que está demonstrado e o que permanece aberto

Demonstrado algebricamente sob a hipótese de escala:

$$
\nu_0\Omega^{-1}=\frac{\hbar}{2m}.
$$

Ainda não demonstrado pela redução estocástica:

1. que $m/m_0$ é exatamente o fator geométrico $\Omega$;
2. que $m_0$ é selecionado sem calibração pelo background estacionário;
3. que a ação oficial produz esse gerador para todo background;
4. que a estabilidade do sóliton determina unicamente sua massa inercial.

Portanto, o cálculo de difusão variável está demonstrado; a emergência
geométrica das massas continua sendo uma etapa solitônica distinta.
