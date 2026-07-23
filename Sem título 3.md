# Relatório de Faltas e Melhorias: Manuscrito Capítulos 1 a 7

Este relatório consolida a auditoria dos sete primeiros capítulos de reescrita do manuscrito da GDQ. O objetivo é garantir que eles reflitam toda a construção acumulada do projeto (conforme registrado nas `questões/`, `memory.md`, e demais arquivos), tornando-os textos definitivos e autossuficientes sem preservar a história dos erros.

---

## Capítulo 01 (O Problema Inicial)

Apesar da clareza conceitual, faltam peças conectoras fundamentais estabelecidas no histórico do projeto.

### Faltas (Elementos Omitidos)
- **A Variável Causal Complexa ($z_\tau$)**: Em `01.9` (Da difusão à geometria), o texto apenas cita a oposição $t = -i\tau$ e os fluxos de Perelman. Falta explicar (como antecipação) que a teoria resolve o "paradoxo de Wick" via a variável $z_\tau = \tau + i\nu_0 t$, preservando a positividade de Wiener e a fase de Feynman sem conflito.
- **Torsão de Bismut na Difusão de Nelson (`01.8`)**: A difusão e o ruído multiplicativo são apresentados com a métrica espacial pura $h_{ij}$. Omitiu-se que as derivadas estocásticas herdam as conexões torcionais do *bulk* (chave para spin e circulação).
- **Testes Simbólicos**: Os scripts didáticos (`comparar_wiener_feynman_kernel.py`, `wick_semigroup_spectrum.py`, etc.) não são citados como demonstração matemática e computacional real, deixando o texto demasiadamente discursivo.

### Melhorias Sugeridas
- **Pontes de transição (`01.5` a `01.7`)**: Inserir parágrafos conectando como a rotação de Wick obriga a tratar amortecimento e fase separadamente, enquanto a representação de Madelung os une no mesmo estado físico.
- **Aviso sobre Nelson (`01.7`)**: Incluir um `> [!WARNING]` alertando que a GDQ não adota a ontologia de "éter clássico e colisões" da mecânica de Nelson original, mas a trata como o limite estocástico efetivo de uma dinâmica geométrica contínua.
- **Status Condicional (`01.8`, `01.9`)**: Marcar com `> [!IMPORTANT]` que o fluxo de Perelman e a difusão são *reduções matemáticas/motivações*. A GDQ deriva da sua Ação Oficial, não é apenas "Perelman com constante de Planck".

---

## Capítulo 02 (A Geometrização da Matéria)

Demonstra excelente evolução ao blindar contra confusões de ferramentas, mas negligencia resultados formais vitais já pacificados (especialmente da Q02).

### Faltas (Elementos Omitidos)
- **Restrição Topológica do Domínio Físico**: `02.10` define a forma-relógio ($\omega_0$), mas omite a restrição consolidada $u = X^*d\theta_1$ e a condição de imersão $X^*d\theta_1 \neq 0$ (o que define o domínio efetivo lorentziano).
- **Seleção da Estrutura de Spin (`02.2`)**: O texto prova as 16 estruturas de $T^4$ e aponta a necessidade de escolha de contorno, mas omite a fixação axiomática provisória em vigor no projeto: o setor fermiônico antiperiódico $\epsilon_F=(1,0,0,0)$.
- **Alerta contra Maxwell (`02.3`/`02.9`)**: Falta o aviso crucial (registrado na Q02) de que a 3-forma de Bismut ($H$) **não** é o tensor de Maxwell e que as conexões $X^*d\theta_a$ são planas.

### Melhorias Sugeridas
- **Reescrita de `02.10`**: Em $h = q - 2\frac{u \otimes u}{s}$, incluir explicitamente $u = X^*d\theta_1$ e uma subseção sobre singularidades causais e limites de $N$.
- **Alerta sobre Maxwell e Gauge**: Criar uma subseção com `> [!WARNING]` estipulando que o gauge local demandará, mais tarde, uma conexão de Ehresmann autêntica.
- **Escalas na Ação (`02.7`)**: Reforçar que $\Lambda_C$ é um corte *adimensional nas coordenadas de Cartan*, não uma escala de energia/comprimento ($\ell_C$, $E_C$).

---

## Capítulo 03 (Causalidade Complexa)

O capítulo estrutura bem a arquitetura sem sinalização retrocausal, mas a formalização diverge das novas definições metrológicas da teoria.

### Faltas (Elementos Omitidos)
- **Origem de $S_R$ e os Campos Fundamentais (`03.6`)**: A fase macroscópica $S_R$ cai de paraquedas. Falta definir explicitamente sua origem na decomposição do campo variacional $f$: $\rho = e^{-(f+\bar{f})/2}$ e $S_R = \frac{\hbar}{2i}(f-\bar{f})$.
- **Polos e Ramos ($\gamma_\pm$) (`03.4`/`03.5`)**: A seleção das Funções de Green e a variável $z_\tau$ não explica rigorosamente como o desvio de polos em $z_\tau$ seleciona $G_{\rm ret}$ vs $G_{\rm adv}$ (ligação pedida no `preservation_map.md`).
- **Mecânica de Aparelhos / DtN (`03.7`)**: O texto injeta $G_{\rm ret}$ diretamente via $\delta\Phi(x) = \int G_{\rm ret}J_{\rm app}\,dy$. Isso viola a cadeia rigorosa do projeto (exigida nos caps. 9, 11 e `AGENTS.md`): o aparelho deve ser visto através do Complemento de Schur/DtN ($\operatorname{Hess}\mathcal S_{\rm GDQ} \to R_{\rm app}$).
- **Local vs Cosmológico**: Não especifica se os resultados causais pertencem ao bulk $\mathbb{R}^4 \times T^4$ ou herdam características térmicas de $T^5 \times S^3$.

### Melhorias Sugeridas
- **Ponte entre 03.3, 03.4 e 03.5**: Demonstrar matematicamente que a prescrição de polos $+i0$ em `03.4` é um exemplo específico de seleção de contorno de `03.3`.
- **Sentido de $\nu_0$ e $m_0$ (`03.2`)**: Esclarecer que $m_0$ remete à massa emergente do soliton material para não parecer um ajuste fenomênico.

---

## Capítulo 04 (Consistência da Ação)

Embora preserve a Ação Oficial perfeitamente, perdeu o rastro da consistência quântica avançada provada nos capítulos posteriores.

### Faltas (Elementos Omitidos)
- **Origem das Simetrias de Calibre (`04.6`)**: Ao recusar o gauge postulado livremente, omite que os campos vetoriais ($A_\mu$) **emergem rigorosamente como isometrias/automorfismos do fibrado interno efetivo** (mecanismo Kaluza-Klein do $T^4$). Isso cria uma falsa tensão com o cálculo de loops em `04.7`.
- **Anomalias da Medida (`04.7`)**: O texto trata o "cancelamento de anomalias" como não-provado. No entanto, o projeto já consolidou (Cap. 14, Atiyah-Patodi-Singer) que a topologia seleciona $N=3$ gerações exatamente para garantir este cancelamento.
- **O Complemento de Schur (`04.7`/`04.6`)**: Ignora o papel ontológico principal do Complemento de Schur ($K_{\rm eff}$) como a interface do aparelho (DtN / $R_{\rm app}$).

### Melhorias Sugeridas
- **Hierarquia de Loops**: Explicitar em `04.7` que "loops" superiores nada mais são que os termos superiores na expansão de Taylor da Ação Oficial ($\delta^3 S, \delta^4 S$), retirando a mística de ferramentas de fora da GDQ.
- **Alerta sobre Fantasmas**: Usar `> [!IMPORTANT]` para destacar que fantasmas (Faddeev-Popov) não têm ontologia na GDQ, sendo apenas representadores do jacobiano do projetor físico.

---

## Capítulo 05 (Equações e Conservação)

Clareza algébrica excelente, mas incompleto no cerne geométrico: faltou estender a conservação para os difeomorfismos.

### Faltas (Elementos Omitidos)
- **O Equilíbrio Dinâmico Geométrico**: `05.4` foca apenas na equação de Hamilton-Jacobi-Bohm, mas omite o verdadeiro "equilíbrio dinâmico" gerado pela variação métrica.
- **Noether para Difeomorfismos (`05.6`)**: Noether é aplicado à invariância de fase (conservando a probabilidade), mas **omite os difeomorfismos do bulk**, que deveriam derivar a identidade de Bianchi e a conservação do tensor energia-momento ($\nabla_A T^{AB} = 0$).
- **O Tensor Energia-Momento ($T_{AB}$) (`05.5`)**: A equação métrica $\mathcal{E}_{AB}^{(g)}=0$ é derivada, mas o lado referente à matéria (fase e amplitude) não é isolado e batizado claramente como $T_{AB}$, enfraquecendo a ponte com o limite de Einstein no Cap. 7.
- **Redução de Routh (`05.7`)**: A seleção da polarização canônica ($p_\rho=0$) é apresentada abruptamente, sem a devida justificação via Redução de Routh dos graus de liberdade rápidos do bulk (como estabelecido em `memory.md`).

### Melhorias Sugeridas
- **Reestruturação e Balanço**: Renomear `05.4` e criar uma seção nova sobre "Equilíbrio Dinâmico e Conservação Covariante" que amarre as equações métricas à conservação $\nabla_A J^A_\xi = 0$.
- **Interpretação do Multiplicador**: Explicar o papel global e sistêmico do multiplicador $\lambda(\tau)$ em `05.4`.

---

## Capítulo 06 (Ponte Global-Local)

Formalizou bem os 6 lemas da ponte, mas não incluiu os resultados quantitativos notáveis recém concluídos pela teoria.

### Faltas (Elementos Omitidos)
- **Derivação Cosmológica Exata de $\alpha$ (Q37)**: O `06.9` lista as condições para herdar acoplamentos ($Z_Q^{\rm lab}=Z_Q^E$), mas omite inteiramente que isso *foi concluído com sucesso* na classe de Einstein isotrópica, atingindo a previsão zero-parâmetro $(\alpha_E^{\rm mean})^{-1} \approx 137.036\dots$ (fator de 1920, projetor $9/(8\pi^4)$, média de 4 autovalores).
- **Espectro do Setor $C_3$ (Q28/Q37)**: `06.10` afirma o gap do setor $C_3$, mas esconde o resultado da taxonomia já pacificado: o espectro relativo positivo **$\{3/2, 3/2\}$** da Hessiana.
- **Status da Polarização via Routh (`06.8`)**: A identidade $\Pi_{S_R} = \rho_{\rm lab}$ omite que ela emerge expressamente da redução de Routh num mínimo estável, sendo a chave final da "ponte".

### Melhorias Sugeridas
- **Exemplo de Metrologia e DtN em `06.9`**: Conectar textualmente a abstração do Lema 6 à prática do Complemento de Schur (DtN) sob a órbita $W(D_5)$ para obter $\alpha$.
- **Cross-Linking Avançado**: Em `06.10`, linkar explicitamente com o Capítulo 14 para as 3 gerações (que decorrerão diretamente do gap $C_3$).

---

## Capítulo 07 (Limite Clássico)

Capítulo excessivamente fragmentado. Formalizou a expansão assimptótica, mas excluiu o método rico que conectava o limite clássico à fenomenologia GDQ.

### Faltas (Elementos Omitidos)
- **Omissão dos "Três Operadores" Históricos (`07.1`, `07.7`)**: O projeto original (histórico `pt-br/28`) alcançava Hamilton-Jacobi impondo $\hbar \to 0$, $T_{\text{efetivo}} \to 0$ e a reversão de Wick ($\tau \to it$). O texto atual descartou essa abordagem física do "fluido espacial esfriando/congelando" em favor apenas do parâmetro adimensional formal $\varepsilon_{\rm cl}$. 
- **Omissão Grave em `memory.md`**: Os arquivos físicos WKB/Liouville/Hamilton-Jacobi existem em `manuscrito/07_classical_limit`, mas o sistema de controle `memory.md` não os lista entre os tópicos consolidados, criando uma inconsistência de "conhecimento do sistema".
- **Falta de Profundidade nas Cáusticas (`07.7`)**: O WKB é apresentado genericamente ($a_0 + \hbar a_1 + \dots$). Falta integrar isso com o colapso estocástico (índice de Maslov e fase estacionária vinda da ação de Wiener).

### Melhorias Sugeridas
- **Desfragmentação Estrutural**: Fundir os 12 micro-arquivos `07.1` a `07.12` em 3 grandes seções coesas: (1) Correspondência e Limite Escalar, (2) Determinismo Clássico e Limite WKB, (3) Correspondências Macroscópicas de Campo.
- **Reintegração Fenomenológica**: Dedicar um box explicativo resgatando a intuição dos "Três Limites" históricos, justificando teoricamente por que o tratamento moderno (expansão formal $\varepsilon_{\rm cl}$) suplantou a manipulação heurística do passado, sem perder a riqueza conceitual geométrica.
