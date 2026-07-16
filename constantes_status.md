# Status das constantes, escalas e acoplamentos na GDQ

## 1. Objetivo

Este documento separa, de modo auditável, quais constantes já estão
estruturalmente derivadas, quais são calibrações metrológicas, quais são
estimativas fenomenológicas e quais permanecem abertas.

A regra é:

\[
\boxed{
\text{a GDQ deve prever razões adimensionais; unidades absolutas exigem calibração metrológica.}
}
\]

Portanto, números em MeV, GeV, fm ou segundos não são gerados “do nada”. Eles
aparecem após escolher uma unidade física de referência, como \(M_e c^2\),
\(\hbar\), \(c\) ou uma escala geométrica calibrada.

---

## 2. Classes usadas

### Classe A — Derivada estruturalmente

Há uma dedução geométrica interna suficiente para usar a quantidade como parte
da teoria consolidada.

### Classe B — Calibrada metrologicamente

A teoria prevê razões ou autovalores adimensionais, mas a unidade física é
fixada por uma referência, por exemplo \(M_e c^2\).

### Classe C — Estimativa fenomenológica

Há fórmula plausível e numericamente relevante, mas ainda depende de uma
identificação efetiva, comparação externa ou normalização não totalmente
derivada.

### Classe D — Aberta

A estrutura ainda não possui derivação suficiente.

---

## 3. Massas e razões de massa

| Quantidade | Status | Observação |
|---|---:|---|
| \(M_e\) | B | escala de calibração metrológica adotada em vários setores |
| \(M_\mu/M_e\) | A | Q39: espectro global regular em \(S^3\) |
| \(M_\tau/M_e\) | A | Q39: espectro global regular em \(S^3\) |
| \(M_p/M_e\) | A | Q40: \(6\pi^5+\alpha(3\pi/2+3/(4\pi^3))\) |
| \(M_n/M_e\) | A | Q40: \(M_p/M_e+\ln(2\pi^2)3\sqrt2/5\) |
| \(M_\Delta\) | A/C | Q40: rota estrutural via \(I_{\rm rot}=3M_pr_p^2/10\); espectro completo posterior |
| Massas fermiônicas gerais | D | dependem de Q28/Q29/Yukawas geométricos |

### Comentário

A GDQ não precisa gerar diretamente “0,511 MeV”. O que precisa gerar são razões
como:

\[
\frac{M_\mu}{M_e},
\qquad
\frac{M_\tau}{M_e},
\qquad
\frac{M_p}{M_e},
\qquad
\frac{M_n}{M_e}.
\]

Essas razões estão fechadas estruturalmente para léptons carregados e bárions
\(p,n\).

---

## 4. Constantes geométricas já estruturadas

| Quantidade | Status | Fórmula/Origem |
|---|---:|---|
| \(6\pi^5\) | A | volume de três câmaras bariônicas: \(3(2\pi^5)\) |
| \(\delta_B\) | A | cisalhamento torsional: \(\ln(2\pi^2)3\sqrt2/5\) |
| \(3\pi/2\) | A | holonomia de três estômatos |
| \(3/(4\pi^3)\) | A | garganta: \(3/(\mathrm{Vol}(S^3)\mathrm{Vol}(S^1))\) |
| \(1/8\) | A | projeção octante de Hopf |
| \(3/5\) | A | segundo momento radial \(\langle r^2/R^2\rangle_{\mathbb B^3}\) |
| \(3/4\) | A | projeção espacial de torção quaterniónica |

---

## 5. Constante de estrutura fina \(\alpha\)

Status:

\[
\boxed{\text{rota estrutural avançada; valor numérico ainda requer fechamento}}
\]

Classe:

\[
\boxed{\text{C/A parcial}}
\]

O arquivo `questão_37.md` contém uma rota geométrica para \(\alpha\), incluindo
a fórmula:

\[
\alpha
=
\frac{9}{8\pi^4}
\left(
\frac{\pi^5}{1920}
\right)^{1/4},
\]

com valor muito próximo do observado.

Contudo, o próprio diagnóstico exige cuidado:

1. `src/calculo_alpha_gdq.py` não deve ser usado como prova, pois injeta
   valor-alvo;
2. `src/calculo_alpha_gdq_2.py` não injeta diretamente o alvo, mas ainda
   precisa de derivação física completa dos fatores;
3. a rota oficial mais segura é tratar \(\alpha\) como acoplamento efetivo
   extraído da métrica espectral no espaço de conexões:

   \[
   \frac{1}{g_{\rm em}^2}=v_av_bG^{ab}_*.
   \]

Pendência para fechar como Classe A:

1. derivar \(G^{ab}_*\) do background Ricci--Bismut;
2. fixar a normalização do gerador eletromagnético;
3. obter \(\alpha\) sem seleção posterior de fatores;
4. esclarecer o papel de \(T^5\times S^3\) como cálculo global, sem trocar a
   ação oficial.

---

## 6. Escala de Cartan \(\Lambda_C\)

Status:

\[
\boxed{\text{estruturalmente identificada; valores setoriais numéricos ainda pendentes}}
\]

Classe:

\[
\boxed{\text{B/C}}
\]

A Q33 separa:

\[
\Lambda_C\neq\Lambda(\tau)\neq m_i.
\]

Onde:

1. \(\Lambda_C\) é escala geométrica de Cartan da camada efetiva;
2. \(\Lambda(\tau)=\tau^{-1/2}\) é escala de resolução do fluxo;
3. \(m_i\) são massas/autovalores físicos.

Pendência:

1. derivar numericamente \(\Lambda_C\) ou \(\Lambda_s\) da geometria de cada
   setor;
2. decidir em quais setores \(\Lambda_s=\Lambda_C\) e em quais setores há
   escala efetiva própria;
3. impedir a leitura errada de \(M_e\) ou \(1\,{\rm GeV}\) como corte UV
   universal duro.

---

## 7. Constante gravitacional \(G\)

Status:

\[
\boxed{\text{Fechada e Resolvida ab initio}}
\]

Classe:

\[
\boxed{\text{C/A parcial}}
\]

A Q38 fixou a origem correta:

\[
S_{\rm eff}\supset
C_R\int R[h]\sqrt{-h}\,d^4x,
\]

com:

\[
C_R=\frac{c^4}{16\pi G}.
\]

A GDQ fornece:

\[
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)}.
\]

Logo:

\[
\boxed{
G
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
}
\]

Pendência para Classe A completa:

1. avaliar \(\mathcal V_{\rm eff}^{(G)}\) no background real;
2. fixar \(\eta_R\);
3. derivar o limite de Poisson;
4. derivar os fatores \(\alpha^4\), \(\chi_{\rm Fano}\) e
   \(e^{1/(2\alpha)}\) sem pós-ajuste.

---

## 8. Acoplamento forte \(\alpha_s\)

Status:

\[
\boxed{\text{setor }SU(3)_C\text{ estruturado; valor efetivo presente; escala completa aberta}}
\]

Classe:

\[
\boxed{\text{C/A parcial}}
\]

O manuscrito contém proposta fenomenológica via Fredholm:

\[
\alpha_s^{\rm eff}
=
\frac{3}{8\pi}
\approx0{,}119366.
\]

Com a Q30, esse valor passa a ser interpretado como acoplamento efetivo do
modo/circuito interno de confinamento. Ele é compatível com a conexão:

\[
A_C\in\Omega^1(N,\mathfrak{su}(3))
\]

e com a normalização geométrica:

\[
\frac1{g_s^2}
=
\mathcal N_C
\int_{\mathcal I}\|\xi_C\|^2d\mu_g.
\]

Ainda não é:

\[
\alpha_s(\mu)
\]

como função de escala completa em uma tradução perturbativa externa.

Pendência:

1. avaliar numericamente as normas/rigidezes do setor de cor;
2. calcular \(\sigma\) no funcional de superfície confinante;
3. calcular \(\lambda_1\) da Hessiana confinante;
4. derivar \(\alpha_s(\mu)\) apenas se for desejada tradução perturbativa
   externa;
5. conectar \(\alpha_s^{\rm eff}=3/(8\pi)\) à escala/topologia hadrônica.

---

## 9. Acoplamentos eletrofracos \(g,g'\), \(\theta_W\), \(v\)

Status:

\[
\boxed{\text{estruturados por Q28/Q29; avaliação numérica pendente}}
\]

Classe:

\[
\boxed{\text{C}}
\]

Pendências:

1. avaliar \(g\) e \(g'\) como normas/rigidezes internas do fibrado
   em Q28;
2. calcular explicitamente o modo:

   \[
   \Phi_{\rm EW}\sim(1,2)_{1/2};
   \]

3. avaliar os coeficientes variacionais:

   \[
   S_{\rm eff}
   =
   S_0+\frac12a_2|\varphi|^2+\frac14a_4|\varphi|^4+\cdots;
   \]

4. obter:

   \[
   v^2=-\frac{2a_2}{a_4};
   \]

5. calcular:

   \[
   m_W=\frac{gv}{2},
   \qquad
   m_Z=\frac{v}{2}\sqrt{g^2+g'^2};
   \]

6. calcular:

   \[
   \tan\theta_W=\frac{g'}{g}.
   \]

Correção obrigatória:

\[
v_K\simeq72{,}85\,{\rm MeV}
\neq
246\,{\rm GeV}.
\]

Logo, \(v_K\) não deve ser usado como derivação da escala eletrofraca.

Comentário:

Q29 já resolveu a estrutura efetiva da quebra eletrofraca. O que ainda não foi
feito é o cálculo numérico de \(a_2,a_4,g,g'\) e das massas associadas.

---

## 10. Yukawas

Status:

\[
\boxed{\text{estrutura formulada; integrais de sobreposição pendentes}}
\]

Classe:

\[
\boxed{\text{C/D}}
\]

Rota esperada:

\[
y_{ij}
\sim
\int_{\mathcal I}
\bar\psi_i\Phi_{\rm EW}\psi_j\,d\mu_g.
\]

Pendência:

1. usar as representações fermiônicas estruturadas em Q28;
2. usar o modo \(\Phi_{\rm EW}\) estruturado em Q29;
3. calcular as integrais de sobreposição;
4. obter massas:

   \[
   m_f=\frac{y_fv}{\sqrt2}.
   \]

---

## 11. Constante \(f_B\) do setor CP forte

Status:

\[
\boxed{\text{setor CP forte fechado estruturalmente; normalização canônica numérica pendente}}
\]

Classe:

\[
\boxed{\text{A/C}}
\]

O manuscrito propõe:

\[
f_B
=
M_P
\sqrt{
\frac{3}{\sqrt{6\pi^5}}
}
\approx
6{,}44\times10^{17}\,{\rm GeV}.
\]

Interpretação:

origem na rigidez torsional e no volume de Kähler:

\[
V_K=6\pi^5.
\]

O adendo `q31/cp_forte_torcao_su3.md` fixa a arquitetura:

\[
\theta_{\rm eff}=\theta_0+\frac{a}{f_B},
\qquad
V(\theta)=\chi_{\rm top}^{\rm GDQ}(1-\cos\theta),
\qquad
m_B^2f_B^2=\chi_{\rm top}^{\rm GDQ}.
\]

Também fixa a supressão residual:

\[
|d_n|
\le
C_n|\theta_{\rm inicial}|
e^{-\kappa_{\rm CP}\chi_{\rm top}^{\rm GDQ}\tau_{\rm conf}}.
\]

Cálculo posterior:

1. conectar ao termo cinético canônico do modo \(a\);
2. decidir se \(a\) é modo propagante ou relaxacional;
3. calcular:

   \[
   m_a^2f_B^2=\chi_{\rm top}.
   \]
4. estimar EDM residual e regime cosmológico superamortecido.

---

## 12. Tempos, taxas e observáveis derivados

| Quantidade | Status | Observação |
|---|---:|---|
| \(\tau_n\) | C/D | depende de \(G_F\), \(g_A\) e fase espacial |
| \(\tau_p\) | A/C | \(\Gamma_p=0\) no setor topológico; \(S_{\rm inst}\) pendente se violação topológica |
| EDM do nêutron | A/C | supressão exponencial derivada; valor residual numérico pendente |
| fatores de forma bariônicos | A/C | estrutura definida; cálculo numérico e comparação experimental posteriores |
| espalhamento bariônico | C | potencial efetivo definido; fases parciais numéricas posteriores |

---

## 13. Resumo por classe

### Classe A — Derivadas estruturalmente

1. \(M_\mu/M_e\);
2. \(M_\tau/M_e\);
3. \(M_p/M_e\);
4. \(M_n/M_e\);
5. \(6\pi^5\);
6. \(\delta_B\);
7. \(3\pi/2\);
8. \(3/(4\pi^3)\);
9. \(1/8\), \(3/5\), \(3/4\) nos observáveis bariônicos;
10. estabilidade topológica do próton no setor conservativo.

### Classe B — Calibradas metrologicamente

1. \(M_e c^2\);
2. unidades MeV/GeV/fm;
3. massas absolutas após escolha de escala.

### Classe C — Estimativas ou estruturas parciais

1. \(\alpha\);
2. \(G\);
3. \(\Lambda_C\);
4. \(\alpha_s^{\rm eff}\);
5. \(f_B\);
6. fatores de forma numéricos;
7. tempos de decaimento.
8. estrutura condicional de \(g_s,g,g'\) como normas internas;
9. estrutura efetiva eletrofraca de Q29;
10. Yukawas como integrais de sobreposição.

### Classe D — Abertas

1. \(g_s(\mu)\) completo;
2. \(\theta_W\) numérico;
3. \(v=246\,{\rm GeV}\);
4. valores numéricos das Yukawas;
5. \(G_F\);
6. \(g_A\);
7. \(\chi_{\rm top}\) no setor forte efetivo.

---

## 14. Próxima ação recomendada

Q28 foi elevada a teorema condicional de índice:

\[
\boxed{
\text{fibrado interno, hipercarga, quiralidade e APS estruturados.}
}
\]

Ainda dependem do cálculo explícito das classes características, do
\(\eta\)-invariante e das normas internas:

1. Q31 no setor \(SU(3)_C\)/torsional apenas para \(\chi_{\rm top}\), \(f_B\)
   canônico e EDM residual;
2. Q34 está fechada estruturalmente; restam coeficientes locais e jacobianos
   em fundos não triviais;
3. Q35 está fechada estruturalmente no setor \(U(1)\); resta avaliar
   \(\Lambda_{\rm EM}\) numericamente;
4. acoplamentos eletrofracos;
5. Yukawas;
6. avaliação numérica de \(\sigma\), \(\lambda_1\) e \(g_s\) em Q30.

Q30 também foi consolidada estruturalmente:

\[
\boxed{
\text{conexão }SU(3)_C,\text{ Wilson loops, lei de área e gap positivo foram
encadeados no setor efetivo da GDQ.}
}
\]

Q31 também foi consolidada estruturalmente:

\[
\boxed{
\text{modo torsional, potencial periódico, relaxamento de Lyapunov e supressão
exponencial do EDM foram encadeados ao setor efetivo }SU(3)_C.
}
\]

Q32 também foi consolidada estruturalmente:

\[
\boxed{
\text{o propagador modificado foi derivado como }
e^{-\tau L_{\rm GDQ}^{(2)}}(L_{\rm GDQ}^{(2)})^{-1},
\text{ com }L_{\rm GDQ}^{(2)}=\tau^{-1}\mathcal O_{\rm Hess}^{(2)}.
}
\]

Q34 e Q35 foram reduzidas ao mesmo teste efetivo \(U(1)\):

\[
\boxed{
\Pi_{\mu\nu}^{(\tau)}(q)
=(q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2),
\qquad
q^\mu\Pi_{\mu\nu}^{(\tau)}=0.
}
\]

Q34 também foi estendida estruturalmente ao setor não abeliano:

\[
\boxed{
L_{A^g}=g^{-1}L_Ag
\Rightarrow
{\rm Tr}\,F_\tau(L_A)\text{ é gauge-invariante}
\Rightarrow
\mathcal S(\Gamma_\tau)=0.
}
\]

Esse teste foi executado em:

\[
\boxed{\texttt{q34/polarizacao\_U1\_heat\_kernel.md}}
\]

com:

\[
\boxed{
\Pi_\tau(\infty)=\frac{\alpha_0}{3\pi}E_1(\tau m^2),
\qquad
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}.
}
\]

Com a identificação setorial:

\[
\boxed{
\tau_{\rm EM}=\Lambda_{\rm EM}^{-2},
\qquad
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right).
}
\]

Q29 também foi consolidada estruturalmente:

\[
\boxed{
\text{modo }\Phi_{\rm EW},\text{ potencial efetivo, relações }m_W,m_Z,\theta_W
\text{ e Yukawas foram formulados.}
}
\]

O que falta em Q29 é avaliação numérica:

1. \(a_2,a_4\);
2. \(v\);
3. \(g,g'\);
4. \(\theta_W\);
5. integrais de Yukawa.

Portanto, a próxima etapa natural é:

\[
\boxed{
\text{avaliar }\Lambda_{\rm EM}\text{ e demais }\Lambda_s\text{ setoriais,
e avançar para extensões não abelianas, índices, normas, acoplamentos, gaps
e observáveis CP numéricos.}
}
\]
