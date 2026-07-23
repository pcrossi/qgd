# Q48 — Espectro Sommerfeld--Dirac como redução espinorial da GDQ

## 1. Operador central

No limite pontual externo:

$$
H_D
=
c\boldsymbol\alpha\cdot\mathbf p
+
\beta m_ec^2
-
\frac{Z\alpha\hbar c}{r}.
$$

Classificação:

$$
\boxed{
\text{redução efetiva de }\mathcal D^B_{p,e}\text{ no campo fraco externo.}
}
$$

---

## 2. Separação por harmônicos espinoriais

Os estados são escritos como:

$$
\psi_{E\kappa m}(r,\theta,\phi)
=
\frac1r
\begin{pmatrix}
G_{E\kappa}(r)\Omega_{\kappa m}(\theta,\phi)\\
iF_{E\kappa}(r)\Omega_{-\kappa m}(\theta,\phi)
\end{pmatrix}.
$$

O número quântico $\kappa$ é:

$$
\kappa=
\begin{cases}
-(j+1/2), & j=\ell+1/2,\\
+(j+1/2), & j=\ell-1/2.
\end{cases}
$$

Logo:

$$
j=|\kappa|-\frac12,
\qquad
m_j=-j,\ldots,j.
$$

---

## 3. Sistema radial acoplado

Com:

$$
V(r)=-\frac{Z\alpha\hbar c}{r},
$$

o sistema radial é:

$$
\frac{dG}{dr}
+
\frac{\kappa}{r}G
-
\frac{1}{\hbar c}
\left(
m_ec^2+E-V(r)
\right)F
=0,
$$

$$
\frac{dF}{dr}
-
\frac{\kappa}{r}F
+
\frac{1}{\hbar c}
\left(
m_ec^2-E+V(r)
\right)G
=0.
$$

Esse par é o objeto que substitui a equação radial escalar do legado no nível
fundamental efetivo.

---

## 4. Quantização

Defina:

$$
\gamma_\kappa=\sqrt{\kappa^2-(Z\alpha)^2}.
$$

A regularidade no núcleo e a integrabilidade no infinito impõem a condição de
truncamento:

$$
n_r=0,1,2,\ldots
$$

com:

$$
n=n_r+|\kappa|.
$$

O espectro é:

$$
E_{n\kappa}
=
m_ec^2
\left[
1+
\frac{(Z\alpha)^2}
{
\left(
n-|\kappa|+\gamma_\kappa
\right)^2
}
\right]^{-1/2}.
$$

Para o hidrogênio:

$$
Z=1.
$$

---

## 5. Relação com a fórmula escalar legada

A equação legada usa $\ell$ e uma correção torsional escalar:

$$
\ell(\ell+1)-4\alpha^2.
$$

Ela pode reproduzir parte do comportamento radial, mas não contém a variável
espinorial correta:

$$
\kappa=\pm(j+1/2).
$$

Portanto:

$$
\boxed{
\text{a fórmula legada é compatível apenas como projeção escalar posterior.}
}
$$

O espectro correto organiza níveis por $n$ e $j$, não por $n$ e $\ell$.

---

## 6. Degenerescência

Como o espectro depende de $n$ e $|\kappa|=j+1/2$, mas não de $m_j$:

$$
\deg_{m_j}(n,j)=2j+1.
$$

No problema Coulomb--Dirac puro também permanece a degenerescência entre
estados com mesmo $n$ e $j$ mas $\ell$ diferente, por exemplo:

$$
2s_{1/2}
\quad\text{e}\quad
2p_{1/2}.
$$

Essa degenerescência é quebrada por campo próximo, tamanho finito, hiperfina e
resposta geométrica da Hessiana.

---

## 7. Expansão de estrutura fina

Para $Z=1$:

$$
E_{nj}
=
m_ec^2
-
\frac{m_ec^2\alpha^2}{2n^2}
-
\frac{m_ec^2\alpha^4}{2n^4}
\left(
\frac{n}{j+1/2}
-
\frac34
\right)
+
O(\alpha^6).
$$

Esse termo $\alpha^4$ é a estrutura fina líder.

Classificação:

$$
\boxed{
\text{derivação efetiva do limite espinorial GDQ.}
}
$$
