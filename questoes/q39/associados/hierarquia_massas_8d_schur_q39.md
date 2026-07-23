# Q39 — Hierarquia de massas leptônicas expandida para a Hessiana 8D

## 1. Objetivo

Este documento reescreve a hierarquia leptônica no nível da Hessiana física
8D da GDQ.

A rota reduzida forneceu:

\[
R_\mu^{(0)}
=
\frac32\alpha^{-1}
+\frac65
+2\alpha,
\]

\[
Q=
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23.
\]

Agora inserimos esses resultados em:

\[
H_8=
\begin{pmatrix}
H_B & J\\
J^\dagger & H_\perp
\end{pmatrix},
\qquad
H_B^{\rm eff}
=
H_B-JH_\perp^{-1}J^\dagger.
\]

---

## 2. Massas como autovalores efetivos 8D

Defina os três modos leptônicos primitivos no setor 3D:

\[
\psi_e,\qquad
\psi_\mu,\qquad
\psi_\tau.
\]

No bloco reduzido:

\[
H_B\psi_\ell=R_\ell^{(0)}\psi_\ell,
\qquad
R_e^{(0)}=1.
\]

Na Hessiana 8D, o operador físico relevante é o Schur:

\[
H_B^{\rm eff}
=
H_B-\Sigma,
\qquad
\Sigma:=JH_\perp^{-1}J^\dagger.
\]

Logo, a razão efetiva é:

\[
R_\ell^{(8)}
=
\langle\psi_\ell,H_B^{\rm eff}\psi_\ell\rangle
=
R_\ell^{(0)}-\sigma_\ell,
\]

onde:

\[
\sigma_\ell
=
\langle\psi_\ell,\Sigma\psi_\ell\rangle.
\]

No background produto:

\[
J=0,
\qquad
\Sigma=0,
\qquad
R_\ell^{(8)}=R_\ell^{(0)}.
\]

---

## 3. Controle do deslocamento 8D

Do critério warped/misto:

\[
\|\Sigma\|
\le
\frac{j_{\rm mix}^2}{m_\perp^2}.
\]

Assim:

\[
|\sigma_\ell|
\le
\frac{j_{\rm mix}^2}{m_\perp^2}.
\]

Portanto:

\[
\boxed{
R_\ell^{(8)}
=
R_\ell^{(0)}
+O\left(\frac{j_{\rm mix}^2}{m_\perp^2}\right).
}
\]

Essa é a hierarquia de massas expandida para 8D.

---

## 4. Setor do múon em 8D

O resultado reduzido é:

\[
R_\mu^{(0)}
=
\frac32\alpha^{-1}
+\frac65
+2\alpha.
\]

A versão 8D é:

\[
\boxed{
R_\mu^{(8)}
=
\frac32\alpha^{-1}
+\frac65
+2\alpha
-\sigma_\mu.
}
\]

com:

\[
|\sigma_\mu|
\le
\frac{j_{\rm mix}^2}{m_\perp^2}.
\]

No produto exato:

\[
\sigma_\mu=0.
\]

Logo:

\[
\boxed{
R_\mu^{(8)}=R_\mu^{(0)}
\quad
\text{no background produto.}
}
\]

---

## 5. Setor do tau em 8D

O tau é determinado pela saturação:

\[
Q(R_\mu,R_\tau)
=
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23.
\]

Na Hessiana 8D, use:

\[
R_\mu^{(8)}=R_\mu^{(0)}-\sigma_\mu,
\]

\[
R_\tau^{(8)}=R_\tau^{(0)}-\sigma_\tau.
\]

Se a saturação tridimensional for preservada pelo Schur, então:

\[
Q(R_\mu^{(8)},R_\tau^{(8)})=\frac23.
\]

Para pequena mistura, o deslocamento de \(R_\tau\) induzido por
\(\delta R_\mu\) é obtido por diferenciação implícita:

\[
dQ
=
\partial_\mu Q\,dR_\mu
+\partial_\tau Q\,dR_\tau
=0.
\]

Logo:

\[
\boxed{
dR_\tau
=
-
\frac{\partial_\mu Q}{\partial_\tau Q}
dR_\mu.
}
\]

Como \(dR_\mu=-\sigma_\mu\), vem:

\[
\boxed{
\delta R_\tau
=
\frac{\partial_\mu Q}{\partial_\tau Q}
\sigma_\mu
-\sigma_\tau^{\rm direct}.
}
\]

Aqui \(\sigma_\tau^{\rm direct}\) é o deslocamento direto do modo tau pelo
Schur. No produto exato:

\[
\sigma_\mu=\sigma_\tau^{\rm direct}=0,
\qquad
R_\tau^{(8)}=R_\tau^{(0)}.
\]

---

## 6. Derivadas explícitas da condição de saturação

Defina:

\[
S=1+\sqrt{R_\mu}+\sqrt{R_\tau},
\qquad
N=1+R_\mu+R_\tau.
\]

Então:

\[
Q=\frac{N}{S^2}.
\]

As derivadas são:

\[
\partial_\mu Q
=
\frac{1}{S^2}
-
\frac{N}{S^3\sqrt{R_\mu}},
\]

\[
\partial_\tau Q
=
\frac{1}{S^2}
-
\frac{N}{S^3\sqrt{R_\tau}}.
\]

No ponto reduzido:

\[
R_\mu^{(0)}\simeq206.768593471,
\qquad
R_\tau^{(0)}\simeq3477.446405098.
\]

O fator de amplificação linear é:

\[
\mathcal A_{\tau\mu}
:=
-
\frac{\partial_\mu Q}{\partial_\tau Q}.
\]

Ele mede quanto uma variação pequena no múon desloca o tau ao preservar
\(Q=2/3\).

---

## 7. Critério de estabilidade da hierarquia 8D

Os três setores primitivos permanecem estáveis se:

\[
\frac{j_{\rm mix}^2}{m_\perp^2}
<
\lambda_B^{\rm gap}.
\]

Além disso, as correções de massa são controladas por:

\[
|R_\ell^{(8)}-R_\ell^{(0)}|
\le
\frac{j_{\rm mix}^2}{m_\perp^2}.
\]

Portanto:

\[
\boxed{
\text{a hierarquia reduzida é rigidamente herdada pela Hessiana 8D
enquanto a mistura for subcrítica.}
}
\]

---

## 8. Estados além de três

Se:

\[
\frac{j_{\rm mix}^2}{m_\perp^2}
\ge
\lambda_B^{\rm gap},
\]

o Schur pode criar modo adicional. Esse modo não é automaticamente uma quarta
geração. Para ser uma quarta geração primitiva, teria que satisfazer:

1. carga de Cauchy primitiva;
2. estabilidade assintótica;
3. localização independente;
4. não ser excitação de \(e,\mu,\tau\);
5. não depender de contorno externo ou background supercrítico.

Sem isso, ele é:

\[
\boxed{
\text{ressonância, estado de contorno, excitação ou composto.}
}
\]

---

## 9. Status

\[
\boxed{
\text{hierarquia leptônica expandida para 8D via Schur.}
}
\]

No background produto, a fórmula reduzida é recuperada exatamente. No
background warped/misto subcrítico, ela recebe correções limitadas e não muda
a contagem de três setores primitivos.
