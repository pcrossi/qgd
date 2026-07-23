# Q39 — Cálculo do caso warped/misto na Hessiana 8D

## 1. Objetivo

Este documento calcula o caso que ficou pendente após o background produto:

\[
\nabla_K f\ne0,
\qquad
H_{BK}\ne0,
\qquad
g_8\ne g_B\oplus g_K.
\]

Neste caso o bloco misto da Hessiana pode ser não nulo:

\[
J\ne0.
\]

O objetivo é calcular a condição precisa sob a qual esse acoplamento não cria
uma quarta geração leptônica primitiva.

---

## 2. Ansatz warped/misto mínimo

Escreva a métrica 8D como:

\[
g_8
=
e^{2A(k)}g_B
\oplus
g_K
+\varepsilon\,\mathcal C_{BK},
\]

onde:

1. \(A(k)\) é o warp toroidal;
2. \(\mathcal C_{BK}\) é o bloco métrico misto;
3. \(\varepsilon\) mede a intensidade da mistura não-produto.

O dilaton e a torção são:

\[
f_*(b,k)=f_B(b)+f_K(k),
\]

\[
H_*=H_B+H_K+H_{BK}.
\]

Defina as três intensidades adimensionais de mistura:

\[
a_W:=\|\nabla_K A\|_\infty,
\]

\[
a_f:=\|\nabla_K f_K\|_\infty,
\]

\[
a_H:=\|H_{BK}\|_\infty.
\]

Essas são quantidades do background. Elas não são novos axiomas.

---

## 3. Forma geral da Hessiana

A Hessiana física projetada continua tendo forma de bloco:

\[
H_8=
\begin{pmatrix}
H_B & J\\
J^\dagger & H_\perp
\end{pmatrix}.
\]

Agora:

\[
J=J_W+J_f+J_H+J_{\mathcal C},
\]

com:

1. \(J_W\): acoplamento produzido por \(\nabla_K A\);
2. \(J_f\): acoplamento produzido por \(\nabla_K f_K\);
3. \(J_H\): acoplamento produzido por \(H_{BK}\);
4. \(J_{\mathcal C}\): acoplamento produzido pelo bloco métrico misto
   \(\mathcal C_{BK}\).

---

## 4. Estimativa de \(H_\perp\)

O complemento toroidal ainda contém o laplaciano positivo de \(K_5\). Para
\(K_5=T^5\):

\[
\lambda_K(n)=\sum_{a=1}^{5}\frac{n_a^2}{R_a^2}.
\]

Após remover \(n=0\):

\[
\lambda_K(n)\ge R_{\max}^{-2}.
\]

Os termos warped/mistos perturbam o gap. Escreva:

\[
H_\perp
\ge
\left(
C_\gamma\tau R_{\max}^{-2}
-V_{\rm mix}
\right)I.
\]

No controle quadrático padrão, a perda de coercividade é limitada por:

\[
V_{\rm mix}
\le
c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\varepsilon^2.
\]

Portanto:

\[
\boxed{
m_\perp^2
=
C_\gamma\tau R_{\max}^{-2}
-
\left(
c_Wa_W^2+c_fa_f^2+c_Ha_H^2+c_C\varepsilon^2
\right).
}
\]

O complemento permanece coercivo quando:

\[
\boxed{
m_\perp^2>0.
}
\]

---

## 5. Estimativa de \(J\)

Pela continuidade da Hessiana em relação ao background, cada bloco misto é
linear na primeira ordem da perturbação:

\[
\|J_W\|\le b_W a_W,
\]

\[
\|J_f\|\le b_f a_f,
\]

\[
\|J_H\|\le b_H a_H,
\]

\[
\|J_{\mathcal C}\|\le b_C\varepsilon.
\]

Assim:

\[
\boxed{
\|J\|
\le
j_{\rm mix}
:=
b_Wa_W+b_fa_f+b_Ha_H+b_C\varepsilon.
}
\]

No caso produto:

\[
a_W=a_f=a_H=\varepsilon=0,
\]

e recuperamos:

\[
J=0.
\]

---

## 6. Complemento de Schur

O operador efetivo 3D é:

\[
H_B^{\rm eff}
=
H_B-JH_\perp^{-1}J^\dagger.
\]

Como:

\[
H_\perp\ge m_\perp^2I,
\]

temos:

\[
\|JH_\perp^{-1}J^\dagger\|
\le
\frac{\|J\|^2}{m_\perp^2}
\le
\frac{j_{\rm mix}^2}{m_\perp^2}.
\]

Logo:

\[
\boxed{
\|H_B-H_B^{\rm eff}\|
\le
\frac{j_{\rm mix}^2}{m_\perp^2}.
}
\]

---

## 7. Critério de preservação do índice

Seja \(\lambda_B^{\rm gap}\) o menor autovalor positivo do bloco 3D no
complemento dos três setores críticos físicos.

O índice crítico é preservado se:

\[
\boxed{
\frac{j_{\rm mix}^2}{m_\perp^2}
<
\lambda_B^{\rm gap}.
}
\]

Equivalente:

\[
\boxed{
j_{\rm mix}
<
\sqrt{\lambda_B^{\rm gap}\,m_\perp^2}.
}
\]

Essa é a condição calculada para o caso warped/misto.

---

## 8. Três regimes físicos

### 8.1 Regime subcrítico

\[
\frac{j_{\rm mix}^2}{m_\perp^2}
<
\lambda_B^{\rm gap}.
\]

Então:

\[
\operatorname{ind}^{-}(H_8)
=
\operatorname{ind}^{-}(H_B).
\]

Não há quarta geração primitiva.

### 8.2 Regime crítico

\[
\frac{j_{\rm mix}^2}{m_\perp^2}
=
\lambda_B^{\rm gap}.
\]

O quarto modo toca o limiar. Fisicamente isso é uma ressonância marginal, não
necessariamente uma partícula estável.

### 8.3 Regime supercrítico

\[
\frac{j_{\rm mix}^2}{m_\perp^2}
>
\lambda_B^{\rm gap}.
\]

O background warped/misto pode criar um modo adicional. Esse modo deve ser
classificado como:

1. estado composto;
2. ressonância;
3. estado de contorno;
4. excitação estabilizada por background externo;
5. ou, se satisfizer cargas primitivas e estabilidade assintótica, candidato a
   novo setor físico.

Ele não contradiz o teorema produto, porque pertence a outro domínio.

---

## 9. Resultado normalizado

No sistema normalizado:

\[
C_\gamma=\tau=R_{\max}=1,
\]

e tomando os coeficientes de controle mínimos:

\[
c_W=c_f=c_H=c_C=1,
\qquad
b_W=b_f=b_H=b_C=1,
\]

temos:

\[
m_\perp^2
=
1-(a_W^2+a_f^2+a_H^2+\varepsilon^2),
\]

\[
j_{\rm mix}
=
a_W+a_f+a_H+\varepsilon.
\]

A condição de estabilidade é:

\[
\boxed{
\frac{
(a_W+a_f+a_H+\varepsilon)^2
}{
1-(a_W^2+a_f^2+a_H^2+\varepsilon^2)
}
<
\lambda_B^{\rm gap}.
}
\]

Se apenas um canal misto estiver ativo com amplitude \(a\), então:

\[
m_\perp^2=1-a^2,
\qquad
j_{\rm mix}=a.
\]

Logo:

\[
\frac{a^2}{1-a^2}<\lambda_B^{\rm gap}.
\]

Resolvendo:

\[
\boxed{
a^2
<
\frac{\lambda_B^{\rm gap}}
{1+\lambda_B^{\rm gap}}.
}
\]

Portanto:

\[
\boxed{
a_{\rm crit}
=
\sqrt{
\frac{\lambda_B^{\rm gap}}
{1+\lambda_B^{\rm gap}}
}.
}
\]

Para \(\lambda_B^{\rm gap}=1\):

\[
\boxed{
a_{\rm crit}=\frac{1}{\sqrt2}\simeq0.70710678.
}
\]

---

## 10. Conclusão

O caso warped/misto não invalida a estrutura. Ele refina a afirmação:

\[
\boxed{
\text{três setores são garantidos enquanto o acoplamento misto for subcrítico.}
}
\]

Estados além de três podem existir em backgrounds supercríticos, mas nesse
caso são estados induzidos por warp, torção mista, contorno ou composição, e
não quarta geração leptônica primitiva do setor produto.

---

## 11. Status

\[
\boxed{
\text{caso warped/misto calculado como critério de Schur; número final depende do background.}
}
\]

Para obter um número absoluto, é necessário calcular no background leptônico:

\[
a_W,\quad a_f,\quad a_H,\quad \varepsilon,\quad
\lambda_B^{\rm gap}.
\]

Sem esses dados, qualquer número específico seria ajuste ou hipótese externa.
