---
title: "Polarização heat-kernel e ausência do polo de Landau"
---

# Polarização heat-kernel e ausência do polo de Landau

Esta nota separa dois cálculos que não devem ser confundidos:

1. o loop geométrico da fase de $f$, derivado diretamente da Hessiana oficial;
2. a tradução $U(1)$ efetiva usada para formular o polo de Landau na linguagem
   perturbativa externa.

Nenhum deles constitui renormalização fundamental por contratermos.

## 1. Loop geométrico da fase no toro

No bulk $M=\mathbb R^4\times T^4$, escreva

$$
f=f_*+i\chi,
\qquad
\bar f=f_*-i\chi.
$$

Para $f_*$ real constante, $\mathcal U=\mathcal U_*$ no setor $\chi$, e a
segunda variação contém

$$
S_\chi^{(2)}
=\frac{Z_\chi}{2}
\int_M g^{MN}\partial_M\chi\partial_N\chi\,dV_g.
$$

Com um ciclo fibrado

$$
ds^2
=h_{\mu\nu}dx^\mu dx^\nu
+R^2(dy+\kappa A_\mu dx^\mu)^2
+ds_{T^3}^2
$$

e decomposição $\chi=\sum_n\chi_ne^{iny}$, obtemos

$$
H_n[A]=-(\partial-iq_nA)^2+m_n^2,
\qquad
q_n=n\kappa,
\qquad
m_n^2=\frac{n^2}{R^2}+\lambda_\perp.
$$

O determinante do par real $n,-n$ é

$$
\Gamma_n^{(1)}[A]=\operatorname{Tr}\ln H_n[A].
$$

O bubble e o termo de contato $A^2|\chi_n|^2$ vêm da mesma Hessiana. O termo
de contato é essencial para Ward. Com corte próprio $s_0$,

$$
\Pi_{n,s_0}(Q^2)
=\frac{q_n^2}{16\pi^2}
\int_0^1dx\,(1-2x)^2
\left[
E_1(s_0m_n^2)
-E_1\!\left(s_0[m_n^2+x(1-x)Q^2]\right)
\right].
$$

Daí

$$
Q^\mu\Pi_{\mu\nu}^{(n)}=0,
\qquad
\Pi_{n,s_0}(\infty)
=\frac{q_n^2}{48\pi^2}E_1(s_0m_n^2)<\infty.
$$

Esse cálculo satisfaz a cadeia ação oficial--Hessiana--operador--determinante--
observável no setor declarado.

## 2. Operador efetivo de comparação e regularização covariante

Seja $L_A$ um operador positivo do tipo Laplace, covariante sob $U(1)$. O
funcional de uma volta regularizado pelo semigrupo é

$$
\Gamma_\tau[A]
=\frac12\operatorname{Tr}
\int_\tau^\infty\frac{ds}{s}e^{-sL_A},
\qquad \tau>0.
$$

Como $L_{A^g}=g^{-1}L_Ag$, a regularização preserva Ward. A segunda variação
em torno de $A=0$ tem a forma

$$
\Pi_{\mu\nu}^{(\tau)}(q)
=(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2).
$$

## 3. Função escalar da comparação

Depois da parametrização de Feynman e da integração gaussiana covariante,

$$
\Pi_\tau(q^2)
=\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\left[
E_1(\tau m^2)
-E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)
\right],
$$

onde

$$
E_1(z)=\int_z^\infty\frac{e^{-u}}{u}\,du.
$$

Em $q=0$ os dois termos coincidem, portanto

$$
\Pi_\tau(0)=0.
$$

Essa subtração é a forma explícita da ausência de massa fotônica no teste.

## 4. Limite infravermelho

Para $\tau q_E^2\ll1$, a diferença de integrais exponenciais tende ao
logaritmo:

$$
\Pi_\tau(q^2)
\longrightarrow
\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\ln\left(1+\frac{x(1-x)q_E^2}{m^2}\right).
$$

No intervalo $m^2\ll q_E^2\ll\tau^{-1}$,

$$
\Pi_\tau(q^2)
=\frac{\alpha_0}{3\pi}\ln\frac{q_E^2}{m^2}
+\text{constante finita}+o(1).
$$

Assim a tradução externa recupera o comportamento perturbativo usual antes
da escala geométrica.

## 5. Saturação ultravioleta

Para $q_E^2\to\infty$ e $0<x<1$,

$$
E_1\!\left(\tau[m^2+x(1-x)q_E^2]\right)\to0.
$$

Como

$$
\int_0^1x(1-x)\,dx=\frac16,
$$

segue

$$
\Pi_\tau(\infty)
=\frac{\alpha_0}{3\pi}E_1(\tau m^2).
$$

Definindo apenas para comparação

$$
\alpha_{\rm eff}(q^2)
=\frac{\alpha_0}{1-\Pi_\tau(q^2)},
$$

o limite ultravioleta é finito se

$$
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
$$

Nessa condição,

$$
\alpha_{\rm eff}(\infty)
=\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}
$$

e não há polo físico no setor suavizado.

## 6. O que a prova não usa

A demonstração não usa a antiga função beta postulada

$$
-b_0\alpha^2+\gamma_C\alpha^3e^{-\Lambda_C^2/Q^2}.
$$

Essa expressão possuía problemas de sinal e não derivava o suposto ponto
fixo. Também não basta dizer que o potencial de Bohm torna $r=0$ inacessível.
O fechamento decorre do operador covariante, da identidade de Ward, do cálculo
de $\Pi_\tau$ e de sua saturação.

## 7. Estatuto

- loop geométrico da fase no toro: derivado da ação oficial;
- finitude de $\Pi_\tau$ para $\tau>0$ na tradução efetiva: demonstrada;
- Ward e $\Pi_\tau(0)=0$: demonstradas;
- recuperação infravermelha: demonstrada no regime declarado;
- ausência do polo: condicional à desigualdade espectral;
- finitude não perturbativa de toda a GDQ: não demonstrada por este teste;
- extensão a qualquer background: exige o operador e o domínio daquele
  background.
