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
\texttt{q38/avaliacao\_Veff\_G.md}
\]

Início executado:

1. `q38/avaliacao_Veff_G.md`;
2. `q38/normalizacao_eta_R.md`;
3. `q38/warp_termico_einstein.md`;
4. `q38/planificacao_estereografica.md`;
5. `q38/fano_impedancia_gravitacional.md`;
6. `q38/solver_auditado_q38.md`;
7. `numerico/q38_gravidade/solve_gravity_q38_auditado.py`;
8. `numerico/q38_gravidade/saida_gravity_q38_auditado.md`;
9. `q38/derivacao_inst_fano_planificacao.md`.

---

### Prioridade 2 — Q34/Q35: loops, calibre e ausência de polo de Landau

Classe:

\[
\boxed{\text{Q34 fechada; Q35 fechada condicionalmente no setor }U(1)}
\]

O que já existe:

1. heat-kernel covariante;
2. polarização \(U(1)\) transversal:

   \[
   \Pi_{\mu\nu}^{(\tau)}
   =
   (q_\mu q_\nu-q^2\delta_{\mu\nu})\Pi_\tau(q^2);
   \]

3. saturação efetiva:

   \[
   \alpha_{\rm eff}(\infty)
   =
   \frac{\alpha_0}
   {1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)};
   \]

4. Slavnov--Taylor geométrico formulado.

Extensões posteriores:

1. calibrar $\Lambda_C$ em unidades físicas e testar a equação de gap;
2. manter a tradução perturbativa fermiônica como auditoria externa;
3. tratar jacobianos topológicos, Bismut e setor não abeliano como extensões
   posteriores de Q34, sem reabrir seu fechamento declarado.

$1/128$ foi retirado do programa atual por decisão explícita do usuário.

Por que vem cedo:

Q34/Q35 controlam a consistência perturbativa externa e evitam contradições
sobre “não temos renormalização”.

Produtos:

1. `q34/loop_U1_teste_minimo.md`;
2. `q34/polarizacao_U1_heat_kernel.md`;
3. `q35/U1_sem_polo_Landau.md`;
4. novo: `q35/Lambda_EM_geometrico.md`.

---

### Prioridade 3 — Q30: confinamento, Wilson loops e mass gap

Classe:

\[
\boxed{\text{estrutural fechada; cálculo explícito/numerico pendente}}
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

O que falta:

1. calcular \(g_s\) como norma interna;
2. calcular \(\sigma\);
3. calcular \(\lambda_1\);
4. formalizar a medida funcional completa do setor \(A_C\);
5. ligar \(\alpha_s^{\rm eff}=3/(8\pi)\) à escala/topologia hadrônica;
6. comparar com glueballs/espectro hadrônico quando houver solver.

Produto:

\[
\texttt{q30/calculo\_sigma\_gap.md}
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

Produto:

\[
\texttt{q31/normalizacao\_modo\_torsional.md}
\]

---

### Prioridade 5 — Q28 e programa quantitativo pós-Q29

Classe:

\[
\boxed{\text{teorema condicional fechado; cálculo explícito pendente}}
\]

Q28 falta:

1. calcular:

   \[
   c_2(E_C),\quad c_3(E_C),\quad c_2(E_W),\quad c_1(L_Y);
   \]

2. calcular espectro de \(\mathcal D_a\);
3. obter \(\eta_a(0)\) e \(h_a\);
4. provar:

   \[
   n_a=1,\qquad a=1,2,3;
   \]

5. calcular \(g_s,g,g'\) como normas internas.

Q29 está fechada de acordo com `bkp/29-0.md`. Não são faltas da questão, mas
trabalhos quantitativos posteriores:

1. calcular o autovetor \(\Phi_{\rm EW}\);
2. calcular \(a_2,a_4\);
3. obter:

   \[
   v^2=-2a_2/a_4;
   \]

4. calcular \(\theta_W\);
5. calcular Yukawas;
6. conectar \(G_F\) à normalização do setor fraco.

A predição absoluta de $\alpha$ constitui programa autônomo e não reabre a
Q29. Por decisão explícita do usuário, $1/128$ não integra o programa atual;
usar $\alpha^{-1}\simeq137$ na ponte constitutiva de baixa energia.

Observação:

Qualquer fórmula simples do tipo:

\[
v\approx m_p\frac{6\pi^5}{7}
\]

deve ser tratada como hipótese/atalho fenomenológico até ser derivada como
autovalor ou mínimo variacional.

Produtos:

1. `q28/classes_indices_explicitos.md`;
2. `q29/hessiana_eletrofraca.md`.

---

### Prioridade 6 — Q32/Q33/Q36: corte, propagador e escala dimensional

Classe:

\[
\boxed{\text{estrutural fechada; auditoria técnica/editorial pendente}}
\]

Q32 falta:

1. coeficientes completos de \(Q_{gg}\) e \(Q_{gs}\);
2. decomposição espectral completa;
3. reflexão positiva OS;
4. reconstrução lorentziana;
5. causalidade:

   \[
   \operatorname{supp}G_{\rm ret}\subseteq J_h^+.
   \]

Q33 falta:

1. derivar \(\Lambda_C\);
2. decidir se universal ou setorial;
3. separar:

   \[
   \Lambda_C,\quad \Lambda(\tau),\quad m_i;
   \]

4. corrigir capítulo antigo sobre \(v_K\).

Q36 falta:

1. auditar toda afirmação de massa absoluta;
2. declarar quando \(M_e\) é calibração metrológica;
3. verificar razão geométrica para cada massa.

Produto:

\[
\texttt{q33\_q36\_auditoria\_escalas.md}
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

Q25 falta:

1. algoritmo explícito;
2. transmissão/reflexão;
3. variância;
4. autocorrelação;
5. benchmarks.

Q26 falta:

1. desenvolver Hopf/resíduos como refinamento;
2. não substituir a prova spinorial já fechada.

Produtos:

1. `questão_24_registros.md`;
2. `q25/especificacao_algoritmica.md`;
3. `q26/hopf_residuos_refinamento.md`.

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

1. `questão_41.md`;
2. `q41/testes_gdq_poco_oscilador.md`.

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
