# Q29 — Bloco 3 — Massas de \(W^\pm\), \(Z\), fóton e ângulo de Weinberg

## 1. Objetivo

Mostrar como:

\[
SU(2)_L\times U(1)_Y
\to
U(1)_{\rm EM}
\]

gera:

\[
m_W,\quad m_Z,\quad m_\gamma=0,
\quad
\theta_W.
\]

Este bloco usa a notação eletrofraca usual apenas como linguagem efetiva de
laboratório. Na GDQ, \(W\), \(Y\), \(g\), \(g'\), \(\theta_W\), \(m_W\) e
\(m_Z\) devem ser lidos como projeções, normas internas, rigidezes e
autovalores da Hessiana geométrica. Eles não são postulados fundamentais
adicionados à ação oficial.

---

## 2. Derivada covariante do modo de ordem

Para:

\[
\Phi_{\rm EW}\sim(1,2)_{1/2},
\]

a derivada covariante é:

\[
\boxed{
D_\mu\Phi
=
\left(
\partial_\mu
-igW_\mu^i\frac{\sigma_i}{2}
-ig'\frac12B_\mu
\right)\Phi.
}
\]

---

## 3. Condensado efetivo

Em calibre unitário:

\[
\boxed{
\langle\Phi\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
0\\v
\end{pmatrix}.
}
\]

Esse vetor preserva:

\[
\boxed{
Q=T_3+Y.
}
\]

Portanto:

\[
\boxed{
SU(2)_L\times U(1)_Y
\to
U(1)_{\rm EM}.
}
\]

---

## 4. Massas carregadas

Definindo:

\[
W_\mu^\pm
=
\frac1{\sqrt2}
\left(
W_\mu^1\mp iW_\mu^2
\right),
\]

o termo:

\[
(D_\mu\Phi)^\dagger(D^\mu\Phi)
\]

gera:

\[
\boxed{
m_W=\frac{gv}{2}.
}
\]

---

## 5. Setor neutro

A matriz de massa neutra é:

\[
\frac{v^2}{8}
\begin{pmatrix}
W_\mu^3 & B_\mu
\end{pmatrix}
\begin{pmatrix}
g^2 & -gg'\\
-gg' & g'^2
\end{pmatrix}
\begin{pmatrix}
W^{3\mu}\\
B^\mu
\end{pmatrix}.
\]

Os autovalores são:

\[
\boxed{
m_\gamma^2=0,
}
\]

e:

\[
\boxed{
m_Z^2
=
\frac{v^2}{4}(g^2+g'^2).
}
\]

Logo:

\[
\boxed{
m_Z=\frac v2\sqrt{g^2+g'^2}.
}
\]

---

## 6. Mistura de Weinberg

Os autovetores são:

\[
\begin{pmatrix}
Z_\mu\\
A_\mu
\end{pmatrix}
=
\begin{pmatrix}
\cos\theta_W & -\sin\theta_W\\
\sin\theta_W & \cos\theta_W
\end{pmatrix}
\begin{pmatrix}
W_\mu^3\\
B_\mu
\end{pmatrix}.
\]

Com:

\[
\boxed{
\tan\theta_W=\frac{g'}{g}.
}
\]

E:

\[
\boxed{
e=g\sin\theta_W=g'\cos\theta_W.
}
\]

---

## 7. Interpretação GDQ dos acoplamentos

Os acoplamentos são normas/rigidezes internas:

\[
\boxed{
\frac1{g^2}
=
\mathcal N_W
\int_{\mathcal I}
\|\xi_W\|^2d\mu_g,
}
\]

\[
\boxed{
\frac1{g'^2}
=
\mathcal N_Y
\int_{\mathcal I}
\|\xi_Y\|^2d\mu_g.
}
\]

Assim:

\[
\boxed{
\tan\theta_W
=
\left(
\frac{
\mathcal N_W\int\|\xi_W\|^2d\mu_g
}{
\mathcal N_Y\int\|\xi_Y\|^2d\mu_g
}
\right)^{1/2}
}
\]

na normalização adotada dos geradores.

---

## 8. Status

\[
\boxed{
\text{massas gauge e mistura eletrofraca derivadas no setor efetivo.}
}
\]

Atualização posterior: a estrutura de massa, o fóton sem massa e a mistura
neutra estão fechados no setor efetivo. O que ainda falta não é importar
\(g,g'\), mas transportar suas normas/rigidezes pelo background global correto
e avaliar a normalização absoluta do canal eletromagnético sem pós-ajuste.
