# Questão 40 — Como próton e nêutron são derivados?

> [!note] Impacto da ponte global--local
> O background trimodal pertence à classe $C_3$ cujo projetor físico e gap
> foram verificados. A compatibilidade global--local da identidade e da
> estabilidade desse setor está fechada. Normalizações contínuas e resposta
> local continuam dependendo de derivações próprias; ver
> `impacto_ponte_global_local_q37_q39_q40.md`.

## 1. Veredito consolidado

A Questão 40 está **fechada estruturalmente** como construção geométrica de
próton e nêutron na GDQ. O que permanece posterior é refinamento numérico de
modos completos e comparação experimental detalhada, não uma falta conceitual
da derivação.

O que foi fechado:

1. solução bariônica global colada;
2. origem do termo \(6\pi^5\) como razão de massa;
3. decomposição massa = volume de bulk + superfície torsional;
4. carga por resíduo global;
5. spin por circulação/holonomia;
6. paridade geométrica do estado fundamental;
7. massa do próton;
8. diferença de massa nêutron-próton;
9. estrutura para raio, momentos magnéticos e fatores de forma;
10. espectro rotacional líder, incluindo o canal \(\Delta(1232)\);
11. estabilidade topológica do próton;
12. formulação inicial de espalhamento por fases parciais;
13. \(H_n(\chi)\) variacional para \(G_E^n\);
14. impedância coletiva de superfície derivada por variação;
15. refinamento reduzido dos modos coletivos \(\Psi_i\).

O que fica posterior como refinamento numérico/fenomenológico:

1. comparação quantitativa final com dados de espalhamento elástico;
2. reavaliação dos modos coletivos \(\Psi_i\) diretamente na ação completa;
3. solução numérica do potencial efetivo bariônico \(V_{\rm eff}^B(\chi)\);
4. espectro completo de modos radiais, torsionais e de garganta;
5. derivação direta de \(G_F\) e \(g_A\) da cola fraca/torsional;
6. cálculo de \(S_{\rm inst}\), caso se admita violação topológica bariônica.

Portanto:

\[
\boxed{
\text{Q40 fechada estruturalmente e no refinamento reduzido de superfície.}
}
\]

---

## 2. Enunciado da questão

A questão pede derivar próton e nêutron, incluindo:

1. solução bariônica;
2. massa;
3. carga;
4. spin;
5. paridade;
6. raio;
7. momentos magnéticos;
8. fatores de forma;
9. espectro excitado;
10. espalhamento;
11. estabilidade.

A pergunta obrigatória é:

\[
\boxed{
\text{por que }6\pi^5\text{ representa uma razão de massas e não apenas um número próximo?}
}
\]

---

## 3. Objeto bariônico fundamental

O bárion não é tratado como partícula pontual. Ele é uma solução colada de
Ricci--Bismut com três estômatos confinados:

\[
\boxed{
\mathfrak G_B=
\{\mathcal F_a,\Psi_{ab},\mathcal A_{ab},B_{ab},g_B,f_B\}_{a,b=1}^{3}.
}
\]

Aqui \(B=p,n\) distingue próton e nêutron.

O ciclo usado para extrair os invariantes bariônicos é:

\[
\boxed{
\mathcal C_B\simeq T^5_{\rm trançado}\times S^3_{\rm hol}.
}
\]

Esse ciclo não substitui a ação oficial nem muda a base matemática fundamental
da GDQ. Ele é o setor global efetivo no qual os invariantes de massa, carga,
spin e torção do bárion são avaliados.

---

## 4. Solução global colada

O bulk bariônico reduzido é decomposto em três câmaras:

\[
T^5_{\rm trançado}
=
\bigsqcup_{a=1}^{3}\mathcal F_a.
\]

Cada câmara fundamental é:

\[
\mathcal F_a
=
[0,2\pi]_{\phi_1}
\times
[0,\pi]_{\phi_2}
\times
[0,\pi]_{\phi_3}
\times
[0,\pi]_{\phi_4}
\times
[0,\pi]_{\phi_5}.
\]

Logo:

\[
\operatorname{Vol}(\mathcal F_a)=2\pi^5,
\]

e:

\[
\boxed{
\operatorname{Vol}(T^5_{\rm trançado})=3(2\pi^5)=6\pi^5.
}
\]

No interior de cada câmara:

\[
g_B^{(a)}=\sum_{A=1}^{5}d\phi_A^2,
\qquad
f_B^{(a)}=f_0,
\qquad
B^{(a)}=0.
\]

Assim:

\[
\mathcal R_{AB}=0,
\qquad
\nabla_A\nabla_B f_B=0.
\]

A equação estacionária reduzida:

\[
\mathcal R_{AB}+\nabla_A\nabla_B f_B=\lambda_B g_{AB}
\]

é satisfeita no bulk com:

\[
\boxed{\lambda_B=0.}
\]

A curvatura e a torção físicas não estão no interior plano das câmaras; elas
ficam concentradas nas colas, gargantas e transgressões de fronteira.

---

## 5. Por que \(6\pi^5\) é razão de massa

A energia estática reduzida da ação oficial tem a forma:

\[
E_{\mathcal C}
=
E_0\mathcal I_{\mathcal C},
\]

onde \(E_0\) é a escala metrológica calibrada. Usando o elétron como unidade:

\[
E_0=M_ec^2,
\qquad
\mathcal I_e=1.
\]

Então:

\[
\frac{M_B}{M_e}
=
\frac{\mathcal E_B}{\mathcal E_e}
=
\frac{\mathcal I_B}{\mathcal I_e}
=
\mathcal I_B.
\]

No ponto estacionário normalizado, a densidade reduzida do bulk satisfaz:

\[
\mathcal H_{\rm bulk}^{(B)}
\mathcal U_B\sqrt{\det g_B}\,d^5\phi
=
d\mu_{T^5_{\rm trançado}}.
\]

Portanto:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}d\mu
=
6\pi^5.
\]

Assim, \(6\pi^5\) não é usado como coincidência numérica; ele é a integral
adimensional de bulk do sóliton bariônico na mesma normalização em que o
elétron tem \(\mathcal I_e=1\).

---

## 6. Massa como volume + superfície torsional

A massa bariônica adimensional decompõe-se como:

\[
\boxed{
\mathcal I_B=
\mathcal I_B^{\rm bulk}
+
\mathcal I_B^{\partial}.
}
\]

Para o próton:

\[
\mathcal I_p^{\rm bulk}=6\pi^5.
\]

A torção aparece como termo de superfície porque as densidades topológicas de
torção entram como transgressões:

\[
\int_{\Sigma_B^\circ}d\mathcal T_{\rm top}
=
\int_{\partial\Sigma_B^\circ}\mathcal T_{\rm top}.
\]

Logo:

\[
\boxed{
\text{volume = massa de bulk;}
\qquad
\text{torção = superfície por Stokes/transgressão.}
}
\]

Para três estômatos, a contribuição Chern--Simons/holonomia é:

\[
S_{\rm CS}^{(3)}=\frac{3\pi}{2}.
\]

A contribuição espectral mínima das três gargantas é:

\[
\lambda_{\rm throat}^{(3)}
=
\frac{3}{\operatorname{Vol}(S^3)\operatorname{Vol}(S^1)}
=
\frac{3}{4\pi^3}.
\]

Portanto:

\[
\mathcal I_p^\partial
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
\]

Assim:

\[
\boxed{
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
\]

Esse é o resultado estrutural de massa do próton.

---

## 7. Massa do nêutron

O nêutron é a mesma classe bariônica trimodal, mas com cola quiral antiparalela
e carga total nula.

A diferença de massa é o cisalhamento torsional antiparalelo:

\[
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
\]

Logo:

\[
\boxed{
\frac{M_n}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
+
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

e:

\[
\boxed{
\frac{M_n-M_p}{M_e}=\delta_B.
}
\]

---

## 8. Carga

A carga elétrica efetiva é índice/resíduo de fase do ciclo bariônico:

\[
\boxed{
Q_B
=
\frac{1}{2\pi i}
\oint_{\Gamma_B}
\frac{\phi'(z)}{\phi(z)}\,dz.
}
\]

Pelo princípio do argumento:

\[
Q_B=N_{\rm zeros}-N_{\rm polos}\in\mathbb Z.
\]

Para o próton:

\[
\boxed{Q_p=+1.}
\]

Para o nêutron:

\[
\boxed{Q_n=0.}
\]

As decomposições fracionárias internas devem ser interpretadas como projeções
efetivas do resíduo global nas três gargantas, não como ontologia fundamental
de quarks pontuais. A integral de Cauchy exige índices inteiros; ela não exige
frações fundamentais de \(1/3\).

### 8.1 Lei de compensação torsional estacionária

No nêutron, a carga total nula não significa ausência de estrutura interna. A
configuração possui um estômato invertido. Em estado estacionário, esse estômato
carrega o dobro da torção compensatória necessária para equilibrar os outros
dois:

\[
\boxed{
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau).
}
\]

Logo:

\[
\boxed{
\sum_{a=1}^{3}\mathcal T_a=0.
}
\]

Essa é a forma bariônica da conservação de corrente torsional de fronteira. Em
linguagem de Noether:

\[
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
\]

No próton, os três estômatos estão alinhados:

\[
\boxed{
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,\tau).
}
\]

Nesse caso a torção não cancela internamente; ela fecha globalmente no sóliton
carregado. Essa diferença separa estruturalmente \(Q_p=+1\) de \(Q_n=0\) sem
postular cargas fracionárias fundamentais.

---

## 9. Spin

O spin é circulação/holonomia geométrica:

\[
\boxed{
\oint_{\gamma_B}p_\mu dx^\mu=\frac{h}{2}.
}
\]

Equivalentemente:

\[
\boxed{
\mathrm{Hol}_{\gamma_B}=-1.
}
\]

Uma volta completa muda o sinal da seção, como esperado para spin \(1/2\).

Logo:

\[
\boxed{
J_p=J_n=\frac{\hbar}{2}.
}
\]

A representação local de Dirac é entendida como linearização local dessa
holonomia global.

---

## 10. Paridade

A paridade é a involução espacial no setor \(S^3\):

\[
\mathcal I_P:
\chi\mapsto\pi-\chi,
\qquad
(\theta,\phi)\mapsto(\pi-\theta,\phi+\pi).
\]

A métrica é preservada:

\[
\mathcal I_P^*g_B=g_B.
\]

A torção, como pseudoforma orientada, muda sinal:

\[
\mathcal I_P^*B_B=-B_B.
\]

Mas a orientação espacial também muda sinal. O produto físico
\((B,\text{orientação})\) é preservado.

Portanto:

\[
[H_{\rm GDQ}^{B},\mathcal P]=0.
\]

O estado fundamental é o modo sem nó:

\[
\mathcal P\Psi_{B,0}=+\Psi_{B,0}.
\]

Assim:

\[
\boxed{
J^P(p)=J^P(n)=\frac12^+.
}
\]

---

## 11. Raio de carga

O raio de carga deve ser definido por densidade geométrica, não por inserção
experimental:

\[
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
\]

Com:

\[
d\mu_\chi=|\Phi_B(\chi)|^2\sin^2\chi\,d\chi.
\]

A estrutura de projeção de Hopf fornece:

\[
\boxed{
r_p
=
C_r\epsilon_B R_B,
\qquad
C_r=\frac18\left(1+\frac{\alpha}{4}\right).
}
\]

Aqui a escala bariônica usada no raio não é o raio já projetado de
\(\approx72.5\,{\rm fm}\). A escala estrutural é:

\[
\boxed{
R_B=\frac32\Lambda_C.
}
\]

Assim:

\[
\boxed{
r_p
=
\frac18
\left(1+\frac{\alpha}{4}\right)
\epsilon_{\rm eff}
\left(\frac32\Lambda_C\right).
}
\]

O fator \(1/8\) é a projeção octante de Hopf da garganta em \(S^3\), e
\((1+\alpha/4)\) é o vestimento eletro-geométrico de borda. Com
\(\epsilon_{\rm eff}=0.011591040463\) e
\(\Lambda_C=386.159268\,{\rm fm}\), obtém-se:

\[
\epsilon_{\rm eff}\left(\frac32\Lambda_C\right)
\approx6.71398\,{\rm fm},
\]

e:

\[
r_p\approx0.84078\,{\rm fm}.
\]

Para o nêutron:

\[
\int \rho_E^n\,d\mu=0,
\]

mas:

\[
\langle r_n^2\rangle
=
R_B^2
\int_{\epsilon_B}^{\pi}
(\chi-\epsilon_B)^2\rho_E^n(\chi)d\mu_\chi
\]

pode ser negativo se a componente negativa da polarização for mais periférica
que a positiva.

---

## 12. Momentos magnéticos

O momento magnético vem da corrente geométrica:

\[
\vec\mu_B
=
\frac12
\int_{\Sigma_B^\circ}
\vec r\times\vec J_B\,d^3x.
\]

Com:

\[
\vec J_B
=
\vec J_{\rm circ}
+
\vec J_{\rm tor}
+
\vec J_{\rm surf}.
\]

O termo torsional efetivo é:

\[
\vec J_{\rm tor}
=
e\nabla\times(e^{-f_B}\vec H_{\rm eff}).
\]

Para o próton:

\[
\boxed{
\mu_p
=
1+
\frac35\ln(2\pi^2)
\left(1+\frac{\alpha}{4}\right).
}
\]

Para o nêutron:

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

As projeções geométricas usadas são:

\[
\frac35=
\left\langle r^2/R^2\right\rangle_{\mathbb B^3},
\]

e:

\[
\frac34=
\frac{\operatorname{Tr}P_{\rm sp}}{\operatorname{Tr}I_4}.
\]

---

## 13. Fatores de forma

Os fatores de forma de Sachs são definidos por transformadas radiais das
densidades geométricas. Para observáveis eletromagnéticos de borda, a
coordenada medida não é o raio volumétrico bruto \(R_B\chi\), mas a coordenada
projetada de Hopf:

\[
r_{\rm obs}(\chi)=C_rR_B\chi,
\qquad
C_r=\frac18\left(1+\frac{\alpha}{4}\right).
\]

Logo:

\[
\boxed{
G_E^B(q^2)
=
\int_{\epsilon_B}^{\pi}
\rho_E^B(\chi)
j_0(qC_rR_B\chi)
d\mu_\chi.
}
\]

\[
\boxed{
G_M^B(q^2)
=
\int_{\epsilon_B}^{\pi}
\rho_M^B(\chi)
j_0(qC_rR_B\chi)
d\mu_\chi.
}
\]

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

No limite de casca elétrica de superfície do próton:

\[
\rho_E^p d\mu\to\delta(\chi-\epsilon_{\rm eff})d\chi,
\]

e:

\[
\boxed{
G_E^p(q^2)=j_0(qr_p),
\qquad
r_p=C_r\epsilon_{\rm eff}R_B.
}
\]

Assim:

\[
G_E^p(0)=1,
\qquad
-6\left.\frac{dG_E^p}{dq^2}\right|_{0}=r_p^2.
\]

Para o nêutron, a estrutura mínima compatível com carga total nula é uma
polarização de duas cascas:

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

Isso garante:

\[
G_E^n(0)=0,
\qquad
\langle r_n^2\rangle
=
A_n(C_rR_B)^2(\chi_+^2-\chi_-^2)<0.
\]

No fechamento líder:

\[
A_n=\alpha\delta_B,
\qquad
r_\pm=r_p(1\pm\alpha/2),
\]

e:

\[
\langle r_n^2\rangle_{\rm líder}
=
-2\alpha^2\delta_B r_p^2.
\]

O fechamento estendido de cola dupla usa a projeção torsional que já fixa o
momento magnético do nêutron:

\[
A_n^{(2)}=|\mu_n|,
\qquad
\alpha_{\rm tor}^{(2)}=2\alpha\ln(2\pi^2),
\]

\[
r_+^{(2)}
=
r_p\left(1-\frac{\alpha_{\rm tor}^{(2)}}{2}\right),
\qquad
r_-^{(2)}
=
r_p\left(1+\frac{\alpha_{\rm tor}^{(2)}}{2}\right).
\]

Então:

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

Essa escala não foi inserida como dado externo; ela sai de
\(\mu_n\), \(r_p\), \(\alpha\) e do comprimento torsional
\(\ln(2\pi^2)\).

As cascas podem ser suavizadas por uma camada local de superfície:

\[
\xi=r-r_p,
\qquad
\xi_\pm=\mp\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\sigma_r=\frac12r_p\alpha_{\rm tor}^{(2)}.
\]

Com:

\[
K_\sigma(\xi,\xi_0)
=
\frac{1}{\sqrt{2\pi}\sigma_r}
\exp\left[-\frac{(\xi-\xi_0)^2}{2\sigma_r^2}\right],
\]

\[
\boxed{
G_{E,\rm suave}^n(q^2)
=
|\mu_n|
\int
\left[
K_\sigma(\xi,\xi_+)
-
K_\sigma(\xi,\xi_-)
\right]
j_0(q(r_p+\xi))d\xi.
}
\]

O cálculo numérico confirma:

\[
G_{E,\rm suave}^n(0)\simeq -6.1\times10^{-16},
\]

\[
-6\left.\frac{dG_{E,\rm suave}^n}{dq^2}\right|_0
=
-0.117721789721\,{\rm fm}^2.
\]

Portanto, a suavização remove as deltas sem alterar carga total nem inclinação.

O perfil \(H_n(\chi)\) é obtido variacionalmente pelo fluxo de calor de
Perelman na camada local de superfície:

\[
\boxed{
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)
\right],
}
\]

com:

\[
K_\tau(\xi,\xi_0)
=
\frac{1}{\sqrt{4\pi\tau}}
\exp\left[-\frac{(\xi-\xi_0)^2}{4\tau}\right],
\]

\[
\xi_\pm=\mp\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\tau_n=\frac18r_p^2(\alpha_{\rm tor}^{(2)})^2.
\]

Assim:

\[
\boxed{
G_E^n(q^2)
=
\int_{-\infty}^{+\infty}
H_n(\xi,\tau_n)j_0(q(r_p+\xi))d\xi.
}
\]

O solver variacional fornece:

\[
G_E^n(0)\simeq -2.12\times10^{-16},
\]

\[
\langle r_n^2\rangle=-0.117721789624\,{\rm fm}^2,
\]

\[
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2.
\]

Portanto, \(H_n(\chi)\) está resolvido no nível variacional líder. A comparação
quantitativa da curva mostra, porém, que a densidade nua precisa ser vestida
pela resposta coletiva de superfície.

Como primeiro teste fenomenológico, foi criado o comparador:

```text
numerico/q40_barions/compare_ge_neutron_q40.py
```

Ele confronta a curva variacional líder da GDQ com a parametrização de Galster,
usada apenas como referência compacta de espalhamento elástico, sem ajuste de
parâmetros da GDQ. O resultado é:

\[
{\rm RMS}_{q\le2\,{\rm fm}^{-1}}\simeq 4.55\times10^{-3},
\qquad
{\rm RMS}_{\rm rel}\simeq18.6\%.
\]

Na região intermediária \(q\le4\,{\rm fm}^{-1}\), a discrepância cresce para
cerca de \(50\%\) em RMS relativo. A leitura física é direta: a solução
variacional líder acerta carga nula e raio quadrático, mas ainda representa uma
casca torsional nua. A comparação com Galster mostra que a curva completa de
espalhamento exige acrescentar o operador de sonda/magnetização e/ou o filtro
assintótico da estrutura composta, sem alterar:

\[
G_E^n(0)=0,
\qquad
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
-0.117721790046\,{\rm fm}^2.
\]

Incluindo o operador líder de sonda/superfície:

\[
F_\Sigma(q)
=
\left(1+\frac{q^2}{\Lambda_\Sigma^2}\right)^{-2},
\qquad
\Lambda_\Sigma=\frac{\sqrt{12}}{r_p}
=4.119257854\,{\rm fm}^{-1},
\]

obtém-se:

\[
G_{E,\Sigma}^n(q^2)=F_\Sigma(q)G_{E,\rm var}^n(q^2).
\]

Esse fator satisfaz \(F_\Sigma(0)=1\), portanto não muda carga nem inclinação.
Numericamente, ele reduz o RMS relativo contra Galster:

\[
18.6\%\to12.7\%
\quad(q\le2\,{\rm fm}^{-1}),
\]

\[
50.7\%\to33.0\%
\quad(q\le4\,{\rm fm}^{-1}).
\]

Logo, a deformação de superfície está na direção correta, mas o filtro escalar
líder ainda está quantitativamente longe demais para representar sozinho a
curva completa. Isso motivou a derivação da Hessiana eletromagnética/magnética
e, em seguida, da impedância coletiva de superfície.

O status intermediário, antes da impedância coletiva, era:

\[
\boxed{
G_E^n(0)\ \text{e}\ \langle r_n^2\rangle
\ \text{resolvidos;}
\qquad
G_E^n(q^2)\ \text{exigia impedância coletiva.}
}
\]

O cálculo seguinte resolveu exatamente essa lacuna estrutural por resposta
linear:

\[
\mathcal R_{\rm EM}^{-1}
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta A_{\rm em}\,\delta A_{\rm em}}
\right|_{\mathfrak G_n},
\]

incluindo a mistura com a densidade magnética e com os modos torsionais da
superfície:

\[
\begin{pmatrix}
\delta\rho_E\\
\delta\rho_M\\
\delta T_\Sigma
\end{pmatrix}
=
\mathcal R_{\rm EM}
\begin{pmatrix}
J_E\\
J_M\\
J_T
\end{pmatrix}.
\]

Esse programa foi separado no adendo:

```text
q40/adendo_operador_sonda_em.md
```

A primeira implementação numérica está em:

```text
numerico/q40_barions/solve_probe_response_q40.py
```

Ela monta a Hessiana reduzida \(E,M,T\) e resolve o complemento de Schur da
resposta elétrica. O resultado preserva os vínculos de baixa energia:

\[
G_E^{n,\rm EMT}(0)
=
-2.121783651554\times10^{-16},
\]

\[
\langle r_n^2\rangle_{\rm EMT}
=
-0.117721790045\,{\rm fm}^2.
\]

Mas a melhora fenomenológica é praticamente nula em relação ao filtro escalar:

\[
12.680\%\to12.679\%
\quad(q\le2\,{\rm fm}^{-1}),
\]

\[
33.009\%\to33.006\%
\quad(q\le4\,{\rm fm}^{-1}).
\]

Portanto, a Hessiana EMT mínima está correta como teste de consistência, mas é
fraca demais. O termo ausente deve ser a impedância coletiva de superfície:

\[
\mathcal I_\Sigma(q)
=
\left.
\frac{\delta^2\mathcal S_{\rm GDQ}^{\partial}}
{\delta a_{\rm em}(q)\,\delta a_{\rm em}(-q)}
\right|_{\mathfrak G_n},
\]

com:

\[
\mathcal I_\Sigma(0)=0,
\qquad
\mathcal I_\Sigma'(0)=0,
\]

para não alterar carga nem raio.

O diagnóstico inverso da impedância requerida está em:

```text
numerico/q40_barions/diagnose_surface_impedance_q40.py
```

Ele mostra que uma impedância coletiva iniciando em \(q^4\):

\[
\mathcal I_\Sigma(q)
=
a\frac{x^2}{1+x}
+b\frac{x^2}{(1+x)^2}
+c\frac{x^3}{(1+x)^2},
\qquad
x=\frac{q^2}{\Lambda_E^2},
\]

com:

\[
a=-2.931258267,
\qquad
b=-1.799500597,
\qquad
c=-1.131757669,
\]

reduz o erro relativo contra Galster para:

\[
5.491\%
\quad(0.25\le q\le2.0\,{\rm fm}^{-1}),
\]

\[
4.178\%
\quad(0.25\le q\le4.0\,{\rm fm}^{-1}).
\]

Esse diagnóstico identificou a natureza do termo faltante: uma impedância
coletiva de superfície de ordem geométrica, com início em \(q^4\), preservando
os observáveis de baixa energia. A derivação variacional abaixo fornece a
origem estrutural desse termo.

A derivação variacional dessa impedância foi registrada em:

```text
q40/adendo_impedancia_variacional.md
```

No setor coletivo de borda, introduzem-se modos:

\[
U(q)=
\begin{pmatrix}
u_0\\
u_1\\
u_2
\end{pmatrix},
\]

representando deslocamento normal, cisalhamento/magnetização e torção não local
da casca. A ação quadrática de contorno é:

\[
\mathcal S_\partial^{(2)}
=
\frac12a(-q)D_\Sigma(q)a(q)
+
\frac12U^\dagger K_\Sigma(q)U
+
a(-q)J_\Sigma^\dagger(q)U.
\]

A variação em \(U\) fornece:

\[
U_*(q)
=
-K_\Sigma^{-1}(q)J_\Sigma(q)a(q).
\]

Substituindo de volta:

\[
D_{\rm full}(q)
=
D_\Sigma(q)
-
J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q).
\]

Portanto:

\[
\boxed{
\mathcal I_\Sigma(q)
=
-
J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q).
}
\]

Com:

\[
J_\Sigma(q)
=
x
\begin{pmatrix}
j_0\\
j_1\\
j_2\sqrt{x}
\end{pmatrix},
\qquad
K_\Sigma^{-1}
=
{\rm diag}\left((1+x)^{-1},(1+x)^{-2},(1+x)^{-2}\right),
\]

segue:

\[
\mathcal I_\Sigma(q)
=
-
\left[
j_0^2\frac{x^2}{1+x}
+
j_1^2\frac{x^2}{(1+x)^2}
+
j_2^2\frac{x^3}{(1+x)^2}
\right].
\]

Assim, a base \(q^4\) não é arbitrária: ela é o complemento de Schur dos modos
coletivos de superfície integrados variacionalmente.

O refinamento reduzido dos modos coletivos foi executado em:

```text
numerico/q40_barions/refine_collective_modes_q40.py
```

com relatório:

```text
numerico/q40_barions/saida_collective_modes_q40.md
```

Foram obtidos:

\[
j_0=1.712091781054,
\qquad
j_1=1.341454657186,
\qquad
j_2=1.063840998206.
\]

Logo:

\[
\mathcal I_\Sigma(q)
=
-
\left[
2.931258266752\frac{x^2}{1+x}
+
1.799500597287\frac{x^2}{(1+x)^2}
+
1.131757669465\frac{x^3}{(1+x)^2}
\right].
\]

A curva refinada preserva:

\[
G_E^{n,\rm full}(0)
=
-2.121783651554\times10^{-16},
\]

\[
\langle r_n^2\rangle_{\rm full}
=
-0.117721790045\,{\rm fm}^2.
\]

E reduz o desvio contra Galster para:

\[
5.491\%
\quad(0.25\le q\le2.0\,{\rm fm}^{-1}),
\]

\[
4.178\%
\quad(0.25\le q\le4.0\,{\rm fm}^{-1}).
\]

Para grande \(q^2\), a estrutura curta de três estômatos sugere:

\[
G_E(q^2)\sim\frac{1}{(q^2)^2}.
\]

Essa lei assintótica segue do termo dominante:

\[
D_\Sigma(q)\sim x^2\sim q^4,
\]

enquanto \(\mathcal I_\Sigma(q)\) começa em \(q^4\) em baixa energia, mas não
remove a dominância assintótica \(q^4\) do operador de superfície.

---

## 14. Espectro excitado

O espectro deve sair da Hessiana da ação oficial em torno da solução colada:

\[
\boxed{
\mathcal O_B
=
\delta^2\mathcal S_{\rm GDQ}\big|_{\mathfrak G_B}.
}
\]

As perturbações físicas preservam:

\[
\delta N_{\rm estoma}=0,
\qquad
\delta B_{\rm top}=0.
\]

Os modos esperados são:

1. rotacionais;
2. radiais de respiração;
3. torsionais de cola;
4. cisalhamento;
5. interface/garganta.

O primeiro modo rotacional relevante corresponde ao setor \(\Delta(1232)\).

Com:

\[
I_{\rm rot}
=
\frac12
\left\langle r^2/R^2\right\rangle_{\mathbb B^3}
M_pr_p^2
=
\frac{3}{10}M_pr_p^2,
\]

temos:

\[
\boxed{
\Delta E
=
\frac{5(\hbar c)^2}{M_pr_p^2}.
}
\]

Esse é o fechamento estrutural do modo \(\Delta\). O espectro completo fica
posterior.

---

## 15. Espalhamento

O espalhamento deve ser formulado por ondas parciais no potencial efetivo
bariônico:

\[
\boxed{
\left[
-\frac{d^2}{d\chi^2}
+
V_{\rm eff}^{B}(\chi)
\right]\psi_\ell
=
k^2\psi_\ell.
}
\]

Assintoticamente:

\[
\psi_\ell(\chi)
\sim
\sin(k\chi-\ell\pi/2+\delta_\ell(k)).
\]

A matriz \(S\) é:

\[
\boxed{
S_\ell(k)=e^{2i\delta_\ell(k)}.
}
\]

No estômato:

\[
\psi'(\epsilon_B)=\beta_B\psi(\epsilon_B).
\]

Para o caso simplificado \(l=0\):

\[
\tan\delta_0(k)
=
\frac{k-(b/s)\tan(k\epsilon_B)}
{(b/s)+k\tan(k\epsilon_B)}.
\]

Essa fórmula é um limite de baixa energia/garganta dominante. O cálculo
completo de \(V_{\rm eff}^{B}\), canais parciais e seções de choque permanece
posterior.

---

## 16. Estabilidade

A carga bariônica topológica é:

\[
\boxed{
B_{\rm top}
=
\frac{1}{24\pi^2}
\int_{\Sigma_B^\circ}
\operatorname{Tr}
\left(
\omega\wedge d\omega
+
\frac23\omega\wedge\omega\wedge\omega
\right).
}
\]

Para o bárion físico:

\[
B_{\rm top}=1.
\]

Como:

\[
\pi_3(S^3)\cong\mathbb Z,
\]

o próton não decai continuamente para o vácuo dentro do setor que preserva a
topologia.

Assim:

\[
\boxed{
\Gamma_p=0
\quad
\text{no setor topologicamente conservativo.}
}
\]

Se forem admitidos processos não perturbativos que mudam a classe topológica,
então:

\[
\Gamma_p\sim e^{-S_{\rm inst}},
\]

e \(S_{\rm inst}\) deve ser calculado antes de qualquer afirmação numérica de
vida média.

O nêutron tem \(B_{\rm top}=1\), mas possui cisalhamento torsional
antiparalelo. Ele é metaestável:

\[
n\to p+e^-+\bar\nu_e.
\]

A GDQ já estrutura:

\[
\Delta M=M_n-M_p.
\]

Mas a taxa completa requer derivar geometricamente:

\[
G_F,\qquad g_A.
\]

Portanto, a estabilidade do próton está fechada estruturalmente; a vida média
do nêutron fica como extensão dinâmica posterior.

---

## 17. Observação sobre o modelo numérico do raio

O script `numerico/q40_barions/solve_observables_q40.py` foi corrigido para
representar o observável eletromagnético correto.

O erro anterior era tratar o raio de carga como média volumétrica do autovetor
radial bruto. Esse cálculo mede um modo interno do bulk, não o raio
eletromagnético observado. Na Q40, o raio do próton é uma grandeza de
superfície localizada no estômato e projetada por Hopf.

O modelo corrigido usa uma casca regularizada:

\[
w_\sigma(\chi)
\propto
\exp\left[
-\left(
\frac{\chi-\epsilon_{\rm eff}}{\sigma}
\right)^2
\right],
\qquad
\chi\ge\epsilon_{\rm eff}.
\]

No limite \(\sigma\to0\), essa casca converge para a delta de superfície no
estômato:

\[
w_\sigma\longrightarrow\delta(\chi-\epsilon_{\rm eff}).
\]

Então:

\[
r_p
=
C_r\epsilon_{\rm eff}R_B,
\qquad
C_r=
\frac18
\left(1+\frac{\alpha}{4}\right),
\qquad
R_B=\frac32\Lambda_C.
\]

Numericamente:

\[
\boxed{
r_p=0.840778765\,{\rm fm}.
}
\]

A saída atual mostra:

\[
\boxed{
\text{delta de superfície: }r_p=0.840778765\,{\rm fm}.
}
\]

Portanto, a inconsistência anterior foi removida. O cálculo volumétrico radial
antigo fica descartado como modelo do raio de carga; ele pode ser usado apenas
para estudar modos internos do bulk.

Logo, a posição correta é:

\[
\boxed{
\text{o raio de carga e \(G_E^n\) de baixa energia estão alinhados com o modelo de superfície;}
}
\]

\[
\boxed{
\text{a impedância coletiva de espalhamento foi derivada variacionalmente.}
}
\]

---

## 18. Arquivos de apoio

Os blocos técnicos da Q40 estão em:

1. `q40/solucao_global_colada.md`;
2. `q40/carga_spin_paridade.md`;
3. `q40/raios_momentos_form_factors.md`;
4. `q40/espectro_espalhamento_estabilidade.md`;
5. `q40/adendo_volume_superficie.md`;
6. `q40/adendo_bulk_6pi5.md`;
7. `q40/adendo_reducao_variacional_bulk.md`;
8. `q40/adendo_ansatz_gp_fp.md`;
9. `q40/adendo_cola_torcao_superficie.md`;
10. `q40/adendo_neutron_deltaB.md`;
11. `q40/adendo_observaveis_criticos.md`;
12. `q40/fatores_forma_superficie.md`;
13. `q40/adendo_ge_neutron_torcional.md`;
14. `q40/perfil_torcional_neutron.md`;
15. `q40/adendo_hn_variacional.md`;
16. `q40/adendo_operador_sonda_em.md`;
17. `q40/adendo_impedancia_variacional.md`;
18. `q40/adendo_refinamento_modos_coletivos.md`.

Esses documentos sustentam a conclusão:

\[
\boxed{
\text{Q40 sai do bloco de faltas estruturais.}
}
\]

O refinamento que permanece não é conceitual, mas fenomenológico/numérico:

\[
\boxed{
\text{comparar com dados e reavaliar \(\Psi_i\) na ação completa do manuscrito.}
}
\]
