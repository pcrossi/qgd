# Faltas e trabalhos posteriores

Este documento registra os pontos que não devem ser tratados como fechados
ainda. A finalidade é separar o que já foi consolidado do que precisa de
trabalho futuro.

---

## 1. Questão 28 — Grupo efetivo do Modelo Padrão

Status atualizado:

$$
\boxed{
\text{contagem e estabilidade do background }C_3\text{ gaussiano fechadas}
}
$$

O índice APS local unitário, o kernel tangencial, o preenchimento, a colagem
$\mathbb Z_6$, as hipercargas e a transmissão da carga global foram
calculados. A relação consolidada é

$$
\boxed{
N_G=\frac A6.
}
$$

A seleção torsional local do junction elementar fornece três estômatos sem
usar o número observado. Pela aditividade APS e pela colagem $\mathbb Z_6$,

$$
N=3
\Longrightarrow
\operatorname{Ind}=3
\Longrightarrow
A=18
\Longrightarrow
N_G=3.
$$

A análise consolidada está em:

\[
\texttt{questão\_28\_final.md}
\]

com os blocos:

1. `q28/fibrado_interno_efetivo.md`;
2. `q28/espectro_hipercarga_anomalias.md`;
3. `q28/indice_tres_geracoes.md`;
4. `q28/classes_caracteristicas_hipercarga.md`;
5. `q28/quiralidade_aps_bismut.md`;
6. `q28/eta_borda_estomatos.md`.
7. `q28/hessiana_espectral_completa_background_c3.md`;
8. `q28/acoplamentos_geometricos_finais.md`.

### Resolvido estruturalmente

1. O fibrado interno efetivo foi definido:

   \[
   E_{\rm int}=E_C\oplus E_W\oplus L_Y.
   \]

2. O setor de cor foi associado a:

   \[
   E_C\simeq\mathbb C^3,
   \qquad
   U(3)\to SU(3)_C
   \]

   por preservação de volume complexo das três câmaras/folhas internas.

3. O setor fraco foi associado a:

   \[
   E_W\simeq\mathbb C^2,
   \qquad
   U(2)\to SU(2)_L
   \]

   com seleção quiral por:

   \[
   P_L=\frac12(1-\Gamma_{\rm GDQ}).
   \]

4. A hipercarga foi associada à linha complexa:

   \[
   L_Y\to N.
   \]

5. O grupo global foi estruturado como:

   \[
   G_{\rm eff}^{\rm global}
   =
   \frac{
   SU(3)_C\times SU(2)_L\times U(1)_Y
   }{\Gamma},
   \qquad
   \Gamma\subseteq\mathbb Z_6.
   \]

6. Os geradores de \(SU(3)\) foram ligados aos potenciais de Killing do
   manuscrito:

   \[
   \partial_aP_A=i\,g_{a\bar b}\xi_A^{\bar b},
   \qquad
   \{P_A,P_B\}_{\rm Poisson}=f_{ABC}P_C.
   \]

7. A conexão efetiva foi decomposta como:

   \[
   A_\mu
   =
   G_\mu^aT_a
   +
   W_\mu^it_i
   +
   B_\mu Y.
   \]

8. A geração efetiva foi escrita como fibrado:

   \[
   \mathcal E_{\rm gen}
   =
   (E_C\otimes E_W\otimes L_Y^{1/6})
   \oplus
   (E_C^*\otimes L_Y^{-2/3})
   \oplus
   (E_C^*\otimes L_Y^{1/3})
   \oplus
   (E_W\otimes L_Y^{-1/2})
   \oplus
   L_Y.
   \]

   Isto corresponde a:

   \[
   (3,2)_{1/6}
   \oplus
   (\bar3,1)_{-2/3}
   \oplus
   (\bar3,1)_{1/3}
   \oplus
   (1,2)_{-1/2}
   \oplus
   (1,1)_1.
   \]

9. As hipercargas foram vinculadas ao quociente global:

   \[
   z_3^{t(R_3)}
   z_2^{p(R_2)}
   e^{i2\pi Y}
   =
   1.
   \]

10. O índice relevante foi formulado:

   \[
   \operatorname{Ind}(\slashed D_{B,A}^{+})
   =
   \int_{\mathcal I}
   \widehat A(T\mathcal I)
   \operatorname{ch}(E_{\rm int})
   +
   \eta_{\partial}.
   \]

11. A antiga identificação por números de Hodge foi descartada por não estar
    definida no background real $T^5\times S^3$. A rota calculada é:

   $$
   N_{\rm ger}=\frac A6.
   $$

12. A borda APS dos estômatos foi formulada com operador tangencial:

   \[
   \mathcal D_a
   =
   \slashed D_{\partial_a}
   +
   \frac18B_{ijk}^{(a)}\gamma^{ijk}
   -iA_i^{(a)}\gamma^i.
   \]

13. O \(\eta\)-invariante local foi definido:

   \[
   \eta_a(s)
   =
   \sum_{\lambda_{a,k}\ne0}
   \operatorname{sign}(\lambda_{a,k})
   |\lambda_{a,k}|^{-s}.
   \]

14. O número geracional local foi escrito como:

   \[
   n_a
   =
   -\frac12
   \left(
   \eta_a(0)+h_a
   \right),
   \qquad
   N_{\rm ger}=\sum_{a=1}^{3}n_a.
   \]

15. O cancelamento de anomalias foi verificado para o espectro de uma geração.

16. A Hessiana física do background estacionário $C_3$ gaussiano foi
    calculada. Depois dos vínculos e da remoção de gauge,

    $$
    \lambda_{\min}
    =\min\left\{
    \frac32\kappa_{\rm rel}T^2,
    \frac1{2\tau}
    \right\}>0.
    $$

17. As normas do fibrado forneceram, no ponto geométrico comum,

    $$
    I_3=I_2=2,
    \qquad
    I_Y=\frac{10}{3},
    $$

    $$
    g_s=g,
    \qquad
    \frac{g'^2}{g^2}=\frac35,
    \qquad
    \sin^2\theta_W=\frac38.
    $$

    Com a normalização eletromagnética adotada,

    $$
    g_s^{\rm match}=g=0{,}494506,
    \qquad
    g'=0{,}383043.
    $$

### Forma condensada do resultado

Na classe estacionária $C_3$ gaussiana construída, o fibrado
$E_{\rm int}=E_C\oplus E_W\oplus L_Y$, a seleção quiral de Bismut, a colagem
APS e o equilíbrio torsional fornecem:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3\,\mathcal E_{\rm gen}
}
\]

e as anomalias cancelam.

### Trabalho auxiliar posterior

1. Avaliar $c_3(E_C)$ em ciclos globais adicionais, caso seja necessário para
   observáveis posteriores. Isso não integra os quesitos de `28-0.md` e não
   reabre a Q28.

### Observação final

Q28 não deve voltar à busca do número três, à Hessiana do background $C_3$
gaussiano nem aos acoplamentos no ponto comum, já calculados. Permanecem apenas
classes globais auxiliares e previsões quantitativas das questões posteriores.

---

## 2. Questão 29 — Quebra eletrofraca

Status:

\[
\boxed{\text{fechada de acordo com o enunciado de \texttt{bkp/29-0.md}}}
\]

O fechamento responde às seis perguntas da Q29: substituto geométrico do
Higgs, potencial efetivo, massas de $W^\pm$, $Z$ e fóton, ângulo de Weinberg,
mecanismo de massa fermiônica e definição da escala $v$. A determinação
absoluta de $\alpha$ não pertence ao enunciado de `bkp/29-0.md` e, portanto,
não reabre a Q29.

A resposta consolidada está em:

\[
\texttt{questão\_29\_final.md}
\]

com os blocos:

1. `q29/modo_ordem_eletrofraco.md`;
2. `q29/potencial_variacional.md`;
3. `q29/massas_gauge_weinberg.md`;
4. `q29/yukawas_escala_v.md`.

### Resolvido estruturalmente

1. Usando o resultado estrutural da Q28, o modo de ordem eletrofraco foi definido
   como:

   \[
   \Phi_{\rm EW}\in\Gamma(E_W\otimes L_Y^{1/2}),
   \qquad
   \Phi_{\rm EW}\sim(1,2)_{1/2}.
   \]

2. O modo foi interpretado como projeção geométrica:

   \[
   \Phi_{\rm EW}
   =
   \Pi_{(1,2)_{1/2}}
   (\delta g,\delta f,\delta\bar f,\delta B).
   \]

3. O potencial foi estruturado como expansão variacional:

   \[
   S_{\rm eff}(\varphi)
   =
   S_0
   +
   \frac12a_2|\varphi|^2
   +
   \frac14a_4|\varphi|^4
   +O(|\varphi|^6),
   \]

   \[
   a_2<0,\qquad a_4>0.
   \]

4. O valor esperado foi definido por:

   \[
   v^2=-2a_2/a_4.
   \]

5. A quebra preserva:

   \[
   Q=T_3+Y,
   \]

   logo:

   \[
   SU(2)_L\times U(1)_Y\to U(1)_{\rm EM}.
   \]

6. As massas gauge foram recuperadas:

   \[
   m_W=\frac{gv}{2},
   \qquad
   m_Z=\frac v2\sqrt{g^2+g'^2},
   \qquad
   m_\gamma=0.
   \]

7. O ângulo de Weinberg foi definido por:

   \[
   \tan\theta_W=\frac{g'}{g},
   \qquad
   e=g\sin\theta_W=g'\cos\theta_W.
   \]

8. Os acoplamentos foram interpretados como normas/rigidezes internas:

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

9. Os Yukawas foram estruturados como integrais de sobreposição:

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

10. As massas fermiônicas seguem:

   \[
   m_f=\frac{y_fv}{\sqrt2}.
   \]

11. A escala de Fermi foi relacionada a \(v\):

   \[
   G_F=\frac{1}{\sqrt2v^2}.
   \]

### Correção obrigatória resolvida

A fórmula:

\[
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\]

não produz \(246\,{\rm GeV}\). Ela produz aproximadamente:

\[
\boxed{
v_K\simeq72{,}85\,{\rm MeV}.
}
\]

Logo, essa expressão não deve ser usada como derivação da escala eletrofraca.
No máximo, pode ser reinterpretada futuramente como escala geométrica auxiliar
ou leptônica, mas não como valor esperado do Higgs.

Na resposta consolidada:

\[
\boxed{
v\neq v_K,
\qquad
v^2=-2a_2/a_4.
}
\]

### Trabalhos quantitativos posteriores — não reabrem a Q29

1. O background pré-quebra, o autovetor de Hopf e a estabilização foram
   calculados. Os coeficientes consolidados são

   $$
   a_2=-0{,}25319668,
   \qquad
   a_4^{\rm total}=2133{,}554507>0,
   $$

   com $\beta_*=0{,}0108937431$. Esse bloco não é mais pendência.
2. A integral interna da normalização cinética foi calculada:

   $$
   \frac{Z_\beta}{C_{\rm GDQ}}
   =\tau\frac{R^2}{12}
   =0{,}332804
   $$

   para $\tau=1$. Falta combinar esse resultado com
   $C_{\rm GDQ}=\hbar\mathfrak C_\gamma/\Lambda_C^2$, proveniente das
   Q33/Q36/Q38, e verificar que coincide com a calibração geométrica

   \[
   v=m_p\frac{6\pi^5}{7}=246{,}111196\,{\rm GeV}.
   \]

3. Transportar as normas $g$, $g'$ e $\theta_W$ do ponto geométrico comum da
   Q28 ao background eletrofraco quebrado. O uso direto dos valores da Q28 com
   $v=m_p6\pi^5/7$ produz $m_W=60{,}85$ GeV e $m_Z=76{,}97$ GeV, portanto o
   transporte não pode ser omitido. A interface local $\ell=1$ foi calculada
   e preserva $\sin^2\theta_W\simeq3/8$; logo, a mudança deve vir da redução
   global $T^5\times S^3$, não do estômato isolado. A variação dos módulos
   $L_A$ foi auditada e não resolve o problema: no setor steady eles são modos
   planos e, para perfis toroidais constantes, cancelam das duas normas. Falta
   derivar perfis/holonomias toroidais diferentes para $W$ e $Y$ ou aceitar
   $3/8$ como valor no ponto geométrico de correspondência. A simulação de
   $W/Z$ mostrou que a rota operacional $2/9$ reproduz corretamente a razão
   das massas; a normalização simultânea exige, como diagnóstico,
   $\alpha_{\rm EW}^{-1}\simeq132{,}47$. Ambos ainda devem ser derivados das
   normas globais, sem usar $m_W,m_Z$ como entrada.
4. O mecanismo fermiônico foi reformulado como

   $$
   M_f=M_f^{(0)}+\frac{v}{\sqrt2}Y_f^{\rm geom},
   $$

   com regras de seleção $\Delta j_L=\Delta j_R=\pm1/2$. Falta somente a
   avaliação numérica dos overlaps para CKM, PMNS e correções de massa; a
   existência da massa primária já pertence ao espectro da Q39.
5. Conectar \(G_F\) à normalização do setor fraco.

O teste de transporte mais recente isolou o alvo sem usar as massas como
entrada. A rigidez de superfície fornece o candidato

$$
\alpha_{\rm EW}^{-1}=132{,}457669,
$$

condicionado à identidade de Schur eletromagnética. O transporte angular de
$3/8$ para $2/9$ requer exatamente

$$
\frac{Z_W}{Z_Y}=\frac{10}{21}.
$$

Falta avaliar ambos no complemento de Schur da Hessiana global; o enunciado
$U(1)\subset U(3)$, sem essa projeção, não demonstra $2/9$.

Atualização: o traço de calor dos operadores quebrados produziu uma curva que
parte de $3/8$ e cruza $2/9$ em
$\tau_*=5{,}9090386\times10^6$. A pendência passou a ser a identificação
independente entre $\tau_*$ e a escala física eletrofraca através de
$(\Lambda_C,z_\tau)$.

Atualização em cascata: o complemento de Schur da colagem DtN foi calculado e
prova $K_{\rm EM}^{\rm eff}=K_0/(1+\mathcal S_\partial)$, condicionado apenas
à identificação constitutiva $\mathcal S_\partial=K_0/K_\partial$. O operador
espectral é autônomo no background estacionário, de modo que a condição
adiabática é exata nessa classe. A escala setorial
$\Lambda_0=126{,}354$ TeV está determinada; sua identificação universal com
$\Lambda_C$ permanece como questão metrológica da Q36.

Correção: a segunda variação da transgressão Q40 não derivou
$\mathcal S_\partial=K_0/K_\partial$. A parcela Chern--Simons avaliada é
topológica e tem Hessiana métrica nula; a parcela espectral é rank-one no
volume. Falta construir a Hessiana da conexão eletromagnética de contorno
$H_{\partial,Q}$ e o bloco misto $J_Q$. Assim, $132{,}457669$ permanece
condicional.

O teste da $\eta$-forma confirmou que $3\pi/2$ pertence à fase ímpar do
determinante, não à rigidez par $F_Q^2$. A normalização absoluta requer a
segunda variação da parte real $\zeta'_{D_Q^2}(0)$ para o espectro carregado
completo. Não usar Chern--Simons como correção direta de $1/e^2$.

A normalização alternativa pelo espaço cosmológico de Einstein também foi
testada. No setor smooth, steady e normalizado, a inserção eletromagnética é
constante/holomorfa e sua integral em $\gamma$ se anula. Um $e\ne0$ por essa
rota requer derivar o resíduo causal do estômato, a mesma pendência estrutural
da Q38.

Conclusão oficial:

\[
\boxed{
\text{Q29 fechada; transporte, overlaps e normalizações absolutas são trabalhos posteriores.}
}
\]

Atualização do colar dinâmico: as Fases 1 e 2 foram concluídas em
`q29/fase1_colar_dinamico_reducao_radial.md` e
`q29/fase2_colar_dinamico_resultado.md`. Mantendo o lapse, a torção fechada e
a interface efetivamente derivada, as condições naturais implicam

$$
a'=c'=f'=0.
$$

O ramo retorna ao cilindro, conserva

$$
H_q^{\rm total}=-2{,}67090856<0
$$

e o modo eletromagnético constante não é normalizável em colar infinito. Isso
fecha negativamente essa rota específica: ela não determina $\alpha$. A
pendência precisa é derivar, da colagem global, o pullback
$I_{\rm int}^{(a,c,f)}$; não escolher coeficientes Robin por ajuste.

### Programa posterior autônomo — constante $\alpha$

A predição absoluta de $\alpha$ fica separada da Q29. Deve ser retomada apenas
quando estiverem disponíveis a Hessiana Hermitiana completa, a normalização
do modo eletromagnético e o pullback métrico--dilatônico da colagem global,
sem seleção posterior de fatores ou contornos.

Fica preservado para investigação futura o resultado

$$
\boxed{\alpha_{\rm LHC}^{\rm efetivo}\simeq\frac{1}{128}}
$$

como **benchmark experimental de alta energia**, não como valor fundamental
de baixa energia nem como derivação da ação. A ponte constitutiva em baixa
energia usa $\alpha^{-1}\simeq137$; o transporte $137\to128$ pertence ao
running efetivo e deve ser auditado separadamente.

---

## 3. Questão 25 — Problema do sinal

Status:

\[
\boxed{\text{resolução geométrica estrutural feita; algoritmo posterior}}
\]

Foi estabelecida a rota geométrica:

\[
\rho(P_{ij}Z)=\rho(Z),
\qquad
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar.
\]

O sinal fermiônico fica na fase/holonomia, enquanto a medida \(\rho\) permanece
positiva.

### Falta para uma resolução computacional forte

1. Construir algoritmo explícito de simulação.
2. Implementar decomposição por domínios e interfaces.
3. Definir matrizes de transmissão/reflexão:

   \[
   \mathsf S_{ab}
   =
   \begin{pmatrix}
   \mathsf R_a & \mathsf T_{ba}\\
   \mathsf T_{ab} & \mathsf R_b
   \end{pmatrix}.
   \]

4. Provar preservação de:

   \[
   \rho>0,
   \qquad
   \operatorname{Hol}(P_{ij})=-1.
   \]

5. Calcular variância dos estimadores.
6. Medir autocorrelação.
7. Demonstrar ausência de reweighting exponencial.
8. Fazer benchmarks, por exemplo, Hubbard 2D dopado.
9. Estimar complexidade algorítmica.

---

## 4. Questão 24 — Assintoticidade da medição

Status:

\[
\boxed{\text{modelo estrutural feito; dominância espectral presente;
ponte com registros ainda pendente}}
\]

A medição foi estruturada por:

1. acoplamento sistema-aparelho-ambiente;
2. decoerência;
3. setores de ponteiro;
4. seleção efetiva de resultado por bacias geométricas.

### Correção de auditoria

O capítulo `pt-br/16 - Problema da Medida.md` já contém uma prova espectral de
dominância assintótica baseada no isomorfismo com difusão de nêutrons em meios
multiplicativos:

\[
\mathcal H\psi_n=\lambda_n\psi_n,
\qquad
0<\lambda_0<\lambda_1<\cdots,
\]

\[
\rho(\boldsymbol r,\tau)
=
\sum_n c_ne^{-\lambda_n\tau}\psi_n(\boldsymbol r)
\xrightarrow{\tau\to\infty}
c_0e^{-\lambda_0\tau}\psi_0(\boldsymbol r).
\]

Logo, não se deve dizer que falta toda prova assintótica. O que falta é
conectar essa dominância espectral ao modelo completo de medição
\(S+A+E\), aos registros \(R_i\) e à regra de Born já tratada na Questão 22.

### Falta demonstrar

1. Ponte entre o operador espectral \(\mathcal H\) e as bacias/registros
   macroscópicos \(R_i\).
2. Prova de estabilidade dos estados de ponteiro.
3. Estimativa da taxa de supressão dos termos fora da diagonal.
4. Condições geométricas para:

   \[
   \langle E_i(t)|E_j(t)\rangle\to0,
   \qquad
   i\ne j.
   \]

5. Relação precisa entre bacias geométricas e resultados únicos.

---

## 5. Questão 26 — Hopf e resíduos para spin

Status:

\[
\boxed{\text{spin fechado via fibrado spinorial; Hopf/resíduos ficam para depois}}
\]

A Questão 26 foi fechada pela rota segura:

1. estrutura spin;
2. grupo \(\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C)\);
3. representações \((1/2,0)\) e \((0,1/2)\);
4. operador de Dirac-Bismut;
5. propriedade \(2\pi\mapsto-1\), \(4\pi\mapsto+1\).

### Falta desenvolver futuramente

1. Usar a fibração de Hopf:

   \[
   S^1\hookrightarrow S^3\to S^2.
   \]

2. Relacionar:

   \[
   S^3\simeq SU(2),
   \qquad
   SU(2)\to SO(3).
   \]

3. Usar resíduos para calcular holonomias:

   \[
   \oint_\gamma\omega
   =
   2\pi i
   \sum_k
   \operatorname{Res}(\omega,z_k).
   \]

4. Conectar esses resíduos à fase:

   \[
   \operatorname{Hol}_\gamma
   =
   \exp
   \left(
   \frac{i}{\hbar}
   \oint_\gamma dS_R
   \right).
   \]

5. Mostrar se a integração no toro retorna naturalmente o setor
   semi-inteiro.

Essa rota deve ser tratada como interpretação/refinamento, não como substituta
da prova por fibrado spinorial.

---

## 6. Questão 30 — Confinamento e mass gap

Status:

\[
\boxed{\text{fechada estruturalmente no setor efetivo GDQ--}SU(3)_C}
\]

O programa quantitativo foi reiniciado em `q30/calculo_sigma_gap.md` a partir
da ação oficial. O solver histórico escolhe background, potenciais e, numa
versão, ação de plaqueta; por isso é teste de operador/engenharia exploratória,
não cálculo de $\sigma$ ou $\lambda_1$ da GDQ. O elo atual é derivar o
funcional transversal $\mathcal L_\perp[g,f,\bar f]$ no tubo de
$\mathbb R^4\times T^4$ antes de executar nova diagonalização.

A primeira redução torsional em `q30/reducao_torcao_bismut_tubo.md` obteve
$|H|^2=24e^{-2B}[(W')^2+(P')^2+(Q')^2]$. Sob $dH=0$, regularidade no eixo e
assíntota produto, o ansatz Hermitiano diagonal força $H=0$. Isso é um no-go
condicional do tubo diagonal simples: a realização confinante deve incluir a
conexão KK não diagonal, fluxo topológico/patches ou um defeito de bordo
explicitamente derivado.

O sistema mínimo de uma direção de Cartan foi fechado analiticamente em
`q30/sistema_radial_minimo_tubo.md`. As equações de $u$ e da elongação nula
impõem $(a')^2/r^2=\mathfrak c_0/\mathfrak c_1$, incompatível com
$a(0)=0$ e $a(\infty)=n_C/q$ para momentos causais constantes. Assim, esse
truncamento está excluído sem necessidade de shooting; deve-se manter a
conexão $SU(3)$ completa ou uma contribuição topológica/de bordo derivada.

O teorema `q30/teorema_gap_holonomia_irredutivel.md` prova que, numa seção
transversal compacta com conexão $SU(3)$ irreducível, o estabilizador
infinitesimal é trivial porque $\mathfrak z(\mathfrak{su}(3))=0$. Assim,
$D_{\mathcal A}^\dagger D_{\mathcal A}$ possui primeiro autovalor positivo.
Esse é o mass gap condicional do setor de conexão GDQ. Ainda falta construir
o minimizador irreducível pela ação e verificar que os demais blocos da
Hessiana não fecham o gap.

O controle da Hessiana completa foi formulado em
`q30/controle_hessiana_fisica_torcional.md`. Depois de excluir elongações e
modos de simetria, a positividade reduz-se exatamente a
$b^2<m_{\mathcal A}^2m_f^2$, onde $b$ é a norma do bloco misto. Essa foi a
redução intermediária antes da análise de representações.

O coeficiente misto foi depois eliminado exatamente em
`q30/desacoplamento_singlet_adjunto.md`: $f$ é singlet e a conexão de cor é
adjunta, portanto $\operatorname{Hom}_{SU(3)}(\mathbf1,\mathbf8)=0$ e $b=0$
no background equivariante. O gap de cor fica independente do bloco escalar.
Resta provar existência e isolamento do minimizador torsional irreducível.

Essa existência foi realizada em
`q30/minimizador_irredutivel_tres_camaras.md` para a seção transversal de três
bordos enquadrados. As holonomias clock--shift $P,Q\in SU(3)$ têm comutante
escalar e, portanto, estabilizador infinitesimal adjunto nulo. A conexão plana
associada minimiza o bloco de curvatura e é isolada quando os frames dos três
bordos são fixados. O gap de cor fica provado nessa realização. Permanece
calcular a tensão total $\sigma$ da ação GDQ; os bordos enquadrados são dados
das fontes topológicas, não novos termos fundamentais.

A separação entre gap e tensão foi corrigida em
`q30/no_go_sigma_holonomia_plana.md`. Como a conexão clock--shift é plana no
bulk, sua densidade local de curvatura é zero: ela prova gap espectral por
holonomia, mas não calcula $\sigma$. A tensão exige resolver
$(g_\Sigma,u_*,v_*,H_*,\mathcal D_{\partial\Sigma})$ na seção de três câmaras.
Não usar tensão de QCD, ação de plaqueta ou raio experimental para preencher
essa lacuna.

Correção posterior solicitada pelo autor: o background transversal não é uma
superfície abstrata de gauge, mas o pescoço Ricci--Bohm estabilizado já usado
na GDQ. Em `q30/correcao_background_transversal_gdq.md`, a área
$\mathcal A_0=\pi r_\perp^2$ emerge do equilíbrio transversal, a tensão é a
diferença de ação por unidade longitudinal
$\sigma_{\rm GDQ}=\mathcal S_\perp[q_*]-\mathcal S_\perp[q_{\rm vac}]>0$ e
$\Delta=\hbar c/r_\perp>0$. Q30 permanece fechada estruturalmente; avaliar os
números em unidades de $\Lambda_C$ é trabalho posterior.

O cálculo operacional de Heaviside foi executado em
`q30/calculo_operacional_heaviside_potencial.md`. Da identidade
$\Delta^2r=-8\pi\delta^{(3)}$, a lei GDQ $V(r)=\sigma_{\rm GDQ}r$ equivale ao
símbolo estático $\widetilde V(k)=-8\pi\sigma_{\rm GDQ}/k^4$. A inversão
regularizada por $(k^2+\mu^2)^{-2}$ converge à lei linear após subtrair
$V_\mu(0)$. É resposta reduzida do tubo, não nova ação fundamental.

A tentativa direta em `q30/tentativa_derivacao_direta_k4_hessiana.md`
mostrou que o símbolo local genérico é $k^2\mathsf M_2$ e seu inverso começa
em $k^{-2}$. O heat-kernel não altera esse comportamento infravermelho. Um
polo $k^{-4}$ elementar exigiria $\det\mathsf M_2=0$ numa direção física e
termo quartico positivo. Na GDQ atual, a interpretação correta é resposta
coletiva não perturbativa da sela tubular.

A medida coletiva foi formulada em `q30/medida_selas_tubulares_lei_area.md`.
Em corte espectral finito, integra-se $e^{-\operatorname{Re}S/\hbar}$ na
thimble do tubo. Laplace e subaditividade fornecem
$-\hbar A^{-1}\log|\langle\mathcal H(C)\rangle|\to\sigma_{\rm eff}>0$ sob
gap e sela isolada. O limite $N\to\infty$ do setor gaussiano foi depois
construído em `q30/limite_espectral_medida_gdq.md`, pois
$e^{-\tau L}L^{-1}$ é de traço para $\tau>0$. Permanecem a coercividade
uniforme da interação e o controle global das thimbles; portanto, isso não é
ainda construção Clay.

A coerção foi auditada em `q30/obstrucao_coercividade_contorno_causal.md`.
Pelo princípio de Laurent, $\oint z_\tau^{-4}dz_\tau=0$: a rigidez física vem
do resíduo do integrando completo. Se
$A(z)=\sum A_mz^m$, altas frequências exigem
$\mathfrak c_1^{\rm phys}=\operatorname{Re}[2\pi iA_3/(4\pi)^4]>0$. O corpus
não fornece $A_3$ para o background tubular nem as fases complexas das selas;
coercividade e Stokes não podem ser decididos sem esses dados causais.

A identificação foi corrigida em `q30/identificacao_A3_a6_tubo.md`.
$A_3$ é o coeficiente cúbico, ou terceiro jato, do pullback causal da Hessiana
ponderada da ação oficial. Ele não é automaticamente o $a_6$ de
Seeley--DeWitt, pois o integrando oficial não foi demonstrado igual a um traço
de calor. Para orientação positiva, $\mathfrak c_1^{\rm phys}>0$ equivale a
$\operatorname{Im}A_3<0$; um background congelado em $z$ dá $A_3=0$.
Permanece derivar a família tubular $(g(z),f(z),\bar f(z))$ até terceira ordem
e o pullback fechado $(\tau(z),t(z))$. O $a_6$ efetivo da Q34 não substitui
esses dados.

O teorema GDQ de puxamento foi incorporado em
`q30/teorema_puxamento_estomato_conservacao_torcao.md`. Para
$Q_T=\int_{\Sigma}H$ conservada, o representante homogêneo mínimo satisfaz
$H=(Q_T/V)\operatorname{vol}_\Sigma$ e
$\mathcal E_T=\kappa_TQ_T^2/(2V)$. Na variável $x=\log(V/V_0)$, a rigidez
torsional é positiva, $\mathcal E_T''=\mathcal E_T>0$, e o terceiro jato é
$d^3\mathcal E_T/dz^3=\mathcal E_T[-(x')^3+3x'x''-x''']$. Portanto, módulo
de torção e distorção não são dados independentes. A pendência foi reduzida a
resolver o jato causal de $x(z)$ pelas equações GDQ e verificar a soma com os
blocos de curvatura/dilatão; a conservação sozinha ainda não fixa a parte
imaginária do $A_3$ total.

A Hessiana vinculada do modo homogêneo foi calculada em
`q30/hessiana_vinculada_garganta_torcional.md`. Para o funcional radial da
Q35, a sela satisfaz
$R^6-4\tau R^4+\tau Q_T^2/\pi^2=0$ e sua rigidez exata é
$K_R=6(3R^2-8\tau)/R^4$. Logo, o modo é estável iff
$R^2>8\tau/3$. Na solução constitutiva com $Q_T=1$ e $\alpha=1/137$,
$K_R=5{,}3288885063>0$. Isso fecha a coercividade local radial e prova que
puxamento e variação do módulo torsional são a mesma resposta vinculada.
Ainda não fecha os modos anisotrópicos, os blocos mistos nem a mobilidade
causal/global.

O teste anisotrópico foi executado em
`q30/auditoria_squashing_volume_fixo.md`. Sob $R^3q=R_0^3$ e carga $Q_T$
fixa, a energia torsional é constante, enquanto
$\mathcal R_B(q)=2(4-q^2)q^{2/3}/R_0^2$ possui
$\mathcal R_B''(1)=-32/(3R_0^2)$. Assim,
$K_q^{V,Q}=-32\tau/(3R_0^2)<0$: conservação torsional não estabiliza o
squashing isovolumétrico. Esse modo é elongação simétrica $S$, não torção de
frame $K$. Ele sai do domínio somente se $S=0$ for dinamicamente consistente
no background Ricci--Bohm completo; essa prova permanece pendente.

A equação normal ao vínculo foi auditada em
`q30/consistencia_setor_sem_elongacao_garganta.md`. Para
$H=h\operatorname{vol}_{\Sigma_3}$ com $h=Q_T/V$, vale
$H_{acd}H_b{}^{cd}=2h^2g_{ab}$; no ciclo redondo,
$\operatorname{Ric}_{ab}\propto g_{ab}$, e o dilatão radial não tem tensão
angular sem traço. Logo,
$\mathcal E_{ab}^{\rm TF}|_{S=0}=0$: o setor homogêneo $S=0$ é uma truncagem
dinamicamente consistente. A auditoria não abeliana auto-dual fornece a mesma
anulação do tensor sem traço. Contudo, a Hessiana de Berger continua negativa
se $S$ for admitido. Assim, a coercividade fecha apenas condicionalmente no
setor constitutivo “elongações não são graus físicos”; não fecha para a
métrica irrestrita da ação oficial.

O bloco raio--dilatão foi calculado em
`q30/bloco_misto_raio_dilatao_normalizado.md`. A normalização de Perelman
impõe $u_0=\log V=3\log R+\mathrm{const.}$; logo, o termo $3\log R$ já é o
pullback do modo homogêneo de $u$, e $K_R$ já contém sua resposta. Modos
$\ell\ge1$ têm média zero e não misturam com o raio por simetria. Sua forma
quadrática mínima é
$\mu_1=3\tau/R^2-1/2$. Na solução vigente,
$\mu_1=0{,}2667910448>0$ (ou autovalor Hessiano
$0{,}5335820896$). Assim, o bloco escalar homogêneo não fecha o gap radial.
Permanecem perfis radiais do colar, Robin/interface e mobilidade causal.

Os perfis radiais e a Robin induzida foram resolvidos no colar produto em
`q30/dtn_collar_radial_torsional.md`. A restrição linearizada do lapse impõe
$\delta f=0$ no perfil radial local, e a projeção da matriz principal em
$(\delta a,\delta c,\delta f)=(\rho,\rho,0)$ fornece
$p_R=12\tau e^{-f_0}R>0$. Com $K_R>0$, o operador é
$\mathcal J_R=-p_R\partial_r^2+K_R>0$. A minimização do bulk produz
$\Lambda_R^{\rm DtN}=\sqrt{p_RK_R}>0$ no semi-eixo e as versões positivas
com $\coth$ ou $\tanh$ no colar finito. Assim, nenhuma mola Robin externa é
necessária para o modo radial homogêneo. Permanecem colar não produto,
interface métrico--dilatônica adicional e mobilidade causal.

O status do colar e da mobilidade foi auditado em
`q30/fechamento_estatico_e_mobilidade_fluxo.md`. Sem fonte de interface
adicional, $\Pi_a=\Pi_c=\Pi_f=0$ seleciona o ramo produto
$a'=c'=f'=0$; portanto o colar não produto não é requisito do problema
vigente. A projeção do fluxo Ricci--Bismut fornece
$G_{RR}=12/R^2$ e magnitude de mobilidade $|\mathsf M_R|=R^2/6$. Na
convenção de descida, a taxa linear é
$\Gamma_R=\mathsf M_RK_R=3-8\tau/R^2>0$; na solução vigente,
$\Gamma_R=0{,}9552238806$ e $\tau_{\rm relax}=1{,}046875$. Isso fecha a
magnitude, não ainda o sinal: o Capítulo 17 combina
$\partial_\tau g=-2E$ com $d\mathcal W/d\tau\ge0$, enquanto o ramo radial é
classificado como mínimo. Falta alinhar a primeira variação nas mesmas
convenções. A reconstrução em tempo físico e Stokes também permanecem.

O sinal foi resolvido em `q30/auditoria_sinal_fluxo_perelman_bismut.md`.
Como $\delta\mathcal W_T=-\tau\langle E_T,\delta g\rangle$, o fluxo
$\partial_\tau g=-2E_T$ é subida:
$\partial_\tau g=(2/\tau)\operatorname{grad}\mathcal W_T$, compatível com
$d\mathcal W_T/d\tau\ge0$. A mobilidade radial auxiliar correta é
$\mathsf M_R^{(\mathcal W)}=R^2/(6\tau)$. Logo, o ramo $K_R>0$ é coercivo
estaticamente, mas repulsor do fluxo entrópico, com taxa de crescimento
$3{,}4747983447$. A interpretação anterior como relaxação foi retirada. Esse
fluxo não fornece a mobilidade causal de $\operatorname{Re}S$ em tempo físico.

A ponte solicitada pelo autor foi construída em
`q30/ponte_operacional_heaviside_yang_mills.md`. O operador regular
$P_\mu=-\Delta+\mu^2$ permite a realização local em cascata
$P_\mu\phi=\rho$, $P_\mu V=-8\pi\sigma_{\rm GDQ}\phi$. Eliminando $\phi$,
$\widetilde V_\mu=-8\pi\sigma_{\rm GDQ}/(k^2+\mu^2)^2$ e, após subtrair a
constante, $V_\mu(r)-V_\mu(0)\to\sigma_{\rm GDQ}r$. Isso demonstra a
equivalência operacional $\simeq_H$ entre a resposta coletiva GDQ e um setor
confinante efetivo tipo Yang--Mills, incluindo lei de área e gap transversal.
Não demonstra igualdade das medidas quânticas completas nem resolve, por si
só, o enunciado literal de Clay.

A noção correta de equivalência foi formulada em
`q30/equivalencia_por_observaveis_heaviside.md`. A topologia fornece o mapa
$\Theta$ entre classes de ciclos/cargas e Heaviside fornece o mapa
$\mathfrak H_\Theta$ entre funções dos operadores reduzidos. Potencial,
tensão, lei de área e gap já coincidem no setor estático. A equivalência
completa, tomando Yang--Mills axiomaticamente, não exige reconstruir
$G^{(3)},G^{(4)},\ldots$ um a um. Basta provar nos geradores: boa definição
no quociente, preservação das relações da álgebra e entrelaçamento do estado
$\omega_{\rm GDQ}\circ\mathfrak H_\Theta=\omega_{\rm YM}$. Pela propriedade
universal, os correladores superiores seguem. Um homeomorfismo dos espaços
brutos não é necessário.

Os três lemas foram construídos em
`q30/tres_lemas_equivalencia_heaviside.md`. (1) Boa definição segue porque
$\Theta$ atua em classes e conjugação não altera traços/cálculo funcional.
(2) Composição, unidade e involução são preservadas, estendendo o mapa a um
$*$-homomorfismo. (3) A bijetividade de $\Theta$ e a invertibilidade para
$\mu>0$ fornecem o inverso; no limite toma-se o quociente pelo modo constante.
O estado transportado é positivo, normalizado e invariante, coincidindo com o
estado Yang--Mills pela unicidade axiomática do vácuo. A última igualdade
permanece condicional à positividade global do estado GDQ/thimble; os dois
lemas algébricos não dependem disso.

O contorno foi fechado em `q30/prova_contorno_causal_thimble_unica.md` sob a
forma matemática das hipóteses adotadas pelo autor. Em cada corte espectral,
coercividade uniforme no componente $Q_T$ implica sela única e ação própria.
O ciclo causal conjugação-simétrico cruza a thimble ascendente uma vez,
$n_N=+1$, logo $[\mathcal C_\gamma]=[\mathcal J_N]$. Com uma única sela não
há par capaz de gerar Stokes; cargas diferentes pertencem a componentes
desconectados. O limite $N\to\infty$ preserva a thimble se a cota coerciva for
uniforme. Assim, positividade e ausência de Stokes estão fechadas
condicionalmente à convexidade global/uniformidade, não apenas à Hessiana
local.

A resposta consolidada está em:

Correção física final do autor, formalizada em
`q30/principio_sem_distanciamento_dois_estomatos.md`: no setor Yang--Mills de
dois estômatos, $S=0$ significa que o distanciamento relativo não é direção
dinâmica admissível. Deformações físicas culminam em redistribuição/torção do
vínculo conservado. O comprimento $L$ de $V(L)=\sigma L$ é separação imposta
por fontes externas e mede trabalho, não um modo livre. Assim, o modo Berger
do prolongamento métrico irrestrito não entra na Hessiana física; a
coercividade deve ser avaliada somente no setor torsional projetado.

1. `questão_30_yang_mills.md`;
2. `q30/conexao_su3_wilson_gap.md`.

Foi corrigida a lacuna original de assumir seção transversal e densidade
constantes. Agora a constância vem do princípio variacional.

No bulk do tubo:

\[
E[q]=\int_0^r\mathcal L_\perp(q,q')\,dz,
\qquad
\frac{\partial\mathcal L_\perp}{\partial z}=0.
\]

Pela identidade de Beltrami:

\[
\sum_a q_a'
\frac{\partial\mathcal L_\perp}{\partial q_a'}
-
\mathcal L_\perp
=
\text{constante}.
\]

No minimizador translacionalmente invariante:

\[
q'(z)=0.
\]

Logo:

\[
\mathcal L_\perp(q_0,0)=\sigma=\text{constante},
\qquad
\frac{d\sigma}{dz}=0.
\]

Como \(q_0\) inclui o raio transversal:

\[
R(z)=R_0,
\qquad
\mathcal A(z)=\pi R_0^2=\mathcal A_0,
\qquad
\frac{d\mathcal A}{dz}=0.
\]

Assim:

\[
V(r)=\sigma r+O(1).
\]

### Resolvido nesta etapa

1. A seção transversal não precisa mais ser assumida constante.
2. A densidade/tensão por comprimento não precisa mais ser assumida constante.
3. A constante de área/tensão \(\sigma\) é obtida como mínimo variacional:

   \[
   \sigma
   =
   \mathcal L_\perp(q_0,0)
   =
   \inf_q\mathcal L_\perp(q,0)
   >
   0.
   \]

4. O crescimento linear segue do princípio variacional:

   \[
   V(r)=\sigma r+O(1).
   \]

### Correção de auditoria

O manuscrito contém dois cálculos físicos adicionais que não devem ser
tratados como ausentes:

1. uma equação integral de Fredholm de segunda espécie para um acoplamento
   forte efetivo:

   \[
   \psi(\theta)
   =
   \phi_0(\theta)
   +
   \lambda\int_0^{2\pi}K(\theta,\theta')\psi(\theta')d\theta',
   \]

   com:

   \[
   T_{\rm transm}=\frac12,
   \qquad
   \alpha_s^{\rm eff}
   =
   \frac12\frac{3}{4\pi}
   =
   \frac{3}{8\pi}
   \approx0{,}119366.
   \]

2. uma previsão fenomenológica para polarização global de híperons:

   \[
   P_\Lambda
   =
   \frac{\hbar\omega_{\rm fluid}}{2k_BT}
   \left(
   \frac{\chi_{{\rm Fano},n}}{\delta^2}
   \right)
   \approx0{,}85\%.
   \]

Esses resultados fortalecem o setor fenomenológico da Questão 30. A ressalva
remanescente é que \(\alpha_s^{\rm eff}=3/(8\pi)\) ainda não é o running
completo \(\alpha_s(\mu)\), e a polarização de híperons não substitui por si só
a cadeia estrutural de Wilson loops, lei de área e gap. Essa cadeia foi
registrada abaixo usando a conexão efetiva \(SU(3)_C\).

### Ponte \(SU(3)\), Wilson loops e gap

Usando a Questão 28, o setor de cor é:

\[
E_C\simeq\mathbb C^3,
\qquad
G_C=SU(3)_C.
\]

A conexão efetiva é:

\[
\boxed{
A_C\in\Omega^1(N,\mathfrak{su}(3)).
}
\]

A curvatura é:

\[
\boxed{
F_C=dA_C+A_C\wedge A_C.
}
\]

A ação efetiva contém:

\[
\boxed{
S_C^{\rm eff}
=
\frac{1}{2g_s^2}
\int_N\operatorname{Tr}(F_C\wedge *_hF_C)
+
S_{\rm torção}
+
S_{\rm Ricci/Bohm}
+
\cdots.
}
\]

Os Wilson loops são holonomias:

\[
\boxed{
W_R(C)
=
\operatorname{Tr}_R
\mathcal P
\exp
\left(
i\oint_CA_C
\right).
}
\]

A constante de área é definida variacionalmente:

\[
\boxed{
\sigma
=
\inf_{\mathcal C_C}
\frac{
E_{\rm surf}[A_C,B,\rho,S_R;S]
}{
\operatorname{Area}(S)
}
>0.
}
\]

Assim:

\[
\boxed{
\langle W_R(C)\rangle
\sim
e^{-\sigma A_{\min}(C)}.
}
\]

Para loop retangular:

\[
\boxed{
V(r)=\sigma r+O(1).
}
\]

A Hessiana confinante:

\[
\mathcal H_{\rm conf}
=
-\Delta_{A_C}+V_{\rm geom}
\]

tem gap positivo se:

\[
\operatorname{Ric}^{B}_f\ge\Lambda_0g,
\qquad
\Lambda_0>0,
\qquad
\sigma>0.
\]

Então:

\[
\boxed{
\lambda_1
\ge
c_D\Lambda_0+c_\sigma\sigma
>
0,
\qquad
\Delta=\hbar\sqrt{\lambda_1}>0.
}
\]

### Ainda fica como cálculo posterior

1. Transportar $g_s^{\rm match}=g$ ao background hadrônico e comparar com o
   valor já obtido na Q30,

   $$
   g_s^{\rm had}=\sqrt{\frac32}.
   $$

2. Calcular numericamente \(\sigma\).
3. Calcular numericamente \(\lambda_1\).
4. Formalizar a medida funcional completa do setor \(A_C\).
5. Derivar a tradução efetiva \(\alpha_s(\mu)\), se for desejada comparação
   perturbativa externa.
6. Conectar \(\alpha_s^{\rm eff}=3/(8\pi)\) à escala/topologia hadrônica.
7. Comparar com glueballs, espectro hadrônico e dados de confinamento.

### Observação

A parte geométrica interna do confinamento ficou fechada estruturalmente:
\(SU(3)_C\), conexão, Wilson loops, lei de área e gap positivo foram
encadeados no setor efetivo da GDQ. O que permanece aberto é a formalização
analítica completa no sentido externo de Yang--Mills puro e a avaliação
numérica dos parâmetros.

---

## 7. Constantes fundamentais e acoplamentos

Status:

\[
\boxed{\text{programa aberto}}
\]

A teoria propõe que constantes fundamentais e acoplamentos sejam derivados da
geometria. Essa ideia precisa ser mantida, mas com exigência alta de prova.

### Falta demonstrar

1. Derivar \(\alpha\) sem seleção posterior de fatores.
2. Derivar \(G\) sem inserir constantes experimentais.
3. Derivar massas de léptons e hádrons como autovalores.
4. Derivar \(\alpha_s(\mu)\), incluindo running. Correção: há no manuscrito
   uma proposta de valor efetivo \(\alpha_s^{\rm eff}=3/(8\pi)\) via Fredholm;
   falta transformá-la em acoplamento renormalizado dependente da escala.
5. Para $\alpha$, o critério de transporte foi demonstrado em
   `teorema_heranca_normalizacao_eletromagnetica.md`: a corrente simplética
   preserva $Z_Q$ quando o canal é localizado ou massless completo sem fuga.
   Ainda falta avaliar $Z_Q^E$ globalmente pela Hessiana oficial e verificar
   qual dessas duas classes descreve o canal elétrico. A avaliação direta em
   `37p/derivacao_ZQ_global_acao_oficial.md` mostrou que
   $\mathcal K_Q=41{,}594825709\ldots$ é uma norma radial não canonizada. A
   matriz de Gram produz exatamente o fator $1/4$, mas a diagonalização neutra
   radial ainda fornece $Z_\gamma=15{,}1626057595\ldots$, não o
   $Z_Q^E=10{,}904984952\ldots$ exigido pela fórmula cosmológica. Não inserir
   a razão residual como prefator. Falta a matriz Hermitiana horizontal
   completa e/ou a contribuição causal ou de Schur derivada da ação.
   O teste sem ajuste `37p/teste_schur_dtn_global.py` usou o DtN redondo
   $K_\partial=\pi^2R^2$ e obteve $\alpha^{-1}=137{,}604601779$, erro de
   $0{,}414868\%$ em $Z_Q$, com Hessiana positiva. O próximo passo preciso é
   calcular o DtN warped--Bismut oficial; não ajustar a diferença restante.
   O caráter massless, o fechamento do canal e o limite DtN em frequência
   zero já não são pendências independentes: em
   `37p/teorema_canal_fotonico_massless.md`, a identidade de Ward fecha o
   canal e a cohomologia relativa $H^1(B^4,S^3)=0$ exclui o modo zero físico,
   sob positividade da Hessiana projetada. Resta somente a avaliação absoluta
   do DtN warped--Bismut.
   A tentativa de identificar diretamente a fórmula cosmológica foi concluída
   em `37p/identificacao_formula_cosmologica_hessiana.md`. O inteiro $1920$ é
   $|W(D_5)|$, mas falta provar que o grupo inteiro, e não apenas o
   estabilizador do eixo elétrico e de $(J,H,f,\mathcal U)$, atua no quociente
   físico. A raiz quarta e o fator $9/8$ também não seguem ainda da Hessiana.
   Esses itens não constituem três parâmetros a ajustar: devem emergir do
   único cálculo pendente do DtN warped--Bismut completo.
   Refinamento posterior: o warp puramente conformal não é mais candidato,
   pois $\int F\wedge\star F$ é conformalmente invariante em quatro dimensões
   com métrica induzida fixa e a truncagem disponível não contém bloco
   escalar--fóton em $A_Q=0$. A classe
   redonda/conformal fecha negativamente em
   $\alpha^{-1}=137{,}604601779\ldots$. A pendência deve ser formulada de modo
   mais restrito: construir o background normal Hermitiano anisotrópico e sua
   matriz cinética transversal, incluindo possível mistura gauge-invariante
   com a 2-forma torsional; não apenas calcular um warp escalar.
   Na interpretação cosmológica da fórmula legada, o peso $1/1920$ já foi
   demonstrado em `37p/interpretacao_media_einstein_formula_legada.md`: a
   covariância por pullback e a transitividade de $W(D_5)$ tornam as energias
   livres degeneradas, e o ensemble fornece $p_a=1/1920$. Nessa rota resta
   O projetor isotrópico foi depois obtido no setor axial coerente: o quarto
   momento de Haar em $S^3$ fornece $1/8$, o traço das três direções
   Cartan--Schouten fornece $3^2$, e a normalização angular fornece
   $\pi^{-4}$. Assim, a rota da fórmula legada fica fechada condicionalmente
   à coerência do autovetor Hopf; não permanece como falta independente.
6. Derivar Yukawas.
7. Separar claramente:

   \[
   \text{estimativa heurística}
   \neq
   \text{teorema derivado}.
   \]

8. Remover ou rebaixar scripts que injetam valores-alvo.

---

## 8. Questão 31 — Problema CP forte

Status:

\[
\boxed{\text{Q31 fechada estruturalmente no setor efetivo GDQ--}SU(3)_C}
\]

Documento técnico consolidado:

1. `questão_31.md`;
2. `q31/cp_forte_torcao_su3.md`.

A estrutura correta foi estabelecida:

\[
\theta_{\rm efetivo}
=
\theta_0+\frac{a}{f_B},
\qquad
a\sim a+2\pi f_B.
\]

O potencial periódico é:

\[
V(\theta)
=
\chi_{\rm top}(1-\cos\theta).
\]

A dinâmica dissipativa é:

\[
\frac{d\theta}{d\tau}
=
-
\kappa_{\rm CP}
\frac{\partial V}{\partial\theta}
=
-
\kappa_{\rm CP}
\chi_{\rm top}
\sin\theta.
\]

Foi demonstrada a monotonicidade de Lyapunov:

\[
\frac{dV}{d\tau}
=
-
\kappa_{\rm CP}
\left(
\frac{\partial V}{\partial\theta}
\right)^2
\le0.
\]

Logo, para dados fora do ponto instável:

\[
\theta(\tau)\to0\pmod{2\pi}.
\]

### Resolvido nesta etapa

1. A forma global do potencial deve ser periódica, não apenas quadrática.
2. O mínimo em \(\theta=0\) não é simplesmente escolhido; ele é atrator do fluxo
   dissipativo.
3. A dinâmica de relaxamento CP foi escrita como teorema de Lyapunov.
4. A previsão conservadora do EDM ficou:

   \[
   |d_n|
   \le
   C_n
   |\theta_{\rm inicial}|
   e^{-\kappa_{\rm CP}\chi_{\rm top}\tau_{\rm conf}}.
   \]

5. A previsão \(d_n=0\) foi rebaixada para caso limite de relaxamento exato ou
   projeção exata no atrator.

### Cálculo posterior

O que permanece não é mais uma lacuna estrutural do mecanismo CP, mas cálculo
funcional, numérico e fenomenológico:

1. Calcular \(\chi_{\rm top}\) no setor forte efetivo da GDQ:

   \[
   \chi_{\rm top}
   =
   \int d^4x\,\langle q(x)q(0)\rangle.
   \]

2. Formalizar \(f_B\) por normalização canônica do modo torsional. Correção: o
   manuscrito já propõe:

   \[
   f_B
   =
   M_P\sqrt{\frac{3}{\sqrt{6\pi^5}}}
   \approx6{,}44\times10^{17}\ {\rm GeV},
   \]

   a partir da rigidez torsional e do volume de Kähler
   \(V_K=6\pi^5\). Falta conectar essa proposta ao termo cinético canônico do
   modo \(a\) no setor oficial da GDQ.
3. Decidir se o modo \(a\) possui polo propagante ou se é apenas modo
   relaxacional geométrico.
4. Derivar a massa/escala:

   \[
   m_a^2f_B^2=\chi_{\rm top}.
   \]

5. Calcular \(\kappa_{\rm CP}\tau_{\rm conf}\).
6. Obter uma previsão numérica para o EDM residual.
7. Demonstrar viabilidade cosmológica:

   \[
   \Gamma_{\rm GDQ}\gg m_a
   \]

   ou condição equivalente de superamortecimento.

8. Conectar a construção ao setor \(SU(3)_C\)/Yang-Mills das Questões 28 e 30.

---

## 9. Questão 32 — Propagador modificado

Status:

\[
\boxed{\text{fechada estruturalmente; redução técnica registrada em adendo}}
\]

A origem correta do fator:

\[
e^{-p^2/\Lambda^2}
\]

não deve ser um regulador inserido manualmente. Ela deve ser:

\[
\boxed{
e^{-\tau L_{\rm GDQ}^{(2)}},
\qquad
\tau=\Lambda^{-2},
}
\]

isto é, o semigrupo de calor gerado pelo operador quadrático normalizado da ação
GDQ.

No regime plano:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

Como o exponencial é função inteira e não possui zeros, ele não introduz polos
novos:

\[
\boxed{
\text{polos apenas em }p_E^2+m^2=0.
}
\]

### Resolvido nesta etapa

1. O gaussiano foi reinterpretado como núcleo de calor, não como fator externo.
2. A escala foi ligada ao fluxo:

   \[
   \tau=\Lambda^{-2}.
   \]

3. A ausência de novos polos foi explicitada.
4. A ausência de fantasmas foi condicionada à inexistência de polos extras.
5. A continuação lorentziana foi condicionada à reconstrução OS/Sudarshan e ao
   cone causal da métrica física \(h\).
6. O bloco escalar oficial da Hessiana foi calculado com:

   \[
   \mathcal U=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
   \]

   e com o termo:

   \[
   \frac{f+\bar f}{2}-n.
   \]

   A forma quadrática obtida foi:

   \[
   \mathcal S_{\rm esc}^{(2)}
   =
   \int_\gamma\frac{d\tau}{\tau}
   \int d\mu_{\sigma_0}
   \left[
   \tau K_2-\tau sK_1+
   \left(\frac{B_0}{2}-1\right)s^2
   \right].
   \]
7. A Hessiana oficial foi organizada em blocos:

   \[
   \mathcal S_{\rm GDQ}^{(2)}
   =
   \int_\gamma\frac{d\tau}{\tau}
   \int d\mu_{\sigma_0,g_0}
   (Q_{ss}+Q_{gs}+Q_{gg}).
   \]

### Ainda falta demonstrar

1. Calcular os coeficientes completos de \(Q_{gg}\) e \(Q_{gs}\) em fundo geral.
2. Executar a decomposição espectral completa dos modos físicos, traço e
   difeomorfismos.
3. Usar como referência técnica:

   \[
   \boxed{\texttt{q32/reducao\_hessiana\_gauge\_fixada.md}}
   \]

4. Verificar, em cada setor efetivo, que o kernel usado é:

   \[
   e^{-\tau L_{\rm GDQ}^{(2)}},
   \]

5. Provar reflexão positiva dos Schwinger functions amortecidos.
6. Reconstruir o propagador lorentziano físico.
7. Demonstrar:

   \[
   \operatorname{supp}G_{\rm ret}\subseteq J_h^+.
   \]

8. Verificar identidades de Ward/Slavnov--Taylor no setor gauge efetivo.
9. Provar independência de regulador ou explicar que \(\Lambda\) é escala física
   geométrica, não regulador removível.

---

## 10. Questão 33 — Escala de corte

Status:

\[
\boxed{\text{estruturalmente respondida; capítulo 33 original precisa
correção futura}}
\]

A Questão 33 separou três objetos que não devem ser confundidos:

\[
\boxed{
\Lambda_C
\neq
\Lambda(\tau)
\neq
m_i.
}
\]

Onde:

1. \(\Lambda_C\) é a escala geométrica de Cartan da camada efetiva;
2. \(\Lambda(\tau)=\tau^{-1/2}\) é a escala de resolução do fluxo;
3. \(m_i\) são massas/autovalores de setores físicos.

### Resolvido nesta etapa

1. \(0{,}511\,{\rm MeV}\) foi rebaixado para escala inercial/Compton do setor
   eletrônico, não corte UV universal.
2. \(\sim1\,{\rm GeV}\) foi interpretado como possível escala hadrônica ou
   solitônica setorial, não corte universal duro.
3. O corte foi ligado ao semigrupo:

   \[
   e^{-\tau L_{\rm GDQ}^{(2)}},
   \qquad
   \Lambda(\tau)=\tau^{-1/2}.
   \]

4. Foi explicitado que experimentos acima de \(1\,{\rm GeV}\) só permanecem
   compatíveis se \(1\,{\rm GeV}\) não for corte universal.

### Ainda falta demonstrar

1. Derivar numericamente \(\Lambda_C\) a partir da geometria, sem escolher valor
   posterior.
2. Decidir se \(\Lambda_C\) é universal ou setorial.
3. Se for universal, mostrar que:

   \[
   \Lambda_C
   \gg
   \text{escalas já testadas em colisores}.
   \]

4. Se for setorial, derivar:

   \[
   \Lambda_e,\quad \Lambda_H,\quad \Lambda_{\rm had},\quad \Lambda_{\rm EW}
   \]

   como espectros de operadores \(L_i^{(2)}\), não como massas inseridas.

5. Corrigir o capítulo 33 original:

   \[
   v_K\simeq72{,}85\,{\rm MeV}
   \neq
   246\,{\rm GeV}.
   \]

6. Não usar:

   \[
   \Lambda_H=m_e
   \]

   como corte de loops do Higgs.

7. Corrigir a notação:

   \[
   M_H\simeq125\,{\rm GeV},
   \qquad
   M_H^2\simeq(125\,{\rm GeV})^2.
   \]

---

## 11. Questão 34 — Calibre em loops

Status:

\[
\boxed{\text{fechada no setor geométrico declarado de 34-0}}
\]

A auditoria em q34/obstrucao_loop_desde_acao_oficial.md corrigiu a rota: o
loop fermiônico é auxiliar, mas Q34 deve ser fechada pelo determinante da
Hessiana geométrica oficial. Não é necessário importar variáveis Grassmann.

O loop geométrico foi executado em q34/loop_geometrico_fase_t4.md. Para o
modo de fase $n=1$ em um ciclo do $T^4$ oficial:

$$
\mathcal S_{\rm GDQ}
\to H_n[A]
\to\operatorname{Tr}\log H_n[A]
\to\Pi_{\mu\nu}^{\rm GDQ}.
$$

A verificação forneceu $\Pi(0)=0$, erro de Ward
$2{,}061\times10^{-20}$, saturação
$\Pi(\infty)=2{,}050140062891\times10^{-3}$ no cenário interno declarado e
erro de refinamento $8{,}949\times10^{-13}$.

O teste de sensibilidade em q34/teste_kernels_covariantes.md comparou o
semigrupo canônico, uma mistura convexa de semigrupos e uma deformação inteira.
Nos três casos, $\Pi(0)=0$, Ward apresentou erro inferior a
$2{,}8\times10^{-20}$ e a resposta permaneceu monótona, finita e saturante.
As amplitudes ultravioletas diferem porque trocar o kernel troca a resolução
física; isso não viola a identidade de calibre. O kernel canônico
$e^{-sH}$ é o semigrupo determinado pela Hessiana oficial.

A Questão 34 exige demonstrar preservação de calibre em loops, incluindo:

1. fixação de gauge;
2. determinante de Faddeev--Popov ou substituto geométrico;
3. fantasmas como ferramenta de auditoria, se necessário;
4. identidades de Ward/Slavnov--Taylor;
5. termos locais efetivos/projeções finitas compatíveis com gauge;
6. função efetiva de escala, se a comparação perturbativa for feita;
7. independência do regulador.

### Resolvido nesta etapa

1. Foi estabelecido que fantasmas não precisam ser ontologia GDQ, mas o
   determinante/jacobiano da órbita de gauge precisa ser tratado.
2. Foi indicada uma fixação de gauge de fundo:

   \[
   F[A]=\bar D^\mu a_\mu=0.
   \]

3. Foi identificado o operador FP:

   \[
   M_{\rm FP}=-\bar D^\mu D_\mu.
   \]

4. Foi conectada a regularização da Questão 32:

   \[
   G_A=e^{-\tau L_A^{(2)}}(L_A^{(2)})^{-1}.
   \]

5. Foi definido o teste mínimo:

   \[
   q^\mu\Pi_{\mu\nu}^{ab}(q)=0.
   \]
6. Foi registrado o adendo técnico:

   \[
   \boxed{\texttt{q34/loop\_U1\_teste\_minimo.md}}
   \]

   onde o setor abeliano é tratado com heat-kernel covariante e o determinante
   de Faddeev--Popov aparece apenas como jacobiano não dinâmico.
7. Foi executado o cálculo mínimo em:

   \[
   \boxed{\texttt{q34/polarizacao\_U1\_heat\_kernel.md}}
   \]

   obtendo:

   \[
   \Pi_{\mu\nu}^{(\tau)}(q)
   =
   (q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2),
   \qquad
   q^\mu\Pi_{\mu\nu}^{(\tau)}=0.
   \]
8. Foi consolidada a extensão não abeliana em:

   \[
   \boxed{\texttt{q34/slavnov\_taylor\_geometrico.md}}
   \]

   com:

   \[
   L_{A^g}=g^{-1}L_Ag
   \quad\Rightarrow\quad
   {\rm Tr}\,F_\tau(L_A)\text{ é gauge-invariante}
   \quad\Rightarrow\quad
   \mathcal S(\Gamma_\tau)=0.
   \]

9. Foi implementada a avaliação numérica auditada comum às Q34/Q35 em
   numerico/q34_q35_u1/solve_polarizacao_u1.py, com testes de regressão em
   numerico/q34_q35_u1/test_polarizacao_u1.py. Para o cenário adimensional
   de teste $\eta=\tau m^2=10^{-6}$, sem pretensão de fixar
   $\Lambda_{\rm EM}$, os seis testes passaram. Foram verificados subtração
   infravermelha, Ward tensorial, saturação, monotonicidade, limite de QED e
   refinamento de quadratura. O relatório está em
   numerico/q34_q35_u1/saida_polarizacao_u1_auditada.md.

10. Os coeficientes locais do setor $U(1)$ foram extraídos em
    q34/coeficientes_locais_U1_heat_kernel.md. Na convenção subtraída,
    $c_F^{\rm IR}=0$ fixa a carga medida, enquanto

    $$
    A_1=\frac{\alpha_0e^{-\eta}}{15\pi},
    \quad
    A_2=-\frac{\alpha_0e^{-\eta}(1+\eta)}{140\pi},
    \quad
    A_3=\frac{\alpha_0e^{-\eta}(2+2\eta+\eta^2)}{1890\pi}.
    $$

    Para $\alpha_0=1/137$ e $\eta=0{,}2749005225$:

    $$
    A_1=1{,}1766587294\times10^{-4},
    \quad
    A_2=-1{,}6072744595\times10^{-5},
    \quad
    A_3=2{,}4517191332\times10^{-6}.
    $$

    A verificação reproduziu erro $O(r^4)$ após a truncagem em $r^3$.

11. O coeficiente não abeliano líder $a_4$ foi consolidado em
    q34/coeficiente_nao_abeliano_a4.md:

    $$
    b_0
    =
    \frac{11}{3}C_A
    -\frac{4}{3}\sum_{\rm Dirac}T(R_f)
    -\frac{1}{6}\sum_{\rm escalar\ real}T(R_s).
    $$

    Para o espectro efetivo da Q28:

    $$
    b_0^{SU(3)}=7,
    \qquad
    b_0^{SU(2)}=\frac{10}{3}
    $$

    sem o modo de ordem no loop. Se $\Phi_{\rm EW}$ propagar como doublet
    escalar complexo, o resultado condicional é $b_0^{SU(2)}=19/6$.
    O coeficiente absoluto de $F^2$ requer gap espectral; sem gap, a
    divergência restante é infravermelha, não ultravioleta.

12. A parte de matéria de $a_6$ foi calculada em
    q34/a6_materia_e_obstrucao_F3.md:

    $$
    c_{2G}^{\rm matter}
    =
    \frac{g^2}{240\pi^2}
    \sum_f
    \frac{T(R_f)}{m_f^2}
    e^{-\tau m_f^2}.
    $$

    O limite $U(1)$ foi reproduzido com diferença algébrica inferior a
    $10^{-18}$. Foi também demonstrado que o coeficiente de
    $\operatorname{tr}(F^3)$ não aparece na função de dois pontos e não pode
    ser inferido de $\Pi_{\mu\nu}$.

13. O bloco vetor--jacobiano de $a_6$ foi montado na forma universal em
    q34/a6_vetor_jacobiano_forma_universal.md. Após integração por partes, os
    pesos brutos dos termos puros de $\Omega$ são $(-8,4,-24)/360$ para
    $((DF)^2,(D\cdot F)^2,F^3)$, e os termos de $E$ possuem pesos
    $(-30,60,30)/360$ para $((DE)^2,E^3,E\Omega^2)$. A normalização foi
    verificada reproduzindo

    $$
    a_4^{\rm VJ}
    =
    \frac{11}{96\pi^2}
    \int F_{\mu\nu}^\delta F_{\mu\nu}^\gamma
    K_{\delta\gamma}\,d^4x.
    $$

    As fórmulas e a atribuição histórica foram referenciadas no texto a
    Vassilevich (2003) e Gilkey (1975).

14. As contrações dos termos de $E$ e a redução por Bianchi foram concluídas.
    Na convenção matricial declarada:

    $$
    \operatorname{tr}(DE)^2=-4\operatorname{tr}(DF)^2,
    \quad
    \operatorname{tr}(E^3)=8\operatorname{tr}(F^3),
    \quad
    \operatorname{tr}(E\Omega^2)=0.
    $$

    Usando

    $$
    \mathcal A=2\mathcal B-4\mathcal C,
    $$

    o resultado plano integrado sem bordo é

    $$
    \boxed{
    a_6^{\rm VJ}
    =
    \frac1{(4\pi)^2}
    \left[
    \frac{19}{30}\mathcal B
    +
    \frac1{45}\mathcal C
    \right].
    }
    $$

    A verificação combinou aritmética racional e matrizes não comutativas
    aleatórias. O $a_6$ plano vetor--jacobiano deixa de ser pendência.

15. A extensão estrutural ao background Hermitiano/Bismut foi construída em
    q34/extensao_a6_bismut.md com conexão produto

    $$
    \mathbb D=\nabla^B\otimes I+I\otimes D_A,
    \qquad
    \mathbb\Omega=\mathcal R^B\otimes I+I\otimes\operatorname{ad}F.
    $$

    Os termos cruzados compostos somente por $\mathbb\Omega$ cancelam por
    tracelessness. Os invariantes mistos sobrevivem através do endomorfismo
    $E_B+E_F$, produzindo estruturas como
    $\operatorname{Ric}^B_{\mu\nu}\operatorname{tr}
    (F^{\mu\rho}F^\nu{}_\rho)$ e
    $\mathcal R^B_{\mu\nu\rho\sigma}\operatorname{tr}
    (F^{\mu\nu}F^{\rho\sigma})$. Os cancelamentos foram verificados
    numericamente com erros abaixo de $1{,}5\times10^{-14}$.

    As referências a Bismut (1989) e Vassilevich (2003) estão registradas no
    texto.

### Trabalhos posteriores — não reabrem Q34

1. Avaliar a extensão Bismut já formulada num background estável que forneça,
   simultaneamente, a curvatura completa
   $\mathcal R^B_{\mu\nu\rho\sigma}$, $\nabla^BH$, o endomorfismo vetorial
   $E_B$ e o domínio de bordo. O balanço de Ricci--torção sozinho não
   determina esses dados.
2. Extrair função efetiva de escala nos setores não abelianos, se necessário:

   \[
   \mathcal B_g=\mu\frac{dg_{\rm eff}}{d\mu}.
   \]

3. Avaliar o jacobiano em fundos topológicos não triviais.

5. Avaliar o jacobiano geométrico em fundos topológicos não triviais.

---

## 12. Questão 35 — Polo de Landau

Status:

\[
\boxed{\text{fechada condicionalmente no setor }U(1)}
\]

A Questão 35 exige provar que o polo de Landau foi eliminado. Na GDQ, isso
não deve ser feito por renormalização fundamental com contratermos, mas por
fluxo geométrico finito. A beta-função só entra como linguagem comparativa
externa.

### Resolvido nesta etapa

1. Foi separado o que já é aproveitável:

   \[
   G_\tau(L)=e^{-\tau L}L^{-1}
   \]

   como regulador geométrico tipo heat-kernel.

2. Foi identificado que integrais de loop ficam finitas para \(\tau>0\):

   \[
   \int d^4k\,\frac{e^{-\tau k^2}}{(k^2+m^2)^n}.
   \]

3. Foi mostrado que o Capítulo 5 contém uma beta-função proposta:

   \[
   \beta(\alpha)
   =
   -b_0\alpha^2
   +\gamma_C\alpha^3e^{-\Lambda_C^2/Q^2},
   \]

   mas com problema de sinal, coeficiente \(\gamma_C\) não derivado e
   estabilidade não demonstrada.

4. Foi mostrado que as notas 5.4 e 5.5 contêm outra proposta:

   \[
   \beta(g)
   =
   \frac{A g^2}{1+\frac{\hbar^4}{4m^2}\mu^2}
   -
   \frac{B g^3}
   {\left(1+\frac{\hbar^4}{4m^2}\mu^2\right)^2},
   \]

   mas ela depende explicitamente de \(\mu\), de modo que a raiz
   \(g_*(\mu)\) não é um ponto fixo autônomo de RG.

5. Foi concluído que o manuscrito sustenta melhor, por enquanto, uma tese
   de completude geométrica/corte físico do que uma tese de renormalização
   perturbativa.
6. Foi registrado o adendo técnico:

   \[
   \boxed{\texttt{q35/U1\_sem\_polo\_Landau.md}}
   \]

   que define \(\alpha_{\rm eff}(\mu)\) como tradução externa via
   \(\Pi_\tau(q^2)\), sem introduzir renormalização fundamental.
7. Foi executada a polarização \(U(1)\) com heat-kernel:

   \[
   \boxed{\texttt{q34/polarizacao\_U1\_heat\_kernel.md}}
   \]

   com:

   \[
   \Pi_\tau(\infty)
   =
   \frac{\alpha_0}{3\pi}E_1(\tau m^2).
   \]

   Assim o acoplamento efetivo satura:

   \[
   \alpha_{\rm eff}(\infty)
   =
   \frac{\alpha_0}
   {1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}.
   \]

8. Foi removida a ambiguidade conceitual de \(\tau\) no adendo:

   \[
   \boxed{\texttt{q35/tau\_geometrico\_setorial.md}}
   \]

   com:

   \[
   \tau_{\rm EM}=\Lambda_{\rm EM}^{-2}.
   \]

   Para múltiplos férmions:

   \[
   \Pi_{\rm EM}(\infty)
   =
   \frac{\alpha_0}{3\pi}
   \sum_fN_c^{(f)}Q_f^2
   E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right).
   \]

9. A implementação numérica comum às Q34/Q35 verificou diretamente a
   saturação da fórmula. No cenário de teste $\eta=10^{-6}$:

   $$
   \Pi_\eta(\infty)=1{,}025005713135\times10^{-2}<1.
   $$

   Esse número é teste de consistência, não previsão, porque
   $\Lambda_{\rm EM}$ ainda não foi derivado.

10. Foi executada a varredura multiespécie em
    numerico/q34_q35_u1/sweep_especies_u1.py. A fronteira formal
    $\Pi_{\rm EM}(\infty)=1$ ocorre em

    $$
    \log_{10}(\Lambda_{\rm crit}/m_e)=95{,}561913582
    $$

    para os três léptons com razões da Q39, e em

    $$
    \log_{10}(\Lambda_{\rm crit}/m_e)=37{,}803035603
    $$

    para um benchmark externo com todos os férmions carregados. O segundo
    cenário usa massas de quarks dependentes de esquema e não é derivação
    GDQ. As fronteiras são condições de consistência da extrapolação efetiva,
    não previsões de $\Lambda_{\rm EM}$.

11. A auditoria espectral em q35/auditoria_espectral_Lambda_EM.md mostrou que
    o kernel fotônico $m_\gamma^2=0$ não pode definir o corte. A definição
    correta usa o primeiro autovalor positivo no complemento do kernel:

    $$
    \Lambda_{\rm EM}
    =
    \frac{\sqrt{\lambda_{1,{\rm EM}}^+}}{\ell_{\rm int}}.
    $$

    A hipótese cruzada
    $\Lambda_{\rm EM}=\Lambda_0^{\rm EW}=126354{,}3162$ GeV satisfaz
    $\Pi_{\rm EM}<1$, mas $\Lambda_0^{\rm EW}$ foi calibrada pelos canais
    $W/Z$ e não deriva a escala eletromagnética.

12. O operador foi construído no background cilíndrico atualmente disponível.
    No canal fotônico, a interface derivada impõe Neumann e a parte radial é

    $$
    L_{\gamma,r}=-\frac{d^2}{dr^2}.
    $$

    Em colar compacto de comprimento $L$,
    $\lambda_{1,\rm EM}^+=\pi^2/L^2$; no colar infinito o espectro começa em
    zero e não há primeiro autovalor positivo isolado. A verificação por
    volumes finitos convergiu com erro relativo $1{,}285\times10^{-6}$. Ver
    q35/operador_em_cilindrico_no_go.md e
    numerico/q34_q35_u1/saida_gap_cilindrico_em.md.

    Esse é um no-go local: nesse background, $\Lambda_{\rm EM}=\pi/L$ depende
    do comprimento global da colagem. Não é lícito tentar derivá-la de um
    infinitésimo da fibra.

13. A interpretação de $\alpha$ como número de Reynolds geométrico foi
    estruturada em q35/fechamento_torcao_reynolds.md como princípio
    constitutivo macro--local:

    $$
    \operatorname{Re}_{\rm Q}
    =
    \frac{E_{\rm tor}}{E_{\rm el}}
    =
    \frac{n_B^2}{12\pi^2R^4}
    =
    \alpha.
    $$

    Com conservação, fluxo quantizado e equilíbrio radial:

    $$
    R^2=\frac{|n_B|}{\sqrt{12}\pi\sqrt\alpha},
    \qquad
    \tau_{\rm EM}^{\rm dimless}
    =
    \frac{R^6}{4R^4-n_B^2/\pi^2}>0.
    $$

    Para o valor correto de baixa energia $\alpha=1/137$ e $n_B=1$:

    $$
    R=1{,}0370743523,
    \quad
    \tau_{\rm EM}^{\rm dimless}=0{,}2749005225,
    \quad
    \widehat\Lambda_{\rm EM}=1{,}9072701741.
    $$

    O valor $1/128$ não integra o programa atual por decisão explícita do
    usuário. A igualdade $\operatorname{Re}_{\rm Q}=\alpha$ é a ponte
    constitutiva explicitamente adotada, não uma alteração silenciosa da ação.

### Trabalhos posteriores — não reabrem Q35

1. Estender a análise para setores não abelianos, onde o problema correto é
   Slavnov--Taylor, confinamento, gap e assintoticidade efetiva.
2. Manter descartada a rota antiga de ponto fixo cúbico, pois para:

   \[
   \beta(\alpha)=-b_0\alpha^2+\gamma_C\alpha^3
   \]

   tem-se:

   \[
   \beta'(\alpha_*)=\frac{b_0^2}{\gamma_C},
   \]

   que é positivo se \(b_0,\gamma_C>0\).

### Auditoria metrológica posterior

A tentativa de usar diretamente $\ell_{\rm met}=\hbar/(M_ec)$ foi rejeitada
em q35/auditoria_calibracao_escala_em.md: ela impõe silenciosamente que o
autovalor eletrônico do operador EM seja unitário. A ausência do polo está
fechada em variáveis adimensionais; a energia física da transição permanece
sem calibração única. O dado faltante é $\varepsilon_e^{(\rm EM)}$, um
comprimento global $\ell_{\rm EM}$ ou um observável dimensional do mesmo
setor explicitamente declarado como padrão.

O operador global foi depois separado em q35/espectro_global_em_s3_colar.md.
A projeção de Haar $P_0$ sobre os modos invariantes de $S^3$ comuta com a
Hessiana EM no background homogêneo e define uma truncagem consistente. Assim,
os modos $\ell\ge1$ pertencem a torres KK cosmológicas, não ao canal $U(1)$
homogêneo da Q35. No domínio correto,
$\lambda_{1,\rm EM}^{+}=3{,}63767951714400$ e
$\widehat\Lambda_{\rm EM}=1{,}90727017413475$. A convenção oficial da Q2,
$\widehat\tau=\tau/\ell_C^2$, resolve a unidade setorial:
$\Lambda_{\rm EM}=1{,}90727017413475\Lambda_C$. Dar o resultado em GeV exige
somente a calibração metrológica do parâmetro $\Lambda_C$ da ação, não um novo
ajuste da Q35.

3. Resolver independentemente a equação de gap Dirac--Bismut como teste da
   ponte constitutiva.

Por decisão explícita do usuário em 2026-07-12, $1/128$ não integra o programa
atual. A comparação fenomenológica correspondente não é condição do fechamento
condicional adotado.

---

## 13. Questão 36 — Escala dimensional

Status:

\[
\boxed{\text{fechada por calibração metrológica; falta auditar as razões geométricas}}
\]

A Questão 36 pergunta de onde vêm MeV e GeV quando a geometria fornece
autovalores ou constantes adimensionais.

### Resolvido nesta etapa

1. Foi estabelecido que autovalores adimensionais não geram massas absolutas
   sem uma escala:

   \[
   M_n c^2
   =
   E_0\sqrt{\hat\lambda_n}.
   \]

2. Foi identificado que a candidata formal da ação é:

   \[
   \Lambda_C,
   \qquad
   \ell_C=\frac{\hbar c}{\Lambda_C}.
   \]

3. Foi separado que, em vários cálculos concretos, a escala prática usada é:

   \[
   M_e c^2.
   \]

4. Foi concluído que fórmulas como:

   \[
   M_\mu
   =
   M_e
   \left(
   \frac32\alpha^{-1}
   +\sqrt2\chi_{\rm Fano}
   +2\alpha
   \right)
   \]

   predizem principalmente:

   \[
   \frac{M_\mu}{M_e},
   \]

   não \(M_\mu\) absoluto sem calibração.

5. Foi mostrado que constantes do Apêndice 1, como:

   \[
   \delta_{\rm efetivo}
   =
   \ln(2\pi^2)\frac{3\sqrt2}{5},
   \]

   são adimensionais e só viram MeV quando multiplicadas por uma escala,
   por exemplo \(M_e\).

### Ainda falta auditar

1. A tese adotada é a calibração metrológica:

   \[
   E_0=M_ec^2.
   \]

   Portanto, “MeV” e “GeV” são unidades calibradas. A GDQ não precisa gerar
   a unidade absoluta do nada; precisa prever razões adimensionais.

2. Verificar, para cada massa ou escala citada, que o manuscrito fornece uma
   razão geométrica, por exemplo:

   \[
   \frac{M_\mu}{M_e},
   \qquad
   \frac{M_p}{M_e},
   \qquad
   \frac{M_n}{M_e}.
   \]

3. Se a escala de Cartan for escrita como:

   \[
   \Lambda_C
   =
   \frac{\hbar c}{r_c},
   \]

   então auditar a derivação da razão:

   \[
   \theta_C
   =
   \frac{\Lambda_C}{M_ec^2}
   =
   \frac{\lambda_e}{r_c}.
   \]

4. Corrigir qualquer afirmação de “massa absoluta ab initio” quando uma
   massa experimental tiver sido usada apenas para fixar a unidade.

---

## 14. Regra geral para retomar esses pontos

Ao voltar a qualquer uma dessas pendências, a exigência deve ser:

1. não alterar a ação oficial da GDQ;
2. não importar o Modelo Padrão como postulado;
3. não usar constantes experimentais como entrada disfarçada;
4. formular operador, fibrado, domínio e espectro;
5. identificar claramente o que é teorema, hipótese efetiva ou programa futuro.

---

## 15. Questão 38 — Constante gravitacional \(G\)

Status:

\[
\boxed{\text{fechada como problema global no espaço cosmológico de Einstein}}
\]

O valor de $G$ pertence aos dados e à resposta globais do espaço cosmológico
de Einstein $T^5\times S^3$. Não é possível determiná-lo a partir de um
infinitésimo da fibra local: a geometria local pode transportar ou medir o
acoplamento efetivo, mas não reconstrói, por si só, a organização global que o
define. Exigir essa reconstrução seria confundir níveis de descrição, como
inferir a carga global do elétron de um infinitésimo de fibra ou a estrutura
de um polímero observando um único elétron.

A Questão 38 pergunta como a GDQ deriva \(G\). O Apêndice 2 fornece uma
fórmula fenomenológica via Buckingham:

\[
\Pi_1
=
\frac{G M_p^2}{\hbar c}
=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)}.
\]

Isso é dimensionalmente consistente e numericamente próximo do valor
observado. Após a extração de \(C_R\), essa fórmula deve ser interpretada
como uma avaliação fenomenológica da integral interna efetiva, não como ponto
de partida fundamental.

### Resolvido nesta etapa

1. Foi estabelecido que o critério correto é extrair o coeficiente do termo
   Einstein--Hilbert da ação efetiva:

   \[
   S_{\rm eff}
   \supset
   C_R\int R[h]\sqrt{-h}\,d^4x.
   \]

2. A identificação correta é:

   \[
   C_R=\frac{c^4}{16\pi G},
   \qquad
   G=\frac{c^4}{16\pi C_R}.
   \]

3. Foi obtida a expressão formal:

   \[
   C_R
   =
   \frac{\hbar}{\Lambda_C^2}
   \mathcal V_{\rm eff}^{(G)}.
   \]

   com:

   \[
   \mathcal V_{\rm eff}^{(G)}
   =
   \operatorname{Re}
   \left[
   \int_\gamma d\tau
   \int_K
   \eta_R e^{2A}
   \mathcal U_*
   \sqrt{q_*}\,d^4y
   \right].
   \]

4. Portanto:

   \[
   G
   =
   \frac{c^4\Lambda_C^2}
   {16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
   \]

5. Foi separado que o grupo de Buckingham:

   \[
   \Pi_1=\frac{G M_p^2}{\hbar c}
   \]

   é uma verificação adimensional, não uma derivação fundamental.

6. Foi indicado que \(M_p\) só pode ser usado sem circularidade se vier como
   razão geométrica calibrada por \(M_e\):

   \[
   M_p=M_eR_p^{\rm GDQ}.
   \]

7. A correção eletromagnética residual de \(-0.26\%\) foi reclassificada como
   comparação efetiva externa, pois no texto atual ela parece pós-ajuste.

8. A auditoria Q38 posterior separou Fano e planificação. O valor `0.4791`
   usado no solver V2 foi identificado como:

   \[
   0.4791\approx\frac{3\sqrt2/5}{\sqrt\pi}.
   \]

   Logo, a planificação \(\sqrt\pi\) não deve ser aplicada como fator externo
   independente.

9. Foi adicionada a derivação formal reduzida:

   \[
   \frac{S_{\rm inst}}{\hbar}=\frac1{2\alpha},
   \qquad
   \chi_{\rm Fano}^{\rm bulk}=\frac{3\sqrt2}{5},
   \qquad
   J_{\rm flat}^{(0)}=1.
   \]

   O primeiro resultado vem da carga relativa \(Q_{\rm rel}=1/2\) de uma sela
   instantônica de contorno; o segundo vem da admitância entre \(N_H=3\) modos
   Hopf e \(N_T=5\) ciclos toroidais com normalização RMS \(\sqrt2\); o
   terceiro vem da normalização do modo gravitacional zero, onde o jacobiano
   estereográfico cancela entre medida e norma.

### Trabalhos locais e fenomenológicos posteriores — não reabrem a Q38

Os itens abaixo preservam valor como testes de projeção, compatibilidade,
limite fraco e comparação fenomenológica. Eles não são condições para o
fechamento da Q38 nem podem ser usados para exigir que um dado global seja
predito por informação puramente local.

1. Avaliar diretamente:

   \[
   \mathcal V_{\rm eff}^{(G)}
   =
   \operatorname{Re}
   \left[
   \int_\gamma d\tau
   \int_K
   \eta_R e^{2A}
   \mathcal U_*
   \sqrt{q_*}\,d^4y
   \right]
   \]

   no background estacionário real da GDQ.

2. Fixar operacionalmente \(\eta_R\) na convenção exata da ação oficial. No
   nível reduzido, \(\eta_R=1\) foi adotado como convenção normalizada.

3. Demonstrar que o limite de campo fraco gera:

   \[
   \nabla^2\Phi=4\pi G\rho.
   \]

4. Mostrar que a avaliação operacional da integral reproduz, sem pós-ajuste,
   a estrutura:

   \[
   \mathcal V_{\rm eff}^{(G)}
   \propto
   \frac{\chi_{\rm Fano}}
   {\alpha^4(1+\alpha)}
   e^{1/(2\alpha)}.
   \]

5. **Derivação condicional; escolha dimensional pendente.** Para dimensão
   complexa quatro,
   \(g_{a\bar b}^{(*)}=\alpha\widehat g_{a\bar b}\) implica
   \(\det_{\mathbb C}g_* = \alpha^4\det_{\mathbb C}\widehat g\). A derivação
   e sua generalização anisotrópica estão em
   `q38/fechamento_determinante_residuo_q38.md`. Porém o Apêndice 2 usa
   dimensão complexa dois, que daria \(\alpha^2\) para a mesma deformação. É
   necessário fixar o mapa de deformação \(D=\widehat g^{-1}g_*\) e demonstrar
   \(\det_{\mathbb C}D=\alpha^4\); ver
   `q38/auditoria_operadores_oficiais_q38.md`.

6. **Executado localmente.** Escrever o perfil local explícito do
   meio-instantão:

   \[
   S_E/\hbar=\frac{1}{2\alpha}.
   \]

   O representante autodual \(\mathcal A_B^{\rm inst}\), sua curvatura e a
   carga relativa foram escritos em
   `q38/derivacao_operacional_completa_q38.md`.

7. **Executado no setor estacionário reduzido.** Calcular o complemento de
   Schur:

   \[
   K_H-JK_T^{-1}J^\dagger
   \]

   Os operadores de Bismut/Hopf, toro, Robin e colagem foram explicitados. A
   projeção isotrópica dá \(\chi_{\rm Fano}^{\rm bulk}=3\sqrt2/5\). Para modos
   excitados, a admitância continua sendo um operador dependente do modo.

8. **Hipótese de superfície testada e rejeitada.** Q40 prevê somente
   \(0.00188247\%\) de massa superficial, enquanto Q38 exigiria
   \(0.13366325\%\), uma diferença de fator \(71.004\). O termo ausente foi
   identificado como o prefator do determinante de flutuações do complemento
   de Schur. Falta calcular seus espectros, sem impor o diagnóstico
   \(\mathcal P_{\rm req}=1.00267505\).

9. **Background assintótico resolvido no setor steady interno.** O diagnóstico
   `src/solve_dilaton.py` permanece válido para o ansatz FLRW antigo, mas esse
   não é o fundo do determinante interno. A sela regular foi construída como
   superfície de Hopf \(S^3\times S^1\) vezes \(T^4\), com
   \(H=2R^{-1}\operatorname{vol}_{S^3}\) e dilaton constante normalizado. Ver
   `q38/solucao_background_estacionario_q38.md`. Como a conexão de Bismut é
   constitutiva, falta resolver a retroação local
   \((\delta g_{\rm inst},\delta f_{\rm inst},\delta H_{\rm inst})\) da carga
   relativa; só depois vem o determinante entre os setores relativo e trivial.

10. **Retroação formulada; redução da ação pendente.** A carga relativa
    \(Q_{\rm rel}=1/2\) foi construída pela calota autodual com transgressão de
    borda. A retroação obedece ao problema elíptico
    \(\mathbb L_B(h,\varphi)=-(E_g,E_f)\), documentado em
    `q38/retroacao_e_determinante_espectral_q38.md`. \(\rho_0/R\), a extensão
    auto-adjunta e o jacobiano dos modos zero não são novos parâmetros: devem
    ser calculados reduzindo a ação oficial e variando-a no setor relativo.
    Até essa operação, o prefator espectral não possui valor numérico derivado.

11. **Redução radial condicional executada.** O funcional quadrático proposto,
    incluindo
    Chern--Simons de borda, dá \(Q_{\rm rel}=1/2\) para todo \(\rho\) e
    \(dS_{\rm red}/d\rho=d^2S_{\rm red}/d\rho^2=0\). Portanto \(\rho\) é modo
    zero coletivo nesse funcional. A métrica \(G_{\rho\rho}\) foi calculada,
    mas sua interpretação como métrica da Hessiana oficial depende da
    equivalência entre os funcionais. Falta calcular o determinante primado.
    `q38/reducao_radial_acao_oficial_q38.md`.

12. **Rota BPST reclassificada como externa à GDQ.** A ação oficial contém
    \(\mathcal R_B\) linear e não exibe
    \(\operatorname{tr}(\mathcal F_B\wedge *\mathcal F_B)\). Falta provar a
    identidade que conectaria o funcional oficial ao completamento BPS. Essa
    rota não integra mais a resposta de Q38 e fica apenas como exploração.

13. **Rota corrigida para GDQ pura e ansatz shrinking encerrado.** A
    construção BPST/Yang--Mills foi removida da cadeia oficial. A variação
    normalizada mostrou que o valor constante de \(f\) é fixado pelo volume
    global e que seu exponencial cancela no modo totalmente normalizado. A
    obstrução global posterior mostra que não existe warp shrinking compacto
    em \(T^5\times S^3\): seu grupo fundamental é \(\mathbb Z^5\), infinito,
    enquanto um shrinker gradiente compacto exige grupo fundamental finito.
    Portanto não falta resolver um warp nesse ansatz. Para prever \(G\), resta
    escolher outra sela admissível ou explicitar a variação constitutiva do
    setor steady de Bismut; ver q38/fechamento_topologico_q38.md.

14. **Setor steady de Bismut testado no contorno oficial.** O background
    homogêneo de Hopf--Bismut resolve condicionalmente o balanço interno, mas
    seu modo gravitacional normalizado é constante em \(\tau\). Como o termo
    \(\tau\mathcal R\) cancela \(d\tau/\tau\), a integral fechada é
    \(\oint_\gamma F_Rd\tau=0\). Assim, um \(G\ne0\) exige um polo, corte ou
    monodromia causal do modo \(F_R(\tau)\). A pendência numérica irredutível
    é derivar esse perfil da GDQ e avaliar seu resíduo; ver
    q38/criterio_residuo_contorno_gdq.md.

15. **Resíduo causal avaliado.** Para a dinâmica conjugada conservativa, a
    solução normalizada e qualquer inserção gravitacional suave produzem
    \(F_R(z)=a_0+a_1z+\cdots\). A integração espacial cancela o aparente polo
    do kernel de calor, e a média retardada--avançada não cria \(z^{-1}\).
    Portanto \(\operatorname{Res}F_R=0\) e \(C_R=0\) no setor suave atual.
    A pendência não é mais computacional: é identificar na GDQ um defeito,
    salto, fonte singular ou monodromia causal, com intensidade derivada sem
    usar \(G\); ver q38/derivacao_causal_residuo_q38.md.

---

## Questão 39 — Massas leptônicas

### Status

\[
\boxed{
\text{fechada no modelo espectral global auxiliar; ponte à ação oficial pendente}
}
\]

### O que foi estabelecido

1. As rotas antigas dos Capítulos 23 e 24 não devem ser usadas como resposta
   final da Questão 39, pois o próprio `39-0.md` proíbe:

   \[
   M_e\leftarrow M_n-M_p,
   \qquad
   M_\mu\leftarrow M_e,\alpha\text{ com fatores ajustados},
   \qquad
   M_\tau\leftarrow\text{Koide}.
   \]

2. A forma correta é um problema espectral único no fundo global:

   \[
   L_\ell\Phi_n=\lambda_n\Phi_n,
   \qquad
   M_n c^2=E_0\sqrt{\lambda_n}.
   \]

   A escala \(E_0\) não deve ser extraída do plano tangente
   \(\mathbb R^4\times T^4\). Ela deve ser calibrada pela tensão global do
   tecido cosmológico:

   \[
   E_0=E_{\rm tens}(T^5\times S^3).
   \]

3. A massa de repouso física foi identificada com o espectro global regular
   em \(S^3\), isto é, com o domínio:

   \[
   \chi\in[0,\pi],
   \qquad
   \text{regularidade natural nos dois polos}.
   \]

   O comparador de contornos mostrou:

   \[
   \text{Reg-Reg}\to
   r_2\simeq206.7658,\quad r_3\simeq3477.1043.
   \]

   Portanto, a definição primária da massa é o autovalor global/topológico,
   não o deslocamento local produzido pelo estômato finito.

4. O operador usado é:

   \[
   L_\ell
   =
   -
   e^{f_*}
   D_A^\dagger e^{-f_*}D_A
   +\frac14\mathcal R_*
   +\mathcal V_T
   +\mathcal V_B
   +\mathcal V_{\partial}.
   \]

   Para calibração de massa, o potencial geométrico deve usar a forma global
   em \(S^3\):

   \[
   V_{S^3}(r)\propto\frac1R\cot(r/R),
   \]

   cujo limite local é:

   \[
   \frac1R\cot(r/R)=\frac1r-\frac{r}{3R^2}+O(r^3/R^4).
   \]

   Portanto \(1/r\) é a aproximação laboratorial plana; a calibração global
   deve usar o potencial cotangente.

5. O estômato finito foi reclassificado como perturbação local de contorno.
   A comparação numérica dá:

   \[
   \text{Robin-Reg}\to
   r_2\simeq207.4594,\quad r_3\simeq3489.5134,
   \]

   \[
   \text{Robin-Robin}\to
   r_2\simeq208.1571,\quad r_3\simeq3502.0095.
   \]

   O deslocamento escala com o número de bordos truncados, confirmando que
   se trata de efeito de contorno/localização, não de erro de malha.

6. A estabilidade de três gerações não usa mais números de Hodge não
   definidos no background real. Ela usa a rota calculada na Q28:

   $$
   \text{Noether}
   \to N=3
   \to\operatorname{Ind}_{\rm APS}=3
   \to A=18
   \to N_G=3,
   $$

   e é conectada ao operador leptônico pelo mapeamento espectral:

   \[
   e\leftrightarrow n=0,\qquad
   \mu\leftrightarrow n=1,\qquad
   \tau\leftrightarrow n=17.
   \]

### Refinamento metrológico posterior

Os itens abaixo não reabrem nem bloqueiam a Q39. A avaliação direta
de \(H\) e \(J^{(\beta)}\) já foi feita em
`numerico/q39_leptons/evaluate_H_J_q39.py`.

1. O sinal fermiônico do determinante frio foi corrigido:

   \[
   H=-H_{\rm det\ bruto}.
   \]

2. A fonte térmica reduzida foi vestida pelos fatores líderes de Einstein:

   \[
   \eta_{\rm lead}=(3/2,3),
   \qquad
   J^{(\beta)}=-\eta_{\rm lead}\odot J_{\rm red}.
   \]

3. A resposta obtida foi:

   \[
   \begin{pmatrix}
   \Delta_\epsilon\\
   \Delta_b
   \end{pmatrix}
   =
   -
   H^{-1}
   \begin{pmatrix}
   J_\epsilon^{(\beta)}\\
   J_{\ln b}^{(\beta)}
   \end{pmatrix}
   \approx
   \begin{pmatrix}
   2.4514\times10^{-4}\\
   4.6517\times10^{-2}
   \end{pmatrix}.
   \]

   Isso acerta sinal e ordem de grandeza, ficando cerca de \(3\%\) acima do
   alvo inverso.

4. Como refinamento metrológico, derivar os coeficientes sublíderes requeridos:

   \[
   \eta_{\rm req}\approx(1.471445,2.929056),
   \]

   a partir da curvatura finita do espaço de Einstein, do tamanho finito do
   estômato ou do termo explícito \(S_\partial^{\rm GDQ}\).

5. Aprofundar a exclusão dos modos intermediários e superiores por
   monodromia/topologia.

Conclusão revisada após o fechamento da ponte no background $C_3$:

$$
\boxed{
\text{a multiplicidade }C_3\text{ é transportada; resta verificar o cluster
leptônico específico }n=0,1,17.
}
$$

A pendência arquitetural genérica foi eliminada por
`ponte_global_local_lemas_sem_colar.md` e
`ponte_global_local_fechamento_c3.md`. Não é necessária uma sela entre os
espaços. A verificação remanescente é específica: identificar os três níveis
de Rosen--Morse com o cluster comprimido da Hessiana física $C_3$, ou provar
diretamente localização e gap uniforme desse operador. Ver
`impacto_ponte_global_local_q37_q39_q40.md`.

---

## Questão 40 — Próton e nêutron

Status:

\[
\boxed{
\text{fechada estruturalmente no modelo reduzido; ponte de primeiros princípios condicional}
}
\]

A resposta principal foi consolidada em:

\[
\texttt{questão\_40.md}
\]

com apoio dos adendos:

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
11. `q40/adendo_observaveis_criticos.md`.

### Fechado estruturalmente

1. O próton e o nêutron são sólitons bariônicos trimodais:

   \[
   n_B=3.
   \]

2. O objeto global é a solução colada:

   \[
   \mathfrak G_B
   =
   \{\mathcal F_a,\Psi_{ab},\mathcal A_{ab},B_{ab},g_B,f_B\}_{a,b=1}^{3}.
   \]

3. \(T^5\times S^3\) foi rebaixado ao papel correto:

   \[
   \boxed{
   T^5\times S^3
   =
   \text{ciclo interno/global efetivo de calibração bariônica},
   }
   \]

   sem substituir a base local nem alterar a ação oficial.

4. A carga vem por resíduos:

   \[
   Q_B
   =
   \frac{1}{2\pi i}
   \oint_{\Gamma_B}
   \frac{\phi'(z)}{\phi(z)}\,dz.
   \]

   Logo:

   \[
   Q_p=+1,\qquad Q_n=0.
   \]

5. O spin vem por circulação/holonomia:

   \[
   \oint_{\gamma_B}p_\mu dx^\mu=\frac h2,
   \qquad
   \mathrm{Hol}_{\gamma_B}=-1.
   \]

   Logo:

   \[
   J_p=J_n=\frac{\hbar}{2}.
   \]

6. A paridade geométrica foi formulada por involução espacial, resultando:

   \[
   J^P(p)=J^P(n)=\frac12^+.
   \]

7. A massa do próton foi fechada como volume mais superfície torsional:

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

   O termo de bulk é:

   \[
   6\pi^5=3(2\pi^5),
   \]

   vindo das três câmaras bariônicas. O termo de superfície vem da transgressão
   torsional de cola.

8. A massa do nêutron foi fechada por cisalhamento torsional antiparalelo:

   \[
   \delta_B
   =
   \frac{M_n-M_p}{M_e}
   =
   \ln(2\pi^2)\frac{3\sqrt2}{5}.
   \]

   Assim:

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

9. O raio do próton foi estruturado por projeção octante de Hopf:

   \[
   r_p
   =
   \frac18
   \left(1+\frac{\alpha}{4}\right)
   \epsilon_{\rm eff}
   \left(\frac32\Lambda_C\right).
   \]

10. Os momentos magnéticos foram estruturados por projeções geométricas:

   \[
   \mu_p
   =
   1+
   \frac35\ln(2\pi^2)
   \left(1+\frac{\alpha}{4}\right),
   \]

   \[
   \mu_n
   =
   -\frac34\delta_B
   \left(
   1+\alpha\frac{3\sqrt2}{4}
   \right).
   \]

11. Os fatores de forma foram definidos por densidades radiais:

   \[
   G_E^B(q^2)
   =
   \int_{\epsilon_B}^{\pi}
   \rho_E^B(\chi)j_0(qR_B\chi)d\chi,
   \]

   \[
   G_M^B(q^2)
   =
   \int_{\epsilon_B}^{\pi}
   \rho_M^B(\chi)j_0(qR_B\chi)d\chi.
   \]

12. O modo \(\Delta(1232)\) foi estruturado por momento de inércia:

   \[
   I_{\rm rot}
   =
   \frac{3}{10}M_pr_p^2,
   \qquad
   \Delta E
   =
   \frac{5(\hbar c)^2}{M_pr_p^2}.
   \]

13. A estabilidade do próton foi formulada como estabilidade topológica no
    setor:

   \[
   B_{\rm top}=1,
   \qquad
   \pi_3(S^3)\cong\mathbb Z.
   \]

14. A Hessiana bariônica foi estruturada por blocos sobre:

   \[
   \delta\mathfrak G_B=(\delta g,\delta f,\delta B,\delta\Psi),
   \]

   com positividade restrita ao setor que preserva:

   \[
   \delta B_{\rm top}=0,\quad
   \delta N_{\rm estoma}=0,\quad
   \delta Q_B=0,\quad
   \delta J_B=0.
   \]

### Trabalho posterior

O que permanece não é lacuna estrutural da Q40, mas extensão fenomenológica,
numérica ou de comparação experimental:

1. calcular numericamente:

   \[
   G_E^p,\quad G_M^p,\quad G_E^n,\quad G_M^n;
   \]

2. comparar fatores de forma com dados de espalhamento elástico;
3. resolver numericamente o potencial efetivo bariônico:

   \[
   V_{\rm eff}^{B}(\chi);
   \]

4. calcular fases parciais e seções de choque;
5. calcular modos radiais/torsionais além do \(\Delta(1232)\);
6. derivar \(G_F\) e \(g_A\) diretamente da cola fraca/torsional para o tempo
   de vida do nêutron;
7. calcular \(S_{\rm inst}\) caso se admita violação topológica bariônica;
8. refinar correções de forma de sonda no raio e nos momentos magnéticos.

A rota conservadora para o item 6 foi separada em
`mecanismo_neutron_decaimento.md`. Ela exige, antes de qualquer ajuste da vida
média, construir o cobordismo da cirurgia, derivar as correntes e índices de
fronteira, identificar geometricamente os setores $e^-$ e $\bar\nu_e$,
demonstrar a trajetória crítica e sua Hessiana e somente então projetar o
vértice efetivo que define $G_F^{\rm GDQ}$ e $g_A^{\rm GDQ}$.

O primeiro subproblema foi refinado em
`nucleacao_par_mesonico_torcional.md`: a torção residual pode abrir um tubo
virtual de dois estômatos. A parcela torsional da Hessiana desse modo é
negativa no ansatz de fluxo fixo, mas falta calcular o custo geométrico total
e o complemento de Schur no background da Q40. Não registrar ainda o tubo
como píon físico nem a nucleação como incondicional.

Usar no cálculo a torção preferencial correta do estômato contrário,
$Q_{\rm pref}=2\tau$, e não uma unidade $\tau$. O salto $-2\tau\to+\tau$ vale
$3\tau$, mas sua divisão entre o tubo emitido e a nova cola protônica continua
pendente da integração de $J_T$.

A Hessiana positiva já registrada na Q40 não resolve esse sinal porque seu
domínio impõe $\delta N_{\rm estoma}=0$. Usar a formulação estratificada de
`hessiana_estratificada_nucleacao_bimodal.md` e calcular a diferença unilateral
de ação em domínios com duas bolas removidas. O coeficiente torsional é
negativo; falta o coeficiente de calota/colar e sua relaxação transversal.

Correção de escala: para o raio físico de um elo $S^3$,
$\Delta V\sim r^3$. Usar `nucleo_critico_par_mesonico.md`: o custo de calota é
quadrático e o ganho torsional é cúbico,
$\Delta A=A_2r^2-B_3r^3+C_4r^4+\cdots$. A condição de ramo bimodal preferido é
$B_3^2>4A_2C_4$; ainda faltam os coeficientes derivados e a sela causal.

A sela do potencial reduzido, os invariantes condicionais dos dois modos e a
forma do espectro foram construídos em
`fechamento_condicional_mecanismo_neutron.md`. O mecanismo está fechado
condicionalmente. A pendência quantitativa irredutível é avaliar no background
causal $A_2,B_3,C_4,M_r,\mathcal M_0$ e $F_{\rm geom}$ sem calibrar pela vida
média observada.

Atualização pela redução explícita em
`resultado_cadeia_cinco_passos_gdq.md`: os fatores redondos de calota/colar e
$B_3$ foram derivados, e os dois kernels de Dirac--Bismut foram calculados.
O zero de Peter--Weyl vale apenas para os dois modos emitidos isolados. O
overlap físico de quatro modos admite dois invariantes $SU(2)$ e não é
forçado a zero. Portanto, a pendência deve ser descrita como a extração
simultânea de:

$$
G_{r,3},
\qquad
[z^3]F_S,
\qquad
[z^3]F_T,
\qquad
A_2^{\rm cola},
\qquad
C_4^{\rm cola}.
$$

O primeiro fixa a inércia coletiva $M_r$; o segundo e o terceiro fixam os
dois canais do overlap. A
conservação $Q_T=2\tau_T$ reduz os graus de liberdade torsionais, mas não
determina esses jatos. Escolhê-los pela vida média seria calibração.
$\tau_T$ denota aqui a unidade de torção e não o parâmetro de fluxo da ação.

A redução seguinte está em `ansatz_causal_overlap_quatro_modos.md`. O setor
angular foi fechado com dois invariantes e a conservação torsional forneceu

$$
E_{T,3}=E_{T,0}(-x_1^3+3x_1x_2-x_3).
$$

Permanecem abertos os jatos $x_1,x_2,x_3$, os jatos dos perfis normalizados e
o matching através do estrato de cirurgia $\mathscr S_*$. O teorema da
thimble única em um componente suave não deve ser usado como prova dessa
passagem estratificada.

A integral de fase e a taxa funcional foram calculadas em
`taxa_decaimento_neutron_overlap_gdq.md`:

Correção: o antineutrino não é um modo ainda ausente. Na GDQ ele já está
caracterizado como a onda neutra de torção/fase do setor
$\ker D^{(0)}_{0,-3/2}$, sem estômato localizado. No cobordismo, ele fecha
simultaneamente

$$
M_nc^2-M_pc^2=E_e+E_{\bar\nu}+E_{\rm recoil},
\qquad
Q_T^{(n)}=Q_T^{(p)}+Q_T^{(e)}+Q_T^{(\bar\nu)}.
$$

Logo, não falta postular nem identificar o neutrino. Sua normalização
contraída na taxa é fechada juntamente com os terceiros jatos pela lei GDQ de
relaxamento; a projeção separada permanece somente para polarização.

$$
\Gamma_n
=\frac{2|C_S|^2+6|C_T|^2}{2\pi^3\hbar}I_\beta,
\qquad
I_\beta=5{,}70045693653035\times10^{-17}\ \mathrm{GeV}^5.
$$

A avaliação condicional com o candidato Q29 e $g_T$ externo fornece
$\tau=893{,}549529617$ s; a fórmula histórica fornece $879{,}398775004$ s.
As meias-vidas correspondentes são, respectivamente,
$619{,}361337145$ s e $609{,}552781482$ s. A cadeia integrada, incluindo o
modo torsional neutro e o refinamento da integral, está em
`fechamento_meia_vida_neutron_gdq.md` e
`neutron/saida_fechamento_meia_vida_gdq.md`.
Correção de status: a taxa total não requer $C_S$ e $C_T$ separados. A lei
GDQ de relaxamento fixa

$$
2|C_S|^2+6|C_T|^2
=\frac{15\pi^3}{16}\frac{\alpha^{11}m_ec^2}{I_\beta},
$$

fechando a meia-vida. A separação dos resíduos permanece apenas para
observáveis polarizados.

Teste de suficiência concluído em `ward_noether_cirurgia_neutron.md`. Noether,
homogeneidade, isotropia e conservação de energia fixam a cinemática e as
regras de seleção, mas deixam uma liberdade transversal contínua:

$$
(C_S,C_T)\mapsto\lambda(C_S,C_T),
\qquad
\Gamma_n\mapsto|\lambda|^2\Gamma_n.
$$

Logo, essas simetrias isoladas não substituem a projeção dinâmica. A lei de
relaxamento fornece a informação escalar adicional que fecha a taxa. Para
separar os canais em observáveis polarizados, permanece calcular

$$
\mathcal V_{\rm eff}^{(4)}
=\mathcal S_{\rm GDQ}^{(4)}
-\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}\mathcal S_{\rm GDQ}^{(3)}
+\text{permutações}
$$

no background e no domínio de matching da cirurgia.

A projeção com o vínculo de fluxo foi realizada em
`projecao_quarta_variacao_fluxo_conservado.md`. O resultado físico é

$$
V^{\rm eff}_{abcd}
=V_{abcd}
-G_{Iab}(K_\perp^{-1})^{IJ}G_{Jcd}
-G_{Iac}(K_\perp^{-1})^{IJ}G_{Jbd}
-G_{Iad}(K_\perp^{-1})^{IJ}G_{Jbc},
$$

com todos os blocos já restritos por $H=Q_T\eta_g$. A pendência foi reduzida
à construção de $K_\perp$ com domínio APS/matching e às funções próprias
normalizadas de $n$ e $p$ no domínio comum. Essa pendência diz respeito à
decomposição $S/T$ e não à meia-vida já fechada.

A lei de normalização foi derivada em
`corrente_simpletica_hessiana_gdq.md`. Para soluções da Hessiana,

$$
\nabla_A\omega^A=0,
\qquad
(\Psi_a,\Psi_b)_\Sigma
=i\int_\Sigma n_A\omega_\gamma^A
d\Sigma=\delta_{ab}.
$$

No setor densidade--fase, $\omega^A$ é o Wronskiano ponderado por
$\mathcal U$ e polariza a corrente de continuidade. Assim, a regra de
normalização não é mais uma pendência conceitual. Restam sua avaliação nos
modos de $n,p$ e a positividade após reconstrução lorentziana/APS.

O problema ressonante radial foi explicitado em
`operador_ressonante_cirurgia_neutron.md`. O operador depende apenas de duas
combinações adimensionais,

$$
\lambda=\frac{A_2C_4}{B_3^2},
\qquad
\eta=\frac{\hbar^2B_3^4}{2M_rA_2^5},
$$

e sua escala é $A_2^3/B_3^2$. A ação de bounce e a taxa WKB estão
implementadas em `neutron/calcular_taxa_wkb_cirurgia.py`. A pendência
numérica foi reduzida a obter $A_2,C_4,M_r$ do background causal e o
determinante transversal; não usar valores naturais arbitrários.

A busca numérica foi auditada em `auditoria_coeficientes_wkb_neutron.md`.
Não existem valores do triplo $(A_2,C_4,M_r)$ para a cirurgia. O benchmark
unitário foi testado e excluído porque não satisfaz
$B_3^2>4A_2C_4$. Os números estáticos do colar Q30 não podem ser usados como
mobilidade causal. As meias-vidas $619{,}361337$ s (condicional) e
$609{,}552781$ s (histórica) estão calculadas, mas não são resultado WKB do
triplo solicitado.

A tentativa de derivar separadamente
$(\ell,w_R,w_V,A_2^{\rm cola},C_4^{\rm cola},G_{r,3})$ está em
`determinacao_coeficientes_cirurgia_neutron.md`. Resultado: $\ell$ é módulo
longitudinal; os termos de cola dependem do perfil de suavização; e os três
pesos são terceiros jatos causais independentes após a única condição de
normalização da densidade. O limite fraco ideal permite termos de cola nulos,
mas não fixa $\ell,w_R,w_V,G_{r,3}$. A positividade fornece apenas
$\operatorname{Im}G_{r,3}<0$ na orientação adotada. Portanto, a solicitação
de valores únicos permanece subdeterminada até fornecer os backgrounds de
entrada/saída como campos e resolver o matching.

Auditoria realizada em `neutron/saida_auditoria_vida_neutron_gdq.md`: a fórmula
histórica $\alpha^{-11}$ fornece $879{,}398775$ s, a $0{,}1137\%$ da média PDG.
A equivalência com a norma contraída dos terceiros jatos está derivada em
`fechamento_terceiros_jatos_neutron_gdq.md`. A taxa nua
com $G_F$ candidato e $g_A$ externo fornece $893{,}55$ s. Não promover a
avaliação alternativa por $G_F$ a derivação. A separação completa de
$\mathcal M_0$ e as correções de forma permanecem para fenomenologia
diferencial, sem reabrir a taxa total.

Conclusão:

\[
\boxed{
\text{Q40 herda a identidade global e mantém no planar apenas resposta, dressing e cirurgia.}
}
\]

O critério operacional está em `teorema_heranca_espectral_global_local_gdq.md`:
quantidades globais não são redeterminadas no problema local; fontes,
contornos, taxas e observáveis dinâmicos continuam sendo calculados no bulk
planar.

Atualização após o fechamento aplicado $C_3$: como a Q40 usa explicitamente
um background trimodal de três estômatos, a compatibilidade global--local
desse setor e o gap da Hessiana projetada não são mais pendências. Isso
transporta identidade, multiplicidade e invariantes topológicos, mas não
deriva automaticamente normalizações contínuas de massa, raio, momentos ou
fatores de forma. Ver `impacto_ponte_global_local_q37_q39_q40.md`.

---

## Trabalho futuro — interação entre objetos clássicos e quânticos

### Objetivo

Construir um capítulo geral da GDQ dedicado às diferentes formas de interação
entre sistemas clássicos macroscópicos e sólitons quânticos. A hipótese
organizadora será:

\[
\boxed{
\text{interação clássico--quântica}
=
\text{acoplamento bulk}
+
\text{modificação do contorno}
+
\text{retroação}
+
\text{fluxo de informação}.
}
\]

O capítulo deverá anteceder as aplicações experimentais ou o capítulo de
medição, permitindo tratar Stern--Gerlach apenas como um exemplo da estrutura
geral.

### Blocos a desenvolver

1. **Definir os regimes**

   - sóliton quântico com estômato, medida \(\mathcal U\), fase e setor
     topológico;
   - objeto clássico como sistema macroscópico de variáveis coletivas
     estáveis;
   - limite clássico como concentração da medida e supressão de coerências.

2. **Classificar as interações**

   - potencial externo no bulk;
   - alteração das condições Robin;
   - deformação métrica;
   - acoplamento por torção;
   - troca de fluxo no contorno;
   - interação térmica/estocástica;
   - interação gravitacional;
   - interação eletromagnética.

3. **Classificar os efeitos**

   - evolução coerente sem medição;
   - espalhamento;
   - deflexão adiabática;
   - decoerência sem registro;
   - medição contínua;
   - captura absorvente;
   - transição não adiabática;
   - cirurgia ou destruição do sóliton.

4. **Formalizar o contorno geral**

   \[
   \left(
   \nabla_n+\mathsf R_{\rm cl}
   \right)\Phi\big|_{\partial\mathcal N}
   =
   J_{\rm cl}.
   \]

   Determinar como o sistema clássico modifica \(\mathsf R_{\rm cl}\),
   \(J_{\rm cl}\), o domínio do operador e seu espectro.

5. **Derivar a retroação**

   \[
   \frac{\delta S_{\rm int}}{\delta X_{\rm cl}}
   =
   F_{\rm backreaction},
   \]

   verificando conservação de energia, momento, carga e fluxo.

6. **Descrever a cadeia de medição**

   \[
   \text{estado coerente}
   \rightarrow
   \text{ramos correlacionados}
   \rightarrow
   \text{decoerência}
   \rightarrow
   \text{captura/registro}.
   \]

   Incorporar a formulação Robin, o gerador estocástico condicionado e a
   prova martingal de Born desenvolvidos na Questão 42.

7. **Aplicações mínimas**

   - Stern--Gerlach;
   - dupla fenda com detector;
   - polarizador de fótons;
   - contador Geiger;
   - espalhamento por potencial clássico;
   - Aharonov--Bohm;
   - Casimir;
   - medição fraca;
   - escolha retardada;
   - Landau--Zener;
   - interação gravitacional com massa macroscópica.

### Critérios de fechamento

Para cada classe de interação, demonstrar:

1. conservação e normalização de \(\mathcal U\);
2. causalidade e ausência de sinalização superluminal;
3. auto-adjuncidade ou definição explícita do setor absorvente;
4. positividade da evolução física;
5. balanço de energia e retroação;
6. independência de coordenadas;
7. limite clássico controlado;
8. recuperação da regra de Born;
9. resultado único quando houver registro;
10. condições de validade adiabática e não adiabática.

### Status

\[
\boxed{
\text{Capítulo futuro registrado; desenvolver após a revisão das questões.}
}
\]

---

## Ponte global--local — pendência física remanescente

### Estado consolidado em 14 de julho de 2026

Os Lemas 1--6, a formulação DtN, o projetor abstrato e o critério de gap estão
fechados estruturalmente. A avaliação física integral continua aberta.

A auditoria em `ponte_global_local_fechamento.md` demonstrou que fixar
$L_{\rm cos}$ e $R_{\rm cos}$ remove apenas os módulos homogêneos. Os vínculos
lineares em $\log L$ e $\log R$ têm segunda variação nula nessas coordenadas
e não geram o limiar local $\mu_*^2>0$ exigido para um gap uniforme.

### Trabalho mínimo restante

Executar uma das rotas abaixo, sem misturá-las:

1. derivar um funcional cosmológico local
   $\mathcal C_{\rm cos}[g,J,f]$, calcular
   $D\mathcal C_{\rm cos}$ e $D^2\mathcal C_{\rm cos}$ e resolver a Hessiana
   vinculada; ou
2. resolver o background global warped da ação oficial, com interface $Y$,
   carga relativa e compensação global.

Somente depois:

1. avaliar $A_*=D\mathcal C(X_*)$;
2. calcular numericamente $P^{\rm phys}$;
3. construir o DtN exterior matricial;
4. verificar $\mu_*^2>0$ e o gap uniforme.

O Capítulo 22 e `questão_38_final.md` fornecem dados cosmológicos de contorno
e estimativas, mas não o funcional e suas duas variações. Esses números não
podem ser usados isoladamente como substituto da Hessiana exterior.

### Atualização do raio e da energia

O vínculo de raio já foi reduzido e implementado:

$$
\mathcal C_R=\frac{2y+z}{3}-\log R_{\rm cos}.
$$

Ele elevou o posto da Jacobiana de oito para nove. A única pendência de
fechamento do sistema de tiro é agora construir a imersão causal
$\iota_t:N^4\to M^8$, transportar $\xi=\iota_{t*}(\partial_t)$ para o exterior
Berger, avaliar a carga de Noether $\mathcal H_\xi$ na polarização DtN/Robin e
substituir a linha trivial $p_v=0$ por
$\mathcal C_E=\mathcal H_\xi-E_H=0$. Não identificar a restrição radial do
lapse com energia física.

### Redução causal obtida

`ponte_global_local_exterior_causal.md` separou o círculo-relógio de $T^4$
do arco radial $s$, derivou o exterior com warps $A_0$ e $A_s$ e obteve

$$
\mathcal H_\xi^{\rm red}
=\frac{p_0^{\rm full}-p_{0,\rm ref}^{\rm full}}{\beta_E}.
$$

O sistema canônico passou nos testes simbólico e de conservação da restrição.
Correção de status: a normalização global de Einstein associada a $\alpha$
fixa, em unidades $R_H=1$,
$\widehat R_{\rm cos}=\pi^2\sqrt\alpha$,
$\widehat\beta_E=2\pi$ e $\widehat E_H=1$. O background homogêneo sem defeito
fixa $p_{0,\rm ref}=0$. Não faltam novos parâmetros físicos; falta transportar
o prefator reduzido da ação para a unidade $E_0=c^4R_H/(2G)$ e executar a
busca. Também deve ser demonstrada a extensão global do relógio por
recobrimento universal ou reconstrução OS. Depois da
sela reduzida, calcular a Hessiana do funcional aumentado incluindo
$\delta J$ e modos não homogêneos; não usar a Hessiana de mínimos quadrados do
solver como Hessiana física.

### Execução do sistema causal final

O sistema $11\times11$ foi montado em
`ponte_global_local_solver_final.py` e executado. Nenhuma sela foi aceita.
Falta avaliar, sem ajuste,

$$
Z_E(\alpha)
=\frac{p_0^{\rm full}/(\beta_EE_H)}
{p_0^{\rm red}e^{-x_0}},
$$

restaurando $\hbar/\Lambda_C^2$, a integral em $\gamma$ e os volumes de
órbita suprimidos. Usar $Z_E=1$ ou $Z_E=1/\Pi_G$ foi testado e rejeitado.
Depois de calcular $Z_E$, repetir a busca, testar o posto, obter a sela e
somente então avaliar a Hessiana física e o gap.

Refinamento: a normalização acumulada
$Z_0=\int ds\,\mathscr V$ cancela os volumes compactos. A forma correta da
pendência é

$$
\mathcal C_E
=K_\gamma(\alpha)\frac{p_0^{\rm red}e^{-x_0}}{Z_0}-1,
$$

com $K_\gamma$ determinado pelo prefator da ação e pela integral causal. O
teste $K_\gamma=1$ removeu o condicionamento de $10^{38}$, mas não convergiu a
uma raiz; não usar esse valor como resultado.

### Plano de execução vigente

O fechamento foi organizado em
`ponte_global_local_plano_loop_agentico.md`. O plano fixa quatro portas que
devem ser satisfeitas sem pós-ajuste: (A) redução causal e normalização
energética; (B) sela bulk--interface com posto completo; (C) projetor e
Hessiana física do funcional aumentado; (D) espectro positivo e gap estável
sob refinamentos de malha, tolerância, domínio e corte harmônico. Uma falha
numérica deve ampliar apenas o setor indicado pelo modo residual ou negativo,
sem reabrir $\alpha$, $R_{\rm cos}$, $E_H$ ou a ação oficial.

### Resultado do loop agêntico

O plano foi executado e consolidado em
`ponte_global_local_loop_agentico_resultado.md`. A Porta A foi fechada no
setor estacionário com o projetor causal normalizado e $K_\gamma=1$. Os dois
ramos integráveis homogêneos de $J$ foram construídos e testados. O ramo
original estagna com resíduo no matching dos momentos; o ramo discreto
$\chi=\pi/2$ reduz o resíduo apenas no limite degenerado em que os dois
colares colapsam. O modo radial contínuo de $J$ foi excluído por Nijenhuis e o
primeiro Beltrami toroidal é um módulo zero desacoplado. Não existe, portanto,
sela não degenerada no ansatz homogêneo/cohomogeneidade--1 testado. A
pendência restante é mudar de classe funcional e derivar o primeiro modo
interno integrável de Kodaira--Spencer com domínio de bordo oficial; somente
depois cabem Hessiana física, estabilidade e gap.

Triagem posterior em `ponte_global_local_triagem_kodaira_resultado.md`:
no background exatamente homogêneo, um modo angular puro não singlet tem
sobreposição linear nula com o tripleto residual singlet quando o operador e
o bordo são equivariantes. Portanto $B_{\mu_1}^{\rm linear}=0$ nessa classe,
embora $|\mu_1|^2$ contenha um singlet e permita retroação quadrática. Ainda é
necessário decompor o Beltrami tensorial sob a simetria preservada. O próximo
cálculo mínimo deve obter da
ação oficial os coeficientes de Galerkin $(\lambda_\mu,g_\mu,C_a,C_c,C_u)$ e
testar uma bifurcação de amplitude finita; não basta adicionar uma coluna
linear ao solver.

Verificação tensorial/global posterior: a decomposição sob
$SU(2)_L\times U(1)_R$ confirmou por Schur que o primeiro setor $j=1/2$ não
acopla linearmente ao residual singlet. As famílias Hopf anisotrópica e
ressonante foram construídas e satisfazem Maurer--Cartan, mas a extensão
compatível de $(g,J,f)$ é um pullback; a covariância da ação força
$\lambda_\mu=g_\mu=C_a=C_c=C_u=0$. Portanto são zeros modulares, não a
bifurcação física. A pendência mínima passa a ser o autoproblema conjunto da
Hessiana de $(g,J,f)$, projetado fora das difeomorfismos e com domínio DtN de
interface.

Teste mínimo da catástrofe estocástica em
`ponte_global_local_teste_catastrofe_resultado.md`: no candidato quase crítico
em $h=0{,}18$, a projeção deu
$r=4{,}49774\times10^{-5}$ e
$b=-3{,}43326\times10^{-5}$, logo
$-r/b\simeq1{,}31005>0$. O sinal é favorável à sustentação estatística do
colar, mas o valor é coordenado e $h$ é uma homotopia auxiliar. Restam a
normalização física do modo e a covariância causal derivada de
$K^{\rm phys}$.

Auditoria vetorial posterior em `ponte_global_local_sela_estatistica.md`
excluiu duas simplificações: a covariância apenas no modo mole anula sua
projeção, mas aumenta a norma do resíduo completo para aproximadamente
$5{,}42$; a covariância isotrópica nas coordenadas do tiro exigiria amplitude
negativa. A pendência não é mais procurar uma variância escalar. É construir
a Hessiana bulk--interface oficial projetada, calcular

$$
C^{\rm phys}=\mathfrak P_\gamma[(K^{\rm phys}-i0_\gamma)^{-1}]
$$

e resolver a equação vetorial média

$$
D\mathcal S_{\rm aug}
+\frac12D^3\mathcal S_{\rm aug}:C^{\rm phys}=0
$$

sem usar o resíduo como alvo.

Auditoria adicional: o bloco cinético Berger bruto tem assinatura $(2,3,0)$,
logo não define uma gaussiana positiva antes dos vínculos, gauge e thimble
causal. A estatística da Questão 16 vive nas coordenadas físicas e ainda falta
derivar seu pullback para o espaço de campos/colagem, isto é, a mobilidade e o
operador de ruído que permitiriam aplicar o teorema de Krylov--Bogoliubov e
calcular a medida invariante sem arbitrariedade.

O pullback foi então calculado: a difusão conhecida da Q16 levanta-se aos
campos como $RDR^\dagger$, com $R$ gerador de difeomorfismos. Portanto

$$
P^{\rm phys}RDR^\dagger P^{\rm phys\dagger}=0.
$$

Isso exclui a componente interior de gauge, mas não o traço browniano da
interface. A pendência mínima passa a ser calcular

$$
B_\partial=P^{\rm phys}RE_\partial,
\qquad
\mathbb D^{\rm phys}=B_\partial D_\partial B_\partial^\dagger
$$

com a extensão elíptica/DtN oficial. Se essa componente também falhar, resta
a sela determinística ou a derivação de um ruído transversal intrínseco;
postulá-lo seria um novo axioma.

O primeiro teste do traço de borda também foi executado: no subespaço dos dois
deslocamentos homogêneos dos colares, a otimização sobre toda covariância
$2\times2$ positiva retornou $C_\partial\simeq0$ e não reduziu o resíduo.
Restam os harmônicos angulares/de forma da interface; o modo homogêneo não
fecha a sela.

Reformulação prioritária após o teste sem colar: a interface
cosmológico--local pode ter sido artificial. Em
`ponte_global_local_sem_interface_resultado.md`, um operador radial global com
defeito localizado converge diretamente ao operador planar com erro
$O(R^{-2})$ e localização uniforme. Deve-se substituir provisoriamente a
pendência “sela global--local” por:

1. transportar o estômato físico pela família apontada;
2. provar convergência da Hessiana oficial projetada;
3. manter DtN apenas no bordo físico do estômato;
4. aplicar os Lemas 3--5 sem colagem entre backgrounds.

Até essa revisão, a sela de colagem não deve ser tratada como condição
necessária da ponte.

Revisão concluída em `ponte_global_local_lemas_sem_colar.md`: a antiga
Hipótese BI foi removida da ponte. Os Lemas 1--6 estão demonstrados como
teorema de transporte condicional ao background local admissível e ao gap
físico $\Delta_0>0$. A pendência verdadeira não é uma sela global--local, mas
avaliar $P^{\rm phys}$ e $\Delta_0$ na Hessiana oficial do estômato local. O
teste de referência confirmou erro espectral $O(R^{-2})$, localização uniforme
e convergência do projetor até $9{,}66\times10^{-8}$.

Aplicação concluída para a classe física $C_3$ em
`ponte_global_local_fechamento_c3.md`. A Hessiana projetada dos três caps
gaussianos possui

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0,
$$

com $\Delta_0=1/2$ na normalização da Q28. O gap foi validado por quatro
malhas e quatro valores de $\tau$. Não resta pendência da ponte para esse
background. A generalização para backgrounds locais não gaussianos permanece
programa futuro e não reabre o teorema aplicado.
