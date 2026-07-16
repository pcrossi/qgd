# Q41 — Adendo técnico: testes GDQ para poço e oscilador

## 1. Objetivo

Este adendo transforma a Questão 41 em um conjunto de testes calculáveis da
GDQ.

A ideia é separar:

1. recuperação do limite Schrödinger--Madelung;
2. interpretação geométrica de \(\rho,S_R\);
3. correções genuinamente GDQ produzidas por contorno, curvatura, torção e
   fluxo métrico.

O critério é:

\[
\boxed{
\text{uma correção só é propriamente GDQ se desaparece no limite plano,
sem torção e com parede ideal.}
}
\]

---

## 2. Variáveis reduzidas

Da ação GDQ:

\[
\mathcal S_{\rm GDQ}
\]

usa-se a decomposição:

\[
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
R=\sqrt\rho.
\]

No setor estacionário reduzido:

\[
I_{\rm Mad}[\rho,S_R,g]
=
\int dt\int_\Sigma
\left[
\rho
\left(
\partial_tS_R
+\frac12G^{AB}\partial_AS_R\partial_BS_R
+V_{\rm ext}
\right)
+\frac{\hbar^2}{8m}
\frac{G^{AB}\partial_A\rho\,\partial_B\rho}{\rho}
\right]d\mu_g.
\]

A variação em \(S_R\) gera continuidade; a variação em \(\rho\) gera
Hamilton--Jacobi--Bohm.

No limite plano:

\[
g\to g_0,
\qquad
B\to0,
\qquad
d\mu_g\to dx.
\]

Nesse limite, poço e oscilador recuperam exatamente a mecânica quântica
elementar.

---

## 3. Teste A — poço com impedância geométrica de contorno

### 3.1 Funcional

Considere:

\[
I_{\rm bulk}
=
\int dt\int_0^L
\left[
\frac{\hbar^2}{2m}|R'|^2
+V R^2
\right]dx.
\]

Para uma parede física de espessura finita, acrescente o termo de contorno:

\[
I_{\partial}
=
\frac{\hbar^2}{2m}
\int dt
\left[
\lambda_0R^2(0,t)
+\lambda_LR^2(L,t)
\right].
\]

Aqui:

\[
\boxed{
\lambda_0,\lambda_L
\text{ são impedâncias geométricas de parede.}
}
\]

### 3.2 Variação

A variação total:

\[
\delta(I_{\rm bulk}+I_\partial)=0
\]

gera no bulk:

\[
-
\frac{\hbar^2}{2m}R''
+VR
=ER.
\]

Nas bordas:

\[
\boxed{
R'(0)=\lambda_0R(0),
\qquad
R'(L)=-\lambda_LR(L).
}
\]

Logo, a parede ideal Dirichlet é o limite:

\[
\lambda_0,\lambda_L\to+\infty.
\]

### 3.3 Espectro para \(V=0\)

No interior:

\[
R(x)=A\cos(kx)+B\sin(kx).
\]

A equação espectral é:

\[
\boxed{
(\lambda_0\lambda_L-k^2)\sin(kL)
+k(\lambda_0+\lambda_L)\cos(kL)=0.
}
\]

No caso simétrico:

\[
\lambda_0=\lambda_L=\lambda_\partial,
\]

com:

\[
\lambda_\partial L\gg1,
\]

tem-se:

\[
k_n
=
\frac{n\pi}{L}
\left[
1-\frac{2}{\lambda_\partial L}
+O((\lambda_\partial L)^{-2})
\right].
\]

Assim:

\[
\boxed{
E_n^{\rm Robin}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}
\left[
1-\frac{4}{\lambda_\partial L}
+O((\lambda_\partial L)^{-2})
\right].
}
\]

### 3.4 Leitura GDQ

A parte nova da GDQ não é a condição de Robin por si só. A parte nova é derivar
\(\lambda_\partial\) da ação de contorno:

\[
\boxed{
\lambda_\partial(q)
=
\lambda_{\rm bare}
-
J_\partial^\dagger(q)K_\partial^{-1}(q)J_\partial(q).
}
\]

Aqui:

1. \(K_\partial\) é a Hessiana dos modos de superfície;
2. \(J_\partial\) é a fonte de acoplamento entre o modo do poço e a parede;
3. o termo \(J^\dagger K^{-1}J\) é o complemento de Schur dos modos relaxáveis.

Esse é o mesmo princípio usado em Q40 para impedância coletiva.

---

## 4. Teste B — oscilador em fundo curvo/torsional

### 4.1 Métrica efetiva

Use uma métrica unidimensional:

\[
ds^2=a^2(x)dx^2,
\qquad
d\mu_g=a(x)dx.
\]

O Laplace--Beltrami é:

\[
\Delta_gR
=
\frac1a\partial_x
\left(
\frac1a\partial_xR
\right).
\]

O funcional estacionário é:

\[
\mathcal E_g[R]
=
\int
\left[
\frac{\hbar^2}{2m}g^{xx}|\partial_xR|^2
+\frac12m\omega^2x^2R^2
+V_{\rm tor}(x)R^2
\right]d\mu_g.
\]

### 4.2 Perturbação fraca

Tome:

\[
a(x)=1+\varepsilon h(x),
\qquad
V_{\rm tor}(x)=\varepsilon W_T(x),
\qquad
|\varepsilon|\ll1.
\]

Em coordenada geodésica:

\[
dy=a(x)dx.
\]

Invertendo:

\[
x(y)=y-\varepsilon H(y)+O(\varepsilon^2),
\qquad
H'(y)=h(y).
\]

O potencial harmônico vira:

\[
\frac12m\omega^2x^2
=
\frac12m\omega^2y^2
-
\varepsilon m\omega^2yH(y)
+O(\varepsilon^2).
\]

Logo:

\[
\boxed{
\Delta E_n^{\rm geom}
=
-
\varepsilon m\omega^2
\langle n|yH(y)|n\rangle
+
\varepsilon\langle n|W_T(y)|n\rangle.
}
\]

Essa expressão é uma previsão formal quando \(h\) e \(W_T\) forem obtidos da
equação métrica GDQ, e não escolhidos livremente.

---

## 5. Teste C — gaussiana como atrator, não ansatz

O funcional plano do oscilador é:

\[
\mathcal E[R]
=
\int_{\mathbb R}
\left[
\frac{\hbar^2}{2m}|R'|^2
+\frac12m\omega^2x^2R^2
\right]dx,
\qquad
\int R^2dx=1.
\]

O fluxo de gradiente normalizado é:

\[
\partial_\tau R
=
-
\frac{\delta}{\delta R}
\left[
\mathcal E[R]-E\int R^2dx
\right].
\]

Isto dá:

\[
\partial_\tau R
=
\frac{\hbar^2}{2m}R''
-
\frac12m\omega^2x^2R
+ER.
\]

Expandindo:

\[
R(\tau,x)=\sum_nc_n(\tau)R_n(x),
\]

segue:

\[
c_n(\tau)
=
c_n(0)e^{-(E_n-E_0)\tau}
\quad(n>0).
\]

Como:

\[
E_n-E_0>0,
\]

temos:

\[
\boxed{
R(\tau,x)\to R_0(x)
=
A e^{-m\omega x^2/(2\hbar)}.
}
\]

Assim, a gaussiana é consequência de dominância espectral do fluxo, não um
chute.

---

## 6. Teste D — Hessiana e índice de Morse

### 6.1 Poço

No poço ideal:

\[
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
-E_n.
\]

Com as mesmas condições de contorno:

\[
\lambda_k(\mathcal J_n)=E_k-E_n.
\]

Para \(n=1\):

\[
E_k-E_1\ge0
\]

módulo normalização. Logo, o estado fundamental é mínimo.

Para \(n>1\), há \(n-1\) direções negativas. O estado excitado é ponto crítico,
não mínimo global.

### 6.2 Oscilador

No oscilador:

\[
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
+\frac12m\omega^2x^2
-E_n.
\]

Logo:

\[
\lambda_k(\mathcal J_n)=E_k-E_n.
\]

O índice de Morse do estado \(n\) é:

\[
\boxed{
\operatorname{ind}_{\rm Morse}(R_n)=n.
}
\]

Na GDQ, esse índice deve ser compatível com a fase de Maslov/Cartan associada
aos pontos de retorno.

---

## 7. Critério de fechamento forte

A Q41 fica estruturalmente fechada pelo documento principal
`questão_41.md`.

O fechamento forte, como teste propriamente GDQ, exige avaliar:

1. \(\lambda_\partial\) a partir de \(K_\partial,J_\partial\);
2. \(h(x)\) e \(W_T(x)\) a partir da equação métrica/torsional reduzida;
3. convergência do fluxo para o atrator gaussiano;
4. espectro da Hessiana e índice de Morse;
5. recuperação exata do limite plano:

   \[
   \lambda_\partial\to\infty,
   \qquad
   h\to0,
   \qquad
   W_T\to0.
   \]

Se esses cinco itens forem demonstrados, poço e oscilador deixam de ser apenas
exemplos de correspondência e passam a ser testes elementares reais da GDQ.

