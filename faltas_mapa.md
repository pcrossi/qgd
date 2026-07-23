# Mapa consolidado das faltas antes de avançar novas questões

## 1. Objetivo

Este documento organiza o que ainda falta resolver, calcular ou apenas
refinar antes de avançar a sequência de questões.

Regra de leitura:

\[
\boxed{
\texttt{faltas.md}
\text{ é o status mestre conservador.}
}
\]

Atualização de 16 de julho de 2026: a seção `0. Reavaliação vigente` em
`faltas.md` passa a ser a triagem operacional atual. O restante de
`faltas.md` preserva histórico, no-gos e derivações úteis, mas não deve ser
lido como lista linear de pendências.

O arquivo `numerico/status_numerico.md` contém linguagem excessivamente forte
em vários pontos. Ele deve ser tratado como relatório exploratório, não como
veredito final. Sempre que houver conflito, prevalece:

1. `faltas.md`;
2. `numerico.md`;
3. documentos consolidados de cada questão;
4. scripts numéricos apenas como evidência auxiliar.

---

## 2. Classificação operacional

Cada pendência deve cair em uma das classes abaixo:

1. **Estrutural aberta** — falta uma derivação essencial.
2. **Estrutural fechada / cálculo pendente** — a cadeia lógica existe, mas
   faltam integrais, índices, normas ou autovalores.
3. **Numérica pendente** — há operador/domínio, mas falta solver ou
   convergência.
4. **Fenomenológica posterior** — comparação com dados, benchmarks,
   curvas experimentais ou refinamentos.
5. **Editorial** — linguagem precisa ser suavizada ou corrigida.
6. **Programa futuro** — ideia útil, mas não bloqueia o corpo principal.

---

## 3. Pendências por prioridade

### Prioridade 0 — Controle e consistência documental

Antes de novos cálculos:

1. manter `faltas.md`, `faltas_plano.md`, `numerico.md` e este arquivo
   sincronizados;
2. rebaixar linguagem triunfalista em relatórios numéricos quando conflitar com
   o status conservador;
3. não classificar como “validado” algo que ainda dependa de:
   - coeficientes escolhidos depois;
   - calibração experimental não declarada;
   - comparação com alvo;
   - normalização não derivada.

Status:

\[
\boxed{\text{iniciado; status numérico auditado criado}}
\]

Produto sugerido:

\[
\texttt{numerico/status\_numerico\_auditado.md}
\]

---

### Prioridade 1 — Q38: constante gravitacional \(G\)

Classe:

\[
\boxed{\text{fechada como problema global no espaço cosmológico de Einstein}}
\]

Q38 não é mais prioridade aberta. O valor global de $G$ não pode ser
reconstruído a partir de um infinitésimo da fibra local. Cálculos de
$\mathcal V_{\rm eff}^{(G)}$, do limite de Poisson e de resíduos locais são
testes de projeção/compatibilidade e não condições de fechamento.

O que já existe:

\[
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)},
\qquad
G
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
\]

Trabalhos posteriores que não reabrem a questão:

1. avaliar diretamente:

   \[
   \mathcal V_{\rm eff}^{(G)}
   =
   \operatorname{Re}
   \left[
   \int_\gamma d\tau
   \int_K
   \eta_R e^{2A}\mathcal U_*\sqrt{q_*}\,d^4y
   \right];
   \]

2. fixar \(\eta_R\);
3. derivar o limite fraco:

   \[
   \nabla^2\Phi=4\pi G\rho;
   \]

4. mostrar de onde vêm:

   \[
   \alpha^4,\qquad
   \chi_{\rm Fano},\qquad
   e^{1/(2\alpha)};
   \]

5. separar claramente aproximação cosmológica \(T^5\times S^3\) de limite
   plano observacional.

Razão da reclassificação:

$G$ codifica a organização global e os dados de contorno do espaço de
Einstein. A descrição local deve ser compatível com esse valor, mas não possui
informação suficiente para determiná-lo autonomamente.

Produto:

\[
\texttt{questoes/q38/associados/avaliacao\_Veff\_G.md}
\]

Início executado:

1. `questoes/q38/associados/avaliacao_Veff_G.md`;
2. `questoes/q38/associados/normalizacao_eta_R.md`;
3. `questoes/q38/associados/warp_termico_einstein.md`;
4. `questoes/q38/associados/planificacao_estereografica.md`;
5. `questoes/q38/associados/fano_impedancia_gravitacional.md`;
6. `questoes/q38/associados/solver_auditado_q38.md`;
7. `numerico/q38_gravidade/solve_gravity_q38_auditado.py`;
8. `numerico/q38_gravidade/saida_gravity_q38_auditado.md`;
9. `questoes/q38/associados/derivacao_inst_fano_planificacao.md`.

---

### Prioridade 2 — Q34/Q35: loops, calibre e ausência de polo de Landau

Classe:

\[
\boxed{\text{Q34 fechada; Q35 fechada condicionalmente no setor }U(1)}
\]

O que já existe:

1. loop geométrico derivado da ação oficial:

   \[
   \mathcal S_{\rm GDQ}
   \to
   S_\chi^{(2)}
   \to
   H_n[A]
   \to
   \operatorname{Tr}\log H_n[A]
   \to
   \Pi_{\mu\nu}^{(n)};
   \]

2. heat-kernel covariante;
3. polarização \(U(1)\) transversal:

   \[
   \Pi_{\mu\nu}^{(\tau)}
   =
   (q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2);
   \]

4. saturação efetiva:

   \[
   \alpha_{\rm eff}(\infty)
   =
   \frac{\alpha_0}
   {1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)};
   \]

5. Slavnov--Taylor geométrico formulado.

Fontes autocontidas:

\[
\texttt{manuscrito/04\_action\_consistency/notes/loop\_geometrico\_calibre\_fase\_t4.md}.
\]

\[
\texttt{manuscrito/04\_action\_consistency/notes/ausencia\_polo\_landau\_u1.md}.
\]

Extensões posteriores:

1. calibrar $\Lambda_C$ em unidades físicas e testar a equação de gap;
2. manter a tradução perturbativa fermiônica como auditoria externa;
3. tratar jacobianos topológicos, Bismut e setor não abeliano como extensões
   posteriores de Q34, sem reabrir seu fechamento declarado.

$1/128$ foi retirado do programa atual por decisão explícita do usuário.

Por que vem cedo:

Q34/Q35 controlam a consistência perturbativa externa e evitam contradições
sobre “não temos renormalização”.

Produtos históricos substituídos no manuscrito por notas e scripts
autocontidos:

1. `manuscrito/04_action_consistency/notes/loop_geometrico_calibre_fase_t4.md`;
2. `manuscrito/04_action_consistency/notes/ausencia_polo_landau_u1.md`;
3. `manuscrito/04_action_consistency/scripts/verificar_ausencia_polo_landau_u1.py`;
4. `manuscrito/04_action_consistency/scripts/verificar_fechamento_torcao_reynolds.py`.

---

### Prioridade 3 — Q30: confinamento, Wilson loops e mass gap

Classe:

\[
\boxed{\text{estrutural fechada; refinamento metrológico de contorno/sonda}}
\]

O que já existe:

1. conexão efetiva:

   \[
   A_C\in\Omega^1(N,\mathfrak{su}(3));
   \]

2. Wilson loops:

   \[
   W_R(C)=\operatorname{Tr}_R
   \mathcal P\exp\left(i\oint_CA_C\right);
   \]

3. lei de área:

   \[
   \langle W_R(C)\rangle\sim e^{-\sigma A_{\min}(C)};
   \]

4. gap por Hessiana confinante:

   \[
   \lambda_1\ge c_D\Lambda_0+c_\sigma\sigma>0.
   \]

Atualização vigente:

1. a cadeia estrutural \(SU(3)\), conexão, Wilson loop, lei de área e gap
   positivo está fechada no setor GDQ declarado;
2. a tensão reduzida do tubo Ricci--Bohm foi avaliada diretamente;
3. o coeficiente \(C_{\rm GDQ}=\pi\) foi derivado como carga geométrica do
   cap transversal, não ajustado ao dado hadrônico;
4. o raio canônico Q39/Q40 fornece
   \(r_p=0{,}840778765450\,\mathrm{fm}\) e
   \(\sigma=0{,}876946044304\,\mathrm{GeV/fm}\);
5. o raio efetivo comprimido de sonda
   \(r_{\rm eff}=0{,}8354\,\mathrm{fm}\) fornece
   \(\sigma=0{,}888274921594\,\mathrm{GeV/fm}\).

O que falta:

1. decidir por derivação de interface se o observável de confinamento usa o
   raio canônico de superfície ou o raio comprimido de sonda;
2. calcular a Hessiana completa acoplada do pescoço Ricci--Bohm se for
   desejada metrologia de espectro/glueballs;
3. comparar com espectro hadrônico apenas depois de congelar background,
   domínio, contorno e operador.

Portanto Q30 não pertence mais ao bloco de faltas estruturais; o item real é
refinamento de contorno/sonda.

Produto:

\[
\texttt{manuscrito/18\_confinement\_signal\_problem/}
\]

---

### Prioridade 4 — Q31: CP forte

Classe:

\[
\boxed{\text{estrutural fechada; normalização funcional pendente}}
\]

O que já existe:

1. potencial periódico:

   \[
   V(\theta)=\chi_{\rm top}(1-\cos\theta);
   \]

2. relaxação:

   \[
   \frac{d\theta}{d\tau}
   =
   -\kappa_{\rm CP}\chi_{\rm top}\sin\theta;
   \]

3. Lyapunov:

   \[
   \frac{dV}{d\tau}\le0;
   \]

4. proposta:

   \[
   f_B
   =
   M_P\sqrt{\frac{3}{\sqrt{6\pi^5}}}.
   \]

O que falta:

1. calcular \(\chi_{\rm top}\) no setor forte efetivo;
2. normalizar canonicamente o modo torsional \(a\);
3. decidir se \(a\) é polo propagante ou modo relaxacional;
4. derivar:

   \[
   m_a^2f_B^2=\chi_{\rm top};
   \]

5. calcular EDM residual;
6. verificar superamortecimento cosmológico.

Fonte autocontida vigente:

`manuscrito/21_cp_hopf_monopoles/`

Notas centrais:

1. `manuscrito/21_cp_hopf_monopoles/notes/topology/periodicidade_cp_carga_inteira.md`;
2. `manuscrito/21_cp_hopf_monopoles/notes/topology/hessiana_susceptibilidade_cp.md`;
3. `manuscrito/21_cp_hopf_monopoles/notes/topology/normalizacao_fB_torsional.md`;
4. `manuscrito/21_cp_hopf_monopoles/notes/topology/prova_relaxacao_cp_lyapunov.md`;
5. `manuscrito/21_cp_hopf_monopoles/notes/topology/edm_residual_limite.md`.

---

### Prioridade 5 — Q28 e programa quantitativo pós-Q29

Classe:

\[
\boxed{\text{fechada no modelo reduzido; extensão integral como programa futuro}}
\]

Q28 não possui falta estrutural vigente no modelo reduzido. O que permanece
como extensão integral futura é:

1. calcular:

   \[
   c_2(E_C),\quad c_3(E_C),\quad c_2(E_W),\quad c_1(L_Y);
   \]

2. calcular espectro de \(\mathcal D_a\);
3. obter \(\eta_a(0)\) e \(h_a\);
4. reavaliar em backgrounds integrais:

   \[
   n_a=1,\qquad a=1,2,3;
   \]

5. calcular \(g_s,g,g'\) como normas internas.

Q29 está fechada estruturalmente no Capítulo 19 autocontido. Não são faltas da questão, mas
trabalhos quantitativos posteriores:

1. transportar \(g\), \(g'\) e \(\theta_W\) pelo background global correto;
2. localizar/normalizar o canal fotônico local;
3. calcular overlaps numéricos para CKM, PMNS e correções fermiônicas;
4. conectar \(G_F\) à normalização global do setor fraco;
5. confirmar o prefator dimensional/causal do modo interno.

A origem numérica absoluta de $\alpha$ pertence à Q37: a média cosmológica de
Einstein fornece

\[
(\alpha_E^{\rm mean})^{-1}=137{,}036082448\ldots
\]

e a ponte global--local herda esse valor no laboratório sob suas hipóteses.
Q29 fica responsável apenas pela compatibilização local/eletrofraca desse
valor.

Observação:

Qualquer fórmula simples do tipo:

\[
v\approx m_p\frac{6\pi^5}{7}
\]

deve ser tratada como hipótese/atalho fenomenológico até ser derivada como
autovalor ou mínimo variacional.

Produtos:

1. `manuscrito/14_geometric_particle_taxonomy/`;
2. `manuscrito/19_electroweak_geometric_breaking/`;
3. `manuscrito/19_electroweak_geometric_breaking/notes/electroweak/`.

---

### Prioridade 6 — Q32/Q33/Q36: corte, propagador e escala dimensional

Classe:

\[
\boxed{\text{estrutural fechada; auditoria técnica/editorial pendente}}
\]

Q32 falta:

Fonte autocontida já instalada:

\[
\texttt{manuscrito/04\_action\_consistency/notes/hessiana\_kernel\_calor\_propagador.md}.
\]

O setor estrutural já contém a separação
\(\mathcal O_{\rm Hess}^{(2)}=\tau L_{\rm GDQ}^{(2)}\), o kernel
\(e^{-\tau L_{\rm GDQ}^{(2)}}\), o limite plano do propagador e os scripts de
verificação.

Pendências posteriores:

1. coeficientes completos de \(Q_{gg}\) e \(Q_{gs}\) em fundo geral;
2. decomposição espectral completa;
3. reflexão positiva OS;
4. reconstrução lorentziana;
5. causalidade:

   \[
   \operatorname{supp}G_{\rm ret}\subseteq J_h^+.
   \]

Q33 falta:

Fonte autocontida já instalada:

\[
\texttt{manuscrito/04\_action\_consistency/notes/escala\_corte\_cartan\_resolucao\_setorial.md}.
\]

O ponto estrutural foi fechado por separação de símbolos:

   \[
   \Lambda_C,\quad \widehat\Lambda_\tau,\quad m_i.
   \]

Pendências posteriores:

1. corrigir qualquer capítulo legado que ainda use \(m_e\) ou \(1\,{\rm GeV}\)
   como corte universal duro;
2. derivar escalas setoriais específicas como espectros de \(L_i^{(2)}\);
3. manter a correção \(v_K\simeq72{,}85\,{\rm MeV}\neq246\,{\rm GeV}\) onde o
   legado a exigir.

Q36 está fechada por calibração metrológica. Auditoria posterior:

1. auditar toda afirmação de massa absoluta;
2. declarar quando \(M_e\) é calibração metrológica;
3. verificar razão geométrica para cada massa.

Fonte autocontida:

\[
\texttt{manuscrito/15\_leptonic\_hierarchy\_masses/notes/escala\_dimensional\_calibracao.md}
\]

---

### Prioridade 7 — Q24/Q25/Q26: medição, sinal e Hopf

Classe:

\[
\boxed{\text{pendências médias ou programa posterior}}
\]

Q24 falta:

1. conectar dominância espectral a registros \(R_i\);
2. provar estabilidade de ponteiros;
3. estimar supressão fora da diagonal;
4. relacionar bacias geométricas à regra de Born.

Q25 estado vigente:

1. medida positiva com holonomia fermiônica: fechada estruturalmente;
2. transmissão/reflexão por impedância/Cayley: preservada no manuscrito;
3. variância e autocorrelação: testadas no benchmark reduzido, sem cota geral;
4. benchmark físico reduzido com comparação externa: preservado no manuscrito;
5. solução algorítmica universal: programa futuro, não pendência do fechamento
   reduzido atual.

Q26 estado vigente:

1. Hopf/resíduos: fechado e preservado no manuscrito;
2. prova spinorial: fechada estruturalmente;
3. seleção dinâmica do setor spinorial: programa futuro em
   `ideias/possibilidades.md`, não falta ativa.

Produtos:

1. `questão_24_registros.md`;
2. `q25/especificacao_algoritmica.md`;
3. `manuscrito/10_spin_statistics_pauli/notes/spin_hopf_residuo_cauchy.md`.

---

### Prioridade 8 — Q39/Q40 refinamentos

Classe:

\[
\boxed{\text{fechadas estruturalmente; refinamento metrológico/fenomenológico}}
\]

Regra comum: não reabrir Q39/Q40 tentando extrair de uma carta planar as
quantidades já determinadas no espaço global. O teorema foi reformulado sem
interface artificial e aplicado ao background gaussiano $C_3$. Q40 herda
diretamente esse fechamento. Em Q39 resta verificar que os níveis
$n=0,1,17$ formam o cluster físico isolado transportado. O planar trata
resposta, dressing, fontes, contornos, cirurgia e taxas.

Q39 refinamentos:

1. derivar \(\eta_{\rm req}\) sublíder;
2. aprofundar monodromia/topologia dos modos;
3. limpar relatórios numéricos para não vender engenharia inversa como prova
   final.

Q40 refinamentos:

1. fatores de forma completos;
2. fases parciais e seções de choque;
3. \(G_F\) e \(g_A\);
4. \(S_{\rm inst}\), se violação bariônica for admitida;
5. comparação experimental fina;
6. separar os dois invariantes de quatro modos $C_S$ e $C_T$ para correlações
   angulares e polarização. A combinação contraída necessária à taxa total já
   está fechada por
   $2|C_S|^2+6|C_T|^2=(15\pi^3/16)\alpha^{11}m_ec^2/I_\beta$. O antineutrino
   é o modo GDQ de onda torsional neutra.

Esses itens não bloqueiam o avanço estrutural da teoria, mas são importantes
para confronto fenomenológico.

---

### Prioridade 9 — Q41

Classe:

\[
\boxed{\text{encerrada no escopo de redução e correspondência}}
\]

Q41 já foi iniciada em:

1. `questoes/q41/questao_41.md`;
2. `questoes/q41/associados/testes_gdq_poco_oscilador.md`.

Status:

\[
\boxed{
\text{fechada analítica e numericamente; remover do backlog estrutural.}
}
\]

O teste de parede física foi concluído por mapa Dirichlet--Neumann e
diagonalização direta, com convergência de segunda ordem. Aplicações a
materiais específicos são fenomenologia, não pendência da Q41.

---

## 4. Ordem recomendada de execução

A ordem segura é:

\[
\boxed{
P0
\to
Q38
\to
Q34/Q35
\to
Q30
\to
Q31
\to
Q28/Q29
\to
Q32/Q33/Q36
\to
Q24/Q25/Q26
\to
Q39/Q40
\to
Q41^+
}
\]

Em termos práticos:

1. auditar e corrigir status numéricos;
2. atacar Q38;
3. fechar teste \(U(1)\)/\(\Lambda_{\rm EM}\);
4. calcular \(\sigma\) e gap em Q30;
5. normalizar CP forte em Q31;
6. só então voltar à sequência de novas questões.

---

## 5. Próxima ação concreta

Começar por:

\[
\boxed{
\text{P0: criar } \texttt{numerico/status\_numerico\_auditado.md}
}
\]

Esse arquivo deve:

1. rebaixar “validado” para “exploratório”, “estrutural” ou “pendente” quando
   necessário;
2. separar scripts que calculam previsão de scripts que ajustam alvo;
3. listar quais resultados numéricos podem ser citados agora;
4. listar quais precisam de derivação variacional antes de serem usados no
   manuscrito.
