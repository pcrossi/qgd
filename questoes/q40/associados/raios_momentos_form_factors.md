# Q40 — Bloco 3 — Raios, momentos magnéticos e fatores de forma

## 1. Objetivo

Este bloco organiza os observáveis eletromagnéticos do próton e do nêutron:

\[
r_p,\qquad \langle r_n^2\rangle,\qquad
\mu_p,\qquad \mu_n,\qquad
G_E^p,\ G_M^p,\ G_E^n,\ G_M^n.
\]

A regra metodológica é: nenhum número experimental deve ser inserido como
escala oculta. Os observáveis devem vir das densidades geométricas da solução
colada \(\mathfrak G_B\).

---

## 2. Densidades efetivas

Para cada bárion definimos quatro densidades efetivas:

\[
\rho_E^B(\chi),
\qquad
\rho_M^B(\chi),
\qquad
B=p,n.
\]

Elas devem satisfazer:

\[
\int \rho_E^p\,d\mu=1,
\qquad
\int \rho_E^n\,d\mu=0,
\]

e:

\[
\int \rho_M^p\,d\mu=\mu_p,
\qquad
\int \rho_M^n\,d\mu=\mu_n.
\]

O elemento de medida radial efetivo é:

\[
d\mu_\chi
=
|\Phi_B(\chi)|^2\sin^2\chi\,d\chi.
\]

com domínio:

\[
\chi\in[\epsilon_B,\pi]
\]

para estômato único.

---

## 3. Raio de carga do próton

O raio quadrático deve ser definido por:

\[
\boxed{
\langle r_p^2\rangle
=
R_B^2
\frac{
\int_{\epsilon_B}^{\pi}
d_g^2(\chi,\epsilon_B)\rho_E^p(\chi)d\mu_\chi
}{
\int_{\epsilon_B}^{\pi}
\rho_E^p(\chi)d\mu_\chi
}.
}
\]

Com:

\[
d_g(\chi,\epsilon_B)=\chi-\epsilon_B
\]

em coordenada angular normalizada, ou:

\[
r=R_B(\chi-\epsilon_B)
\]

em unidade física.

Ponto crítico: o fator numérico que transforma
\(\epsilon_B R_B\) no raio físico não pode ser inserido como \(0.125\) sem
derivação. Ele precisa sair de uma média geométrica:

\[
C_r^2
=
\frac{
\int_{\epsilon_B}^{\pi}
(\chi-\epsilon_B)^2\rho_E^p(\chi)d\mu_\chi
}{
\epsilon_B^2
\int_{\epsilon_B}^{\pi}
\rho_E^p(\chi)d\mu_\chi
}.
\]

Então:

\[
\boxed{
r_p=C_r\,\epsilon_B R_B.
}
\]

Derivação proposta no adendo `questoes/q40/associados/adendo_observaveis_criticos.md`:

\[
C_r=\frac18\left(1+\frac{\alpha}{4}\right).
\]

O fator \(1/8\) é a projeção octante de Hopf da garganta em \(S^3\), e
\((1+\alpha/4)\) é o vestimento eletro-geométrico de borda.

---

## 4. Raio quadrático do nêutron

Para o nêutron:

\[
\int \rho_E^n\,d\mu=0.
\]

Mas o raio quadrático pode ser não nulo:

\[
\boxed{
\langle r_n^2\rangle
=
R_B^2
\int_{\epsilon_B}^{\pi}
(\chi-\epsilon_B)^2\rho_E^n(\chi)d\mu_\chi.
}
\]

Para obter:

\[
\langle r_n^2\rangle<0,
\]

a densidade deve ter polarização radial:

\[
\rho_E^n(\chi)=\rho_+(\chi)-\rho_-(\chi),
\]

com:

\[
\int \rho_+d\mu=\int \rho_-d\mu,
\]

mas:

\[
\int r^2\rho_-d\mu
>
\int r^2\rho_+d\mu.
\]

Interpretação: carga negativa efetiva mais periférica que a positiva.

Pendência: escrever \(\rho_+\) e \(\rho_-\) a partir do cisalhamento torsional
da cola do nêutron.

---

## 5. Momentos magnéticos

O ponto de partida é:

\[
\boxed{
\vec\mu_B
=
\frac12\int_{\Sigma_B^\circ}
\vec r\times\vec J_B\,d^3x.
}
\]

A corrente efetiva deve ser decomposta em:

\[
\vec J_B
=
\vec J_{\rm circ}
+
\vec J_{\rm tor}
+
\vec J_{\rm surf}.
\]

O termo torsional tem forma:

\[
\vec J_{\rm tor}
=
e\nabla\times(e^{-f_B}\vec H_{\rm eff}).
\]

Então:

\[
\vec\mu_{\rm tor}
=
e\int e^{-f_B}\vec H_{\rm eff}\,d^3x
+
\text{termo de fronteira}.
\]

---

## 6. Próton

O documento de faltas propõe:

\[
\mu_p
=
1+\kappa_p,
\]

\[
\kappa_p
=
\frac35\ln(2\pi^2)
\left(1+\frac{\alpha}{4}\right).
\]

Essa fórmula reproduz:

\[
\mu_p\approx2.792847\,\mu_N.
\]

Status: numericamente forte. A derivação proposta do fator:

\[
\frac35.
\]

é:

\[
\frac35
=
\left\langle r^2/R^2\right\rangle_{\mathbb B^3}.
\]

---

## 7. Nêutron

O documento de faltas propõe:

\[
\mu_n
=
-\frac34\delta_B
\left(1+\alpha\frac{3\sqrt2}{4}\right).
\]

Essa fórmula reproduz aproximadamente:

\[
\mu_n\approx-1.913\,\mu_N.
\]

Status: numericamente forte. A derivação proposta do fator:

\[
\frac34.
\]

é:

\[
\frac34
=
\frac{\operatorname{Tr}P_{\rm sp}}{\operatorname{Tr}I_4},
\]

isto é, a projeção espacial tridimensional da torção quaterniónica de
fronteira.

---

## 8. Fatores de forma

Os fatores de forma de Sachs devem ser definidos por transformadas radiais
projetadas. Usamos:

\[
j_0(x)=\frac{\sin x}{x}.
\]

### 8.1. Correção importante: escala projetada do observável

Como o raio de carga do próton é um observável de superfície projetado por
Hopf, a variável física que entra na transformada de espalhamento não é o raio
volumétrico bruto \(R_B\chi\). A variável observável é:

\[
r_{\rm obs}(\chi)
=
C_r R_B\chi,
\qquad
C_r=\frac18\left(1+\frac{\alpha}{4}\right).
\]

Portanto, para observáveis eletromagnéticos de borda:

\[
\boxed{
G_E^B(q^2)
=
\int_{\epsilon_B}^{\pi}
\rho_E^B(\chi)
j_0(q C_rR_B\chi)
d\mu_\chi.
}
\]

\[
\boxed{
G_M^B(q^2)
=
\int_{\epsilon_B}^{\pi}
\rho_M^B(\chi)
j_0(q C_rR_B\chi)
d\mu_\chi.
}
\]

Essa substituição é a mesma correção conceitual que removeu a inconsistência
do raio do próton: o espalhamento eletromagnético mede a seção projetada da
garganta, não o volume radial completo do bulk.

As normalizações obrigatórias são:

\[
G_E^p(0)=1,
\qquad
G_E^n(0)=0,
\]

\[
G_M^p(0)=\mu_p,
\qquad
G_M^n(0)=\mu_n.
\]

A expansão de baixa energia dá:

\[
G_E^B(q^2)
=
G_E^B(0)
-
\frac{q^2}{6}\langle r_B^2\rangle
+
O(q^4).
\]

Para o próton, no limite de casca de superfície:

\[
\rho_E^p(\chi)d\mu_\chi
\longrightarrow
\delta(\chi-\epsilon_{\rm eff})\,d\chi.
\]

Logo:

\[
\boxed{
G_E^p(q^2)
=
j_0(qr_p),
\qquad
r_p=C_r\epsilon_{\rm eff}R_B.
}
\]

Essa expressão satisfaz:

\[
G_E^p(0)=1,
\qquad
-6\left.\frac{dG_E^p}{dq^2}\right|_{q^2=0}=r_p^2.
\]

Para o momento magnético do próton, a aproximação líder de superfície é:

\[
\boxed{
G_M^p(q^2)
=
\mu_p\,j_0(qr_{M,p}),
}
\]

com:

\[
r_{M,p}=r_p
\]

no primeiro fechamento geométrico. Correções posteriores podem separar o raio
magnético do raio elétrico por uma densidade torsional não infinitesimal.

Para o nêutron, a condição estrutural é:

\[
\int\rho_E^n d\mu=0.
\]

Assim, o menor ansatz compatível com a GDQ é uma polarização de duas cascas:

\[
\boxed{
\rho_E^n d\mu
=
A_n\left[
\delta(\chi-\chi_+)-\delta(\chi-\chi_-)
\right]d\chi,
\qquad
\chi_- > \chi_+.
}
\]

Então:

\[
\boxed{
G_E^n(q^2)
=
A_n\left[
j_0(q C_rR_B\chi_+)
-
j_0(q C_rR_B\chi_-)
\right].
}
\]

Automaticamente:

\[
G_E^n(0)=0.
\]

E:

\[
\langle r_n^2\rangle
=
A_n(C_rR_B)^2(\chi_+^2-\chi_-^2)<0.
\]

Essa é a forma correta do nêutron: carga total nula, mas distribuição
eletro-geométrica polarizada. O sinal negativo surge porque a componente
negativa efetiva fica mais periférica que a positiva.

No fechamento líder:

\[
A_n=\alpha\delta_B,
\qquad
r_\pm=r_p(1\pm\alpha/2),
\]

e:

\[
\boxed{
\langle r_n^2\rangle_{\rm líder}
=
-2\alpha^2\delta_B r_p^2.
}
\]

No fechamento estendido de cola dupla, a amplitude é a projeção torsional
espacial já fixada pelo momento magnético do nêutron:

\[
A_n^{(2)}=|\mu_n|
=
\frac34\delta_B
\left(
1+\alpha\frac{3\sqrt2}{4}
\right),
\]

e o deslocamento relativo das duas interfaces antiparalelas é:

\[
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
\]

Logo:

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
\right],
}
\]

e:

\[
\boxed{
\langle r_n^2\rangle_{\rm ext}
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2
\approx
-0.11772\,{\rm fm}^2.
}
\]

As cascas já podem ser substituídas por um perfil suave local de superfície:

\[
\xi=r-r_p,
\qquad
\xi_\pm=\mp\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\sigma_r=\frac12r_p\alpha_{\rm tor}^{(2)}.
\]

Com:

\[
\rho_E^n(\xi)
=
|\mu_n|[K_\sigma(\xi,\xi_+)-K_\sigma(\xi,\xi_-)],
\]

a carga total permanece nula e a inclinação permanece:

\[
\langle r_n^2\rangle_{\rm suave}
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
\]

O perfil variacional líder da cola torsional é:

\[
H_n(\xi,\tau_n)
=
|\mu_n|
[K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)],
\]

e determina:

\[
G_E^n(q^2)
=
\int H_n(\xi,\tau_n)j_0(q(r_p+\xi))d\xi.
\]

O solver confirma \(G_E^n(0)\simeq0\) e
\(\langle r_n^2\rangle=-0.117721789624\,{\rm fm}^2\). Portanto, a pendência não
é mais obter \(H_n(\chi)\), mas comparar a curva completa com espalhamento
elástico e incluir correções de sonda/magnetização.

Para o momento magnético do nêutron:

\[
\boxed{
G_M^n(q^2)=\mu_n\,j_0(qr_{M,n})
}
\]

é a aproximação líder. Como \(\mu_n<0\), o sinal vem da orientação torsional
oposta da corrente efetiva. A determinação de \(r_{M,n}\) exige resolver a
densidade magnética torsional completa.

---

## 9. Lei assintótica

Para grande \(q^2\), a contribuição dominante vem da estrutura curta de
contorno. Com três estômatos confinados, a lei esperada é:

\[
G_E(q^2)\sim\frac{1}{(q^2)^2}.
\]

Status: plausível por contagem dimensional/contorno, mas deve ser demonstrada
por análise assintótica da transformada radial.

---

## 10. Pendências deste bloco

1. calcular \(G_M^p\) e \(G_M^n\) com densidades magnéticas torsionais, não só normalização;
2. comparar \(G_E^n(q^2)\) variacional com dados de espalhamento elástico;
3. refinar as correções de forma de sonda;
4. provar a lei assintótica \(G\sim(q^2)^{-2}\) por análise de Fourier da borda.

Status:

\[
\boxed{
\text{observáveis eletromagnéticos fechados estruturalmente; comparação numérica fica como trabalho posterior.}
}
\]
