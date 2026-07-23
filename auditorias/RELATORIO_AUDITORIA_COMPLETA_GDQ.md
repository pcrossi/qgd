# Auditoria técnica integral do manuscrito GDQ

Data da auditoria: 2026-07-06  
Corpus: `pt-br`, comparação estrutural com `en`, notas técnicas e scripts em `src`.

## 1. Escopo e método

Foram incluídos:

- capítulos 00 a 41;
- apêndices 1 a 12;
- notas técnicas referenciadas pelos capítulos;
- `Referencias.md`;
- scripts `calculo_alpha_gdq.py`, `calculo_alpha_gdq_2.py`,
  `monte_carlo_alpha_gdq.py`, `validar_g_topologico.py`,
  `plot_dupla_fenda.py` e `plot_escolha_retardada.py`;
- comparação estrutural entre as versões portuguesa e inglesa.

Cada unidade foi avaliada segundo:

1. definição dos objetos matemáticos;
2. validade das passagens algébricas e variacionais;
3. consistência dimensional;
4. compatibilidade entre capítulos;
5. independência entre entrada e resultado;
6. relação com resultados conhecidos;
7. previsões falsificáveis;
8. suficiência bibliográfica.

As classificações usadas são:

- **Válido/reprodução:** recupera um resultado conhecido por uma transformação
  ou cálculo correto, sem validar a ontologia GDQ.
- **Hipótese:** postulado possível, mas não demonstrado.
- **Lacuna:** conclusão que pode talvez ser obtida, porém falta derivação.
- **Circular:** o resultado ou equivalente é usado como entrada.
- **Incorreto:** há contradição matemática, dimensional, numérica ou física
  identificável.

## 2. Conclusão executiva

A GDQ ainda não é uma teoria quântica de matéria matematicamente fechada.
O manuscrito é um programa especulativo que combina formalismos legítimos
(Madelung, Nelson, Ricci/Perelman, geometria hermitiana, Bismut e Cartan)
com novas identificações físicas. As respostas distribuídas pelo corpo do
texto melhoram a abrangência do projeto, mas não eliminam as principais
lacunas porque frequentemente:

- introduzem a propriedade que deveriam derivar;
- trocam analogia por igualdade;
- recuperam uma fórmula conhecida após assumir sua equação ou solução;
- escolhem constantes geométricas depois de conhecer o valor experimental;
- não definem um único sistema de campos válido em todos os capítulos;
- usam “teorema”, “prova” e “ab initio” sem demonstrar as hipóteses exigidas.

O material possui valor como caderno de hipóteses e programa de pesquisa.
Não sustenta, no estágio atual, alegações de resolução de gravitação
quântica, problema do sinal, medida, confinamento, mass gap, CP forte,
hierarquia eletrofraca ou Navier–Stokes.

## 3. Problemas estruturais transversais

### 3.1 Não existe uma definição única da teoria

Faltam, reunidos em um só lugar:

- variedade base, assinatura e condições de contorno;
- fibrados e grupos estruturais;
- lista de campos independentes;
- dimensões físicas dos campos;
- conexão escolhida (Levi-Civita, Chern, Bismut ou Cartan);
- ação única e real;
- espaço de estados e produto interno;
- observáveis;
- prescrição de quantização;
- condições de unitariedade e causalidade;
- relação exata entre tempo físico `t`, fluxo `τ` e escala de RG.

Em diferentes capítulos, `τ` é área, tempo difusivo, logaritmo adimensional
de escala e coordenada conjugada imaginária de `t`. Essas interpretações não
são intercambiáveis sem fatores dimensionais e um mapa explicitamente
definido.

### 3.2 Kähler, Bismut e torção são misturados

Uma variedade Kähler com sua conexão de Levi-Civita possui torção zero.
Preservar a estrutura complexa não obriga torção. Uma conexão de Bismut com
torção pode ser definida numa variedade hermitiana adequada, mas devem ser
especificados a 3-forma `H`, sua normalização, `dH`, a conexão e as equações
de movimento. O manuscrito alterna essas estruturas como se fossem a mesma.

### 3.3 O mapeamento Perelman–Madelung não foi provado

As relações entre `f`, ação, amplitude, densidade e kernel de calor variam:

- `f=-S/ħ`;
- `f=-(S_I-iS_R)/ħ`;
- `ρ=e^{-Re f}`;
- `ρ=e^{S_I/ħ}`;
- `ρ=(4πτ)^{-n/2}e^{-f}`;
- `S_I=ħ W`.

As últimas duas são objetos de naturezas diferentes: a densidade conjugada
de Perelman é uma função local normalizada; `W` é um funcional global. Uma
igualdade entre elas exige um teorema de representação que não é fornecido.

### 3.4 A ação do capítulo 4 não gera as equações declaradas

A ação escrita não contém claramente um termo canônico
`ρ ∂τ S_R`, mas sua variação é apresentada como se produzisse
`∂τ ρ + div(ρv)=0`. Duas soluções da mesma equação de transporte não são
idênticas sem as mesmas condições iniciais e de contorno. A variação em
`Re f` também apresenta uma derivada extra do potencial de Bohm.

É necessário recalcular todas as equações de Euler–Lagrange, incluindo
termos de bordo, vínculos, multiplicadores e variação da medida.

### 3.5 Assinatura e continuação analítica

O funcional de Perelman é originalmente riemanniano. O espaço-tempo físico
é lorentziano. Uma subvariedade lagrangiana de uma variedade Kähler
positiva não adquire automaticamente assinatura `(-,+,+,+)`. A continuação
analítica, domínio dos operadores e condições de reflexão positiva
Osterwalder–Schrader não são tratados.

### 3.6 Dimensionalidade inconsistente

O núcleo escolhe dimensão complexa 4/real 8. Outros trechos usam:

- dimensão complexa 2 para justificar `α⁴`;
- dimensão complexa 5 ou bola real 10 nos scripts;
- `T⁵×S³`, que tem oito dimensões reais, sem relação demonstrada com a
  variedade complexa inicial;
- espaço de configuração `3N`, também sem mapa para a geometria 8D.

A alegação de seleção única de `n=4` usa leis de potência e cancelamentos de
anomalia não derivados.

### 3.7 Regularização e renormalização

Os fatores gaussianos `exp(-p²/Λ²)` são inseridos, não derivados de um
operador cinético. Para que constituam uma teoria UV consistente é preciso
demonstrar:

- propagador proveniente da ação;
- prescrição de polos;
- unitariedade;
- causalidade;
- identidades de Ward/Slavnov–Taylor;
- invariância de calibre;
- comportamento multiloop;
- independência de regulador;
- compatibilidade com colisões muito acima de 1 GeV.

Há cortes incompatíveis de aproximadamente `0,511 MeV` e `1 GeV`.

### 3.8 Ajuste retrospectivo e circularidade

Os principais exemplos são:

- massa do elétron usando a diferença experimental nêutron–próton;
- massa do nêutron usando massas experimentais do elétron e próton;
- múon usando `M_e`, `α` e termos numéricos escolhidos;
- tau usando a relação empírica de Koide;
- `G` usando `M_p`, `α` e um exponencial não derivado;
- densidade escura usando raio do próton e horizonte de Hubble;
- raio do próton muônico usando ambos os raios-alvo;
- correções descritas como “a fração que faltava”.

Esses cálculos podem ser correlações numéricas, mas não são previsões.

### 3.9 Estatística e confronto experimental

Não há:

- função de verossimilhança;
- propagação de incertezas;
- penalização por número de escolhas;
- análise de sensibilidade;
- conjunto de treino versus teste;
- comparação com modelos concorrentes;
- previsão registrada antes da observação.

Concordância percentual isolada é insuficiente, especialmente quando
constantes experimentais entram na fórmula.

## 4. Matriz capítulo a capítulo

### Capítulos 00–05: fundação

| Documento | Avaliação | Pontos faltantes/correções |
|---|---|---|
| 00 Terminologia | Útil como glossário, mas redefine termos consolidados. | Separar definições padrão de metáforas próprias; definir “estômato”, “rede”, “impedância” e “Sudarshan” operacionalmente. |
| 01 Feynman/Wiener | A decomposição de Madelung e parte de Nelson são reproduções legítimas. A suposta falha geral da rotação de Wick por derivadas totais não é demonstrada. | Tratar fases de bordo, estados, condições de contorno e continuação analítica rigorosamente. Corrigir sinais/fatores da velocidade osmótica e distinguir mecânica estocástica de equivalência completa à MQ. |
| 02 Geometrização | Núcleo hipotético. Partícula = solíton e fase = torção são postulados. Kähler implicar torção é incorreto. | Especificar conexão, ação, assinatura, soluções solitônicas, cargas, spin e estabilidade espectral. Demonstrar seleção de dimensão e anomalias. |
| 03 Causalidade | O contorno temporal complexo e o propagador simétrico são assumidos. `S_I=ħW` mistura função local e funcional global. | Definir problema de valor de contorno, provar ausência de sinalização, positividade e equivalência de medidas. Corrigir dimensões de `dt_C`. |
| 04 Ação/loops | A tentativa de ação unificada é central, mas as variações declaradas não seguem da expressão. Regularização é imposta. | Refazer cálculo variacional completo e derivar propagadores/vértices. |
| 05 Renormalização | A beta-função GDQ é proposta sem cálculo de diagramas; sinais e ponto fixo são escolhidos. | Derivar contratermos e beta-funções a partir da ação; demonstrar cancelamento de fantasmas e anomalias BRST. |

### Capítulos 06–10: aplicações quânticas iniciais

| Documento | Avaliação | Pontos faltantes/correções |
|---|---|---|
| 06 Poço/oscilador | Recupera resultados padrão assumindo Hamilton–Jacobi de Madelung, ansatz gaussiano e quantização EBK/Maslov. | Não valida a nova geometria. Corrigir derivação do índice de Maslov: dois turning points dão índice total 2 e fase total `π`, mas a apresentação alterna `π/2` e `π`. |
| 07 problema do sinal | Tornar `ρ` positiva apenas desloca o sinal para fase/nós. A complexidade fermiônica não desaparece. | Fornecer algoritmo, custo assintótico, benchmark e prova de que observáveis de fase têm variância polinomial. A cirurgia topológica não resolve por si só NP-hardness. |
| 08 buracos negros | Balanço newtoniano gaussiano não analisa singularidade relativística. Tensor de Bohm é postulado e sua conservação não é provada. | Resolver equações covariantes, verificar condições de energia, horizonte, estabilidade e limite de grande massa. |
| 09 spin | Circulação inteira não produz automaticamente spin 1/2 nem representações de `Spin(3,1)`. | Construir espinores, álgebra de Clifford, ação de Dirac e transformação de 720°. |
| 10 Stern–Gerlach | Reproduz a força de dipolo após assumir `κ=±1` e `μ_B`. | Derivar dois autovalores, probabilidades de resultados, contextualidade e dinâmica para campos em direções arbitrárias. |

### Capítulos 11–21: estatística, medida e limite geométrico

| Documento | Avaliação | Pontos faltantes/correções |
|---|---|---|
| 11 spin–estatística | A mudança de sinal é essencialmente assumida pela holonomia. Correções COW/LAGEOS/Fano não têm derivação comum. | Demonstrar localidade, positividade de energia e covariância — hipóteses do teorema spin–estatística. Separar experimentos não relacionados. |
| 12 Hartman | `g_xx∝ρ` é o resultado decisivo e é imposto por vínculo. | Derivar a métrica da ação sem multiplicador desenhado para produzi-la; distinguir phase, dwell e traversal times; verificar causalidade de pulsos. |
| 13 Born | `ρ=R²` segue porque `R` foi definido como `exp(S_I/2ħ)`. É identidade, não derivação da regra de Born. | Derivar probabilidades de resultados, aditividade, contextualidade e normalização sem assumir `ρ=|ψ|²`. |
| 14 monopolos | `B=curl v` exclui monopolos por definição. Isso não é previsão independente. | Derivar eletromagnetismo e topologia de fibrados; confrontar monopolos de Dirac/'t Hooft–Polyakov. |
| 15 Wallstrom | A soma de Poisson soma setores inteiros já rotulados por `m`; portanto introduz a quantização que deveria explicar. A minimização do termo quadrático não seleciona universalmente inteiro diferente de zero. | Obter a condição de single-valuedness da estrutura de estados, não de uma soma imposta; tratar nós e domínios multiplamente conexos. |
| 16 medida | Dominância do estado fundamental de um semigrupo dissipativo não produz resultados Born gerais nem preserva superposições. | Modelar aparelho, ambiente, base preferida, probabilidades e repetibilidade. Evitar inserir amplitudes Born nos pesos de partição. |
| 17 monotonicidade com torção | Próximo de resultados conhecidos de fluxo de Ricci generalizado, mas hipóteses, normalizações e referências faltam. | Citar teoremas corretos; especificar variedade compacta, `dH`, gauge do dilaton e termos de bordo. Monotonicidade não implica estabilidade física automaticamente. |
| 18 incerteza | A derivação osmótica de Heisenberg é em grande parte válida sob hipóteses de regularidade. Extensões entrópica/GUP não seguem. | Corrigir fator de `u`, definir variâncias, condições de bordo e provar os termos extras de Fubini–Study/GUP. |
| 19 Zeeman/Stark | Recupera Hamiltonianos padrão após introduzir acoplamento mínimo, `μ_B`, spin e `g_geom`. | Calcular `g=2` e Schwinger a partir da teoria; distinguir índices e dimensões da torção; derivar polarizabilidade. |
| 20 tempo de fluxo | Equipara `τ=ln(L/L0)` a variável difusiva e a parte imaginária do tempo. Há conflito dimensional. | Escolher uma definição ou fornecer mapas com escalas. Provar emergência de Lorentz, não apenas assumir planura assintótica. |
| 21 NESS | Fano e Zwanzig–Mori são formalismos conhecidos inseridos fenomenologicamente. | Derivar projetor, kernel de memória, produção de entropia e coeficientes a partir da ação GDQ. |

### Capítulos 22–31: constantes, partículas e calibres

| Documento | Avaliação | Pontos faltantes/correções |
|---|---|---|
| 22 vácuo/G | Mistura estimativas diferentes. A “diluição 1D”, fator 28, projeção `α²` e meio-instantão são escolhidos. Há manipulações sem unidades em 22.4. | Definir densidades com unidades em cada integral; derivar fatores; prever cosmologia completa. |
| 23 elétron | Usa `M_n-M_p` experimental para obter `M_e`; não é massa ab initio. Fano e correção de 32,73 eV são ajustados. | Derivar escala absoluta e autovalor de operador antes de usar massas medidas; incluir espectro e incerteza. |
| 24 hierarquia | Lei exponencial não é resolvida. Fórmula do múon é numerologia e tau usa Koide. | Obter operador espectral explícito e todos os autovalores; incluir neutrinos e quarks; prever antes de ajustar. |
| 25 taxonomia | Classificação qualitativa por número de modos não reproduz representações do Modelo Padrão. | Tabela completa de `SU(3)×SU(2)×U(1)`, hipercarga, quiralidade, antipartículas, gerações, anomalias e regras de decaimento. |
| 26 próton/nêutron | `6π⁵` aproxima razão de massas, mas sua seleção não é derivada. Muitas correções usam alvos conhecidos. O espectro beta reproduz a fórmula padrão. | Resolver solíton 3D/4D, obter massa, raio, fatores de forma, spin e espalhamento. Corrigir afirmação sobre energia do antineutrino: o espectro beta é contínuo. |
| 27 confinamento | Assume área transversal finita e densidade constante; então `V=σr` é tautológico. Não prova Yang–Mills mass gap. | Formular campo de calibre não abeliano rigoroso, limite contínuo, positividade, gap e Wilson loops. `α_s=3/(8π)` não inclui running. |
| 28 limite clássico | `ħ→0` de Bohm não é uniforme; a derivação de Maxwell/Einstein contém os resultados desejados como equações de redução. | Fazer expansão WKB/decoerência controlada e derivar, não inserir, tensores de Maxwell e Einstein. |
| 29 α | Buckingham só identifica um grupo adimensional, não seu valor. Os fatores `9/8`, `1920` e característica 5 não são derivados de variedade definida. Há erro numérico textual pequeno. | Especificar grupo, ação, representação, operador e espectro. Fazer análise de seleção estatística entre fórmulas possíveis. |
| 30 CP forte | É essencialmente um mecanismo de áxion, mas o potencial é escolhido para ter mínimo em `θ_eff=0`. | Derivar suscetibilidade QCD, periodicidade, massa/acoplamentos do áxion e cosmologia. A alegação de EDM exatamente zero é mais forte que o mecanismo permite. |
| 31 calibres | Vetores de Killing não geram automaticamente o grupo do Modelo Padrão. A escala eletrofraca contém erro aritmético grave. | A fórmula escrita para `v_K` dá cerca de `72,85 MeV`, não `246 GeV`. Construir espaço interno, geradores, representações e acoplamentos. |

### Capítulos 32–41: fenomenologia e aplicações

| Documento | Avaliação | Pontos faltantes/correções |
|---|---|---|
| 32 cosmologia | MOND, Hubble, lítio, WEP, birrefringência e Bullet Cluster são modelos independentes com fatores escolhidos. Há duas fórmulas incompatíveis para `a0`; a passagem `5,46e-10/(2π)=1,21e-10` é aritmeticamente falsa (`≈8,69e-11`). | Derivar equações cosmológicas e perturbações; ajustar conjuntamente CMB, BAO, lentes, BBN e estrutura. |
| 33 UV/eletrofraca | Corte de `0,511 MeV` é incompatível com física observada acima dessa energia. `125 GeV²` é notação dimensional errada para `(125 GeV)²`. | Derivar filtro e demonstrar amplitudes do Modelo Padrão em altas energias. Corrigir escala eletrofraca. |
| 34 Hopf/monopolos | Hopf pode representar spinorialidade, mas os fatores topológicos usados depois não seguem da fibração. Monopolo é excluído por definição. | Construir fibrado, conexão, classes de Chern e espectro; evitar repetir Wallstrom sem resolver a circularidade. |
| 35 anomalias | Fórmulas para `g-2` e raio do próton são combinações dimensionais calibradas. O cálculo do raio apresenta erro: `0,8778×0,07479×10^-3×3,7915≈0,000249`, não `0,0369 fm`. | Atualizar status experimental, derivar amplitudes e corrigir aritmética. |
| 36 decaimento alfa | A parte de Gamow reproduz física conhecida; métrica exponencial e correção são assumidas. Resultado para U-238 é aproximado e depende de frequência escolhida. | Ajustar série isotópica completa com parâmetros previamente fixados; propagar incertezas. |
| 37 dupla fenda | As fórmulas são superposição padrão de dois pacotes gaussianos, renomeada como Perelman. A decoerência é inserida por fator exponencial. | Derivar dinâmica métrica distinta e uma previsão diferente da MQ. Corrigir argumento de mínimos: pacotes gaussianos finitos realmente podem não zerar, sem nova física. |
| 38 hidrogênio | A equação radial é construída para se parecer com Coulomb/Dirac, mas é escalar e não reproduz estrutura espinorial Dirac. `α=r_s/λ_c` redefine `r_s` para obter a carga. | Calcular níveis, degenerescências, fine/hyperfine structure e Lamb shift numericamente sem parâmetros ajustados. |
| 39 Casimir | Recupera a derivação padrão por soma de modos e Poisson. A identidade inicial de Bohm é tautológica. | Mostrar contribuição nova, condições materiais, temperatura e geometria real; derivar regulador da GDQ. |
| 40 Aharonov–Bohm | Recupera a fase padrão após acoplamento mínimo e Stokes. Não demonstra mecanismo local observável. | Definir campos locais adicionais e prever efeito distinto sem violar invariância de calibre. |
| 41 rotor | Espectro rígido é assumido. Distorção centrífuga introduz `γ_elastic` livre e apenas reparametriza a fórmula espectroscópica. | Derivar `γ_elastic` e comparar várias moléculas sem reajuste. Corrigir `u=(ħ/m)∇S_R` se `S_R` já tem unidade de ação. |

## 5. Matriz dos apêndices

| Apêndice | Avaliação | Lacuna principal |
|---|---|---|
| 1 índice torsional | Constantes são montadas por normalizações e fatores escolhidos. A estabilidade de Koide é afirmada sem Hessiana explícita. | Definir operador de Jacobi e derivar seus autovalores; provar grupo de ordem 1920 e característica 5. |
| 2 auditoria cosmológica | Registra falhas anteriores, o que é positivo. A correção final diz usar “exatamente a fração que faltava”, evidência explícita de ajuste. | Congelar modelo e testar novos dados; corrigir tratamento de incerteza de `G`. |
| 3 arrasto | Identifica incorretamente `1/(4π³)` como primeiro autovalor de Laplaciano por volume. Ação de Chern–Simons e `6π⁵` não seguem das projeções dadas. | Especificar domínio/métrica/condições e calcular espectro real. |
| 4 existência/unicidade | Existência local de EDE não implica global. O princípio do máximo é aplicado a potencial singular dependente da própria densidade. A inferência de curvaturas iguais para métricas iguais é inválida. | Teoremas com hipóteses, estimativas a priori e controle de explosão. |
| 5 química | Reformula Madelung qualitativamente; não calcula uma ligação. | Resolver H₂ ou sistema mínimo e comparar energia/comprimento de ligação. |
| 6 Klein–Nishina | A cinemática Compton é imposta e o fator de spin necessário à fórmula final é inserido na “média geométrica”. | Derivar amplitude, polarizações e normalização a partir da ação. |
| 7 mésons/neutrinos | PMNS é essencialmente parametrizada por ângulos escolhidos; fórmula de massa tem problemas dimensionais. | Massas, diferenças quadráticas e fases CP previstas por operador definido. |
| 8 simulação de solíton | O código é uma visualização de campos 2D, não integração fiel do tensor de Ricci/Bismut em 8D nem validação bariônica. | Testes de convergência, conservação, solução estacionária e comparação quantitativa. |
| 9 escolha retardada | O amortecimento logístico é inserido. O script altera franjas somente após a posição da escolha, apesar do texto retrocausal. Há inconsistência `Ω=e^{-λτ}` versus volume linear `1-2λτ`. | Modelo unitário completo, no-signalling e comparação com probabilidades experimentais. |
| 10 Tsallis | Expansão perto de `q=1` é formal; equiparar termos médios não demonstra equivalência das entropias. | Distribuição estacionária derivada e previsão independente de `q`. |
| 11 ensemble | A medida funcional sobre métricas não é definida. A última derivação de Born coloca `|⟨i|ψ⟩|²` diretamente em `Z`. | Regularização da integral funcional e derivação não circular das probabilidades. |
| 12 Navier–Stokes | Não resolve o problema Clay. O Teorema 2 assume precisamente a estimativa uniforme global que precisa ser provada; Grönwall contém `∫||∇u||∞`, o critério de blow-up. O limite singular não é justificado. | Provar estimativa uniforme independente de `ε` sem assumir controle de vorticidade. |

## 6. Notas técnicas

As notas ampliam justificativas, mas não alteram o veredito porque:

- notas 1–5 repetem as identificações Nelson–Perelman e regularização sem
  derivação do operador;
- nota 2.8 concentra muitas alegações de topologia, dimensão e anomalias,
  porém não fornece as demonstrações completas anunciadas;
- notas 8–10 expandem buracos negros, spin e Stern–Gerlach sem construir a
  teoria espinorial;
- notas 27–30 aplicam os mesmos fatores `δ`, Fano, `6π⁵`, `1920` e Koide,
  logo não são validações independentes;
- notas 31–33 apresentam explicações possíveis para anomalias cosmológicas,
  mas não realizam ajuste conjunto nem derivam novos dados.

Cada nota deve ser transformada em um destes três formatos:

1. lema com hipóteses e prova;
2. cálculo fenomenológico reproduzível;
3. hipótese explicitamente rotulada, com teste que poderia refutá-la.

## 7. Auditoria dos scripts

### `calculo_alpha_gdq.py`

É circular:

- define `alpha_alvo=1/137.035999084`;
- calcula `tr_T4` da diferença necessária para atingir esse alvo;
- define `lambda_2_sq` usando `137.035999084`;
- constrói uma matriz cujo determinante necessariamente reproduz o alvo.

O erro residual `~10^-16` mede apenas consistência da construção.

### `calculo_alpha_gdq_2.py`

Calcula corretamente a fórmula escolhida, obtendo
`α^-1≈137.036082448`. Não demonstra que `9/(8π⁴)` e
`(π⁵/1920)^(1/4)` são impostos pela teoria. A mensagem “formalmente válida”
não decorre de erro relativo pequeno.

### `monte_carlo_alpha_gdq.py`

O Monte Carlo confirma aproximadamente uma razão volumétrica `1/16` para o
domínio programado. A identificação posterior dessa razão, da potência
`1/4` e do fator de rigidez com `α` é externa à simulação. “O número emergiu
sozinho” é incorreto.

### `validar_g_topologico.py`

Reproduz a fórmula proposta. A concordância é melhorada por
`delta_em=0.0013063`, escolhido para corrigir o resíduo. Não é validação
independente.

### Scripts de dupla fenda e escolha retardada

São visualizações funcionais de modelos analíticos assumidos. Não resolvem
as equações métricas GDQ. Os parâmetros são normalizados e não há comparação
estatística com dados.

## 8. Tradução inglesa

A tradução preserva majoritariamente estrutura, equações e problemas do
original. Pontos a corrigir:

- padronizar GDQ/QGD;
- não traduzir torção como “tension”;
- distinguir stress tensor, torsion tensor e strain tensor;
- corrigir links Obsidian e títulos inexistentes;
- revisar termos como “stomata”, “causal folding”, “metric mesh” e
  “Sudarshan theorem”, que não possuem definição técnica padrão;
- manter a mesma versão e os mesmos números entre idiomas.

A versão inglesa não deve ser tratada como validação independente.

## 9. Referências faltantes

A bibliografia atual é insuficiente. O manuscrito precisa, no mínimo, de
literatura primária ou textos de referência sobre:

- construção rigorosa de integrais de caminho e Osterwalder–Schrader;
- mecânica estocástica e críticas a Nelson/Wallstrom;
- fluxos de Ricci generalizados, pluriclosed flow e Bismut;
- Einstein–Cartan e férmions com torção;
- quantização geométrica e metaplectic correction;
- teorema spin–estatística;
- BRST, anomalias e renormalização;
- QCD, confinamento, lattice gauge theory e mass gap;
- física de neutrinos e ajustes globais PMNS;
- cosmologia CMB/BAO/BBN/lensing;
- decoerência e teoria quântica da medição;
- Navier–Stokes e limites de baixa compressibilidade/capilaridade quântica.

Toda afirmação “demonstra-se” deve apontar para uma prova interna completa
ou referência exata com hipóteses compatíveis.

## 10. Previsões e critérios de falsificação necessários

Antes de novos ajustes, o modelo deve congelar seus parâmetros e publicar
ao menos uma previsão:

1. valor de uma grandeza ainda não usada em nenhuma fórmula;
2. intervalo de incerteza;
3. escala de renormalização;
4. condições experimentais;
5. diferença quantitativa em relação ao Modelo Padrão/GR;
6. critério explícito que refutaria a GDQ.

Candidatos possíveis:

- desvio espectroscópico específico não absorvível em constantes padrão;
- correção angular em espalhamento com energia e polarização definidas;
- relação entre dois observáveis cosmológicos usando parâmetros fixados em
  outro conjunto de dados;
- espectro completo de um operador solitônico, incluindo estados ausentes.

## 11. Plano de correção  Once the record is published you will no longer be able to change the files in the upload! However, you will still be able to update the record's metadata later.recomendado

### Prioridade 0 — retirar alegações não sustentadas

Substituir “prova”, “resolução”, “única”, “exata” e “ab initio” por
“hipótese”, “ansatz”, “estimativa” ou “reprodução”, conforme o caso.
Retirar imediatamente a alegação de solução de Navier–Stokes.

### Prioridade 1 — especificação matemática mínima

Produzir um artigo-base de 20–30 páginas contendo somente:

- dados geométricos;
- campos;
- ação;
- simetrias;
- dimensões;
- variações completas;
- um limite conhecido;
- uma solução não trivial.

Nenhuma fenomenologia deve preceder essa etapa.

### Prioridade 2 — escolher um único setor

O melhor candidato é uma extensão controlada de Madelung/Nelson em
variedade hermitiana com torção. Não tentar simultaneamente explicar todas
as constantes e anomalias.

### Prioridade 3 — validação independente

- separar parâmetros ajustados de previstos;
- remover constantes-alvo dos scripts;
- adicionar testes unitários de dimensões e aritmética;
- usar notebooks reproduzíveis;
- fazer análise de sensibilidade e comparação estatística.

### Prioridade 4 — somente então ampliar

Após consistência do modelo-base, escolher uma aplicação pequena, como
oscilador, espalhamento ou espectroscopia, e produzir uma previsão nova.

## 12. Veredito final

O corpo do manuscrito contém respostas explícitas a várias objeções que uma
leitura apenas dos capítulos fundamentais não captaria. Essas respostas,
porém, não fecham a teoria. Elas deslocam as lacunas para novos postulados,
normalizações, escolhas topológicas ou fatores fenomenológicos.

Classificação técnica atual:

> Programa especulativo de geometrização da mecânica quântica, amplo e
> criativo, mas matematicamente subdefinido, internamente inconsistente em
> pontos essenciais e fenomenologicamente dominado por reproduções,
> circularidade e ajustes retrospectivos.

O avanço decisivo não virá de adicionar mais fenômenos. Virá de reduzir o
escopo, fixar uma ação coerente e demonstrar uma única consequência nova
sem usar o resultado como entrada.
