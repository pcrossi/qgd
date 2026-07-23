# Respostas necessárias para resolver as inconsistências da GDQ

## 1. Finalidade

Este documento lista as respostas que a GDQ precisa fornecer para encerrar
as inconsistências identificadas na auditoria técnica.

Uma inconsistência não é resolvida apenas por uma explicação conceitual.
Cada resposta precisa assumir uma destas formas:

1. definição explícita;
2. demonstração matemática;
3. cálculo reproduzível;
4. referência a um teorema cujas hipóteses sejam satisfeitas;
5. comparação experimental independente;
6. reconhecimento de que a alegação original estava errada e foi retirada.

Para cada questão, a resposta deve informar:

```text
Enunciado:
Hipóteses:
Definições:
Derivação:
Resultado:
Limitações:
Teste independente:
Arquivos afetados:
Status: aberto | parcial | resolvido | refutado
```

---

# Parte I — Definição fundamental da teoria

## 2. O que é matematicamente a GDQ?

### Perguntas obrigatórias

1. Qual é a variedade fundamental \(M\)?
2. Qual é sua dimensão real e complexa?
3. Ela é compacta, completa ou possui bordo?
4. Qual é a assinatura da métrica?
5. Qual é sua topologia?
6. Existe estrutura spin?
7. Qual é a subvariedade identificada com o espaço-tempo físico?
8. Como essa subvariedade recebe assinatura lorentziana?
9. As dimensões complementares são coordenadas físicas, espaço de fase ou
   fibras internas?

### Resposta aceitável

Uma definição completa de \((M,g,J)\), atlas, dimensão, assinatura,
condições globais e estruturas adicionais.

### Critério de resolução

Todos os capítulos usam a mesma geometria ou declaram explicitamente uma
redução derivada dela.

---

## 3. Por que a dimensão escolhida é quatro complexa?

### Perguntas obrigatórias

1. \(n=4\) é axioma ou resultado?
2. Se for resultado, qual mecanismo seleciona \(n=4\)?
3. Qual é o conteúdo de campos usado no cálculo de anomalias?
4. Quais são suas representações?
5. Qual é o polinômio de anomalia?
6. Por que as demais dimensões falham?
7. Como a dimensão complexa 4 é compatível com os scripts em dimensão
   complexa 5 e com trechos que usam dimensão complexa 2?

### Resposta aceitável

Um cálculo de índice e anomalias para todas as dimensões candidatas, depois
de definir campos e representações.

### Resposta alternativa aceitável

Declarar \(n=4\) como axioma e retirar alegações de derivação.

---

## 4. Qual conexão geométrica é usada?

### Perguntas obrigatórias

1. A conexão fundamental é Levi-Civita, Chern, Bismut ou Cartan?
2. Qual é sua fórmula?
3. Qual é sua torção?
4. A torção é uma 3-forma totalmente antissimétrica?
5. \(dH=0\)?
6. Quais identidades de Bianchi são satisfeitas?
7. Como a conexão se transforma sob calibre?
8. Em que sentido a variedade continua sendo chamada Kähler?

### Resposta necessária

Definir inequivocamente:

\[
\nabla g,\qquad \nabla J,\qquad
T(X,Y),\qquad H(X,Y,Z)=g(T(X,Y),Z).
\]

### Correção obrigatória

Retirar a afirmação de que preservar uma estrutura complexa obriga o
surgimento de torção. Isso não é verdadeiro para a conexão de Levi-Civita
de uma variedade Kähler.

---

## 5. Quais são os campos fundamentais?

### Perguntas obrigatórias

Para cada campo:

1. qual é seu domínio?
2. qual é seu contradomínio?
3. qual é sua unidade?
4. ele é real ou complexo?
5. é dinâmico ou fixo?
6. qual é sua lei de transformação?
7. qual é seu dado inicial?

### Campos que precisam ser distinguidos

- métrica \(g\);
- estrutura complexa \(J\);
- torção \(H\) ou \(B\);
- campo de Perelman \(f\);
- densidade \(\rho\);
- amplitude \(R\);
- ação/fase \(S_R\);
- potencial osmótico \(S_I\);
- tempo físico \(t\);
- parâmetro de fluxo \(\tau\);
- campos de calibre;
- campos fermiônicos.

### Critério de resolução

Nenhum símbolo muda de significado entre capítulos sem mapa explícito.

---

# Parte II — Tempo, assinatura e causalidade

## 6. O que é \(\tau\)?

### Inconsistência atual

\(\tau\) aparece como:

- tempo de fluxo;
- variável com dimensão de área;
- tempo difusivo;
- logaritmo adimensional de escala;
- coordenada imaginária associada a \(t\).

### Perguntas obrigatórias

1. Qual é a definição fundamental de \(\tau\)?
2. Qual é sua dimensão física?
3. Qual é sua relação com a escala de renormalização?
4. Qual é sua relação com \(t\)?
5. A evolução em \(\tau\) é física ou auxiliar?

### Resposta aceitável

Escolher uma definição e fornecer mapas dimensionais para os demais usos.

---

## 7. Como surge o tempo lorentziano?

### Perguntas obrigatórias

1. Quais funções de Schwinger são construídas?
2. Elas satisfazem reflexão positiva?
3. Há invariância euclidiana?
4. Há simetria por permutação?
5. Há propriedade de cluster?
6. Qual Hamiltoniano lorentziano é reconstruído?
7. Ele é autoadjunto e limitado inferiormente?

### Resposta aceitável

Verificação das hipóteses de Osterwalder–Schrader e reconstrução explícita.

### Resposta não aceitável

Escrever simplesmente \(t=-i\tau\) ou usar \(J^2=-1\).

---

## 8. Como a causalidade é preservada?

### Perguntas obrigatórias

1. Qual é o cone causal?
2. Quais são os propagadores retardado, avançado e de Feynman?
3. Por que usar metade avançado e metade retardado não permite sinalização
   para o passado?
4. Como comutadores de observáveis separados espacialmente se comportam?
5. Como o modelo trata experimentos de escolha retardada sem retrocausalidade
   observável?

### Critério de resolução

Demonstrar microcausalidade ou apresentar uma alternativa operacional
compatível com no-signalling.

---

# Parte III — Ação e equações de movimento

## 9. Qual é a ação fundamental da GDQ?

### Perguntas obrigatórias

1. Qual é a expressão completa?
2. Quais variáveis são independentes?
3. A ação é real?
4. Qual é sua unidade?
5. Quais são suas simetrias?
6. Quais termos de bordo são necessários?
7. Quais multiplicadores representam vínculos?
8. O funcional de Perelman é ação física ou funcional auxiliar?

### Resposta aceitável

Uma ação única e dimensionalmente consistente.

### Critério de resolução

Nenhuma equação física central é adicionada externamente depois da ação.

---

## 10. A ação produz a equação de continuidade?

### Problema atual

A ação do capítulo 4 não apresenta claramente um termo temporal capaz de
produzir \(\partial_\tau\rho\).

### Resposta necessária

Exibir:

\[
\frac{\delta I}{\delta S}=0
\quad\Longrightarrow\quad
\partial_\tau\rho+\nabla_\mu(\rho v^\mu)=0.
\]

O cálculo deve incluir integração por partes e condições de bordo.

---

## 11. A ação produz Hamilton–Jacobi–Bohm?

### Resposta necessária

Demonstrar:

\[
\frac{\delta I}{\delta\rho}=0
\]

e obter exatamente:

\[
\partial_tS+\frac{|\nabla S|^2}{2m}+V
-\frac{\hbar^2}{2m}\frac{\Delta\sqrt{\rho}}{\sqrt{\rho}}=0.
\]

### Correção necessária

Eliminar a derivada adicional aplicada ao potencial de Bohm no capítulo 4,
caso ela não resulte da ação.

---

## 12. A ação produz o fluxo métrico?

### Perguntas obrigatórias

1. A equação métrica é elíptica, parabólica ou hiperbólica?
2. Ela descreve fluxo auxiliar ou evolução física?
3. Qual tensor energia-momento é obtido?
4. Como aparece o termo de torção?
5. A equação satisfaz identidade de Bianchi?
6. Há conservação covariante?

### Resposta aceitável

Variação completa em \(g^{\mu\nu}\), sem inserir o tensor pretendido por
analogia.

---

## 13. Por que \(\mathcal U=\rho\)?

### Problema atual

Duas funções satisfazerem a mesma equação de transporte não implica que
sejam iguais.

### Resposta necessária

Fornecer:

- mesmas condições iniciais;
- mesmas condições de contorno;
- espaço funcional;
- teorema de unicidade aplicável.

### Resposta alternativa

Tratar \(\mathcal U=\rho\) como vínculo explícito da ação.

---

# Parte IV — Perelman, Madelung e Nelson

## 14. Qual é o mapeamento Perelman–Madelung?

### Perguntas obrigatórias

1. Qual é o mapa entre \((g,f,\tau)\) e \((\rho,S,t)\)?
2. O mapa preserva equações?
3. É injetivo, sobrejetivo ou apenas parcial?
4. Como trata nós \(\rho=0\)?
5. Como trata fase multivalorada?
6. Como trata estados dependentes do tempo?
7. Como trata superposição?

### Resposta aceitável

Um teorema preciso com prova ou uma delimitação explícita do domínio onde a
correspondência funciona.

### Possível conclusão válida

O mapeamento pode ser apenas uma analogia parcial. Isso deve ser aceito se
for o resultado matemático.

---

## 15. Como \(f\), \(S_I\) e \(\rho\) se relacionam?

### Perguntas obrigatórias

1. \(f\) é real ou complexo?
2. Se \(f\) é complexo, a medida de Perelman permanece positiva?
3. A relação é
   \(\rho=e^{-f}\), \(\rho=e^{S_I/\hbar}\) ou inclui
   \((4\pi\tau)^{-n/2}\)?
4. Como a normalização é preservada?
5. Como \(S_I=\hbar\mathcal W\) poderia relacionar um campo local a um
   funcional global?

### Correção provável

Retirar \(S_I=\hbar\mathcal W\), salvo se for fornecido um operador que
transforme o funcional global em campo local.

---

## 16. Qual é o coeficiente de difusão?

### Perguntas obrigatórias

1. É \(\nu=\hbar/(2m)\) ou \(\nu_0\) universal?
2. Como uma difusão universal produz massas distintas?
3. O fator \(\Omega=m/m_0\) é derivado ou definido?
4. Como termos envolvendo gradientes de \(\Omega\) são tratados na
   Fokker–Planck?

### Critério de resolução

Derivar a equação estocástica com difusão variável, incluindo todos os
termos de Itô.

---

# Parte V — Existência, unicidade e estabilidade

## 17. O sistema possui problema de Cauchy bem posto?

### Respostas necessárias

1. classificação das EDPs;
2. gauge utilizado;
3. espaços funcionais;
4. existência local;
5. unicidade local;
6. dependência contínua dos dados;
7. critérios de continuação.

### Resposta não aceitável

Invocar genericamente DeTurck sem mostrar que o sistema acoplado satisfaz
suas hipóteses.

---

## 18. Existem solítons que possam representar partículas?

### Perguntas obrigatórias

1. Qual é a solução explícita ou numérica?
2. Qual é sua energia?
3. É finita?
4. Qual é sua carga?
5. Qual é seu spin?
6. Qual é sua massa?
7. É estável linear e não linearmente?
8. Possui modos zero?
9. Qual é seu comportamento assintótico?
10. Como interage com outro solíton?

### Critério de resolução

Exibir uma solução das equações da GDQ, não um perfil escolhido externamente.

---

## 19. Monotonicidade implica estabilidade?

### Perguntas obrigatórias

1. Qual funcional é monotônico?
2. Sob quais hipóteses?
3. A monotonicidade é crescente ou decrescente?
4. Qual é a relação com energia física?
5. O extremo é mínimo, máximo ou sela?
6. Qual é o espectro da segunda variação?

### Critério de resolução

Calcular a Hessiana ou operador de Jacobi e demonstrar estabilidade.

---

# Parte VI — Estrutura quântica

## 20. Qual é o espaço de Hilbert?

### Respostas necessárias

- definição do espaço;
- produto interno;
- domínio dos operadores;
- estados físicos;
- evolução;
- observáveis;
- sistemas compostos;
- regra de produto tensorial.

---

## 21. A evolução é unitária?

### Perguntas obrigatórias

1. Qual operador gera evolução em \(t\)?
2. Ele é autoadjunto?
3. A norma é preservada?
4. Como uma dinâmica dissipativa em \(\tau\) se relaciona à evolução
   unitária em \(t\)?
5. Estados instáveis são descritos por Hamiltoniano efetivo ou teoria
   aberta?

### Critério de resolução

Prova de conservação do produto interno em tempo físico.

---

## 22. Como a regra de Born é derivada?

### Problema atual

Definir \(R=\sqrt{\rho}\) apenas reescreve \(\rho=R^2\).

### Perguntas obrigatórias

1. Por que probabilidades são quadráticas nas amplitudes?
2. Como alternativas exclusivas se somam?
3. Como sistemas compostos são tratados?
4. Como surge a base de medição?
5. Como são obtidas probabilidades em bases arbitrárias?

### Resposta aceitável

Uma derivação operacional que não use pesos Born em nenhuma etapa.

---

## 23. Como a objeção de Wallstrom é resolvida?

### Problema atual

A soma de Poisson utilizada já soma setores rotulados por inteiros.

### Perguntas obrigatórias

1. Qual estrutura global torna a fase \(S^1\)-valued?
2. Qual fibrado de linhas está envolvido?
3. Como a integralidade da primeira classe de Chern surge?
4. Por que circulações não inteiras não são estados admissíveis?
5. Como estados com nós são tratados?

### Resposta aceitável

Quantização derivada do espaço de estados ou do fibrado, sem introduzir
previamente índices inteiros.

---

## 24. Como o problema da medida é resolvido?

### Respostas necessárias

Construir um modelo contendo:

- sistema;
- aparelho;
- ambiente;
- interação;
- registros;
- decoerência;
- probabilidades;
- repetibilidade.

### Questões adicionais

1. Por que uma base é selecionada?
2. Um resultado único ocorre ou apenas decoerência?
3. Há variáveis adicionais?
4. Há colapso real?
5. O modelo permite sinalização?

### Resposta não aceitável

Inserir \(|\langle i|\psi\rangle|^2\) na função de partição e depois alegar
que a regra de Born foi derivada.

---

## 25. O problema do sinal foi realmente resolvido?

### Perguntas obrigatórias

1. Onde a fase fermiônica é armazenada?
2. Como observáveis sensíveis ao sinal são calculados?
3. Qual é a variância do estimador?
4. Qual é a complexidade assintótica?
5. Quais benchmarks são usados?
6. A superfície nodal precisa ser conhecida?

### Critério de resolução

Um algoritmo reproduzível com erro controlado e custo não exponencial em
uma classe de problemas relevante.

---

# Parte VII — Spin, calibre e Modelo Padrão

## 26. Como surge spin \(1/2\)?

### Respostas necessárias

1. fibrado spin;
2. álgebra de Clifford;
3. representação de \(\mathrm{Spin}(3,1)\);
4. operador de Dirac;
5. transformação sob \(2\pi\) e \(4\pi\);
6. graus de liberdade físicos.

### Resposta não aceitável

Usar apenas circulação inteira ou definir \(\kappa=\pm1\).

---

## 27. Como surge a estatística fermiônica?

### Perguntas obrigatórias

1. Por que campos de spin semi-inteiro anticomutam?
2. A teoria é local?
3. A energia é positiva?
4. A teoria é lorentziana?
5. As hipóteses do teorema spin–estatística são satisfeitas?

---

## 28. Como surge o grupo do Modelo Padrão?

### Respostas necessárias

Derivar:

\[
SU(3)_C\times SU(2)_L\times U(1)_Y
\]

e especificar:

- geradores;
- constantes de estrutura;
- representações;
- hipercargas;
- quiralidade;
- bósons de calibre;
- acoplamentos;
- cancelamento de anomalias.

Vetores de Killing genéricos não bastam.

---

## 29. Como ocorre quebra eletrofraca?

### Perguntas obrigatórias

1. Existe Higgs ou substituto?
2. Qual é o potencial?
3. Como \(W^\pm\), \(Z\) e fóton adquirem suas massas?
4. Qual é o ângulo de Weinberg?
5. Como férmions adquirem massa?
6. Qual é a escala \(v\)?

### Correção aritmética obrigatória

A fórmula atual

\[
v_K=\frac{M_e}{\alpha}
\left(1-\frac{3}{4\pi^2}\right)^{-1/2}
\]

produz aproximadamente \(72{,}85\,\mathrm{MeV}\), não
\(246\,\mathrm{GeV}\).

---

## 30. Como confinamento e mass gap são demonstrados?

### Perguntas obrigatórias

1. Qual é a teoria de calibre não abeliana?
2. Qual é a ação?
3. Como se definem Wilson loops?
4. A lei de área é derivada?
5. A seção transversal do tubo emerge ou é assumida?
6. Qual é o espectro do Hamiltoniano?
7. Como se prova gap positivo?

### Resposta não aceitável

Assumir área constante e densidade constante para então concluir
\(V(r)=\sigma r\).

---

## 31. Como o problema CP forte é resolvido?

### Perguntas obrigatórias

1. O campo geométrico é equivalente a um áxion?
2. Qual é sua periodicidade?
3. Qual é seu potencial?
4. Qual é sua massa?
5. Qual é sua constante de decaimento?
6. Como a suscetibilidade topológica da QCD entra?
7. Qual EDM residual é previsto?
8. A cosmologia do campo é viável?

### Correção necessária

Minimizar um potencial escolhido com mínimo em
\(\theta_{\mathrm{efetivo}}=0\) reproduz o mecanismo de áxion; não constitui
por si só uma nova solução.

---

# Parte VIII — Renormalização e ultravioleta

## 32. De onde vem o propagador modificado?

### Perguntas obrigatórias

1. Qual termo da ação gera \(e^{-p^2/\Lambda^2}\)?
2. O operador contém infinitas derivadas?
3. Quais são seus polos?
4. Há estados fantasma?
5. A continuação lorentziana é causal?

### Resposta não aceitável

Inserir manualmente o fator gaussiano em uma integral.

---

## 33. Qual é a escala de corte?

### Inconsistência atual

O texto usa aproximadamente \(0{,}511\,\mathrm{MeV}\) e \(1\,\mathrm{GeV}\).

### Perguntas obrigatórias

1. Existe uma única escala?
2. É física ou regulador?
3. Por que experimentos muito acima dessa escala continuam descritos pelo
   Modelo Padrão?
4. Como o corte depende da partícula?

---

## 34. A teoria preserva calibre em loops?

### Respostas necessárias

- fixação de gauge;
- determinante de Faddeev–Popov;
- fantasmas;
- identidades de Ward/Slavnov–Taylor;
- contratermos;
- beta-funções;
- independência do regulador.

### Critério de resolução

Ao menos um cálculo completo de loop derivado da ação.

---

## 35. O polo de Landau foi eliminado?

### Perguntas obrigatórias

1. Qual beta-função foi calculada?
2. Quais diagramas contribuem?
3. Qual é o esquema de renormalização?
4. O ponto fixo é estável?
5. É compatível com o running observado de \(\alpha\)?

Uma beta-função postulada não resolve o problema.

---

# Parte IX — Constantes e massas

## 36. De onde vem a escala dimensional?

### Perguntas obrigatórias

1. Qual comprimento ou energia fundamental é assumido?
2. Ele é derivado ou medido?
3. Como autovalores adimensionais se tornam MeV ou GeV?
4. A escala é universal?

### Critério de resolução

Se uma massa experimental fixa a escala, as demais grandezas devem ser
classificadas como razões previstas, não massas ab initio.

---

## 37. Como \(\alpha\) é derivada?

### Respostas necessárias

1. definir o setor \(U(1)\);
2. normalizar seu termo cinético;
3. normalizar a carga mínima;
4. demonstrar a relação entre operador geométrico e acoplamento;
5. especificar a escala de renormalização;
6. calcular \(\alpha(\mu)\).

### Questões sobre os números atuais

1. Por que \(9/(8\pi^4)\)?
2. Por que \(1920\)?
3. Qual grupo possui ordem 1920?
4. Por que a característica usada vale 5?
5. Qual variedade possui esses invariantes?
6. Por que a raiz quarta é necessária?

### Correção dos scripts

`calculo_alpha_gdq.py` deve ser retirado como evidência porque injeta
explicitamente o valor-alvo.

---

## 38. Como \(G\) é derivada?

### Perguntas obrigatórias

1. Por que o grupo de Buckingham escolhido tem a forma proposta?
2. Por que aparece \(\alpha^4\)?
3. Por que aparece \(e^{-1/(2\alpha)}\)?
4. O meio-instantão existe numa solução explícita?
5. Por que o fator de Fano entra?
6. A massa do próton é entrada?
7. A correção eletromagnética foi prevista ou escolhida para eliminar o
   resíduo?

### Critério de resolução

Derivar o limite newtoniano da ação e identificar \(G\) no coeficiente de
Einstein–Hilbert, antes da comparação numérica.

---

## 39. Como massas leptônicas são derivadas?

### Respostas necessárias

1. operador espectral;
2. domínio;
3. condições de contorno;
4. escala dimensional;
5. mapa autovalor–massa;
6. espectro completo;
7. estabilidade dos estados.

### Restrições

- não usar \(M_n-M_p\) para prever \(M_e\);
- não usar \(M_e\) e \(\alpha\) com fatores escolhidos para prever \(M_\mu\);
- não usar Koide como derivação de \(M_\tau\).

---

## 40. Como próton e nêutron são derivados?

### Respostas necessárias

- solução bariônica;
- massa;
- carga;
- spin;
- paridade;
- raio;
- momentos magnéticos;
- fatores de forma;
- espectro excitado;
- espalhamento;
- estabilidade.

### Questão obrigatória

Por que \(6\pi^5\) representa uma razão de massas e não apenas um número
numericamente próximo?

---

# Parte X — Aplicações quânticas

## 41. O poço e o oscilador testam a GDQ?

### Resposta necessária

Separar:

- resultados obtidos diretamente de Schrödinger/Madelung;
- resultados realmente produzidos por dinâmica métrica adicional.

Recuperar a solução depois de assumir seu ansatz não valida a nova teoria.

---

## 42. Stern–Gerlach

### Respostas necessárias

1. derivar os dois autovalores;
2. obter probabilidades;
3. tratar campo em direção arbitrária;
4. reproduzir sequências incompatíveis de medidas;
5. explicar contextualidade.

---

## 43. Efeito Zeeman e \(g-2\)

### Perguntas obrigatórias

1. \(g=2\) é derivado ou assumido?
2. A correção de Schwinger é calculada?
3. Qual diagrama ou operador produz a anomalia?
4. O resultado depende da escala?

---

## 44. Dupla fenda

### Perguntas obrigatórias

1. Qual equação GDQ é resolvida?
2. A métrica é evoluída?
3. Qual resultado difere da superposição padrão de gaussianas?
4. Qual previsão experimental distingue a GDQ?
5. O fator de decoerência é derivado?

### Correção dos scripts

Os gráficos atuais devem ser descritos como visualizações de um modelo
assumido, não simulações completas da GDQ.

---

## 45. Hartman

### Perguntas obrigatórias

1. Por que \(g_{xx}\propto\rho\)?
2. Essa relação resulta da ação?
3. Qual definição de tempo de tunelamento é usada?
4. Como deformação de pulsos é tratada?
5. A velocidade de frente permanece causal?

---

## 46. Aharonov–Bohm

### Perguntas obrigatórias

1. A fase padrão é apenas recuperada por acoplamento mínimo?
2. Qual mecanismo local adicional é previsto?
3. Há observável diferente da eletrodinâmica convencional?
4. A invariância de calibre é preservada?

---

## 47. Casimir

### Perguntas obrigatórias

1. O resultado vem da GDQ ou da soma padrão de modos?
2. Qual é a contribuição geométrica nova?
3. Como materiais, temperatura e geometria real são tratados?
4. O regulador é físico ou auxiliar?

---

## 48. Hidrogênio

### Respostas necessárias

- equação espinorial correta;
- espectro;
- degenerescências;
- estrutura fina;
- estrutura hiperfina;
- Lamb shift;
- dependência do raio do próton;
- comparação sem ajuste posterior.

Uma equação escalar ajustada para reproduzir Sommerfeld não substitui a
equação de Dirac.

---

## 49. Rotor molecular

### Perguntas obrigatórias

1. O espectro \(l(l+1)\) é derivado?
2. O parâmetro elástico é previsto?
3. A constante de distorção é calculada para várias moléculas?
4. O mesmo parâmetro funciona sem reajuste?

---

# Parte XI — Fenomenologia nuclear e partículas

## 50. Decaimento beta

### Correção necessária

O antineutrino não possui energia fixa de \(0{,}782\,\mathrm{MeV}\) no
decaimento beta livre. A energia é distribuída continuamente entre elétron,
antineutrino e recuo.

### Respostas necessárias

- amplitude de decaimento;
- acoplamento fraco;
- espaço de fase;
- espectro;
- vida média;
- correções radiativas;
- correlações angulares.

---

## 51. Decaimento alfa

### Perguntas obrigatórias

1. A métrica exponencial é derivada?
2. A frequência de tentativa é prevista?
3. Os mesmos parâmetros descrevem uma série isotópica?
4. Qual é a melhoria estatística sobre Gamow?

---

## 52. Klein–Nishina

### Perguntas obrigatórias

1. A amplitude vem da ação?
2. Como canais \(s\) e \(u\) aparecem?
3. Como polarizações e spin são somados?
4. A normalização da seção de choque é derivada?

Inserir a média de spin necessária para obter a fórmula final não é uma
derivação.

---

## 53. Neutrinos

### Respostas necessárias

- mecanismo de massa;
- unidades corretas;
- três massas;
- diferenças de massas quadradas;
- matriz PMNS;
- fase CP;
- hierarquia;
- efeito MSW;
- previsão independente.

---

# Parte XII — Cosmologia e gravitação

## 54. Como relatividade geral emerge?

### Perguntas obrigatórias

1. Qual limite da ação produz Einstein–Hilbert?
2. Como \(G\) aparece?
3. Qual tensor energia-momento acopla à métrica?
4. A equivalência fraca e forte é preservada?
5. Quais correções pós-newtonianas são previstas?

---

## 55. Buracos negros

### Respostas necessárias

- solução covariante;
- horizonte;
- invariantes de curvatura;
- extensão geodésica;
- condições de energia;
- estabilidade;
- evaporação;
- informação.

Um balanço energético newtoniano não resolve singularidades de GR.

---

## 56. Energia escura

### Perguntas obrigatórias

1. Por que a densidade do próton define a densidade UV?
2. Por que a diluição é linear?
3. Por que há 28 modos multiplicativos?
4. Por que a projeção é \(\alpha^2\)?
5. A equação de estado é \(w=-1\)?
6. Como perturbações cosmológicas evoluem?

---

## 57. MOND e \(a_0\)

### Correções necessárias

Unificar as fórmulas incompatíveis e corrigir:

\[
\frac{5{,}46\times10^{-10}}{2\pi}
\approx8{,}69\times10^{-11},
\]

não \(1{,}21\times10^{-10}\).

### Respostas necessárias

- derivação única de \(a_0\);
- curvas de rotação;
- lentes gravitacionais;
- dinâmica de aglomerados;
- CMB;
- comparação com MOND e matéria escura.

---

## 58. Hubble, lítio, Bullet Cluster e birrefringência

### Respostas necessárias

Um único modelo cosmológico deve calcular conjuntamente:

- \(H(z)\);
- CMB;
- BAO;
- supernovas;
- abundâncias BBN;
- lentes;
- crescimento de estrutura;
- birrefringência.

Explicações isoladas com fatores diferentes não resolvem o setor
cosmológico.

---

# Parte XIII — Erros numéricos obrigatórios

## 59. Escala eletrofraca

Corrigir a alegação de \(246\,\mathrm{GeV}\) produzida pela fórmula atual.

## 60. Raio do próton

Corrigir:

\[
0{,}8778\times0{,}07479\times10^{-3}\times3{,}7915
\approx0{,}000249\,\mathrm{fm},
\]

não \(0{,}0369\,\mathrm{fm}\).

## 61. Aceleração cosmológica

Corrigir a divisão por \(2\pi\) indicada na seção anterior.

## 62. Potências e unidades

Substituir expressões como:

\[
125\,\mathrm{GeV}^2
\]

quando o pretendido é:

\[
(125\,\mathrm{GeV})^2.
\]

## 63. Auditoria automática

Criar testes que verifiquem:

- todas as fórmulas numéricas;
- unidades de ambos os lados;
- valores intermediários;
- tolerâncias;
- dependências de constantes experimentais.

---

# Parte XIV — Scripts e simulações

## 64. `calculo_alpha_gdq.py`

### Resposta necessária

Reconhecer que o script é circular e removê-lo como validação.

### Motivo

O valor experimental de \(\alpha\) determina os invariantes e autovalores
que depois reproduzem o mesmo valor.

---

## 65. `calculo_alpha_gdq_2.py`

### Resposta necessária

Demonstrar a origem matemática dos fatores usados. O script apenas avalia a
fórmula.

---

## 66. Monte Carlo de \(\alpha\)

### Resposta necessária

Separar:

1. demonstração da razão volumétrica;
2. identificação dessa razão com acoplamento eletromagnético.

O Monte Carlo valida apenas a primeira.

---

## 67. Validador de \(G\)

### Resposta necessária

Remover a correção escolhida para cancelar o resíduo ou derivá-la antes de
consultar \(G\).

---

## 68. Simulação bariônica

### Respostas necessárias

- equações discretizadas;
- correspondência com a ação;
- ordem de convergência;
- estabilidade;
- independência de malha;
- conservação;
- extração de massa, raio e spin.

Uma animação 2D não valida um solíton bariônico 8D.

---

# Parte XV — Navier–Stokes

## 69. A alegação atual deve ser retirada?

Sim, até existir uma prova válida.

### Lacuna central

A estimativa uniforme em \(H^s\) depende de:

\[
\int_0^T\|\nabla u\|_{L^\infty}\,dt,
\]

que é precisamente o tipo de controle cuja ausência permite blow-up.

### Respostas necessárias para reabrir a alegação

1. estimativa uniforme independente de \(\epsilon\);
2. ausência de hipótese equivalente ao critério de regularidade;
3. convergência forte suficiente para o termo não linear;
4. recuperação da incompressibilidade;
5. controle global para dados gerais;
6. revisão por especialistas independentes.

Navier–Stokes deve permanecer separado da validação central da GDQ.

---

# Parte XVI — Referências e originalidade

## 70. Qual parte é realmente nova?

### Respostas necessárias

Para cada construção:

1. citar antecedentes;
2. descrever diferença formal;
3. identificar novo teorema ou previsão;
4. evitar alegações de originalidade sem busca bibliográfica.

### Áreas obrigatórias de revisão

- Nelson e Wallstrom;
- Madelung e Bohm;
- informação de Fisher;
- Ricci flow e Perelman;
- Bismut e generalized Ricci flow;
- Einstein–Cartan;
- quantização geométrica;
- Osterwalder–Schrader;
- BRST e renormalização;
- QCD e lattice;
- decoerência e medida.

---

# Parte XVII — Falsificabilidade

## 71. Qual previsão pode refutar a GDQ?

### Resposta necessária

Registrar:

```text
Observável:
Valor previsto:
Incerteza:
Escala:
Parâmetros utilizados:
Dados usados na calibração:
Dados reservados:
Resultado do Modelo Padrão:
Critério de refutação:
Data de congelamento:
```

### Requisitos

- não usar valor já conhecido;
- não alterar o modelo após conhecer o resultado;
- publicar incerteza;
- comparar com alternativas;
- aceitar resultado negativo.

---

# Parte XVIII — Ordem obrigatória das respostas

As questões não podem ser respondidas em ordem arbitrária.

## Bloco A — Fundação

1. definição da geometria;
2. conexão;
3. campos;
4. tempo e assinatura;
5. ação;
6. equações variacionais.

## Bloco B — Consistência

7. problema de Cauchy;
8. estabilidade;
9. causalidade;
10. unitariedade;
11. Perelman–Madelung.

## Bloco C — Estrutura quântica

12. espaço de Hilbert;
13. Born;
14. Wallstrom;
15. medida;
16. spin e estatística.

## Bloco D — Teoria de campos

17. calibre;
18. anomalias;
19. dimensão;
20. renormalização.

## Bloco E — Fenomenologia

21. solução solitônica;
22. escala dimensional;
23. constantes;
24. massas;
25. previsão cega.

Modelo Padrão completo, cosmologia e Navier–Stokes vêm depois desses blocos.

---

# Parte XIX — Critério final de encerramento

A auditoria somente poderá ser considerada respondida quando:

1. cada inconsistência tiver status explícito;
2. respostas matemáticas puderem ser reproduzidas;
3. erros objetivos tiverem sido corrigidos;
4. alegações não demonstradas tiverem sido reclassificadas;
5. scripts circulares não forem usados como evidência;
6. uma formulação única gerar as equações centrais;
7. a teoria tiver ao menos uma solução não trivial estável;
8. a estrutura quântica for operacional;
9. houver ao menos uma previsão verdadeiramente cega;
10. resultados negativos forem preservados, não escondidos por mudança
    retrospectiva da geometria.

O objetivo não é produzir uma resposta favorável para cada questão. O
objetivo é determinar quais componentes da GDQ podem ser sustentados e
quais precisam ser corrigidos ou abandonados.

---

# Nota de fechamento — 2026-07-18

Este documento fica fechado como checklist histórico de auditoria.

O estado vigente das respostas não deve mais ser lido diretamente daqui, mas
dos documentos canônicos criados durante a consolidação:

- `questoes/`, para as questões técnicas consolidadas;
- `relativas/`, para auditorias relativas ao texto legado e validações fracas;
- `memory.md`, para o mapa técnico vigente;
- `faltas.md`, para o backlog conservador;
- `brain/`, para axiomas, definições, teoremas, hipóteses e notas
  estruturadas;
- `metodologia/`, para o protocolo reaproveitável de cálculo, validação e
  refutação.

Classificação final:

$$
\boxed{
\text{RESPOSTAS\_NECESSARIAS\_GDQ está fechado como auditoria histórica.}
}
$$

Isso não significa que todo refinamento metrológico da GDQ esteja terminado.
Significa que as inconsistências originais foram triadas: algumas foram
resolvidas nas questões, algumas foram reclassificadas como condicionais,
outras foram movidas para trabalhos futuros, e alegações frágeis do texto
legado foram retiradas do núcleo da teoria.
