# Q31 — Ponte torsional entre CP forte, \(SU(3)_C\), \(\chi_{\rm top}\), \(f_B\) e EDM

Este adendo consolida a resposta estrutural da Questão 31 depois do fechamento
da ponte efetiva \(SU(3)_C\) na Questão 30.

O objetivo não é transformar a GDQ em QCD perturbativa nem postular um áxion
elementar. O objetivo é mostrar que o setor forte efetivo já contém os
ingredientes necessários para o relaxamento de CP:

1. uma conexão efetiva \(SU(3)_C\);
2. uma densidade topológica \(F_C\wedge F_C\);
3. um modo angular torsional \(\vartheta_B\);
4. um potencial periódico controlado por \(\chi_{\rm top}\);
5. um fluxo dissipativo de Lyapunov que leva \(\theta_{\rm eff}\) ao mínimo CP.

---

## 1. Entrada herdada da Q30

Da Questão 30, o setor de cor efetivo é:

\[
A_C\in\Omega^1(N,\mathfrak{su}(3)),
\]

com curvatura:

\[
F_C=dA_C+A_C\wedge A_C.
\]

A densidade topológica forte é:

\[
q_C(x)
=
\frac{1}{8\pi^2}
\operatorname{Tr}(F_C\wedge F_C),
\]

ou, em componentes,

\[
q_C(x)
=
\frac{g_s^2}{32\pi^2}
F_{\mu\nu}^a\tilde F^{a\mu\nu}.
\]

A carga topológica é:

\[
Q_C
=
\int_N q_C
\in\mathbb Z.
\]

Essa integralidade é o que força a periodicidade:

\[
\theta\sim\theta+2\pi.
\]

Assim, a Q31 não começa de um escalar arbitrário. Ela começa de uma fase
topológica associada à conexão \(SU(3)_C\) efetiva já construída.

---

## 2. Modo torsional geométrico

Na GDQ, o candidato que substitui o áxion elementar é o modo angular da torção
de Cartan/Bismut.

Se \(B\) representa a 3-forma torsional efetiva, então em \(N^4\):

\[
*B
\]

é uma 1-forma axial. A componente longitudinal/topológica dessa forma define
um ângulo:

\[
\vartheta_B\sim\vartheta_B+2\pi.
\]

O campo canonicamente dimensional, quando for necessário descrevê-lo como modo
efetivo, é:

\[
a=f_B\vartheta_B.
\]

Logo:

\[
a\sim a+2\pi f_B.
\]

A combinação física que entra no setor CP é:

\[
\boxed{
\theta_{\rm eff}
=
\theta_0+\vartheta_B
=
\theta_0+\frac{a}{f_B}.
}
\]

Ponto importante: \(a\) é axion-like como variável efetiva, mas sua origem na
GDQ é geométrica/torsional. Portanto não é necessário postular uma nova partícula
elementar fundamental.

---

## 3. Potencial periódico a partir da susceptibilidade topológica

A energia de vácuo do setor forte efetivo deve ser periódica:

\[
E(\theta)=E(\theta+2\pi).
\]

No setor mínimo, a forma compatível com a periodicidade e com a estabilidade CP
é:

\[
\boxed{
V_{\rm CP}(\theta_{\rm eff})
=
\chi_{\rm top}^{\rm GDQ}
\left(1-\cos\theta_{\rm eff}\right).
}
\]

Para pequenos ângulos:

\[
V_{\rm CP}
=
\frac12\chi_{\rm top}^{\rm GDQ}\theta_{\rm eff}^2
+O(\theta_{\rm eff}^4).
\]

Assim, a expressão quadrática do manuscrito deve ser lida apenas como expansão
local perto do mínimo, não como potencial global.

A susceptibilidade topológica é:

\[
\boxed{
\chi_{\rm top}^{\rm GDQ}
=
\left.
\frac{\partial^2E_{\rm vac}(\theta)}
{\partial\theta^2}
\right|_{\theta=0}
=
\int d^4x\,
\langle q_C(x)q_C(0)\rangle_{\rm GDQ}.
}
\]

Essa fórmula fixa a massa/escala do modo:

\[
\boxed{
m_B^2f_B^2=\chi_{\rm top}^{\rm GDQ}.
}
\]

Se o modo torsional possuir polo propagante, \(m_B\) é uma massa efetiva. Se o
modo for puramente relaxacional, \(m_B\) é a escala de retorno ao atrator CP, não
uma partícula assintótica.

---

## 4. \(f_B\) como normalização canônica do modo torsional

O manuscrito propõe:

\[
V_K=6\pi^5,
\]

e:

\[
\boxed{
f_B
=
M_P\sqrt{\frac{3}{\sqrt{6\pi^5}}}
\approx
6{,}44\times10^{17}\ {\rm GeV}.
}
\]

A leitura correta é:

\[
\boxed{
f_B^2
=
\text{coeficiente cinético do ângulo torsional }\vartheta_B.
}
\]

Ou seja, se a expansão efetiva da ação torsional produz:

\[
S_{\rm tor}^{(2)}
=
\frac12
\int_N
f_B^2
(\partial\vartheta_B)^2\,d{\rm vol}_h,
\]

então:

\[
a=f_B\vartheta_B
\]

é a variável canonicamente normalizada.

Portanto, a fórmula numérica para \(f_B\) deixa de ser tratada como chute quando
for demonstrado que a rigidez torsional e o volume de Kähler do sóliton geram
exatamente esse coeficiente cinético.

Status: há derivação geométrica proposta; falta o cálculo funcional completo da
normalização canônica a partir da ação oficial.

---

## 5. Relaxamento por Lyapunov

Defina:

\[
V(\theta)=\chi_{\rm top}^{\rm GDQ}(1-\cos\theta),
\qquad
\chi_{\rm top}^{\rm GDQ}>0.
\]

A dinâmica dissipativa da GDQ é:

\[
\boxed{
\frac{d\theta}{d\tau}
=
-
\kappa_{\rm CP}
\frac{\partial V}{\partial\theta},
\qquad
\kappa_{\rm CP}>0.
}
\]

Como:

\[
\frac{\partial V}{\partial\theta}
=
\chi_{\rm top}^{\rm GDQ}\sin\theta,
\]

segue:

\[
\frac{d\theta}{d\tau}
=
-
\kappa_{\rm CP}
\chi_{\rm top}^{\rm GDQ}
\sin\theta.
\]

Ao longo do fluxo:

\[
\frac{dV}{d\tau}
=
\frac{\partial V}{\partial\theta}
\frac{d\theta}{d\tau}
=
-
\kappa_{\rm CP}
\left(
\frac{\partial V}{\partial\theta}
\right)^2
\le0.
\]

Logo \(V\) é função de Lyapunov.

Os pontos críticos são:

\[
\sin\theta=0
\quad\Rightarrow\quad
\theta=n\pi.
\]

A segunda variação:

\[
\frac{d^2V}{d\theta^2}
=
\chi_{\rm top}^{\rm GDQ}\cos\theta
\]

mostra que:

1. \(\theta=0\pmod{2\pi}\) é mínimo estável;
2. \(\theta=\pi\pmod{2\pi}\) é máximo instável.

Portanto, para dados iniciais fora do ponto instável:

\[
\boxed{
\theta_{\rm eff}(\tau)\to0\pmod{2\pi}.
}
\]

Isto responde à objeção central: o mínimo CP não é escolhido à mão. Ele é o
atrator estável do fluxo dissipativo quando \(\chi_{\rm top}^{\rm GDQ}>0\).

---

## 6. EDM residual

Para ângulos pequenos:

\[
d_n\simeq C_n\theta_{\rm residual}\,e\,{\rm cm}.
\]

Perto do mínimo:

\[
\frac{d\theta}{d\tau}
\simeq
-
\kappa_{\rm CP}
\chi_{\rm top}^{\rm GDQ}
\theta.
\]

Logo:

\[
\theta(\tau)
=
\theta(0)
\exp\left(
-
\kappa_{\rm CP}
\chi_{\rm top}^{\rm GDQ}
\tau
\right).
\]

No tempo efetivo de confinamento \(\tau_{\rm conf}\):

\[
\boxed{
|d_n|
\le
C_n
|\theta_{\rm inicial}|
\exp\left(
-
\kappa_{\rm CP}
\chi_{\rm top}^{\rm GDQ}
\tau_{\rm conf}
\right).
}
\]

A previsão estrutural segura é supressão exponencial do EDM. A previsão
\(d_n=0\) é o caso limite de projeção exata no atrator, ou de relaxamento
assintótico completo.

---

## 7. Cosmologia do modo

Se o modo torsional for tratado como campo propagante, a equação efetiva é:

\[
\ddot\theta
+
(3H+\Gamma_{\rm GDQ})\dot\theta
+
m_B^2\sin\theta
=0.
\]

Para evitar superprodução tipo áxion livre, a GDQ deve operar no regime:

\[
\boxed{
3H+\Gamma_{\rm GDQ}>2m_B
}
\]

ou, de modo mais forte:

\[
\boxed{
\Gamma_{\rm GDQ}\gg m_B.
}
\]

Se o modo não possuir polo assintótico, a leitura cosmológica é ainda mais
simples: não há condensado axiônico livre; há apenas relaxação torsional
dissipativa no meio geométrico.

---

## 8. Veredito estrutural da Q31

A Questão 31 fica fechada estruturalmente sob as hipóteses já explicitadas:

1. a Q30 fornece o setor \(SU(3)_C\), \(F_C\) e \(q_C=\operatorname{Tr}(F_C\wedge F_C)\);
2. a torção fornece o ângulo \(\vartheta_B\);
3. a integralidade topológica fornece \(\theta\sim\theta+2\pi\);
4. \(\chi_{\rm top}^{\rm GDQ}>0\) fornece a curvatura do potencial;
5. o fluxo de Perelman fornece a dissipação de Lyapunov;
6. o EDM residual é exponencialmente suprimido.

O que permanece aberto é cálculo explícito, não a arquitetura do mecanismo:

1. calcular \(\chi_{\rm top}^{\rm GDQ}\);
2. derivar \(f_B\) por normalização canônica a partir da ação oficial;
3. decidir numericamente se há polo propagante ou apenas modo relaxacional;
4. calcular \(\kappa_{\rm CP}\tau_{\rm conf}\);
5. estimar o EDM residual;
6. verificar cosmologia quantitativa.

\[
\boxed{
\text{Q31 fechada estruturalmente; pendências movidas para cálculo funcional,
numérico e fenomenológico.}
}
\]
