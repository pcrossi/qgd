# Q43 — Expansão da anomalia magnética pela Hessiana GDQ

## 1. Objetivo

Este adendo trata os itens pendentes da Q43 sem trocar a GDQ por QED:

1. formalizar os termos superiores de \(g\);
2. escrever explicitamente o objeto \(H_C^{-1}m_\perp\);
3. indicar como separar elétron, múon e tau;
4. classificar a dependência de escala;
5. definir o contrato mínimo para cálculo numérico.

O resultado não é uma predição metrológica completa. É a forma correta do
problema que deve ser avaliado pela Hessiana física da ação oficial.

---

## 2. Setor vinculado

Fixe a circulação de Noether:

\[
\mathcal C[\Phi]=C.
\]

O funcional aumentado no campo magnético externo \(B\) é:

\[
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda(\mathcal C[\Phi]-C).
\]

O campo \(B\) é fonte externa/aparelho. Ele não altera a ação oficial.

No ponto estacionário \(\Phi_0\), defina:

\[
c=\left.\frac{\delta\mathcal C}{\delta\Phi}\right|_{\Phi_0},
\qquad
m=\left.\frac{\delta M}{\delta\Phi}\right|_{\Phi_0}.
\]

Decomponha:

\[
m=\gamma_0c+m_\perp,
\qquad
\gamma_0=\frac{q}{mc}.
\]

A primeira parcela é a parte protegida por Noether. A segunda é a resposta
geométrica interna que não muda a carga conservada.

---

## 3. Hessiana física com vínculo

Se \(H\) é a Hessiana física da ação oficial no background \(\Phi_0\), a
Hessiana no setor de circulação fixa é a restrição/projeção:

\[
H_C=P_C^\dagger H P_C,
\]

onde \(P_C\) remove:

1. modos de difeomorfismo/gauge;
2. modo de fase comum;
3. direção de variação da carga \(\mathcal C\);
4. modos nulos exatos de Noether.

Equivalente via complemento de Schur, para vínculos lineares:

\[
H_C^{-1}
=
H_{\rm phys}^{-1}
-
H_{\rm phys}^{-1}c
\left\langle c,H_{\rm phys}^{-1}c\right\rangle^{-1}
c^\dagger H_{\rm phys}^{-1}.
\]

Essa fórmula deve ser lida como pseudoinversa no subespaço físico. Ela não é
inversão de modo de gauge.

---

## 4. Resposta magnética

A resposta efetiva do multiplicador ao campo é:

\[
\gamma_{\rm eff}
=
-\left.\frac{\partial\lambda}{\partial B}\right|_{B=0}
=
\frac{\langle c,H_C^{-1}m\rangle}
{\langle c,H_C^{-1}c\rangle}.
\]

Substituindo \(m=\gamma_0c+m_\perp\):

\[
\gamma_{\rm eff}
=\gamma_0+\Delta\gamma_{\rm geom},
\]

\[
\Delta\gamma_{\rm geom}
=
\frac{\langle c,H_C^{-1}m_\perp\rangle}
{\langle c,H_C^{-1}c\rangle}.
\]

Logo:

\[
g
=
\frac{2mc}{q}\gamma_{\rm eff}
=
2(1+a_{\rm geom}),
\]

\[
a_{\rm geom}
=
\frac{\Delta\gamma_{\rm geom}}{\gamma_0}.
\]

---

## 5. Expansão perturbativa geométrica

Escreva a Hessiana e a fonte transversal como séries no parâmetro
eletrogeométrico efetivo \(\alpha\):

\[
H_C
=H_0+\alpha H_1+\alpha^2H_2+\cdots,
\]

\[
m_\perp
=\alpha m_1+\alpha^2m_2+\alpha^3m_3+\cdots.
\]

Então, usando a expansão de Neumann da pseudoinversa no subespaço físico:

\[
H_C^{-1}
=G_0+\alpha G_1+\alpha^2G_2+\cdots,
\]

com:

\[
G_0=H_0^{-1},
\]

\[
G_1=-G_0H_1G_0,
\]

\[
G_2=G_0H_1G_0H_1G_0-G_0H_2G_0.
\]

Defina:

\[
D_0=\langle c,G_0c\rangle.
\]

Se a variação do denominador for mantida, escreva:

\[
D
=\langle c,H_C^{-1}c\rangle
=D_0+\alpha D_1+\alpha^2D_2+\cdots.
\]

Os primeiros coeficientes da anomalia são:

\[
a_1
=
\frac{1}{\gamma_0}
\frac{\langle c,G_0m_1\rangle}{D_0},
\]

\[
a_2
=
\frac{1}{\gamma_0}
\left[
\frac{\langle c,G_0m_2+G_1m_1\rangle}{D_0}
-
\frac{\langle c,G_0m_1\rangle D_1}{D_0^2}
\right],
\]

\[
\begin{aligned}
a_3
=\frac{1}{\gamma_0}\Bigg[
&\frac{\langle c,G_0m_3+G_1m_2+G_2m_1\rangle}{D_0}\\
&-
\frac{\langle c,G_0m_2+G_1m_1\rangle D_1}{D_0^2}\\
&+
\frac{\langle c,G_0m_1\rangle(D_1^2-D_0D_2)}{D_0^3}
\Bigg].
\end{aligned}
\]

Assim:

\[
a_{\rm geom}
=
\alpha a_1+\alpha^2a_2+\alpha^3a_3+\cdots.
\]

Na normalização harmônica já demonstrada:

\[
a_1=\frac{1}{2\pi}.
\]

Os termos \(a_2,a_3,\ldots\) dependem de \(H_1,H_2,\ldots\) e
\(m_2,m_3,\ldots\). Eles ainda não foram avaliados.

---

## 6. Relação com a hierarquia leptônica

A hierarquia leptônica não deriva o Zeeman. Ela fornece os backgrounds nos
quais a resposta Zeeman deve ser calculada.

Para cada lépton carregado:

\[
\ell\in\{e,\mu,\tau\},
\]

há um background espectral:

\[
\Phi_\ell,
\qquad
H_{C,\ell},
\qquad
m_{\perp,\ell}.
\]

Então:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{-1}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{-1}c_\ell\rangle
}.
\]

Logo:

\[
\text{Q39}
\longrightarrow
\Phi_e,\Phi_\mu,\Phi_\tau
\longrightarrow
H_{C,e},H_{C,\mu},H_{C,\tau}
\longrightarrow
a_e,a_\mu,a_\tau.
\]

Sem essa ponte, uma fórmula específica para \(g_\mu-2\) permanece
fenomenologia.

---

## 7. Dependência de escala

O termo mínimo:

\[
g_0=2
\]

é protegido por Noether e não depende da escala do aparelho no regime linear.

O termo líder:

\[
a^{(1)}=\frac{\alpha}{2\pi}
\]

depende apenas da normalização eletrogeométrica \(\alpha\).

As ordens superiores dependem de:

1. background \(\Phi_\ell\);
2. domínio de \(H_{C,\ell}\);
3. contorno físico;
4. remoção de modos nulos;
5. normalização global--local de \(\alpha\);
6. escala leptônica herdada da Q39.

---

## 8. Contrato numérico mínimo

Um cálculo numérico completo deve fornecer:

1. matriz ou operador discretizado \(H_{C,\ell}\);
2. vetores discretizados \(c_\ell\) e \(m_{\perp,\ell}\);
3. projetor físico \(P_C\);
4. pseudoinversa estável de \(H_{C,\ell}\);
5. verificação de independência de gauge;
6. refinamento de malha;
7. cálculo de

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{-1}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{-1}c_\ell\rangle
}.
\]

Até esse contrato ser preenchido, somente o termo líder
\(\alpha/(2\pi)\) está calculado.

---

## 9. Status

\[
\boxed{
\text{expansão formal fechada;}
\quad
\text{coeficientes superiores abertos.}
}
\]

Este adendo fecha a forma matemática correta dos itens 1--4. O item 5 é
implementado no script de verificação líder da Q43.

