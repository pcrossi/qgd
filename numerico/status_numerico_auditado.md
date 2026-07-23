# Status numérico auditado da GDQ

## Atualização — ponte global--local sem colar

`ponte_global_local_teste_sem_colar.py` é um teste de consistência do limite
apontado num canal radial de referência. Confirmou erro $O(R^{-2})$,
localização e convergência do projetor, mas não é a Hessiana completa.

`ponte_global_local_validar_gap_c3.py` é teste de convergência de uma
quantidade analítica da Q28. Discretiza o conjugado de $-\Delta_f$ e recupera
$1/(2\tau)$. Para $\tau=1$, o erro caiu de $6{,}997\times10^{-5}$ em 400
pontos para $1{,}098\times10^{-6}$ em 3200 pontos. Nenhum dado experimental
foi usado.

Classificação: avaliação direta e teste de convergência; não é ajuste nem
previsão dimensional.

## 1. Função deste documento

Este arquivo audita o conteúdo de `numerico/status_numerico.md` sem apagá-lo.
Ele não invalida os scripts numéricos; apenas classifica o papel de cada
resultado.

A regra operacional é:

\[
\boxed{
\texttt{faltas.md}\text{ permanece como status mestre conservador.}
}
\]

Portanto, sempre que um relatório numérico usar linguagem como “validado”,
“sem mocks”, “prova definitiva” ou “pronto para crítica”, essa linguagem deve
ser lida apenas como entusiasmo de relatório local, não como conclusão final,
a menos que o mesmo fechamento também esteja registrado em `faltas.md`.

---

## 2. Classes usadas na auditoria

Cada resultado numérico deve ser classificado em uma das classes abaixo:

1. **Derivação estrutural** — segue diretamente da ação ou de uma variação
   formal já escrita.
2. **Avaliação direta** — calcula uma integral, autovalor, índice ou norma já
   definido estruturalmente.
3. **Teste de consistência** — verifica convergência, estabilidade ou limite.
4. **Engenharia inversa controlada** — encontra parâmetros necessários para
   atingir um alvo e depois tenta interpretá-los geometricamente.
5. **Comparação fenomenológica** — compara com CODATA ou dados experimentais.
6. **Hipótese efetiva** — usa uma forma funcional plausível ainda não
   derivada variacionalmente.

Somente as classes 1 e 2, quando completas, podem ser usadas como fechamento
preditivo forte.

---

## 3. Auditoria por bloco

### Q34/Q35 — Polarização \(U(1)\) e polo de Landau

Evidência numérica disponível:

1. numerico/q34_q35_u1/solve_polarizacao_u1.py;
2. numerico/q34_q35_u1/test_polarizacao_u1.py;
3. numerico/q34_q35_u1/saida_polarizacao_u1_auditada.md.
4. numerico/q34_q35_u1/sweep_especies_u1.py;
5. numerico/q34_q35_u1/test_sweep_especies_u1.py;
6. numerico/q34_q35_u1/saida_sweep_especies_u1.md.

Classificação:

1. a fórmula de $\Pi_\tau(q^2)$ é derivação estrutural já documentada;
2. sua avaliação é **avaliação direta**;
3. Ward tensorial, refinamento, monotonicidade, limite de QED e saturação são
   **testes de consistência**;
4. $\eta=10^{-6}$ é cenário adimensional declarado, não valor físico;
5. o cálculo não determina $\Lambda_{\rm EM}$ e não constitui comparação
   fenomenológica.

Os seis testes de regressão passaram. No cenário declarado:

$$
\Pi_\eta(\infty)=1{,}025005713135\times10^{-2}<1.
$$

Não declarar que $\Lambda_{\rm EM}$ foi previsto.

A varredura multiespécie localizou a fronteira formal $\Pi_{\rm EM}=1$ em
$\log_{10}(\Lambda_{\rm crit}/m_e)=95{,}561913582$ para os léptons GDQ e
$37{,}803035603$ para o benchmark externo de férmions carregados. Os dez
testes combinados passaram. Essas raízes são limites de consistência, não
escalas geométricas previstas; o benchmark de quarks é dependente de esquema.

A escala eletrofraca calibrada
$\Lambda_0^{\rm EW}=126354{,}3162$ GeV foi testada apenas como hipótese de
universalidade. Ela fornece $\Pi_{\rm EM}(\infty)=0{,}0675577855$ no cenário
leptônico e $0{,}1610754352$ no benchmark completo, ambos sem polo. Isso é
teste de consistência condicional, não derivação de $\Lambda_{\rm EM}$; ver
questoes/q35/associados/auditoria_espectral_Lambda_EM.md.

O operador radial fotônico no colar cilíndrico foi discretizado por volumes
finitos em numerico/q34_q35_u1/verificar_gap_cilindrico_em.py. O refinamento
até 800 células reproduziu $\lambda_1=\pi^2/L^2$ com erro relativo
$1{,}285\times10^{-6}$ e confirmou $\lambda_1\to0$ quando $L\to\infty$.
Classificação: **avaliação direta e teste de convergência**. O resultado é um
no-go local; não determina o comprimento global $L$.

A identidade torsão--Reynolds foi verificada em
numerico/q34_q35_u1/verificar_fechamento_torcao_reynolds.py. Para
$\alpha=1/137$ e $n_B=1$, o cálculo fornece
$R=1{,}0370743523$, $\tau_{\rm EM}=0{,}2749005225$ e
$\widehat\Lambda_{\rm EM}=1{,}9072701741$, com resíduos algébricos inferiores
a $2\times10^{-16}$. Classificação: **avaliação direta de um princípio
constitutivo declarado**, não derivação independente de $\alpha$.

$1/128$ não integra o programa atual por decisão explícita do usuário em
2026-07-12.

Os coeficientes locais $U(1)$ foram verificados em
numerico/q34_q35_u1/verificar_coeficientes_locais_u1.py. A série truncada em
$r^3$ convergiu com erro $O(r^4)$; no último ponto o erro relativo foi
$3{,}288\times10^{-12}$. Classificação: **avaliação direta e teste de
consistência**. O cálculo não inclui ainda os invariantes não abelianos.

Os fatores de grupo do coeficiente não abeliano $a_4$ foram verificados em
numerico/q34_q35_u1/verificar_coeficiente_nao_abeliano.py:
$b_0^{SU(3)}=7$, $b_0^{SU(2)}=10/3$ e, condicionalmente à propagação do modo
de ordem como doublet escalar complexo, $b_0^{SU(2)}=19/6$. Classificação:
**avaliação algébrica de auditoria perturbativa externa**.

A parcela de matéria de $a_6$ foi verificada em
numerico/q34_q35_u1/verificar_a6_materia.py. O limite $U(1)$ de
$c_{2G}^{\rm matter}$ coincidiu com o coeficiente abeliano anterior a menos de
$10^{-18}$. Classificação: **avaliação algébrica de auditoria externa**. O
coeficiente de $F^3$ e o bloco vetor--jacobiano não foram calculados.

Os pesos universais do bloco vetor--jacobiano foram verificados exatamente em
numerico/q34_q35_u1/verificar_a6_vetor_jacobiano.py. O controle $a_4$
reproduziu $11/(96\pi^2)$, e os pesos de $a_6$ foram manipulados como frações
racionais, sem erro de ponto flutuante. Classificação: **verificação algébrica
da fórmula universal externa**. A redução final foi executada. Matrizes não comutativas
verificaram $\operatorname{tr}(DE)^2=-4\operatorname{tr}(DF)^2$,
$\operatorname{tr}(E^3)=8\operatorname{tr}(F^3)$ e
$\operatorname{tr}(E\Omega^2)=0$. A aritmética racional forneceu
$a_6^{\rm VJ}=(4\pi)^{-2}[(19/30)\mathcal B+(1/45)\mathcal C]$ no fundo
plano integrado sem bordo. Permanecem Bismut e bordo.

A conexão produto Bismut--gauge foi testada em
numerico/q34_q35_u1/verificar_tracos_bismut_gauge.py. Os cancelamentos
quadrático e cúbico dos termos mistos puros de $\Omega$ foram confirmados com
erros de $1{,}421\times10^{-14}$; a fatoração do termo misto via $E_BF^2$
teve erro $1{,}332\times10^{-15}$. Classificação: **teste algébrico de
consistência da extensão estrutural**. Não é avaliação de um background
físico completo.

### Q39 — Hierarquia de massas leptônicas

Status conservador:

\[
\boxed{
\text{fechada estruturalmente como espectro global; refinamento metrológico pendente.}
}
\]

Evidência numérica disponível:

1. comparação de contornos em `numerico/q39_leptons/compare_boundaries_q39.py`;
2. solver térmico em `numerico/q39_leptons/thermal_solver_q39.py`;
3. avaliação formal \(H/J\) em `numerico/q39_leptons/evaluate_H_J_q39.py`;
4. relatórios locais em `numerico/q39_leptons/`.

Classificação:

1. o espectro Rosen--Morse e a estrutura de contorno são derivação estrutural;
2. a comparação de contornos é teste de consistência;
3. o ajuste térmico inicial foi engenharia inversa controlada;
4. a avaliação \(H/J\) aproxima a prova preditiva, mas ainda exige ligação
   final entre \(\eta_{\rm req}\), monodromia e resposta do estômato.

Não declarar ainda:

\[
\text{“massa leptônica completamente prevista sem pendência”.}
\]

Pode declarar:

\[
\text{“Q39 tem rota espectral consistente e numericamente estável; falta fechar a resposta térmica/monodrômica final.”}
\]

---

### Q40 — Observáveis bariônicos

Status conservador:

\[
\boxed{
\text{fechada estruturalmente; fenomenologia quantitativa posterior.}
}
\]

Evidência numérica disponível:

1. solvers de observáveis em `numerico/q40_barions/`;
2. comparação do \(G_E^n\);
3. modos coletivos;
4. impedância de superfície;
5. resposta de sonda eletromagnética/magnética.
6. `neutron/resolver_cadeia_gdq_neutron.py`: diagonalização exata-numérica dos
   blocos de Dirac--Bismut, com resíduos nulos;
7. `neutron/verificar_overlap_quatro_modos.py`: Gram angular
   $\operatorname{diag}(2,6)$ e identidade de Fierz com resíduo nulo;
8. `neutron/verificar_jatos_causais.py`: verificação simbólica da regra de
   Leibniz causal e do terceiro jato torsional;
9. `neutron/calcular_taxa_overlap_gdq.py`: integral analítica e numérica do
   espaço de fase, fórmula da taxa em $C_S,C_T$ e avaliações condicional e
   histórica claramente separadas;
10. `neutron/verificar_projecao_fluxo_quartica.py`: projetor do vínculo de
    fluxo, jatos torsionais até quarta ordem e complemento de Schur verificados
    simbolicamente com resíduo zero;
11. `neutron/verificar_corrente_simpletica.py`: identidade de Green da
    corrente simplética ponderada verificada simbolicamente com resíduo zero;
12. `neutron/calcular_taxa_wkb_cirurgia.py`: operador radial, ação de bounce e
    taxa WKB implementados parametricamente, sem defaults físicos enquanto os
    coeficientes causais estiverem ausentes;
13. `neutron/auditar_coeficientes_wkb_neutron.py`: busca e teste do benchmark
    unitário; ausência de bounce demonstrada e transplante das rigidezes Q30
    para $M_r$ rejeitado;
14. `neutron/verificar_nao_identificabilidade_coeficientes.py`: resíduo causal
    cúbico e dois perfis de matching com os mesmos dados de borda e custos
    distintos, demonstrando simbolicamente a não unicidade.
15. `neutron/fechar_meia_vida_gdq.py`: auditoria integrada dos kernels
    eletrônico e torsional neutro, Gram angular, balanços de energia/torção,
    refinamento do espaço de fase e cálculo de
    $T_{1/2}=609{,}552781482$ s sob a lei GDQ $\alpha^{-11}$ com
    $\alpha^{-1}=137{,}035999177$. O valor $1/128$ não é usado.

Classificação:

1. a lei de distribuição de torção/carga por estômatos é estrutura GDQ;
2. os fatores de forma são comparação fenomenológica;
3. a curva completa de espalhamento ainda depende de resolver \(H_n(\chi)\)
   variacionalmente com operador final;
4. \(G_F\), \(g_A\), \(S_{\rm inst}\) e modos excitados permanecem trabalho
   posterior;
5. o zero orbital entre os dois modos emitidos isolados não é o overlap de
   quatro modos. A álgebra completa admite dois invariantes, com Gram
   $\operatorname{diag}(2,6)$. A combinação contraída necessária à taxa está
   fechada; a separação $C_S/C_T$ permanece para polarização.
6. o antineutrino já é caracterizado internamente como a onda torsional neutra
   $\ker D^{(0)}_{0,-3/2}$. A meia-vida usa o terceiro jato contraído já
   fechado pela lei GDQ; os dois jatos individuais não são necessários para
   esse observável.

Não declarar ainda:

\[
\text{“todos os observáveis bariônicos foram previstos em detalhe”.}
\]

Pode declarar:

\[
\text{“Q40 está estruturalmente fechada para próton/nêutron; a fenomenologia de espalhamento permanece em refinamento.”}
\]

---

### Q38 — Constante gravitacional \(G\)

Status:

\[
\boxed{
\text{Fechada condicionalmente pela rota de contorno global; rota bulk suave excluída.}
}
\]

Evidência numérica disponível:

1. `numerico/q38_gravidade/solve_gravity_q38.py`;
2. `numerico/q38_gravidade/saida_gravity_q38_puro.md`;
3. `numerico/q38_gravidade/solve_gravity_q38_v2.py`;
4. `numerico/q38_gravidade/saida_gravity_q38_v2.md`;
5. `numerico/q38_gravidade/solve_gravity_q38_auditado.py`;
6. `numerico/q38_gravidade/saida_gravity_q38_auditado.md`;
7. `questoes/q38/associados/derivacao_inst_fano_planificacao.md`.

Classificação:

1. a extração de \(C_R\) é derivação estrutural;
2. o solver puro mostra que um ansatz simples não basta;
3. o solver V2 é hipótese efetiva promissora;
4. a “planificação estereográfica” e o fator residual de \(0,34\%\) ainda
   precisam ser derivados da redução da ação, não apenas aplicados;
5. o solver auditado mostrou que o valor `0.4791` usado no V2 é
   aproximadamente:

   \[
   \frac{3\sqrt2/5}{\sqrt\pi},
   \]

   portanto Fano e planificação estavam misturados;
6. com \(\chi_{\rm Fano}^{\rm bulk}=3\sqrt2/5\) e sem
   \(J_{\rm flat}\) independente, o erro fica em \(0,2668\%\);
7. aplicar \(J_{\rm flat}=\sqrt\pi\) separadamente leva a erro de
   aproximadamente \(43,7\%\), logo a planificação não está validada como
   fator externo;
8. a derivação formal posterior fixou:

   \[
   \frac{S_{\rm inst}}{\hbar}=\frac1{2\alpha},
   \qquad
   \chi_{\rm Fano}^{\rm bulk}=\frac{3\sqrt2}{5},
   \qquad
   J_{\rm flat}^{(0)}=1.
   \]

   Esses resultados valem no nível topológico/variacional reduzido.

Não declarar ainda:

\[
\text{“}G\text{ foi previsto numericamente sem hipótese efetiva”.}
\]

Pode declarar:

\[
\text{“A GDQ identifica }G\text{ por }C_R\text{ e fecha a combinação topológica reduzida}
\text{ de }\Pi_1;\text{ falta o operador local completo.”}
\]

Também pode declarar:

\[
\text{“A auditoria numérica de Q38 isolou a boa concordância na combinação }
\alpha^4(1+\alpha)e^{-1/(2\alpha)}/\chi_{\rm Fano}^{\rm bulk},
\text{ e mostrou que }J_{\rm flat}^{(0)}=1\text{ no modo zero normalizado.”}
\]

---

### Q37 — Estrutura fina \(\alpha\)

Atualização arquitetural: a convergência apontada fornece agora a relação
geométrica entre o espaço cosmológico e o bulk local, removendo a objeção de
incompatibilidade pura. Isso não muda a classificação dos números abaixo.
$\alpha$ é uma normalização contínua e ainda exige avaliar

$$
K_Q^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}
$$

na norma do modo eletromagnético físico. Nenhuma concordância numérica desta
seção foi promovida a previsão cega ou derivação da ação oficial pela ponte.

Status conservador:

\[
\boxed{
\text{rota geométrica forte; revisar dependência de simetria e normalização.}
}
\]

Evidência numérica disponível:

1. `numerico/q37_alpha/solve_alpha_q37.py`;
2. `numerico/q37_alpha/solve_alpha_q37_v2.py`;
3. saídas associadas.

Classificação:

1. quando a contagem \(T^5\times S^3\), \(1920\) simetrias e a normalização
   são impostas, o resultado é excelente;
2. ainda deve ficar explícito quais fatores vêm de topologia, quais vêm de
   volume e quais vêm de escolha cosmológica.

Não declarar ainda:

\[
\text{“}\alpha\text{ foi derivada independentemente de toda escolha de fundo”.}
\]

Pode declarar:

\[
\text{“}\alpha\text{ tem uma rota geométrica muito forte no fundo cosmológico de Einstein.”}
\]

---

### Q28/Q29 — Grupo de gauge e escala eletrofraca

Status conservador:

\[
\boxed{
\text{estrutura condicional/efetiva; cálculo explícito de índices, normas e acoplamentos pendente.}
}
\]

Evidência numérica disponível:

1. `numerico/q28_q29_eletrofraco/solve_electroweak_q28_q29.py`;
2. versões e saídas associadas.

Classificação:

1. \(SU(3)\times SU(2)\times U(1)\) por potenciais de Killing e colchetes de
   Poisson é rota estrutural;
2. \(v_{\rm GDQ}=m_pV_K/7\) deve ser tratado como hipótese efetiva/metrológica
   até a Hessiana eletrofraca ser avaliada;
3. \(\sin^2\theta_W=2/9\) é uma relação geométrica promissora, mas precisa de
   normalização dos fibrados e acoplamentos.

Não declarar ainda:

\[
\text{“o setor eletrofraco completo substitui o Higgs sem cálculo pendente”.}
\]

Pode declarar:

\[
\text{“Q28/Q29 estão fechadas como estrutura condicional; falta transformar a estrutura em cálculo de índices e normas.”}
\]

---

### Q30 — Confinamento, Wilson loops e mass gap

Status conservador:

\[
\boxed{
\text{fechada estruturalmente; }\sigma,\lambda_1,g_s\text{ ainda precisam ser calculados.}
}
\]

Evidência numérica disponível:

1. `numerico/q30_confinamento/solve_confinement_q30.py`;
2. saídas locais do potencial e espectro.

Classificação:

1. conexão \(SU(3)\), Wilson loops, lei de área e Hessiana confinante estão
   estruturalmente formulados;
2. a tensão de corda \(\sigma\), o primeiro autovalor \(\lambda_1\) e a norma
   interna \(g_s\) ainda são avaliação direta pendente.

Não declarar ainda:

\[
\text{“mass gap de Yang--Mills computado numericamente de forma final”.}
\]

Pode declarar:

\[
\text{“A rota GDQ para confinamento está definida; falta cálculo explícito dos invariantes numéricos.”}
\]

---

### Q31 — CP forte

Status conservador:

\[
\boxed{
\text{fechada estruturalmente; normalização funcional e }\chi_{\rm top}\text{ pendentes.}
}
\]

Evidência numérica disponível:

1. `numerico/q31_cp_forte/solve_cp_axion_q31.py`;
2. relatórios locais.

Classificação:

1. \(V(\theta)=\chi_{\rm top}(1-\cos\theta)\) e relaxação torsional são
   estrutura GDQ;
2. \(\chi_{\rm top}=1/V_K\) é hipótese reduzida útil, não substitui a
   susceptibilidade funcional completa;
3. \(f_B\) precisa de normalização cinética canônica;
4. EDM residual e cosmologia são comparações posteriores.

Não declarar ainda:

\[
\text{“CP forte completamente resolvido numericamente”.}
\]

Pode declarar:

\[
\text{“Q31 tem mecanismo estrutural de relaxação; falta normalizar }\chi_{\rm top}
\text{ e }f_B\text{ funcionalmente.”}
\]

---

### Q34/Q35 — Loops, calibre e ausência de polo de Landau

Status conservador:

\[
\boxed{
\text{Q34 fechada; Q35 fechada condicionalmente no setor }U(1).
}
\]

Evidência numérica:

1. `verificar_loop_geometrico_t4.py`: $\Pi(0)=0$, erro de Ward
   $2{,}061\times10^{-20}$, erro de refinamento $8{,}949\times10^{-13}$;
2. `comparar_kernels_geometricos.py`: três kernels covariantes preservam Ward
   com erro máximo $2{,}794\times10^{-20}$, monotonicidade, finitude e
   saturação; as amplitudes UV variam entre os kernels.

Classificação:

1. o primeiro bloco é avaliação direta do loop derivado e teste de
   convergência;
2. a comparação de kernels é teste de consistência e sensibilidade, não
   previsão cega;
3. a invariância robusta é a identidade de calibre, não igualdade numérica
   entre resoluções físicas distintas;
4. $1/128$ não integra o programa atual por decisão explícita do usuário;
5. a calibração setorial é
   $\Lambda_{\rm EM}=1{,}90727017413475\Lambda_C$.

Não declarar:

\[
\text{“renormalização fundamental da GDQ”.}
\]

Linguagem correta:

\[
\text{“escala externa efetiva”, “projeção finita”, “vestimento geométrico”.}
\]

---

## 4. Termos que devem ser evitados nos relatórios finais

Evitar, salvo quando houver derivação estrutural e avaliação direta completa:

1. “validado”;
2. “sem mocks”;
3. “prova definitiva”;
4. “cravou”;
5. “perfeição”;
6. “pronto para crítica científica”;
7. “fim do Higgs”;
8. “fim do Modelo Padrão”;
9. “sem necessidade de áxion” quando a normalização torsional ainda estiver
   pendente;
10. “\(G\) derivado numericamente” quando \(\mathcal V_{\rm eff}^{(G)}\) ainda
    usa hipótese efetiva.

Linguagem recomendada:

1. “fechado estruturalmente”;
2. “avaliação direta pendente”;
3. “rota promissora”;
4. “teste de consistência”;
5. “hipótese efetiva”;
6. “comparação fenomenológica”;
7. “engenharia inversa controlada”;
8. “derivação variacional formal”.

---

## 5. Prioridade após esta auditoria

A próxima prioridade é Q38:

\[
\boxed{
\text{avaliar }\mathcal V_{\rm eff}^{(G)}
\text{ e derivar a ponte entre o fundo cosmológico }T^5\times S^3
\text{ e o limite plano observacional.}
}
\]

Produto de trabalho:

\[
\texttt{questoes/q38/associados/avaliacao\_Veff\_G.md}
\]
