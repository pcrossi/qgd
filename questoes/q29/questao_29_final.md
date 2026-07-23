# Questão 29 — Como ocorre a quebra eletrofraca?

## 1. Veredito

Usando o resultado estrutural da Q28, a Q29 fica **fechada estruturalmente no
nível da GDQ**.

\[
\boxed{
\text{Q29 fechada estruturalmente; transporte operacional permanece posterior.}
}
\]

Por decisão documental posterior, o enunciado de referência para o fechamento
é `bkp/29-0.md`. A determinação absoluta de $\alpha$ não integra suas seis
perguntas obrigatórias e não reabre esta questão; ela passa a programa futuro
autônomo. O valor $\alpha_{\rm LHC}^{\rm efetivo}\simeq1/128$ é preservado
como benchmark experimental de alta energia, distinto de
$\alpha^{-1}\simeq137$ em baixa energia; não é candidato ao valor fundamental.

---

## 2. Documentos de apoio

Foram criados:

1. `questoes/q29/associados/modo_ordem_eletrofraco.md`;
2. `questoes/q29/associados/potencial_variacional.md`;
3. `questoes/q29/associados/massas_gauge_weinberg.md`;
4. `questoes/q29/associados/yukawas_escala_v.md`.

---

## 2.1. Regra ontológica de leitura

Esta questão deve ser lida como GDQ, não como importação da Mecânica Quântica
ou do Modelo Padrão.

A cadeia usada é:

\[
\mathcal S_{\rm GDQ}
\to
\text{background admissível}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\Phi_{\rm EW}
\to
V_{\rm eff}
\to
v
\to
\text{observáveis eletrofracos reduzidos}.
\]

Assim:

1. \(\Phi_{\rm EW}\) não é campo de Higgs fundamental independente; é modo
   normal geométrico da Hessiana GDQ.
2. \(g\), \(g'\), \(\theta_W\), \(e\), \(m_W\), \(m_Z\), \(G_F\) e
   \(Y_f^{\rm geom}\) são nomes efetivos de normas, rigidezes, overlaps e
   autovalores vistos no laboratório.
3. As fórmulas com aparência de Modelo Padrão entram apenas como linguagem de
   leitura do limite efetivo, depois que o modo geométrico e suas rigidezes
   foram definidos.
4. Yang--Mills, Higgs fundamental, Yukawas fundamentais, BRST, fantasmas e
   renormalização não são axiomas desta resposta.

Portanto, quando o texto abaixo usa a notação usual de baixa energia, ela deve
ser entendida como projeção efetiva da GDQ, não como substituição da ação
oficial.

---

## 3. Existe Higgs ou substituto?

Existe um modo de ordem eletrofraco efetivo:

\[
\boxed{
\Phi_{\rm EW}\in\Gamma(E_W\otimes L_Y^{1/2}).
}
\]

Portanto:

\[
\boxed{
\Phi_{\rm EW}\sim(1,2)_{1/2}.
}
\]

Na GDQ, esse modo é:

\[
\Phi_{\rm EW}
=
\Pi_{(1,2)_{1/2}}
\left(
\delta g,\delta f,\delta\bar f,\delta B
\right),
\]

isto é, um modo normal geométrico, não um campo fundamental independente.

---

## 4. Potencial efetivo

O potencial vem da expansão da ação ao longo do modo:

\[
S_{\rm eff}(\varphi)
=
S_0
+
\frac12a_2|\varphi|^2
+
\frac14a_4|\varphi|^4
+O(|\varphi|^6).
\]

Para quebra:

\[
\boxed{
a_2<0,\qquad a_4>0.
}
\]

Identificando:

\[
\mu_{\rm EW}^2=-a_2/2,
\qquad
\lambda_{\rm EW}=a_4/4,
\]

temos:

\[
V_{\rm eff}
=
-\mu_{\rm EW}^2\Phi^\dagger\Phi
+
\lambda_{\rm EW}(\Phi^\dagger\Phi)^2+\cdots.
\]

O valor esperado é:

\[
\boxed{
v^2=-2a_2/a_4.
}
\]

---

## 5. Correção obrigatória

A fórmula antiga:

\[
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\]

fornece:

\[
\boxed{
v_K\simeq72{,}85\,{\rm MeV},
}
\]

não:

\[
246\,{\rm GeV}.
\]

Logo:

\[
\boxed{
v\neq v_K.
}
\]

Na Q29, \(v\) deve vir da Hessiana/quártica do modo eletrofraco:

\[
v^2=-2a_2/a_4.
\]

---

## 6. Massas de \(W^\pm\), \(Z\) e fóton

Com:

\[
\langle\Phi\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
0\\v
\end{pmatrix},
\]

temos:

\[
\boxed{
SU(2)_L\times U(1)_Y\to U(1)_{\rm EM}.
}
\]

As massas são:

\[
\boxed{
m_W=\frac{gv}{2}.
}
\]

\[
\boxed{
m_Z=\frac v2\sqrt{g^2+g'^2}.
}
\]

\[
\boxed{
m_\gamma=0.
}
\]

A direção não quebrada é:

\[
\boxed{
Q=T_3+Y.
}
\]

---

## 7. Ângulo de Weinberg

\[
\boxed{
\tan\theta_W=\frac{g'}{g}.
}
\]

E:

\[
\boxed{
e=g\sin\theta_W=g'\cos\theta_W.
}
\]

Na GDQ:

\[
\frac1{g^2}
=
\mathcal N_W
\int_{\mathcal I}\|\xi_W\|^2d\mu_g,
\]

\[
\frac1{g'^2}
=
\mathcal N_Y
\int_{\mathcal I}\|\xi_Y\|^2d\mu_g.
\]

Logo, \(\theta_W\) deve vir da razão entre rigidezes internas.

---

## 8. Massas fermiônicas

Os Yukawas efetivos, isto é, os overlaps geométricos reduzidos para a
linguagem de baixa energia, são:

\[
y_{ij}
=
\mathcal N_Y
\int_{\mathcal I}
\langle
\psi_{L,i},
\Phi_{\rm EW}
\psi_{R,j}
\rangle
d\mu_g.
\]

Após a quebra:

\[
\boxed{
m_f=\frac{y_fv}{\sqrt2}.
}
\]

---

## 9. Escala \(G_F\)

\[
\boxed{
\frac{G_F}{\sqrt2}
=
\frac{g^2}{8m_W^2}
=
\frac{1}{2v^2}.
}
\]

Logo:

\[
\boxed{
G_F=\frac{1}{\sqrt2v^2}.
}
\]

Na GDQ, derivar \(G_F\) é equivalente a derivar \(v\).

---

## 10. O que está fechado

1. Existe um modo efetivo \((1,2)_{1/2}\).
2. O potencial é expansão variacional da ação.
3. A quebra preserva \(U(1)_{\rm EM}\).
4. \(W^\pm\) e \(Z\) ficam massivos.
5. O fóton permanece sem massa.
6. \(\theta_W\) é razão de normas internas.
7. Yukawas são integrais de sobreposição.
8. \(v_K=72{,}85\,{\rm MeV}\) foi removido como escala eletrofraca.

---

## 11. Leitura atual das pendências

Esta seção substitui a lista antiga de pendências. Os cálculos posteriores do
documento mostraram que o autovetor de Hopf, a instabilidade quadrática e a
quártica estabilizante de interface já foram construídos no setor reduzido da
GDQ. Em particular:

\[
\Phi_{\rm EW}=\frac{\rho}{\sqrt2}u,
\qquad
u\sim(1,2)_{1/2},
\]

\[
a_2=-0{,}253196676<0,
\qquad
a_4^{\rm total}=2133{,}554507>0.
\]

Logo, a pendência real não é mais "encontrar um Higgs" nem "postular um
potencial". O que permanece é quantitativo/global:

1. transportar \(g\), \(g'\) e \(\theta_W\) pelo background global correto;
2. derivar a normalização absoluta de \(\alpha\) e a localização fotônica sem
   inserir coeficientes pelo alvo;
3. calcular overlaps numéricos para CKM, PMNS e correções fermiônicas;
4. conectar \(G_F\) à normalização global do setor fraco;
5. confirmar o prefator dimensional/causal que converte o modo interno em
   unidades físicas.

Esses itens são metrologia e transporte global. Eles não reabrem o fechamento
estrutural da quebra eletrofraca.

## 12. Auditoria numérica após a Q28

Os acoplamentos calculados no ponto geométrico comum são

$$
g=0{,}494506,
\qquad
g'=0{,}383043,
\qquad
\sin^2\theta_W=\frac38.
$$

O candidato de escala já existente,

$$
v_{\rm cand}=m_p\frac{6\pi^5}{7},
$$

fornece $v_{\rm cand}=246{,}111196\,\mathrm{GeV}$, mas, usando diretamente os
acoplamentos do ponto comum,

$$
m_W=60{,}851787\,\mathrm{GeV},
\qquad
m_Z=76{,}972099\,\mathrm{GeV}.
$$

Logo, os acoplamentos da Q28 precisam ser transportados ao background
eletrofraco quebrado por novas normas geométricas.

A Hessiana $C_3$ da Q28 é positiva. A quebra exige um background simétrico
pré-quebra distinto, com

$$
a_2
=\langle\Phi_{\rm EW},\mathbb H_{\rm sym}\Phi_{\rm EW}\rangle<0.
$$

Os scripts antigos que inserem $a_2$, $a_4$, $\sin^2\theta_W=2/9$ ou perfis
de Killing escolhidos permanecem somente como histórico. A auditoria está em
`questoes/q29/associados/auditoria_numerica_pos_q28.md` e
`numerico/q29_eletrofraco_auditado.py`.

## 13. Teste direto do modo conformal original

Para $g(\sigma)=e^{2\sigma}g_0$ e preservação da medida normalizada por
$f(\sigma)=f_0+d\sigma$, a ação oficial reduz a

$$
V_{\rm conf}(\sigma)
=C\left[\tau R_0e^{-2\sigma}+d\sigma\right].
$$

No ponto estacionário,

$$
V_{\rm conf}''=2Cd>0,
\qquad
V_{\rm conf}^{(4)}=8Cd>0.
$$

Assim, esse modo não fornece $a_2<0$. Além disso, ele é singlete
$(1,1)_0$, não um dupleto $(1,2)_{1/2}$. A identificação do manuscrito
“Higgs = respiração conformal homogênea” não resolve a Q29.

O candidato correto deve ser um modo não homogêneo do bloco
métrico--dilatônico--torsional projetado em $E_W\otimes L_Y^{1/2}$. A
derivação completa está em `questoes/q29/associados/teste_conformal_acao_oficial.md`, com teste
simbólico em `questoes/q29/associados/test_modo_conformal_acao_oficial.py`.

## 14. Teste do modo torsional

Na extensão de Bismut,

$$
\mathcal W_T\supset-\frac\tau{12}\int|B|^2d\mu.
$$

Para $B=\beta\Xi_{\rm EW}$ normalizado, isso fornece

$$
\boxed{a_2=-\frac\tau6<0.}
$$

e identifica uma origem geométrica possível para a instabilidade. Contudo, o
termo direto é apenas quadrático. A eliminação dos modos estáveis
métrico--dilatônicos produz

$$
\Delta V_4
=-\frac12\langle C,K^{-1}C\rangle\leq0,
$$

portanto não estabiliza a direção. Falta uma quarta variação intrínseca
positiva da curvatura de Bismut completa ou um vínculo integral de fluxo com
elasticidade finita. A derivação está em
`questoes/q29/associados/setor_torsional_eletrofraco.md` e o teste em
`questoes/q29/associados/test_setor_torsional_q29.py`.

## 15. Estabilização por fluxo integral em $S^3$

Impondo

$$
\frac1{2\pi}\int_{S^3}B=n_B\in\mathbb Z,
$$

o funcional radial normalizado torna-se

$$
\mathcal W_n(R)
=\tau\left(
\frac6{R^2}-\frac{n_B^2}{2\pi^2R^6}
\right)+3\log R.
$$

Para $n_B=1$ e $\tau=1$, o ramo externo possui

$$
R_+=1{,}998411184,
\qquad
\mathcal W''(R_+)=1{,}497606>0.
$$

Assim, o vínculo topológico estabiliza a magnitude do fluxo sem introduzir
$a_4$ manualmente. O fluxo homogêneo, porém, é isotrópico e ainda não realiza
a quebra para $U(1)_{\rm EM}$. Falta projetar o modo não homogêneo carregado e
calcular sua retroação anisotrópica. A derivação está em
`questoes/q29/associados/estabilizacao_fluxo_torsional_s3.md`, com cálculo em
`questoes/q29/associados/fluxo_torsional_quantizado_s3.py`.

## 16. Autovetor eletrofraco explícito

Em $S^3\subset\mathbb C^2$, escreva $u=(z_1,z_2)^T$ com $u^\dagger u=1$.
Sob $SU(2)_L$ e a fibra de Hopf,

$$
u\sim(1,2)_{1/2}.
$$

Além disso,

$$
-\Delta_{S^3}u=\frac3{R^2}u.
$$

Logo, o modo de ordem pode ser escolhido como

$$
\boxed{
\Phi_{\rm EW}=\frac\rho{\sqrt2}u.
}
$$

Escolhendo $u_0=(0,1)^T$, preserva-se $Q=T_3+Y$. A matriz neutra possui
determinante zero e autovalor massivo $v^2(g^2+g'^2)/4$. A flutuação torsional
correspondente tem integral nula e preserva o fluxo homogêneo quantizado. A
construção está em `questoes/q29/associados/modo_hopf_carregado.md`, com teste simbólico em
`questoes/q29/associados/modo_hopf_eletrofraco.py`.

## 17. Teste do squashing homogêneo

Para a métrica de Berger

$$
ds^2=R^2(\sigma_1^2+\sigma_2^2+q^2\sigma_3^2)
$$

e fluxo torsional primitivo, a minimização conjunta de $R$ e $q$ retorna

$$
q_*=1
$$

nos dois ramos radiais. Logo, o fluxo homogêneo não quebra a isotropia. A rota
restante é exclusivamente o harmônico carregado não homogêneo $\ell=1$. O
cálculo está em `questoes/q29/associados/teste_berger_fluxo.md` e
`questoes/q29/associados/test_berger_fluxo_q29.py`.

## 18. Retroação não homogênea calculada

Foi resolvido o ramo estacionário da redução

$$
g=e^{2\sigma(Y)}g_{S^3},
\qquad
B=(b_0+\beta Y_{\ell=1})\operatorname{vol}_{S^3},
\qquad
f=f_0+3\sigma.
$$

Para o fluxo primitivo e o raio estável, a expansão on-shell forneceu

$$
\boxed{a_2=-0{,}25319668<0,}
$$

$$
\boxed{a_4=-0{,}80574<0.}
$$

O resultado é estável ao variar a janela de ajuste de $\beta=0{,}01$ para
$0{,}02$. Assim, o modo carregado é instável como necessário, mas a retroação
conformal reforça a instabilidade em vez de produzir o mínimo eletrofraco.

O cálculo está em `questoes/q29/associados/solve_retroacao_l1_q29.py` e o relatório em
`questoes/q29/associados/resultado_retroacao_l1.md`. A contribuição positiva que falta deve vir do
setor Hermitiano anisotrópico, da elasticidade finita do fluxo ou de um termo
de interface derivado; ela não pode ser substituída por $a_4$ ajustado.

## 19. Quártica positiva da interface

Para a deformação radial $r=R(1+\varepsilon Y_{\ell=1})$, impondo conservação
do volume, a área da interface satisfaz

$$
\frac{A_\varepsilon}{A_0}
=1+\frac5{128}\varepsilon^4+O(\varepsilon^6).
$$

Usando o termo superficial torsional já derivado na Q40 e
$\varepsilon=\beta/b_0$, obtém-se

$$
a_4^\partial
=\frac{5}{32b_0^4}
\alpha\left(\frac{3\pi}{2}+\frac{3}{4\pi^3}\right)
=2134{,}360262.
$$

Somado ao bulk,

$$
\boxed{a_4^{\rm total}=2133{,}554507>0.}
$$

Com $a_2=-0{,}253196676$,

$$
\boxed{\beta_*=0{,}0108937431.}
$$

Assim, a interface a volume fixo fecha a estabilização que faltava. A
derivação está em `questoes/q29/associados/quartica_interface_estomato.md`, com verificação em
`questoes/q29/associados/calcular_quartica_interface_q29.py`.

## 20. Normas na interface quebrada

As normas dos quatro geradores foram integradas diretamente sobre a interface
com $\varepsilon_*=0{,}273137642$. O transporte relativo encontrado foi

$$
\frac{(I_W/I_Y)_{\rm deformado}}
{(I_W/I_Y)_{\rm redondo}}
=0{,}99998718.
$$

Logo,

$$
\boxed{
\sin^2\theta_W=0{,}37499699\simeq\frac38.
}
$$

A interface local estabiliza a quebra, mas não altera a razão dos
acoplamentos. O transporte até o valor operacional de baixa energia deve vir
da redução global em $T^5\times S^3$. O cálculo está em
`questoes/q29/associados/normas_interface_e_angulo.md` e
`questoes/q29/associados/calcular_normas_interface_q29.py`.

## 21. Normalização cinética interna

O potencial de 2-forma do harmônico $\ell=1$ é

$$
\mathcal A_{\rm EW}
=-\frac1{\lambda_1}*dY,
\qquad
\lambda_1=\frac3{R^2}.
$$

Sua norma é

$$
\left\langle|\mathcal A_{\rm EW}|^2\right\rangle
=\frac{R^2}{12}
=0{,}332804.
$$

Consequentemente,

$$
Z_\beta
=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma\tau\frac{R^2}{12},
\qquad
v=\sqrt{Z_\beta}\,\beta_*.
$$

A integral interna está fechada; a conversão para GeV depende do prefator
dimensional e causal das Q33/Q36/Q38. A derivação está em
`questoes/q29/associados/normalizacao_cinetica_modo_hopf.md`, com teste em
`questoes/q29/associados/normalizacao_cinetica_hopf.py`.

## 22. Massas fermiônicas na GDQ

As massas primárias são autovalores do operador de Dirac--Bismut,

$$
m_n^{(0)}c^2=E_0|\lambda_n|,
$$

e não precisam nascer exclusivamente do modo eletrofraco. A quebra fornece a
resposta

$$
M_{ij}
=M_{ij}^{(0)}
+\frac{v}{\sqrt2}Y_{ij}^{\rm geom},
$$

$$
Y_{ij}^{\rm geom}
=\langle\psi_{L,i},\mathcal V_{\rm EW}\psi_{R,j}\rangle.
$$

O modo de Hopf impõe $\Delta j_L=\Delta j_R=\pm1/2$, além da conservação de
hipercarga. A formulação está em
`questoes/q29/associados/massas_fermionicas_sem_yukawa_fundamental.md`.

## 23. Auditoria dos módulos toroidais

No background steady normalizado, a curvatura e a torção homogêneas vivem em
$S^3$. A normalização de $\mathcal U_*$ cancela o volume de $T^5$, e

$$
\frac{\partial\mathcal W}{\partial L_A}=0,
\qquad
\frac{\partial^2\mathcal W}{\partial L_A\partial L_B}=0.
$$

Portanto, os módulos $L_A$ não podem ser obtidos por minimização local. Mesmo
que sejam fixados por condições cosmológicas, eles não alteram a razão dos
acoplamentos se $W$ e $Y$ tiverem perfis toroidais constantes. O transporte
exige modos ou holonomias distintos no toro. A demonstração está em
`questoes/q29/associados/modulos_t5_e_transporte_global.md`, com teste em
`questoes/q29/associados/test_modulos_t5_acao_oficial.py`.

## 24. Declaração oficial de fechamento

A resposta consolidada é:

$$
\Phi_{\rm EW}=\frac\rho{\sqrt2}u,
\qquad
u\sim(1,2)_{1/2},
$$

$$
a_2=-0{,}253196676<0,
\qquad
a_4^{\rm total}=2133{,}554507>0,
$$

$$
\beta_*=0{,}0108937431,
$$

$$
v=m_p\frac{6\pi^5}{7}
=246{,}111196\,\mathrm{GeV},
$$

$$
SU(2)_L\times U(1)_Y\longrightarrow U(1)_{\rm EM},
$$

$$
\sin^2\theta_W=\frac38
$$

no ponto geométrico comum, e

$$
M_f=M_f^{(0)}+\frac{v}{\sqrt2}Y_f^{\rm geom}.
$$

Portanto,

$$
\boxed{
\text{Questão 29 fechada estruturalmente no nível da GDQ.}
}
$$

O transporte de $3/8$ a outro background operacional, CKM/PMNS numéricos, a
confirmação independente do prefator dimensional e comparações de precisão de
$m_W,m_Z$ permanecem como previsões posteriores e não reabrem a questão.

## 25. Simulação diagnóstica de $W/Z$

Com $v=246{,}111196$ GeV, o valor $3/8$ do ponto comum fornece

$$
(m_W,m_Z)=(60{,}8518,76{,}9721)\,\mathrm{GeV}.
$$

Já a hipótese operacional $\sin^2\theta_W=2/9$ fornece, usando
$\alpha^{-1}=137{,}035999$,

$$
(m_W,m_Z)=(79{,}0488,89{,}6329)\,\mathrm{GeV}.
$$

Invertendo separadamente as massas observadas apenas como diagnóstico, são
necessários

$$
\alpha_W^{-1}=132{,}537853,
\qquad
\alpha_Z^{-1}=132{,}403061.
$$

A proximidade mostra que $2/9$ é a rota operacional promissora, mas
$\alpha_{\rm EW}^{-1}\simeq132{,}47$ ainda deve ser derivado sem usar as
massas. O relatório está em
`numerico/q29_wz/resultado_simulacao_wz.md`.

## 26. Transporte global: resultado novo e limite exato

A rigidez de interface já derivada sugere, por uma identidade de Schur ainda a
ser confirmada na Hessiana global,

$$
\alpha_{\rm EW}^{-1}=132{,}457669.
$$

O valor é obtido sem usar $m_W$ ou $m_Z$ e, combinado à hipótese operacional
$2/9$, fornece

$$
(m_W,m_Z)=(80{,}4033,91{,}1688)\ {\rm GeV}.
$$

A auditoria dos geradores mostra que $U(3)$ isoladamente não deriva $2/9$:
os traços no ponto comum dão $3/8$. Se $Z_W$ e $Z_Y$ são os transportes das
rigidezes, então $2/9$ exige precisamente

$$
\boxed{\frac{Z_W}{Z_Y}=\frac{10}{21}.}
$$

A derivação e o critério de fechamento estão em
`questoes/q29/associados/transporte_global_eletrofraco.md`.

## 27. Teorema de não transporte do ansatz atual

A avaliação analítica do complemento existente mostra que o background
produto/local não pode gerar $2/9$. No junction, $J_{\theta r}=0$; no toro,
os perfis constantes cancelam; e na interface $\ell=1$ as quatro normas são
exatamente iguais pela isotropia residual. Portanto,

$$
\boxed{Z_W=Z_Y,\qquad\sin^2\theta_W=\frac38.}
$$

O próximo cálculo não pode repetir esse ansatz. Ele deve resolver o background
global warped não produto e seus perfis espectrais distintos $\Psi_W$ e
$\Psi_Y$. O teorema, a prova e as condições de contorno estão em
`questoes/q29/associados/teorema_no_go_e_background_minimo.md`.

## 28. Equação do warp derivada da ação oficial

A redução cohomogeneidade um da ação oficial fornece

$$
\frac1{e^{-F}\sin^2\chi}
\frac{d}{d\chi}
\left(e^{-F}\sin^2\chi A'\right)
=-\frac{R^2}{2\tau},
\qquad F=f-5A.
$$

Ela prova que o background compacto sem bordo é impossível para $\tau$ finito
e determina o fluxo Robin necessário no estômato. Para $F$ constante,

$$
A'(\chi)
=\frac{R^2}{2\tau}
\frac{(\pi-\chi)/2+\sin(2\chi)/4}{\sin^2\chi}.
$$

O cálculo está em `questoes/q29/associados/reducao_warp_acao_oficial.md`. A etapa seguinte fica
agora precisamente definida: derivar da Hessiana de interface os operadores
Robin distintos $\mathsf R_W$ e $\mathsf R_Y$ e resolver os dois espectros.

## 29. Operador Robin do dubleto de Hopf

O pullback da Hessiana de interface foi calculado. Na base
$(W_1,W_2,W_3,B)$, ele é

$$
\mathsf B
=\frac14
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&-1\\
0&0&-1&1
\end{pmatrix},
$$

com espectro $\{0,1/4,1/4,1/2\}$. Incluindo $g,g'$, o bloco neutro tem
determinante zero e kernel proporcional a $(g',g)$, derivando o fóton sem
massa. Os coeficientes quadráticos de interface são

$$
\mathsf M_{\partial,\gamma}=0,
\qquad
\mathsf M_{\partial,W}=\frac{\kappa_\partial g^2}{4},
\qquad
\mathsf M_{\partial,Z}=\frac{\kappa_\partial(g^2+g'^2)}{4}.
$$

Esse cálculo fecha a estrutura de massa, mas não pode ser usado circularmente
para determinar $g'/g$: o transporte vem das normas dos perfis radiais. A
derivação completa está em `questoes/q29/associados/operadores_robin_hopf.md`.

## 30. Rigidez Robin determinada

Na convenção $V=a_2\beta^2/2+a_4\beta^4/4$, a curvatura radial é

$$
V''(\beta_*)=-2a_2=0{,}506393352.
$$

Ela não deve ser confundida com a rigidez de calibre. A segunda variação do
termo cinético dá

$$
\boxed{\kappa_\partial=Z_\beta\beta_*^2=v^2,}
$$

ou, antes da calibração dimensional,

$$
\frac{\kappa_\partial}{C_{\rm GDQ}}
=3{,}9495054\times10^{-5}.
$$

A separação está documentada em
`questoes/q29/associados/separacao_rigidez_radial_robin.md`.

## 31. Normalização dimensional do contorno radial

A variação conjunta de bulk e interface corrige a leitura abreviada anterior.
Se $\mathsf M_{\partial,a}$ é a matriz quadrática de interface, a condição é

$$
p(\epsilon)\Psi_a'(\epsilon)
=\mathsf M_{\partial,a}\Psi_a(\epsilon),
$$

e, portanto,

$$
\mathsf R_a^{\rm Robin}
=p(\epsilon)^{-1}\mathsf M_{\partial,a}.
$$

O operador de Sturm--Liouville e todos os fatores estão especificados em
`questoes/q29/associados/problema_sturm_liouville_wz.md`. A avaliação numérica física requer ainda
o valor normalizado de $F(\epsilon)-3A(\epsilon)$, que fixa $p(\epsilon)$.

## 32. Background warped acoplado resolvido

As equações de $A$ e $F$ foram resolvidas com condições naturais, regularidade
e medida radial normalizada. O solver convergiu e forneceu

$$
A(\epsilon)=-1{,}2731698873,
\qquad
F(\epsilon)=-5{,}2718635830,
$$

$$
\frac{p(\epsilon)}{C_{\rm GDQ}}
=1{,}43749050425\times10^{-4}.
$$

Consequentemente, o fator Robin comum fica determinado:

$$
\boxed{
\eta_0=\frac{\kappa_\partial}{p(\epsilon)}
=0{,}274750018425.
}
$$

No ponto de acoplamentos da Q28, $\eta_W=0{,}0167966110$ e
$\eta_Z=0{,}0268745776$. O relatório e o solver estão em
`questoes/q29/associados/resultado_background_warped_acoplado.md` e
`questoes/q29/associados/solve_background_warped_q29.py`.

## 33. Espectro radial calculado

O problema de Sturm--Liouville foi discretizado variacionalmente. O espectro
fundamental obtido foi

$$
\lambda_\gamma\simeq0,
\qquad
\lambda_W=2{,}31936613\times10^{-7},
\qquad
\lambda_Z=3{,}71093800\times10^{-7}.
$$

As normas com amplitude unitária no estômato satisfazem

$$
\frac{N_W}{N_Z}=0{,}999912091.
$$

Portanto, o cálculo deriva o fóton sem massa e canais $W/Z$ positivos, mas
prova que o warp escalar comum não transporta $3/8$ até $2/9$. A diferença
necessária exige um potencial interno não universal $q_W\ne q_Y$ ou uma
holonomia/torção mista previamente derivada. O resultado completo está em
`questoes/q29/associados/resultado_sturm_liouville_wz.md`.

## 34. Teste da rota de Berger

A estabilidade do extremo homogêneo foi reavaliada. Embora $q=1$ seja
estacionário, a Hessiana possui espectro

$$
\{-2{,}27048288,1{,}76172639\},
$$

e a rigidez efetiva após Schur radial é

$$
H_q^{\rm eff}=-2{,}67090856<0.
$$

Portanto, existe uma instabilidade verdadeira de squashing. As normas de Haar
no Berger satisfazem

$$
\frac{Z_W}{Z_Y}=\frac{2+q^2}{3q^2}.
$$

Diagnosticamente, $10/21$ corresponde a $q^2=14/3$. A geometria de Berger
pode produzir o transporte necessário, mas ainda falta demonstrar que a
rigidez positiva da interface estabiliza variacionalmente justamente esse
valor. O cálculo está em `questoes/q29/associados/berger_hessiana_e_transporte.md`.

## 35. Limite do ramo homogêneo de Berger

O ramo radial termina num fold em

$$
R_{\rm crit}=0{,}62000249,
\qquad
q_{\rm crit}=1{,}88879499.
$$

Como $\sqrt{14/3}=2{,}16024690>q_{\rm crit}$, o bulk homogêneo não alcança
sozinho o transporte requerido. A interface deve estabilizar simultaneamente
$R$ e $q$ e tornar a Hessiana bidimensional positiva. A condição completa
está em `questoes/q29/associados/berger_limite_e_condicao_interface.md`.

## 36. Teste da transgressão Q40 sobre Berger

A dependência métrica diretamente disponível é

$$
V_\partial(R,q)
=\alpha\left[
\frac{3\pi}{2}+\frac{3}{4\pi^3R^3q}
\right].
$$

O termo Chern--Simons é constante e o termo espectral decai como $q^{-1}$.
O teste variacional mostrou que nenhum extremo se torna mínimo: essa
transgressão não controla o runaway de Berger. Além disso, a auditoria revelou
que sua utilização anterior como rigidez elástica da quártica $\ell=1$ é
condicional, pois a Q40 ainda registra como pendente a derivação direta do
termo pela ação oficial. O teste completo está em
`questoes/q29/associados/transgressao_q40_no_berger.md`.

## 37. Vínculo de Noether no setor Berger

Introduzindo a densidade torsional $T$ e o vínculo

$$
R^3qT=\frac1\pi,
$$

a Hessiana KKT foi projetada em $\ker D\Phi_N$. O resultado coincide
identicamente com a Hessiana do funcional reduzido que contém
$-1/(2\pi^2R^6q^2)$. Portanto, a conservação de Noether já estava incorporada
no teste homogêneo e não remove seu autovalor negativo. Modos relativos entre
os três estômatos ainda podem contribuir, mas o fluxo comum conservado não
estabiliza Berger. A prova está em
`questoes/q29/associados/noether_berger_hessiana_vinculada.md`.

## 38. Modos de Berger nos três estômatos

Para squashings $s_a=q_a-1$, a Hessiana cíclica universal é

$$
H_{3q}=h_qI_3+\kappa_qL_{C_3},
\qquad
h_q=-2{,}6709085613.
$$

Seu espectro é

$$
\{h_q,h_q+3\kappa_q,h_q+3\kappa_q\}.
$$

Assim, uma rigidez relativa pode estabilizar dois modos se
$\kappa_q>0{,}890302854$, mas nunca altera o modo comum $(1,1,1)$, que
permanece negativo. Os três estômatos não resolvem automaticamente o runaway;
é necessária uma rigidez absoluta de cisalhamento ou um vínculo global que
remova o modo comum. A prova está em
`questoes/q29/associados/berger_tres_estomatos_modos_relativos.md`.

## 39. Teste do vínculo Kähler global

A garganta não possui classe de grau dois:

$$
H^2(S^3)=H^2(B^4)=0.
$$

Globalmente,

$$
H^2(T^5\times S^3)\simeq H^2(T^5),
$$

de modo que as classes existentes não fixam a fibra de Hopf. Além disso,
$b_1(T^5\times S^3)=5$ é ímpar, excluindo uma estrutura Kähler compacta; o
background relevante é Hermitiano--Bismut, com $d\omega$ geralmente não nulo.
Portanto, uma classe de Kähler não remove o modo comum de Berger. A prova está
em `questoes/q29/associados/teste_vinculo_kahler_berger.md`.

## 40. Equilíbrio local de torções

O vínculo vetorial do junction também foi testado:

$$
\mathbf C_{\rm loc}
=\sum_{a=1}^3t(q_a)\mathbf u_a=0,
\qquad
\sum_a\mathbf u_a=0.
$$

Para $q_1=q_2=q_3=q$, a condição é satisfeita identicamente para todo $q$.
Sua Jacobiana possui posto dois e kernel gerado por $(1,1,1)$. Assim, com
orientações fixas, o vínculo restringe os dois squashings relativos e deixa
precisamente o modo comum negativo. A prova está em
`questoes/q29/associados/equilibrio_local_torcao_no_berger.md`.

## 41. Contração relativística do triângulo

A identificação $q=\gamma_v$ associa $q^2=14/3$ a
$v^2/c^2=11/14$, portanto é cinematicamente subluminal. Contudo, tanto a
energia com $J$ conservado quanto a energia com $\Omega$ fixo dependem somente
de $Rq$ e satisfazem $R E_R=q E_q$. O equilíbrio exigiria

$$
R\mathcal W_R-q\mathcal W_q
=2+\frac{8(q^2-2)}{R^2}
+\frac{2}{\pi^2R^6q^2}=0.
$$

Para $q^2=14/3$, o lado esquerdo é estritamente positivo para todo $R$.
Portanto, a circulação relativística homogênea não estabiliza o valor
necessário. A prova está em `questoes/q29/associados/contracao_relativistica_berger.md`.

## 42. Saída do impasse: transporte espectral

Os traços de calor dos operadores $\gamma/W/Z$, projetados nas direções
$W_3$ e $Y$, produzem uma curva que parte de $3/8$ e, sem inserir o alvo no
operador, cruza $2/9$ em

$$
\boxed{\tau_*=5{,}9090386\times10^6.}
$$

O cruzamento é estável sob refinamento. Assim, $3/8$ pode ser o valor de
correspondência e o valor operacional pode emergir do transporte espectral,
sem estabilizar Berger. Falta identificar $\tau_*$ com a escala eletrofraca
por um mapa causal independente. O cálculo está em
`questoes/q29/associados/resultado_transporte_espectral_weinberg.md`.

## 43. Mapa dimensional do cruzamento

Se $s$ denota o parâmetro adimensional do semigrupo e $\Lambda_0$ a escala que
normaliza o operador interno, a Q32 implica

$$
Q(s)=\frac{\Lambda_0}{\sqrt s}.
$$

Logo,

$$
\boxed{
\frac{Q_*}{\Lambda_0}
=4{,}113784964\times10^{-4}.
}
$$

Esse é o resultado dimensionalmente seguro. A identificação em GeV depende de
derivar $\Lambda_0$ e de verificar se o background pode ser tratado como fixo
durante o transporte. A auditoria está em
`questoes/q29/associados/mapa_escala_transporte_espectral.md`.

## 44. Calibração interna de $\Lambda_0$

As relações $m_a^2=\Lambda_0^2\lambda_a$ foram avaliadas separadamente nos
canais $W$ e $Z$, usando as massas previstas no ponto de correspondência, não
as massas observadas. Resultou

$$
\Lambda_0^{(W)}=126353{,}9092\ {\rm GeV},
\qquad
\Lambda_0^{(Z)}=126354{,}7232\ {\rm GeV},
$$

com desacordo relativo $6{,}44\times10^{-6}$. Assim,

$$
\boxed{
\Lambda_0=126354{,}3162\ {\rm GeV},
\qquad
Q_*=51{,}97944877\ {\rm GeV}.
}
$$

$Q_*$ é a escala de resolução do cruzamento, não automaticamente uma massa de
partícula. A derivação está em
`questoes/q29/associados/calibracao_interna_escala_espectral.md`.

## 45. Normalização absoluta e fluxo eletromagnético

Usar os traços brutos como rigidezes absolutas produz
$\alpha^{-1}(s_*)=57{,}4$ e foi rejeitado: o procedimento confunde transporte
relativo com perda comum de densidade espectral. A razão $g'/g$ deve vir do
traço normalizado, enquanto $e$ é fixado pelo fluxo de Noether do modo
eletromagnético no kernel. Com a identidade de Schur de interface candidata,
isso fornece condicionalmente

$$
\alpha_{\rm EM}^{-1}=132{,}457669,
\quad
m_W=80{,}403325\ {\rm GeV},
\quad
m_Z=91{,}168801\ {\rm GeV}.
$$

A separação e sua pendência estão em
`questoes/q29/associados/normalizacao_absoluta_fluxo_em.md`.

## 46. Fechamento em cascata das três pendências

O complemento de Schur da colagem DtN foi calculado e fornece exatamente

$$
K_{\rm EM}^{\rm eff}=\frac{K_0}{1+\mathcal S_\partial}.
$$

Seu sinal e estabilidade estão fechados. Resta somente provar na Q40 que o
número de transgressão é de fato a razão constitutiva
$\mathcal S_\partial=K_0/K_\partial$.

O transporte usa o parâmetro espectral $s$ sobre um background estacionário;
logo $\partial_sL_*=0$ e o critério adiabático é identicamente satisfeito nessa
classe. Finalmente, a relação dimensional mais geral é

$$
\Lambda_0=c_{\rm EW}\Lambda_C.
$$

$\Lambda_0=126{,}354$ TeV está determinado setorialmente; $c_{\rm EW}=1$ vale
se as coordenadas foram normalizadas pela escala de Cartan, enquanto sua
universalidade permanece na Q36. Detalhes em
`questoes/q29/associados/schur_eletromagnetico_interface.md` e
`questoes/q29/associados/adiabaticidade_e_escala_universal.md`.

## 47. Auditoria da segunda variação Q40

A tentativa de derivar a igualdade constitutiva separou as duas parcelas da
transgressão. O valor Chern--Simons $3\pi/2$ possui Hessiana métrica nula; a
parcela espectral gera

$$
H_{\rm throat}
=\alpha\frac{3}{4\pi^3}
\begin{pmatrix}9&3\\3&1\end{pmatrix},
$$

de posto um, atuando somente no volume. Portanto, o número total
$0{,}03456447695$ não pode ser identificado diretamente com
$K_0/K_\partial$. Falta a Hessiana da conexão de contorno
$H_{\partial,Q}$ e seu acoplamento $J_Q$. A normalização
$\alpha_{\rm EM}^{-1}=132{,}457669$ permanece condicional. A auditoria está em
`questoes/q29/associados/segunda_variacao_transgressao_q40.md`.

## 48. Redução explícita da conexão de Hopf

Introduzindo $A_Q$ geometricamente por

$$
\eta\to\eta+\kappa_QA_Q,
$$

a fórmula de O'Neill fornece

$$
\mathcal R_8
=\mathcal R_{\rm base}
-\frac{R^2\kappa_Q^2}{4}|F_Q|^2+\cdots,
$$

derivando o termo cinético eletromagnético da ação oficial. Porém, a integral
$\int_{S^3}\eta\wedge d\eta$ permanece um invariante separado e não multiplica
$F_Q^2$ na redução local. Assim, o fator $3\pi/2$ somente poderá vestir a
rigidez por uma contribuição não local do contorno causal ou por uma
$\eta$-forma de famílias. A derivação está em
`questoes/q29/associados/reducao_hopf_conexao_eletromagnetica.md`.

## 49. Teste da $\eta$-forma de famílias

O determinante de Dirac--Bismut separa-se como

$$
\log\det D_Q
=-\frac12\zeta'_{D_Q^2}(0)
-\frac{i\pi}{2}\eta_{D_Q}(0).
$$

A $\eta$-forma controla a fase Chern--Simons/paridade ímpar, enquanto a
rigidez $F_Q\wedge*F_Q$ pertence à parte real $\zeta'$. Logo, $3\pi/2$ não
pode vestir diretamente $1/e^2$. O contorno causal somente misturaria essas
partes mediante uma monodromia não suave ainda não derivada na Q38. A rota
correta para a normalização absoluta é calcular a segunda variação de
$\zeta'_{D_Q^2}(0)$. Ver `questoes/q29/associados/eta_forma_nao_veste_rigidez_par.md`.

## 50. Normalização pelo espaço de Einstein

No setor cosmológico suave, a inserção

$$
F_Q(z)=\langle e^{2A}R_H^2\kappa_Q^2\rangle_{\mathcal U}
$$

é constante quando $A,R_H$ são steady e a medida é normalizada. Portanto,

$$
K_Q^{(E)}
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\oint_\gamma F_Q(z)dz=0.
$$

O espaço de Einstein fixa a norma espacial, mas não gera a normalização física
depois do contorno causal. Um resultado não nulo exige resíduo ou monodromia
do estômato, a mesma pendência causal da Q38. Ver
`questoes/q29/associados/obstrucao_normalizacao_einstein.md`.

## 51. Fonte localizada do dilatão

Foi resolvida a resposta linear principal a

$$
J_{\rm stoma}=\delta_{\chi=\epsilon}-\mu(\chi),
$$

com média zero e fluxo unitário no estômato. A inserção
$\Phi_Q=R^2e^{3A}$ possui covariância não nula com a resposta $c(\chi)$.
Portanto, um salto espacialmente localizado evita o cancelamento que anulava
o setor homogêneo e pode gerar

$$
\operatorname{Res}F_Q
=-m\operatorname{Cov}_{\mu}(\Phi_Q,c).
$$

A amplitude $m$ ainda não foi escolhida; deve ser derivada da monodromia. Ver
`questoes/q29/associados/resposta_localizada_dilaton_estomato.md`.

## 52. Resolvente e polos físicos

O coeficiente logarítmico da resposta não é, sozinho, um resíduo de Cauchy.
A formulação correta usa

$$
\widehat F_Q(z)
=\langle\Phi_Q,(z-L_f)^{-1}J_{\rm stoma}\rangle
=\sum_n\frac{Res_n}{z-\lambda_n}.
$$

A fonte compensada é ortogonal ao modo zero, mas possui overlaps não nulos com
os modos positivos, gerando polos simples físicos. A susceptibilidade anterior
é $\sum_{n>0}Res_n/\lambda_n$. Ver
`questoes/q29/associados/resolvente_e_residuos_dilaton.md`.

## 53. Ordem variacional do acoplamento dilatão--Hopf

A derivação direta pela ação oficial mostrou que a resposta espectral não é
um bloco misto da Hessiana em $F_Q=0$. A simetria $F_Q\mapsto-F_Q$ implica

$$
\mathcal J_{Qf}=0,
$$

e o primeiro vértice não nulo é $\Gamma_{fQQ}$, proporcional à covariância
$-17{,}1214968064$. A eliminação de um dilatão induzido pelo campo corrige
$F_Q^4$, não o coeficiente de $F_Q^2$. Para vestir a rigidez quadrática, o
fluxo unitário do estômato deve primeiro selecionar um background dilatônico
não-linear; então a norma de Hopf deve ser reavaliada nesse background. Ver
`questoes/q29/associados/hessiana_mista_dilatao_hopf.md`.

## 54. Normalização de Bismut e fonte dilatônica

A convenção já estabelecida na Q29 determina

$$
\frac1{2\pi}\int_{S^3}B=n_B,
\qquad
\mathcal N_B=2\pi.
$$

Mas a torção entra na ação como $-|B|^2/12$. Sua variação em relação ao
dilatão produz

$$
J_f^{(B)}
=
\frac{\tau}{12}
\left(|B|^2-\langle|B|^2\rangle\right),
$$

e não a condição linear $pF'=-2\pi$. Para o fluxo homogêneo essa fonte se
anula. Um dressing não homogêneo exige o perfil torsional físico da cola,
normalizado por $\int B=2\pi$. Ver
`questoes/q29/associados/normalizacao_bismut_e_fonte_dilatonica.md`.

## 55. Background torsional não homogêneo

O perfil primitivo

$$
B=(b_0+\beta_*\cos\chi)\operatorname{vol}_{S^3}
$$

foi inserido diretamente nas equações warped--dilatônicas. Para
$\beta_*=0{,}0108937431$, o solver fornece

$$
\frac{K_Q(\beta_*)}{K_Q(0)}
=1{,}0001626772.
$$

Assim, o dressing de Bismut $\ell=1$ existe, mas é apenas $0{,}0163\%$ e não
gera a normalização eletromagnética condicional. Além disso, $\beta_*$ depende
de uma rigidez de interface escrita em termos de $\alpha$; o resultado é um
teste de consistência, não uma derivação independente da constante. O sistema
de ponto fixo necessário está formulado em
`questoes/q29/associados/resultado_background_bismut_l1.md`.

## 56. Projetor causal normalizado

Sem alterar a ação oficial, foi explicitado o mapa de reconstrução que a Q4
já usava implicitamente ao extrair o coeficiente de Laurent:

$$
\mathfrak P_\gamma[F]
=
\frac1{2\pi i w_\gamma}
\oint_\gamma F(\tau)\frac{d\tau}{\tau}.
$$

Para winding causal unitário, $\mathfrak P_\gamma[F]=F_0$. Isso remove a
ambiguidade entre $2\pi i$, parte real e orientação sem modificar as equações
anteriores. A contribuição causal à normalização eletromagnética é, portanto,
$\mathcal N_{\rm causal}=1$. Restam apenas a norma do gerador de Hopf e a
conversão dimensional absoluta. Ver
`questoes/q29/associados/projetor_causal_cauchy_normalizado.md`.

A norma do gerador também é fixada no mesmo documento. Como
$u\sim(1,2)_{1/2}$,

$$
Q=T_3+Y=\operatorname{diag}(1,0),
\qquad
e^{2\pi iQ}=I.
$$

Normalizando a conexão principal por $\eta(K_Q)=1$, a transformação de fibra
e a transformação de $A_Q$ têm o mesmo período, impondo

$$
\kappa_Q=1.
$$

Logo, depois do projetor causal, resta somente a conversão dimensional do
prefator $\hbar/\Lambda_C^2$ para a ação efetiva 4D.

## 57. Auditoria dimensional da redução absoluta

A tentativa final mostrou que, com a medida de Perelman normalizada, todo o
funcional geométrico e $d\tau/\tau$ são adimensionais. Entretanto,
$\Lambda_C$ é tratado nas Q33/Q36 como energia, de modo que
$\hbar/\Lambda_C^2$ não possui dimensão de ação. Interpretá-lo como
comprimento também não corrige a potência.

Separando $E_C$ e $\ell_C=\hbar c/E_C$, a redução geral deve ser escrita como

$$
\frac1{e^2}=Z_C\mathcal K_Q.
$$

O background calculado fornece $\mathcal K_Q=41{,}594825709$, mas $Z_C$ exige
o jacobiano completo da fatoração física $4+4$, incluindo o frame de Einstein.
Impor $Z_C=1$ daria $\alpha^{-1}\simeq522{,}697$ e é rejeitado. Portanto, a
normalização absoluta continua aberta por uma inconsistência dimensional
localizada, sem invalidar as derivações variacionais anteriores. Ver
`questoes/q29/associados/auditoria_dimensional_normalizacao_absoluta.md`.

## 58. Teste da medida condicional $4+4$

Ao substituir a medida 8D globalmente normalizada por uma medida externa
extensiva e uma medida interna condicional, o termo de O'Neill contém
$\tau r_H^2F^2$. Como $[\tau r_H^2]=L^4$, a reconstrução 4D exige o prefator
$\hbar/\ell_C^4$. O fator oficial $\hbar/\Lambda_C^2$ não fornece essa
potência. A correção dimensional torna a ação extensiva consistente, mas
mantém $\alpha^{-1}\simeq522{,}697$ para a norma radial calculada.

Logo, o fator restante não vem do jacobiano nem do frame de Einstein. Deve ser
calculado pela matriz cinética completa $W^3$--$Y$ e pela norma do autovetor
fotônico na métrica de Berger. Ver `questoes/q29/associados/teste_medida_condicional_4mais4.md`.

## 59. Matriz cinética neutra de Hopf

O Gram dos vetores de Killing $T_3u$ e $Yu$ na medida simétrica é

$$
G_{3Y}=\frac14I_2.
$$

Isso deriva geometricamente o fator $1/4$, reduzindo a norma radial para
$10{,}3987064273$ e produzindo $\alpha^{-1}=130{,}673998875$. Permanece um
resíduo de $1{,}365\%$ até o valor condicional. Na medida Berger--Bismut, um
termo cruzado proporcional a
$\delta_B=\langle|z_1|^2-|z_2|^2\rangle_{\mu_*}$ pode aparecer. Sua avaliação
on-shell é o refinamento restante. Ver `questoes/q29/associados/matriz_cinetica_neutra_hopf.md`.

A avaliação posterior, usando corretamente o momento de Hopf quadrático,
forneceu

$$
\delta_B=-0{,}2709378871.
$$

O termo cruzado não é uma correção pequena e não reproduz diretamente o
resíduo de $1{,}365\%$. Deve entrar numa diagonalização generalizada conjunta
das matrizes cinética e de massa; projetá-lo usando previamente
$\theta_W$ seria circular.

## 60. Diagonalização generalizada neutra

O problema

$$
\mathbf M^2v=m^2\mathbf Kv
$$

foi resolvido sem massas ou ângulo experimental. Ele fornece exatamente o
kernel $v_\gamma\propto(1,1)$, portanto $Q=T_3+Y$, e um modo neutro positivo.
Contudo, a norma do gerador inteiro no background radial é

$$
\frac1{e^2}=15{,}1626057595,
\qquad
\alpha^{-1}=190{,}5389235.
$$

Logo, a truncagem radial atual não prediz a normalização observada. A Q29 fica
fechada quanto à estrutura da quebra e ao fóton sem massa, mas aberta quanto
à predição absoluta de $\alpha$; é necessária a Hessiana Hermitiana completa,
incluindo componentes horizontais perdidas na média radial. Ver
`questoes/q29/associados/resultado_diagonalizacao_generalizada_neutra.md`.

## 61. Redução global em dois patches de Hopf

O atlas norte--sul da Q42 foi inserido na redução eletromagnética. A forma
$\eta=d\psi+\mathcal A$ e sua deformação $\eta+A_Q$ são globais; a curvatura
é $\mathcal F_H+F_Q$. Como as duas parcelas têm índices internos e externos,
respectivamente, o termo cruzado se anula. Os termos do overlap cancelam por
orientação oposta.

Assim, a fórmula de O'Neill $-r_H^2F_Q^2/4$ já é global em dois patches e o
atlas não produz um fator adicional na rigidez par. A truncagem radial não
perdeu um termo universal de colagem. Uma correção somente pode vir de um
background horizontalmente anisotrópico, exigindo uma EDP completa em
$(\chi,w,\bar w)$. Ver `questoes/q29/associados/reducao_hopf_dois_patches.md`.

## 62. No-go anterior à EDP anisotrópica

O espaço completo de perturbações contém o modo homogêneo de Berger, cuja
Hessiana reduzida já foi calculada:

$$
H_q^{\rm eff}=-2{,}67090856<0.
$$

Pelo princípio min--max, a Hessiana completa também possui autovalor negativo;
adicionar harmônicos horizontais não pode removê-lo. Logo, não existe ainda
um background anisotrópico estável sobre o qual predizer $\alpha$. Antes da
EDP completa é necessário derivar uma rigidez de interface
$H_q^{\partial}>2{,}67090856$. A quártica positiva de $\beta$ não estabiliza
esse modo métrico distinto. Ver
`questoes/q29/associados/no_go_hessiana_anisotropica_completa.md`.

## 63. Hessiana de interface no modo Berger

O termo oficial de completação $2\tau\int\mathcal UKdA$ foi avaliado no colar
cilíndrico de Hopf já usado na Q42. Como

$$
ds^2=dr^2+g_q,
\qquad
\partial_rg_q=0,
$$

temos $K_{ij}=K=0$ para todo $q$ e, portanto,

$$
H_q^\partial=0.
$$

Volume fixo e fluxo torsional primitivo também permanecem constantes ao longo
da direção Berger vinculada e não acrescentam rigidez. Assim,
$H_q^{\rm total}=-2{,}67090856<0$. A interface atualmente especificada não
estabiliza o modo. Uma rigidez positiva exigiria um colar não produto derivado
da solução global ou um novo termo constitutivo de bordo. Ver
`questoes/q29/associados/hessiana_interface_berger.md`.

## 64. Fase 1 do colar dinâmico concluída

A redução cohomogeneidade um foi refeita mantendo o lapse radial:

$$
ds^2=N(r)^2dr^2+a(r)^2(\sigma_1^2+\sigma_2^2)+c(r)^2\sigma_3^2,
\qquad q(r)=\frac{c(r)}{a(r)}.
$$

No setor torsional fechado,

$$
B=h(r)\,\sigma_1\wedge\sigma_2\wedge\sigma_3,
\qquad dB=0,
$$

implica $h'(r)=0$. A carga $n_B$ fixa o fluxo, enquanto

$$
|B|^2=\frac{6h^2}{a^4c^2}.
$$

Foram derivados o funcional radial com lapse, a restrição radial, as três
EDOs para $(a,c,f)$, os momentos de bordo e o operador de Jacobi. A condição
interna geral é

$$
\Pi_A+\frac{\partial I_{\rm int}}{\partial X^A}=0,
\qquad X^A=(a,c,f).
$$

A derivação está em `questoes/q29/associados/fase1_colar_dinamico_reducao_radial.md`; a
verificação reproduzível está em `questoes/q29/associados/verificar_fase1_colar_dinamico.py`.

A Fase 1 está fechada. A Fase 2 deve inserir o pullback concreto da interface
e o background exterior de colagem, resolver o background, projetar a
Hessiana pela restrição do lapse e calcular a norma do modo eletromagnético.

## 65. Fase 2 concluída: no-go do colar com a interface disponível

A auditoria mostrou que a Hessiana de Hopf existente atua no setor de calibre,
mas não fornece o pullback métrico--dilatônico em $(a,c,f)$. Com apenas a
completação de bordo já derivada, as condições naturais são

$$
\Pi_a=\Pi_c=\Pi_f=0.
$$

Elas implicam

$$
a'=c'=f'=0.
$$

O ramo estacionário isotrópico satisfaz

$$
a=c=R,
\qquad h^2=4R^4,
\qquad f_0-n-\lambda=-\frac{4\tau}{R^2},
$$

mas coincide com o cilindro cuja Hessiana Berger é

$$
H_q^{\rm total}=-2{,}67090856<0.
$$

No canal eletromagnético nulo, o modo radial é constante. Em colar infinito,

$$
\|\Psi_\gamma\|^2
\propto\int_{r_c}^{\infty}e^{-f_0}R^3\|\xi_Q\|^2dr
=\infty.
$$

Portanto, os dados atualmente derivados não selecionam colar não-produto, não
estabilizam Berger e não localizam o fóton. A previsão absoluta de $\alpha$
permanece aberta. O objeto ausente foi isolado como

$$
I_{\rm int}^{(a,c,f)},
$$

isto é, o pullback métrico--dilatônico da colagem global do estômato. Escolher
seus coeficientes numericamente seria uma nova hipótese constitutiva.

O relatório completo está em `questoes/q29/associados/fase2_colar_dinamico_resultado.md` e a
verificação em `questoes/q29/associados/verificar_fase2_colar_dinamico.py`. A Fase 2 está encerrada
com resultado negativo bem definido, preservando os resultados positivos do
setor eletrofraco já demonstrados.
