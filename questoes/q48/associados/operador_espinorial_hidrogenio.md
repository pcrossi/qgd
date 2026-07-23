# Q48 — Operador espinorial efetivo do hidrogênio na GDQ

## 1. Enunciado local

Queremos construir o operador correto para o elétron no background protônico,
sem substituir a GDQ por Dirac/QED como ontologia fundamental.

A cadeia usada é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{p,*}
\to
\operatorname{Hess}_{\Phi_{p,*}}\mathcal S_{\rm GDQ}
\to
\mathcal D^B_{p,e}.
$$

Classificação:

$$
\boxed{
\mathcal D^B_{p,e}\text{ é uma redução efetiva espinorial da Hessiana física.}
}
$$

Não é ação fundamental nova.

---

## 2. Campo físico

Pela Q26, o elétron deve ser descrito por uma seção espinorial:

$$
\psi\in\Gamma(S\otimes L_Q).
$$

Aqui:

- $S$ é o fibrado de spin do espaço-tempo físico reconstruído;
- $L_Q$ é a linha de carga $U(1)$ herdada do setor eletrogeométrico;
- a estrutura de Clifford satisfaz

$$
\{\gamma^a,\gamma^b\}=2\eta^{ab}.
$$

A circulação/Hopf interpreta geometricamente o spin, mas não substitui a
representação espinorial.

---

## 3. Background protônico

O próton entra como background bariônico composto da Q40:

$$
\Phi_{p,*}=(g_p,f_p,B_p,\mathcal A_p,\ldots).
$$

Na região atômica externa, usa-se o limite estacionário:

$$
g_{\mu\nu}^{(p)}
=
\eta_{\mu\nu}
+
h_{\mu\nu}^{(p)},
\qquad
|h_{\mu\nu}^{(p)}|\ll1.
$$

O modo eletromagnético efetivo é a projeção $U(1)$ normalizada:

$$
A_\mu^{(p)}
=
\Pi_{U(1)}\Phi_{p,*}.
$$

No limite coulombiano:

$$
A_0^{(p)}(r)=\frac{Ze}{4\pi\epsilon_0r},
\qquad
\mathbf A^{(p)}=0,
\qquad
Z=1.
$$

Esse limite usa $\alpha$ já transportada pela Q37; não usa hidrogênio para
ajustar a carga.

---

## 4. Operador Dirac--Bismut efetivo

A linearização espinorial da Hessiana física define:

$$
\mathcal D^B_{p,e}\psi
=
\left[
i\hbar c\,\gamma^a e_a{}^\mu
\left(
\nabla_\mu^B+\frac{iQ}{\hbar c}A_\mu^{(p)}
\right)
-
m_ec^2
\right]\psi.
$$

Com:

$$
Q=-e.
$$

A conexão espinorial com torção de Bismut pode ser escrita como:

$$
\nabla_\mu^B
=
\partial_\mu
+
\frac14\omega_{\mu ab}^{B}\gamma^a\gamma^b,
$$

onde:

$$
\omega_{\mu ab}^{B}
=
\omega_{\mu ab}^{\rm LC}
+
K_{\mu ab}^{B}.
$$

O contorsor $K^B$ é determinado pela torção $H=d^c\omega$ do background GDQ.

No limite fraco externo, a contribuição de $K^B$ se reduz à seleção
espinorial mínima e às correções de curto alcance:

$$
\mathcal D^B_{p,e}
=
\mathcal D_{\rm Coul}
+
\delta\mathcal D_{\rm tor}
+
\delta\mathcal D_{\rm near}.
$$

---

## 5. Domínio e produto interno

O produto interno físico é:

$$
\langle\psi,\varphi\rangle
=
\int_{\Sigma_t}
\psi^\dagger\varphi\,d\mu_{\rm phys}.
$$

No limite externo plano:

$$
d\mu_{\rm phys}=d^3x.
$$

O domínio natural é:

$$
\mathcal D(\mathcal D^B_{p,e})
=
H^1_{\rm loc}(\mathbb R^3\setminus\mathcal N_p,S\otimes L_Q)
\cap
\mathcal B_p.
$$

$\mathcal N_p$ é a vizinhança interna do próton; $\mathcal B_p$ é a condição de
interface. No limite pontual:

$$
\mathcal B_p:\quad
\psi\text{ regular em }r=0,\qquad
\psi\in L^2(\mathbb R^3).
$$

Com raio finito:

$$
\left(
n^a\nabla_a^B+\mathsf R_p
\right)\psi\big|_{\partial\mathcal N_p}=0.
$$

Aqui $\mathsf R_p$ é a impedância de superfície/DtN do background protônico,
herdada da Q40.

---

## 6. Auto-adjunticidade física

A identidade de Green para o operador de primeira ordem fornece o termo de
bordo:

$$
\langle\psi,\mathcal D\varphi\rangle
-
\langle\mathcal D\psi,\varphi\rangle
=
\int_{\partial\Omega}
\psi^\dagger i\hbar c\,\gamma^n\varphi\,d\Sigma.
$$

No domínio físico admissível, a condição de contorno deve anular esse fluxo
normal. No limite pontual regular isso ocorre por regularidade e
integrabilidade. No caso de próton com superfície, isso impõe que
$\mathsf R_p$ seja auto-adjunto no espaço de traços físicos.

Logo:

$$
\boxed{
\mathcal D^B_{p,e}\text{ é simétrico/auto-adjunto no domínio físico projetado.}
}
$$

Classificação:

$$
\boxed{
\text{teorema condicional ao domínio }\mathcal B_p\text{ e à positividade DtN.}
}
$$

---

## 7. Redução ao problema de Coulomb

Quando:

$$
\delta\mathcal D_{\rm tor}\to0,
\qquad
\delta\mathcal D_{\rm near}\to0,
\qquad
\mathsf R_p\to\text{regularidade pontual},
$$

obtemos:

$$
\left[
c\boldsymbol\alpha\cdot\mathbf p
+
\beta m_ec^2
-
\frac{Z\alpha\hbar c}{r}
\right]\psi
=
E\psi.
$$

Essa é a equação de Dirac como redução operacional da GDQ no setor externo de
campo fraco.

Portanto:

$$
\boxed{
\text{a equação escalar do legado deve ser obtida apenas após quadrar/projetar
esta equação espinorial.}
}
$$
