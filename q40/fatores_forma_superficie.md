# Q40 — Adendo: fatores de forma como observáveis de superfície

## 1. Ponto de partida

Na GDQ, os observáveis eletromagnéticos do bárion não são médias volumétricas
ingênuas do bulk. Eles são projeções de borda da garganta/estômato.

O raio do próton já fixou a regra:

\[
r_p=C_r\epsilon_{\rm eff}R_B,
\qquad
C_r=\frac18\left(1+\frac{\alpha}{4}\right),
\qquad
R_B=\frac32\Lambda_C.
\]

Portanto, a variável radial que entra no espalhamento elástico é:

\[
r_{\rm obs}(\chi)=C_rR_B\chi.
\]

Usar \(R_B\chi\) diretamente recoloca o erro volumétrico já descartado.

---

## 2. Fator de forma elétrico do próton

No limite de casca de superfície:

\[
\rho_E^p(\chi)d\mu_\chi
\to
\delta(\chi-\epsilon_{\rm eff})d\chi.
\]

Logo:

\[
\boxed{
G_E^p(q^2)=j_0(qr_p),
\qquad
j_0(x)=\frac{\sin x}{x}.
}
\]

As normalizações seguem imediatamente:

\[
G_E^p(0)=1.
\]

E:

\[
G_E^p(q^2)
=
1-\frac{q^2r_p^2}{6}+O(q^4),
\]

portanto:

\[
\boxed{
-6\left.\frac{dG_E^p}{dq^2}\right|_{q^2=0}=r_p^2.
}
\]

Assim, o mesmo objeto geométrico que fixa \(r_p\) fixa também a inclinação de
baixa energia de \(G_E^p\).

---

## 3. Fator de forma magnético do próton

A normalização é:

\[
G_M^p(0)=\mu_p.
\]

No fechamento líder de superfície:

\[
\boxed{
G_M^p(q^2)=\mu_p\,j_0(qr_{M,p}),
\qquad
r_{M,p}=r_p.
}
\]

Separar \(r_{M,p}\) de \(r_p\) requer resolver a distribuição torsional
magnética de fronteira. Isso é fenomenologia posterior, não lacuna estrutural.

---

## 4. Fator de forma elétrico do nêutron

O nêutron satisfaz:

\[
G_E^n(0)=0.
\]

Mas isso não implica densidade elétrica local nula. A estrutura correta é uma
polarização de carga total zero:

\[
\rho_E^n d\mu
=
A_n[
\delta(\chi-\chi_+)-\delta(\chi-\chi_-)
]d\chi,
\qquad
\chi_->\chi_+.
\]

Então:

\[
\boxed{
G_E^n(q^2)
=
A_n[
j_0(qC_rR_B\chi_+)
-
j_0(qC_rR_B\chi_-)
].
}
\]

Com isso:

\[
G_E^n(0)=0.
\]

E:

\[
\boxed{
\langle r_n^2\rangle
=
A_n(C_rR_B)^2(\chi_+^2-\chi_-^2)<0.
}
\]

O sinal negativo aparece porque a componente negativa efetiva está mais externa
que a positiva.

O fechamento líder mínimo usa:

\[
A_n=\alpha\delta_B,
\qquad
r_\pm=r_p(1\pm\alpha/2),
\]

o que garante sinal negativo, mas produz apenas a polarização local mínima.

O fechamento estendido de cola dupla usa a mesma projeção torsional que fixa o
momento magnético do nêutron:

\[
A_n^{(2)}=|\mu_n|
=
\frac34\delta_B
\left(
1+\alpha\frac{3\sqrt2}{4}
\right),
\]

e o deslocamento relativo das duas interfaces antiparalelas:

\[
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
\]

Assim:

\[
r_\pm^{(2)}
=
r_p\left(1\pm\frac{\alpha_{\rm tor}^{(2)}}{2}\right),
\]

\[
\boxed{
G_{E,{\rm ext}}^n(q^2)
=
|\mu_n|
\left[
j_0(qr_+^{(2)})
-
j_0(qr_-^{(2)})
\right].
}
\]

E:

\[
\boxed{
\langle r_n^2\rangle_{\rm ext}
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2
\approx
-0.11772\,{\rm fm}^2.
}
\]

Esse número não entra como dado externo. Ele é consequência de
\(\mu_n\), \(r_p\), \(\alpha\) e do comprimento torsional
\(\ln(2\pi^2)\).

### 4.1 Perfil suave de superfície

As duas cascas podem ser substituídas por uma camada suave local sem alterar
as normalizações de baixa energia. A coordenada correta é a coordenada local de
superfície:

\[
\xi=r-r_p.
\]

Como a componente positiva está ligeiramente no lado interno do estômato e a
componente negativa no lado externo, não se deve impor artificialmente o domínio
volumétrico \([\epsilon_{\rm eff},\pi]\) nessa etapa.

Definimos:

\[
K_\sigma(\xi,\xi_0)
=
\frac{1}{\sqrt{2\pi}\sigma_r}
\exp\left[-\frac{(\xi-\xi_0)^2}{2\sigma_r^2}\right],
\]

\[
\xi_\pm
=
\mp\frac12 r_p\alpha_{\rm tor}^{(2)},
\qquad
\sigma_r
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
\]

Então:

\[
\boxed{
\rho_E^n(\xi)
=
|\mu_n|
\left[
K_\sigma(\xi,\xi_+)
-
K_\sigma(\xi,\xi_-)
\right].
}
\]

E:

\[
\boxed{
G_{E,\rm suave}^n(q^2)
=
|\mu_n|
\int_{-\infty}^{+\infty}
\left[
K_\sigma(\xi,\xi_+)
-
K_\sigma(\xi,\xi_-)
\right]
j_0(q(r_p+\xi))d\xi.
}
\]

Como as duas gaussianas têm a mesma largura:

\[
G_{E,\rm suave}^n(0)=0,
\qquad
\langle r_n^2\rangle_{\rm suave}
=
\langle r_n^2\rangle_{\rm ext}.
\]

O solver numérico confirma:

\[
G_{E,\rm suave}^n(0)\simeq -6.1\times10^{-16},
\]

\[
-6\left.\frac{dG_{E,\rm suave}^n}{dq^2}\right|_0
=
-0.117721789721\,{\rm fm}^2,
\]

com diferença de apenas \(\sim 10^{-10}\,{\rm fm}^2\) em relação ao fechamento
por cascas.

---

## 5. Fator de forma magnético do nêutron

A normalização é:

\[
G_M^n(0)=\mu_n.
\]

No fechamento líder:

\[
\boxed{
G_M^n(q^2)=\mu_n\,j_0(qr_{M,n}).
}
\]

O raio magnético \(r_{M,n}\) deve vir da densidade de corrente torsional:

\[
\vec J_n
=
\vec J_{\rm circ}
+
\vec J_{\rm tor}
+
\vec J_{\rm surf}.
\]

Enquanto essa densidade não for resolvida, \(G_M^n(q^2)\) está fechado apenas
por normalização e forma estrutural, não por curva fenomenológica completa.

---

## 6. Status

\[
\boxed{
\text{os fatores de forma estão fechados estruturalmente em normalização e baixa energia.}
}
\]

O perfil variacional líder \(H_n(\chi)\) foi obtido no adendo próprio como
solução de fluxo de calor de Perelman na camada de superfície:

\[
H_n(\xi,\tau_n)
=
|\mu_n|
[K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)].
\]

Com isso, a curva líder \(G_E^n(q^2)\) também fica determinada:

\[
G_E^n(q^2)
=
\int H_n(\xi,\tau_n)j_0(q(r_p+\xi))d\xi.
\]

Ficam posteriores:

1. separação entre raios elétricos e magnéticos;
2. comparação quantitativa com dados de espalhamento elástico;
3. correções de sonda/magnetização;
4. análise assintótica rigorosa em grande \(q^2\).
