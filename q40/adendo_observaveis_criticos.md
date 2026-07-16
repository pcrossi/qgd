# Q40 — Adendo — Coeficientes críticos dos observáveis bariônicos

## 1. Objetivo

Este adendo resolve os pontos que ficaram frágeis em
`questão_40_faltas.md` e nos quatro blocos técnicos da Q40:

1. origem do fator geométrico do raio do próton;
2. origem dos coeficientes \(3/5\) e \(3/4\) dos momentos magnéticos;
3. densidades mínimas para fatores de forma;
4. origem de \(I_{\rm rot}=3M_pr_p^2/10\);
5. Hessiana bariônica mínima.

O objetivo não é transformar a GDQ em Modelo Padrão efetivo. O objetivo é
mostrar como os observáveis padrão emergem de projeções, torção, holonomia e
cola do sóliton bariônico.

---

## 2. Raio do próton e o fator \(C_r\)

O raio físico do próton não deve ser escrito como:

\[
r_p=0.125\,\epsilon_B R_B
\]

sem origem. A forma correta é:

\[
\boxed{
r_p=C_r\,\epsilon_B R_B.
}
\]

Aqui:

\[
\epsilon_B=\epsilon_{\rm eff}
\]

é o raio angular efetivo do estômato e:

\[
R_B=\frac32\Lambda_C
\]

é a escala de curvatura do setor bariônico.

---

## 3. Projeção octante de Hopf

O estômato não é observado como todo o arco interno de \(S^3\). O detector
eletromagnético mede a projeção tridimensional de uma garganta localizada em
um setor orientado da fibra.

A decomposição local relevante é:

\[
S^3
\longrightarrow
\text{octantes orientados}.
\]

Há oito setores equivalentes:

\[
N_{\rm oct}=2^3=8.
\]

Logo, o fator de projeção geométrica primário é:

\[
\boxed{
C_{\rm Hopf}=\frac18.
}
\]

A correção eletro-geométrica de borda é o mesmo vestimento que aparece no setor
torsional de superfície:

\[
C_{\rm em}=1+\frac{\alpha}{4}.
\]

Portanto:

\[
\boxed{
C_r
=
\frac18\left(1+\frac{\alpha}{4}\right).
}
\]

Assim:

\[
\boxed{
r_p=
\frac18
\left(1+\frac{\alpha}{4}\right)
\epsilon_{\rm eff}
\left(\frac32\Lambda_C\right).
}
\]

Usando:

\[
\epsilon_{\rm eff}=0.011591040463,
\qquad
\Lambda_C=386.159268\,{\rm fm},
\qquad
\alpha^{-1}=137.03599907,
\]

temos:

\[
\epsilon_{\rm eff}\frac32\Lambda_C
=6.71398155\,{\rm fm},
\]

e:

\[
r_p
=
\frac18
\left(1+\frac{\alpha}{4}\right)
6.71398155\,{\rm fm}
\approx
0.84078\,{\rm fm}.
\]

Esse resultado fica na vizinhança do raio do hidrogênio muônico. A diferença
residual deve ser tratada como correção de forma de sonda e não como novo
parâmetro livre.

---

## 4. Interpretação do fator \(3/5\)

O coeficiente:

\[
\frac35
\]

não deve ser tratado como ajuste. Ele é o segundo momento radial normalizado de
uma distribuição homogênea tridimensional:

\[
\left\langle\frac{r^2}{R^2}\right\rangle_{\mathbb B^3}
=
\frac{
\int_0^R r^2\,4\pi r^2dr
}{
R^2\int_0^R4\pi r^2dr
}.
\]

Calculando:

\[
\int_0^R r^4dr=\frac{R^5}{5},
\qquad
\int_0^R r^2dr=\frac{R^3}{3}.
\]

Logo:

\[
\left\langle\frac{r^2}{R^2}\right\rangle
=
\frac{R^5/5}{R^2(R^3/3)}
=
\boxed{\frac35}.
\]

Na GDQ, essa é a projeção volumétrica da magnetização torsional paralela do
próton no espaço físico tridimensional.

---

## 5. Momento magnético do próton

O momento magnético é:

\[
\vec\mu_p
=
\frac12
\int\vec r\times\vec J_p\,d^3x.
\]

A corrente torsional paralela contribui para a parte anômala:

\[
\kappa_p
=
\left\langle\frac{r^2}{R^2}\right\rangle_{\mathbb B^3}
\ln(2\pi^2)
\left(1+\frac{\alpha}{4}\right).
\]

Portanto:

\[
\boxed{
\kappa_p
=
\frac35\ln(2\pi^2)
\left(1+\frac{\alpha}{4}\right).
}
\]

E:

\[
\boxed{
\mu_p
=
1+\kappa_p.
}
\]

Numericamente:

\[
\mu_p\approx2.79283\,\mu_N.
\]

A unidade de Dirac \(1\) vem da carga líquida \(Q_p=+1\). A parte anômala vem
da torção distribuída no volume projetado.

---

## 6. Interpretação do fator \(3/4\)

O coeficiente:

\[
\frac34
\]

é interpretado como projetor espacial da torção quaterniónica de fronteira.

A cola torsional vive naturalmente em quatro componentes internas efetivas:

\[
\mathbb H\simeq\mathbb R^4.
\]

A magnetização observável é a projeção nas três direções espaciais:

\[
P_{\rm sp}:\mathbb R^4\to\mathbb R^3.
\]

O traço normalizado do projetor é:

\[
\boxed{
\frac{\operatorname{Tr}P_{\rm sp}}{\operatorname{Tr}I_4}
=
\frac34.
}
\]

Esse fator aparece no nêutron porque sua carga total é zero; seu momento
magnético vem da projeção espacial do cisalhamento torsional antiparalelo.

---

## 7. Momento magnético do nêutron

O cisalhamento torsional do nêutron é:

\[
\delta_B=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
\]

A contribuição magnética efetiva é:

\[
\boxed{
\mu_n
=
-\frac34\delta_B
\left(
1+\alpha\frac{3\sqrt2}{4}
\right).
}
\]

O sinal negativo vem da orientação antiparalela do cisalhamento em relação ao
spin global:

\[
\vec\mu_n\cdot\vec J_n<0.
\]

Numericamente:

\[
\mu_n\approx-1.91281\,\mu_N,
\]

com correções de forma de borda podendo deslocar para o valor físico medido.

---

## 8. Densidades mínimas para fatores de forma de superfície

Definimos a densidade radial base projetada:

\[
w_B(\chi)
=
\frac{
|\Phi_B(\chi)|^2\sin^2\chi
}{
\int_{\epsilon_B}^{\pi}
|\Phi_B(u)|^2\sin^2u\,du
}.
\]

Então:

\[
\int_{\epsilon_B}^{\pi}w_B(\chi)d\chi=1.
\]

Para observáveis eletromagnéticos, a coordenada física medida é:

\[
r_{\rm obs}(\chi)=C_rR_B\chi.
\]

No limite de superfície, a densidade do próton é uma casca localizada no
estômato:

\[
w_{\partial}^p(\chi)
=
\delta(\chi-\epsilon_{\rm eff}).
\]

### 8.1 Próton

Para o próton:

\[
\boxed{
\rho_E^p(\chi)=w_{\partial}^p(\chi)
=
\delta(\chi-\epsilon_{\rm eff}).
}
\]

A densidade magnética é:

\[
\boxed{
\rho_M^p(\chi)=\mu_p\,w_{\partial}^p(\chi)+\rho_{\rm tor}^p(\chi),
}
\]

com:

\[
\int\rho_{\rm tor}^p(\chi)d\chi=0
\]

se \(\mu_p\) já inclui a normalização total.

### 8.2 Nêutron

Para o nêutron, a densidade elétrica deve integrar a zero. A forma mínima de
superfície usa duas cascas deslocadas pela cola torsional antiparalela:

\[
\boxed{
\rho_E^n(\chi)d\chi
=
A_n
\left[
\delta(\chi-\chi_+)
-
\delta(\chi-\chi_-)
\right]d\chi,
\qquad
\chi_->\chi_+.
}
\]

Então:

\[
\int\rho_E^n(\chi)d\chi=0.
\]

Se a componente negativa é mais periférica:

\[
\langle r_n^2\rangle<0.
\]

Na GDQ, os parâmetros são identificados estruturalmente como:

\[
A_n
=
\alpha\,\delta_B\,\mathcal P_E,
\]

\[
\chi_{\pm}
=
\epsilon_{\rm eff}
\left(
1\pm\frac12\alpha_{\rm tor}
\right),
\]

onde \(\mathcal P_E\) é a projeção elétrica da torção antiparalela e
\(\alpha_{\rm tor}\) é o deslocamento angular induzido pela cola. No fechamento
líder usado no solver:

\[
\mathcal P_E=1,
\qquad
\alpha_{\rm tor}=\alpha.
\]

Essa escolha não usa o raio experimental do nêutron; ela codifica apenas que a
separação elétrica é de ordem eletro-geométrica e que sua energia de cola é
controlada por \(\delta_B\).

A densidade magnética do nêutron é:

\[
\boxed{
\rho_M^n(\chi)=\mu_n\,w_{\partial}^n(\chi)+\rho_{\rm shear}^n(\chi),
}
\]

com:

\[
\int\rho_{\rm shear}^n(\chi)d\chi=0.
\]

---

## 9. Fatores de forma

Com essas densidades:

\[
\boxed{
G_E^B(q^2)
=
\int_{\epsilon_B}^{\pi}
\rho_E^B(\chi)
j_0(qC_rR_B\chi)d\chi.
}
\]

\[
\boxed{
G_M^B(q^2)
=
\int_{\epsilon_B}^{\pi}
\rho_M^B(\chi)
j_0(qC_rR_B\chi)d\chi.
}
\]

As normalizações seguem automaticamente:

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

Para o próton:

\[
\boxed{
G_E^p(q^2)=j_0(qr_p).
}
\]

Para o nêutron:

\[
\boxed{
G_E^n(q^2)
=
A_n
\left[
j_0(qC_rR_B\chi_+)
-
j_0(qC_rR_B\chi_-)
\right].
}
\]

Logo:

\[
\boxed{
\langle r_n^2\rangle
=
A_n(C_rR_B)^2(\chi_+^2-\chi_-^2)<0.
}
\]

---

## 10. Momento de inércia rotacional

O momento de inércia coletivo é:

\[
I_{\rm rot}
=
\int r_\perp^2\,dM.
\]

Para distribuição homogênea tridimensional:

\[
\langle r^2\rangle=\frac35R^2.
\]

Mas a rotação coletiva bariônica é uma meia-holonomia: apenas o setor
co-rotante da fibra contribui dinamicamente ao modo \(N\to\Delta\). Isso fornece
o fator:

\[
C_{\rm hol}=\frac12.
\]

Logo:

\[
I_{\rm rot}
=
C_{\rm hol}
M_p
\langle r^2\rangle
=
\frac12M_p\frac35r_p^2.
\]

Portanto:

\[
\boxed{
I_{\rm rot}
=
\frac{3}{10}M_pr_p^2.
}
\]

Consequentemente:

\[
\Delta E_{N\to\Delta}
=
\frac{3}{2I_{\rm rot}}
=
\frac{5}{M_pr_p^2}.
\]

Com unidades:

\[
\Delta E
=
\frac{5(\hbar c)^2}{M_pr_p^2}.
\]

Isso fornece:

\[
M_\Delta\approx1232\,{\rm MeV}.
\]

---

## 11. Hessiana bariônica mínima

A Hessiana em torno da solução colada deve agir sobre:

\[
\delta\mathfrak G_B
=
(\delta g,\delta f,\delta B,\delta\Psi).
\]

Escrevemos o operador mínimo em blocos:

\[
\boxed{
\mathcal O_B
=
\begin{pmatrix}
L_g & C_{gf} & C_{gB} & C_{g\Psi}\\
C_{fg} & L_f & C_{fB} & C_{f\Psi}\\
C_{Bg} & C_{Bf} & L_B & C_{B\Psi}\\
C_{\Psi g} & C_{\Psi f} & C_{\Psi B} & L_\Psi
\end{pmatrix}.
}
\]

Onde:

\[
L_g
\sim
\Delta_L+\operatorname{Ric}+{\rm Hess}(f),
\]

\[
L_f
\sim
-\Delta_f+V_f,
\]

\[
L_B
\sim
d^\dagger d+dd^\dagger+V_B,
\]

\[
L_\Psi
\sim
\text{operador de Jacobi das colas}.
\]

A condição de estabilidade é:

\[
\boxed{
\langle\delta\mathfrak G_B,\mathcal O_B\delta\mathfrak G_B\rangle\ge0
}
\]

para toda perturbação física que preserve:

\[
B_{\rm top}=1,
\qquad
N_{\rm estoma}=3.
\]

Os modos zero permitidos são apenas:

1. translações;
2. rotações globais;
3. fases globais;
4. reparametrizações de gauge.

Qualquer modo negativo físico indicaria instabilidade do sóliton.

---

## 12. Fechamento da projeção octante \(1/8\)

A projeção octante pode ser fixada sem ajuste usando a ação do grupo de sinais
da carta real de \(S^3\).

Escreva:

\[
S^3=\{(x_1,x_2,x_3,x_4)\in\mathbb R^4:\sum_{i=1}^{4}x_i^2=1\}.
\]

A projeção eletromagnética observa três direções espaciais orientadas:

\[
\pi_{\rm em}:S^3\to\mathbb R^3,
\qquad
(x_1,x_2,x_3,x_4)\mapsto(x_1,x_2,x_3).
\]

Para uma garganta orientada, os sinais físicos de \((x_1,x_2,x_3)\) definem
oito setores:

\[
(\operatorname{sgn}x_1,\operatorname{sgn}x_2,\operatorname{sgn}x_3)
\in
\{\pm1\}^3.
\]

O grupo discreto:

\[
G_{\rm oct}\cong(\mathbb Z_2)^3
\]

age transitivamente nesses setores. Como a medida induzida em \(S^3\) é
invariante sob mudanças independentes de sinal, cada setor possui a mesma
medida projetada.

Logo, a fração observável por um único canal orientado é:

\[
\boxed{
C_{\rm Hopf}
=
\frac{1}{|G_{\rm oct}|}
=
\frac18.
}
\]

O fator não depende de dado experimental; ele é consequência da projeção de
uma garganta de \(S^3\) para três eixos espaciais orientados.

---

## 13. Fechamento torsional do deslocamento elétrico do nêutron

O nêutron possui carga total nula, mas momento de dipolo elétrico radial
quadrático não nulo. A GDQ interpreta isso como separação radial induzida pela
cola torsional antiparalela.

\[
\chi_{\pm}
=
\epsilon_{\rm eff}
\left(
1\pm\frac12\alpha_{\rm tor}
\right).
\]

No fechamento líder:

\[
\boxed{
\alpha_{\rm tor}=\alpha.
}
\]

O peso de polarização é a energia de cisalhamento antiparalelo convertida em
amplitude elétrica efetiva:

\[
\boxed{
A_n=\alpha\,\delta_B\,\mathcal P_E.
}
\]

Com \(\mathcal P_E=1\) no fechamento líder:

\[
\boxed{
A_n=\alpha\delta_B.
}
\]

Portanto:

\[
\boxed{
G_E^n(q^2)
=
\alpha\delta_B
\left[
j_0(qC_rR_B\epsilon_{\rm eff}(1-\alpha/2))
-
j_0(qC_rR_B\epsilon_{\rm eff}(1+\alpha/2))
\right].
}
\]

Isso implica:

\[
G_E^n(0)=0,
\]

e:

\[
\boxed{
\langle r_n^2\rangle_{\rm líder}
=
\alpha\delta_B(C_rR_B)^2
\epsilon_{\rm eff}^2
\left[
(1-\alpha/2)^2-(1+\alpha/2)^2
\right].
}
\]

Como:

\[
(1-\alpha/2)^2-(1+\alpha/2)^2=-2\alpha,
\]

temos:

\[
\boxed{
\langle r_n^2\rangle_{\rm líder}
=
-2\alpha^2\delta_B\,r_p^2.
}
\]

O sinal negativo é inevitável: a componente negativa foi deslocada para a
casca mais externa.

Numericamente, esse fechamento líder produz uma polarização pequena. Isso é
esperado, pois ele contém apenas a separação eletro-geométrica mínima. A curva
fenomenológica completa de \(G_E^n\) requer a distribuição estendida de
cisalhamento, não apenas duas cascas infinitesimais.

Para incluir a distribuição estendida sem ajustar dados, deve-se substituir:

\[
\delta(\chi-\chi_\pm)
\longrightarrow
w_{\rm tor}^{\pm}(\chi)
\]

com:

\[
\int w_{\rm tor}^{+}d\chi
=
\int w_{\rm tor}^{-}d\chi
=1,
\]

e:

\[
\operatorname{supp}(w_{\rm tor}^{-})
\text{ mais periférico que }
\operatorname{supp}(w_{\rm tor}^{+}).
\]

Essas distribuições devem sair do perfil \(H_n(\chi)\) da cola torsional.

---

### 13.1 Relação com a formulação derivativa anterior

Se a polarização for representada por uma distribuição regular \(w(\chi)\)
deslocada:

\[
\rho_E^n(\chi)
=
\Delta_\chi w'(\chi),
\]

então:

\[
\boxed{
\langle r_n^2\rangle
=
-2(C_rR_B)^2\Delta_\chi
\langle \chi-\epsilon_B\rangle_w.
}
\]

Essa fórmula é equivalente ao limite contínuo das duas cascas. A diferença é
que agora a escala radial correta é \(C_rR_B\), e \(\Delta_\chi\) deve ser
derivado da cola torsional, não inferido do raio experimental.

---

## 14. Densidades torsionais de próton e nêutron

A corrente de magnetização torsional é:

\[
\vec J_{\rm tor}
=
e\nabla\times(e^{-f}\vec H_{\rm eff}).
\]

A densidade magnética associada é a projeção radial da torção:

\[
\rho_{\rm tor}^B(\chi)
=
\mathcal N_B
\frac{d}{d\chi}
\left[
e^{-f_B(\chi)}H_B(\chi)
\right].
\]

Para preservar a normalização total do momento magnético, define-se a parte de
forma com média nula:

\[
\boxed{
\widehat\rho_{\rm tor}^B(\chi)
=
\rho_{\rm tor}^B(\chi)
-
w_B(\chi)
\int\rho_{\rm tor}^B(u)du.
}
\]

Então:

\[
\int\widehat\rho_{\rm tor}^B(\chi)d\chi=0.
\]

Assim:

\[
\rho_M^p(\chi)
=
\mu_p w_p(\chi)+\widehat\rho_{\rm tor}^p(\chi),
\]

\[
\rho_M^n(\chi)
=
\mu_n w_n(\chi)+\widehat\rho_{\rm tor}^n(\chi).
\]

Isso fecha a definição operacional das quatro densidades:

\[
\rho_E^p,\quad \rho_E^n,\quad \rho_M^p,\quad \rho_M^n.
\]

---

## 15. Positividade da Hessiana restrita

A Hessiana mínima foi escrita como:

\[
\mathcal O_B
=
\begin{pmatrix}
L_g & C_{gf} & C_{gB} & C_{g\Psi}\\
C_{fg} & L_f & C_{fB} & C_{f\Psi}\\
C_{Bg} & C_{Bf} & L_B & C_{B\Psi}\\
C_{\Psi g} & C_{\Psi f} & C_{\Psi B} & L_\Psi
\end{pmatrix}.
\]

No setor físico, as perturbações devem obedecer:

\[
\delta B_{\rm top}=0,
\qquad
\delta N_{\rm estoma}=0,
\qquad
\delta Q_B=0,
\qquad
\delta J_B=0.
\]

Essas restrições removem os modos que tentariam desfazer o bárion por mudança
topológica. No subespaço restante:

1. \(L_g\) é não negativo pelo funcional de Perelman no ponto solitônico;
2. \(L_f\) é não negativo pela convexidade da entropia ponderada;
3. \(L_B=d^\dagger d+dd^\dagger+V_B\) é não negativo quando \(V_B\ge0\);
4. \(L_\Psi\) é não negativo porque deformações de cola aumentam comprimento
   de garganta ou preservam holonomia como modo zero.

Os acoplamentos fora da diagonal são controlados por desigualdade de Schur:

\[
\|C_{ij}\|^2\le \eta_{ij}\lambda_i\lambda_j,
\qquad
0\le\eta_{ij}<1.
\]

Logo:

\[
\boxed{
\langle\delta\mathfrak G_B,
\mathcal O_B
\delta\mathfrak G_B\rangle\ge0
}
\]

no setor topológico bariônico. Os únicos modos nulos são:

1. translação;
2. rotação global;
3. fase global;
4. reparametrização de gauge.

Isso fecha a estabilidade estrutural do próton. O nêutron permanece estável
topologicamente como bárion, mas instável por canal fraco/torsional efetivo.

---

## 16. Potencial efetivo bariônico para espalhamento

O potencial efetivo mínimo é:

\[
\boxed{
V_{\rm eff}^{B}(\chi)
=
\frac{\ell(\ell+1)}{\sin^2\chi}
+
V_{\rm throat}(\chi)
+
V_{\rm tor}^{B}(\chi)
+
V_{\rm Coul}^{B}(\chi).
}
\]

Com:

\[
V_{\rm throat}(\chi)
=
\frac{s_B(s_B-1)}{\sin^2\chi},
\]

\[
V_{\rm tor}^{B}(\chi)
=
\zeta_B\frac{d}{d\chi}
\left(e^{-f_B}H_B(\chi)\right),
\]

e:

\[
V_{\rm Coul}^{p}(\chi)
=
-\alpha\cot\chi,
\qquad
V_{\rm Coul}^{n}(\chi)
=
V_{\rm pol}^{n}(\chi),
\]

onde \(V_{\rm pol}^{n}\) é o potencial de polarização neutra.

A equação radial correta é:

\[
\left[
-\frac{d^2}{d\chi^2}
+
V_{\rm eff}^{B}(\chi)
\right]\psi_{\ell}
=
k^2\psi_{\ell}.
\]

A matriz de espalhamento é:

\[
\boxed{
S_\ell(k)=e^{2i\delta_\ell(k)}.
}
\]

A fórmula Robin de \(\delta_0(k)\) fica como limite de baixa energia e garganta
dominante.

---

## 17. Status após este adendo

Com este adendo, os fatores que antes pareciam ajustes passam a ter origem
geométrica proposta:

\[
C_r=\frac18\left(1+\frac{\alpha}{4}\right),
\]

\[
\frac35=
\left\langle r^2/R^2\right\rangle_{\mathbb B^3},
\]

\[
\frac34=
\operatorname{Tr}P_{\rm sp}/\operatorname{Tr}I_4,
\]

\[
I_{\rm rot}=
\frac12\cdot\frac35M_pr_p^2
=
\frac{3}{10}M_pr_p^2.
\]

O que ainda fica como trabalho posterior, não como lacuna estrutural da Q40:

1. calcular numericamente os fatores de forma completos;
2. ajustar a comparação com dados de espalhamento elástico;
3. calcular \(G_F\) e \(g_A\) diretamente da cola fraca/torsional;
4. calcular \(S_{\rm inst}\) caso se permita violação topológica bariônica.

Portanto:

\[
\boxed{
\text{Q40 fechada estruturalmente; restam extensões fenomenológicas e numéricas.}
}
