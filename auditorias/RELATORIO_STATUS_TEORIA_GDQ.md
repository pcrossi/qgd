# Relatório de Status da GDQ — Avaliação de Completude

> [!warning] Relatório histórico, superado em 12 de julho de 2026
> Este arquivo foi produzido antes dos resultados negativos finais da Q38,
> antes da consolidação da Q42 e antes do fechamento numérico da Q41. Ele
> também tratou incorretamente o uso de $T^5\times S^3$ como contradição
> automática com o bulk local. O status canônico atualizado está em
> `auditorias/RELATORIO_STATUS_TEORIA_GDQ_REVISADO.md`.
>
> Atualização de 14 de julho de 2026: a relação entre os espaços foi
> demonstrada por convergência apontada direta, sem interface artificial, e
> aplicada ao background gaussiano $C_3$. Q40 recebe o fechamento direto do
> setor trimodal; Q39 ainda requer identificar o cluster $n=0,1,17$; Q37
> ainda requer a normalização contínua do modo eletromagnético. Ver
> `topicos/ponte_global_local/impacto_ponte_global_local_q37_q39_q40.md`.

## 0. Escopo e método

Esta avaliação usa exclusivamente:

1. os arquivos `questoes/q02/questao_02.md` a `questoes/q41/questao_41.md` (incluindo variantes:
   `questoes/q28/questao_28_final.md`, `questoes/q29/questao_29_final.md`, `questoes/q30/questao_30_yang_mills.md`,
   `questoes/q40/questao_40_faltas.md`, `questoes/q40/questao_40_obs.md`);
2. os capítulos principais em `pt-br/` (manuscrito original), usados como
   referência cruzada, não como fonte primária de veredito.

Não foram usados `en/`, `bkp`, `lixo`, scripts de `questoes/q37/associados/`, nem os documentos
de auditoria antigos (`respostas*.md`, `auditorias/RELATORIO_AUDITORIA_COMPLETA_GDQ.md`
etc.), exceto quando citados dentro das próprias questões.

Cada questão foi classificada em quatro níveis:

- **Fechada** — resultado matemático completo, sem lacuna estrutural.
- **Fechada estruturalmente / condicional** — arquitetura e derivação lógica
  completas, mas dependente de um cálculo numérico, espectral ou de
  verificação de hipótese técnica ainda não realizada.
- **Aberta** — a pergunta original não tem resposta demonstrada; existe só
  um programa de pesquisa.
- **Inconsistente / a reconciliar** — existe uma resposta, mas ela contradiz
  um axioma ou resultado já fixado em outra questão.

---

## 1. Panorama por bloco temático

### Bloco A — Fundação geométrica e axiomática (Q2–Q9)

| Q | Tema | Status |
|---|---|---|
| 2 | Definição matemática da GDQ (\(M=\mathbb R^4\times T^4\), assinatura, spin, ação) | **Fechada** como EFT axiomática; previsão numérica aberta |
| 3 | Por que \(n=4\) complexo | **Fechada** — declarado axioma; derivação dinâmica (Atiyah–Singer) é programa futuro |
| 4 | Ação e consistência quântica de loops | **Fechada condicional** — EFT perturbativa via BRST auxiliar + form factor de Cartan; não é prova não perturbativa |
| 5 | Campos fundamentais | **Fechada** — dicionário ontológico completo |
| 6 | O que é \(\tau\) | **Fechada** |
| 7 | Emergência do tempo lorentziano | **Fechada condicional** — depende da verificação setorial de OS1–OS5 |
| 8 | Preservação da causalidade | **Fechada** |
| 9 | Ação fundamental única | **Fechada** |

Este bloco é o mais maduro da teoria: define de forma única e sem
ambiguidade a variedade, a ação, os campos, a causalidade e a reconstrução
lorentziana. Praticamente todas as antigas contradições de notação
(\(\tau+it\) vs \(z_\tau\), \(n=2\) vs \(n=4\), Kähler estrito vs
hermitiano-torsional) foram resolvidas.

### Bloco B — Dinâmica efetiva, hidrodinâmica de Madelung e problema de Cauchy (Q10–Q19)

| Q | Tema | Status |
|---|---|---|
| 10 | Continuidade \(\partial_\tau\rho+\nabla(\rho v)=0\) | **Fechada** — teorema, não postulado |
| 11 | Hamilton–Jacobi–Bohm | **Fechada** |
| 12 | Fluxo métrico / tensor energia-momento | **Fechada** |
| 13 | \(\mathcal U=\rho/(4\pi z_\tau)^n\) | **Fechada** |
| 14 | Mapa Perelman–Madelung | **Fechada, mas parcial** — correspondência é local/setorial, não bijeção global (nós, fases multivaloradas exigem dados extras) |
| 15 | Relação \(f,S_I,\rho\) | **Fechada** |
| 16 | Coeficiente de difusão \(\nu_0\) | **Fechada** |
| 17 | Problema de Cauchy bem posto | **Fechada** — elíptico/parabólico com gauges de DeTurck e Hodge, existência e unicidade local |
| 18 | Solítons como partículas | **Fechada como critério** — solução gaussiana neutra explícita; elétron/próton completos como solução NÃO estão provados |
| 19 | Monotonicidade ⇒ estabilidade | **Fechada condicionalmente** ao operador de Jacobi; vale para o solíton neutro, aberto para carregados/spinoriais |

Bloco tecnicamente sólido. A ação produz corretamente as equações efetivas
(continuidade, Hamilton–Jacobi–Bohm, fluxo métrico) como teoremas
derivados, não como adições externas — este é um ponto de força real da
reconstrução.

### Bloco C — Fundamentos quânticos (Q20–Q27)

| Q | Tema | Status |
|---|---|---|
| 20 | Espaço de Hilbert | **Fechada estruturalmente** |
| 21 | Unitariedade da evolução | **Fechada**, condicionada à verificação OS já discutida em Q7/Q20 |
| 22 | Regra de Born | **Fechada estruturalmente** — dado o aparato de Hilbert/projetores, mas a seleção de base pelo aparelho fica para Q24 |
| 23 | Objeção de Wallstrom | **Fechada** — quantização de circulação decorre de integralidade de \(c_1(L)\), não mais postulada via soma de Poisson |
| 24 | Problema da medida | **Fechada com ressalva explícita** — decoerência e estatística resolvidas; resultado único exige uma hipótese ontológica extra (seleção de bacia de atração) não demonstrada |
| 25 | Problema do sinal fermiônico | **Aberta como algoritmo** — reformulação geométrica sim (sinal armazenado na fase, medida positiva), mas sem prova de custo/variância polinomial |
| 26 | Origem do spin 1/2 | **Fechada estruturalmente** |
| 27 | Estatística fermiônica | **Fechada estruturalmente**, condicionada ao setor spinorial efetivo local (Q20/Q21/Q26) |

Ponto notável: **Q23 é um caso de axioma reduzido a teorema** — a
quantização da circulação, antes justificada por um argumento analítico
(soma de Poisson) tratado quase como postulado à parte, agora segue da
integralidade topológica de \(c_1(L)\in H^2(M^*,\mathbb Z)\), i.e., é
consequência da estrutura de fibrado de linha já admitida.

### Bloco D — Modelo Padrão, massas e constantes (Q28–Q41)

Este é o bloco menos maduro e o que concentra as inconsistências mais
sérias.

| Q | Tema | Status |
|---|---|---|
| 28 (+ final) | Emergência de \(SU(3)_C\times SU(2)_L\times U(1)_Y\) | **Fechada estruturalmente na classe estacionária $C_3$ gaussiana.** Noether seleciona três estômatos; APS + $\mathbb Z_6$ dão $N_G=3$; a Hessiana física tem gap positivo; as normas fornecem $g_s=g$, $g'^2/g^2=3/5$ e $\sin^2\theta_W=3/8$ no ponto geométrico comum |
| 29 (+ final) | Quebra eletrofraca | **Oficialmente fechada estruturalmente.** Modo de Hopf $(1,2)_{1/2}$, $a_2<0$, quártica positiva de interface, mínimo $\beta_*$, escala calibrada $v=246{,}111196$ GeV, quebra para $U(1)_{EM}$ e mecanismo fermiônico extensivo. Transporte operacional de $\theta_W$, CKM/PMNS e precisão de $W/Z$ permanecem posteriores |
| 30 (+ yang_mills) | Confinamento / mass gap | **Fechada estruturalmente** (cota de gap, tensão de corda, lei de área de Wilson qualitativa); cálculo numérico de \(\sigma\), \(\lambda_1\), conexão com \(\alpha_s(\mu)\) pendente |
| 31 | Problema CP forte | **Fechada estruturalmente** no setor efetivo \(SU(3)_C\); normalização, EDM numérico e cosmologia pendentes |
| 32 | Propagador modificado | **Fechada estruturalmente** |
| 33 | Escala de corte \(\Lambda_C\) | **Fechada estruturalmente** — mas exige correção do capítulo 33 original, que confundia \(\Lambda_C\) setorial com massas físicas |
| 34 | Preservação de gauge em loops | **Fechada** (abeliano) + **fechada estruturalmente** (não abeliano via Slavnov–Taylor geométrico); coeficientes quantitativos pendentes |
| 35 | Polo de Landau | **Fechada estruturalmente** no setor \(U(1)\); \(\Lambda_{\rm EM}\) numérico pendente |
| 36 | Origem da escala dimensional | **Fechada por calibração metrológica** — teoria prevê razões adimensionais; pendência é verificar caso a caso que essas razões são geométricas, não ajustadas |
| 37 | Derivação de \(\alpha\) | **Estruturalmente aberta / inconsistente** — ver §2 |
| 38 | Derivação de \(G\) (gravitação) | **Fechada e Resolvida ab initio** |
| 39 | Massas leptônicas (3 gerações) | **"Resolvida" segundo o arquivo, mas construída sobre geometria incompatível** — ver §2 |
| 40 (+ variantes) | Massas/observáveis de próton e nêutron | **Parcialmente fechada** — massas \(p,n\) estruturadas; observáveis adicionais (\(\Delta(1232)\), \(\tau_n\), espalhamento) usam a mesma geometria problemática — ver §2 |
| 41 | Poço/oscilador como teste | **Fechada como auditoria conceitual** — teste fraco, não prova conteúdo novo da GDQ |

---

## 2. Achado crítico: inconsistência geométrica não resolvida

As Questões 2 e 3 fixam, como **axioma oficial e definitivo**, a geometria:

\[
M=\mathbb R^4\times T^4,\qquad \dim_{\mathbb R}M=8,\qquad\dim_{\mathbb C}M=4.
\]

Elas descartam explicitamente qualquer geometria baseada em
\(T^5\times S^3\), afirmando (Q3, §5.1): *"A expressão antiga
\(\mathbb C^4\times(T^5\times S^3)\) não descreve uma variedade real de
dimensão oito... essa forma não pode ser usada para justificar um bulk real
8D"*, e (Q37, §9): *"a fórmula depende de \(T^5\times S^3\), entendido
agora como compactificação cosmológica auxiliar, não como base local"*.

Apesar disso:

- **Q37** (derivação de \(\alpha\)) conclui que a fórmula fechada antiga
  (baseada em \(T^5\times S^3\), com o número 1920 e uma "característica de
  Euler 5") **não pertence à geometria final** e não deve ser usada como
  demonstração — mas nenhuma derivação alternativa em \(\mathbb R^4\times
  T^4\) foi concluída (isso já havia sido confirmado experimentalmente
  nesta sessão: os scripts protótipo em `questoes/q37/associados/` produziram valores de
  \(\alpha\) muitas ordens de grandeza fora do CODATA).
- **Q39** (massas leptônicas, 3 gerações) usa integralmente
  \(T^5\times S^3\) como domínio espectral (`\(\Omega_\ell = T^5\times
  S^3\setminus\ldots\)`) e invoca o índice de Atiyah–Singer sobre essa
  mesma variedade para "provar" rigidamente 3 gerações. O arquivo classifica
  a questão como **"Resolvida"**, mas essa conclusão está construída sobre
  exatamente a geometria que Q2/Q3 declararam inválida como bulk
  fundamental.
- **Q40 / Q40_faltas / Q40_obs** (próton, nêutron, \(\Delta(1232)\),
  \(\tau_n\)) reutilizam a mesma base \(S^3\) (potencial de Rosen–Morse em
  \(S^3\), raio de estômato, condições de Robin) sem reconciliá-la com
  \(\mathbb R^4\times T^4\).

**Consequência lógica**: o bloco numérico mais "impressionante" da teoria
(massas de léptons e bárions com poucos parâmetros livres, \(\tau_n\approx
879{,}6\,\)s, \(r_p\), \(\Delta(1232)\)) não está de fato demonstrado a
partir da geometria oficial da GDQ. Ele pertence a um **modelo auxiliar
paralelo** (\(T^5\times S^3\)) cuja relação com a ação oficial em
\(\mathbb R^4\times T^4\) nunca foi estabelecida. As próprias Q3 e Q37 já
avisam disso, mas Q39/Q40 não reincorporam esse aviso — tratam o resultado
como fechado sem mencionar a ressalva.

**Recomendação**: reclassificar Q39 e Q40 (e as previsões numéricas
associadas) de "resolvida"/"fechada estruturalmente" para **"resultado
obtido em modelo auxiliar \(T^5\times S^3\); pendente de reconciliação ou
rederivação em \(\mathbb R^4\times T^4\)"**. Isso não invalida o valor
heurístico dos cálculos (as fórmulas podem estar corretas *dentro* do
modelo auxiliar), mas impede que sejam citados como derivação de primeiros
princípios da GDQ oficial.

---

## 3. Axiomas candidatos a reduzir a teoremas (já demonstrados neste estado)

Estes são casos em que algo que era tratado como postulado independente
passou a ser **consequência demonstrada** de axiomas mais básicos já
aceitos:

1. **Quantização da circulação / condição de Wallstrom (Q23)** — deixa de
   ser postulada via soma de Poisson e passa a ser teorema de
   integralidade de \(c_1(L)\in H^2(M^*,\mathbb Z)\) para o fibrado de
   linha \(L\to M^*\).
2. **Equação de continuidade (Q10)** — deixa de ser assumida e é obtida por
   variação de \(S_R\) na redução Madelung da ação oficial.
3. **Equação de Hamilton–Jacobi–Bohm (Q11)** — idem, por variação de
   \(\rho\).
4. **Equação de fluxo métrico / tensor energia-momento (Q12)** — \(T_{\mu\bar\nu}\)
   deixa de ser postulado por analogia e é obtido por
   \(-\tfrac{2}{\sqrt g}\delta S_{\rm mat}/\delta g^{\mu\bar\nu}\).
5. **Anticomutação fermiônica / princípio de exclusão (Q27)** — deixa de
   ser atribuída à circulação clássica (Q2) e é derivada do teorema
   spin–estatística padrão, dado o setor spinorial local, causal, de
   energia positiva já construído (Q7, Q8, Q20).
6. **Unitariedade da evolução temporal (Q21)** — deixa de ser postulada e é
   obtida do teorema de Stone aplicado ao Hamiltoniano reconstruído por
   Osterwalder–Schrader (Q7).
7. **Identidade de Ward/Slavnov–Taylor no setor de calibre (Q34)** —
   preservação de gauge sob loops deixa de ser suposta e é obtida da
   covariância do operador \(L_{A^g}=g^{-1}L_Ag\) sob o traço funcional.
8. **No-signalling (Q8)** — deixa de ser postulado por fiat e é derivado da
   microcausalidade (\([\mathcal A(O_A),\mathcal A(O_B)]=0\) fora do cone
   de \(h\)) mais a estrutura de operações locais de Kraus.

## 4. Axiomas que permanecem axiomas (sem redução demonstrada)

1. \(M=\mathbb R^4\times T^4\) (Q2) — escolha de variedade e topologia.
2. \(n=\dim_{\mathbb C}M=4\) (Q3) — explicitamente declarado axioma; rota
   Atiyah–Singer para derivá-lo é só "programa futuro".
3. Escolha da estrutura spin antiperiódica dentre as 16 possíveis (Q2) —
   nenhuma seleção dinâmica demonstrada.
4. Escolha do ciclo-relógio \(\omega=d\theta_1\) e da restrição
   \(X^*\omega\neq0\) (Q2) — cinemática imposta, não derivada.
5. Emergência do grupo do Modelo Padrão \(SU(3)_C\times SU(2)_L\times U(1)_Y\)
   (Q28) — explicitamente **não** é teorema; é a maior lacuna aberta do
   bloco D.
6. Seleção de três gerações — alegada como teorema em Q39, mas apenas
   *dentro* do modelo auxiliar \(T^5\times S^3\) (ver §2); dentro da
   geometria oficial \(\mathbb R^4\times T^4\), permanece axiomática/aberta.
7. Resultado único de medida (Q24) — decoerência e estatística são
   teoremas, mas a unicidade do resultado exige uma hipótese ontológica
   extra não demonstrada (seleção de bacia de atração).

---

## 5. Outros pontos que merecem atenção

1. **Defasagem entre `questão_*.md` e `pt-br/`.** Uma busca por "axioma" nos
   capítulos de `pt-br/` retorna apenas 2 ocorrências fora do padrão
   (`03 - Causalidade...`, notas de apoio), enquanto os arquivos
   `questão_*.md` fazem dezenas de correções estruturais explícitas
   (\(\tau+it\to z_\tau\), \(n=2\to n=4\), \(\mathcal U\) redefinida,
   \(K(\tau)\sim\tau^{-2}\to\tau^{-4}\), etc.). Isso indica que **o
   manuscrito principal em `pt-br/` ainda não incorporou boa parte das
   correções da reconstrução**. Enquanto isso não for propagado, o
   manuscrito e a auditoria (`questão_*.md`) descrevem duas versões
   parcialmente divergentes da teoria.
2. **Duplicidade de arquivos sem reconciliação explícita** — pares como
   `questoes/q28/historico/questao_28.md`/`questoes/q28/questao_28_final.md`, `questoes/q29/historico/questao_29.md`/`questoes/q29/questao_29_final.md`,
   `questoes/q30/questao_30.md`/`questoes/q30/questao_30_yang_mills.md`, e o trio
   `questoes/q40/questao_40.md`/`questoes/q40/questao_40_faltas.md`/`questoes/q40/questao_40_obs.md` coexistem sem
   um arquivo "índice" que diga qual é a versão vigente. Recomenda-se
   consolidar cada par/trio em um único arquivo final, com o anterior
   arquivado.
3. **Uso de valores experimentais como calibração vs. como entrada
   disfarçada.** Várias questões (Q36, Q39, Q40) fixam a escala via massa do
   elétron (\(M_e\)) e depois reportam razões adimensionais. Isso é
   metodologicamente aceitável (calibração de unidade), mas o próprio Q36
   alerta que é preciso verificar, caso a caso, que essas razões vêm
   realmente da geometria e não escondem ajuste fino. Essa verificação não
   foi feita de forma sistemática.
4. **Q25 (problema do sinal fermiônico)** é a única questão do bloco C
   claramente aberta como problema computacional, não apenas como
   cálculo pendente — vale destacar isso porque, ao contrário das
   pendências "numéricas" do bloco D, aqui falta também uma demonstração
   *qualitativa* (limite polinomial de variância/custo).
5. **Q18 e Q41** alertam contra afirmações de que a GDQ já "prova" o
   elétron/próton/nêutron como solução completa ou que o poço/oscilador
   "validam" a teoria — essas ressalvas devem ser mantidas ativamente ao
   divulgar resultados, pois é fácil overclaim a partir dos títulos das
   questões "fechadas".

---

## 6. Veredito geral de completude

- **Fundação axiomática e formulação matemática (Q2–Q21): ~90–95% madura.**
  A teoria tem uma ação única, campos bem definidos, causalidade,
  reconstrução lorentziana e hidrodinâmica de Madelung completamente
  derivada da ação, com problema de Cauchy bem posto.
- **Fundamentos quânticos (Q22–Q27): ~85% madura.** Born, Wallstrom,
  spin-estatística e unitariedade são teoremas condicionais bem
  demonstrados; falta unicidade ontológica da medida (Q24) e o algoritmo
  do problema do sinal (Q25).
- **Setor de partículas e constantes (Q28–Q41): ~35–45% maduro no sentido
  de primeiros princípios.** A arquitetura formal está montada em quase
  todas as questões ("fechada estruturalmente"), mas (a) o grupo do Modelo
  Padrão não emerge como teorema (Q28), e (b) as previsões numéricas mais
  citadas (massas leptônicas Q39, massas/raio/tempo de vida bariônicos
  Q40) foram obtidas em uma geometria auxiliar (\(T^5\times S^3\)) que
  contradiz o axioma oficial (\(\mathbb R^4\times T^4\)) fixado nas
  próprias Q2/Q3. Essa reconciliação é a lacuna mais urgente da teoria.

**Prioridade recomendada para a próxima etapa**: não é mais fechar novas
questões estruturais, e sim (1) reconciliar ou re-derivar Q37/Q39/Q40 na
geometria oficial \(\mathbb R^4\times T^4\), e (2) fechar Q28
(emergência do grupo de calibre do Modelo Padrão), da qual dependem Q29,
Q31 e partes de Q30/Q34/Q35.
