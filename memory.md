# Memória técnica consolidada da Geometrodinâmica Quântica (GDQ)

> Documento de memória do projeto. Não substitui as demonstrações completas,
> os arquivos `questão_*.md` ou o manuscrito. Sua função é impedir perda de
> contexto, registrar a versão vigente da teoria e distinguir resultados,
> hipóteses, evidência numérica e trabalhos futuros.

## 1. Como usar esta memória

### 1.1 Hierarquia das fontes

Quando dois arquivos discordarem, usar esta ordem de autoridade:

1. ação oficial preservada nas Questões 4 e 9;
2. documentos finais e conservadores de cada questão;
3. `faltas.md`, `faltas_mapa.md` e `faltas_plano.md`;
4. relatórios numéricos auditados;
5. manuscrito `pt-br/`, como fonte das ideias originais;
6. rascunhos, backups, scripts exploratórios e relatórios triunfalistas.

Um resultado numérico não corrige sozinho uma lacuna variacional. Uma
concordância obtida depois de conhecer o alvo deve ser registrada como
engenharia inversa ou comparação fenomenológica, não como previsão.

### 1.2 Vocabulário de status

- **Demonstrado:** segue dos axiomas e da ação dentro do domínio declarado.
- **Fechado estruturalmente:** operador, domínio e cadeia lógica existem, mas
  ainda pode faltar integral, índice, espectro ou avaliação numérica.
- **Condicional:** correto se uma hipótese técnica explicitada for satisfeita.
- **Efetivo:** redução consistente em determinado regime; não é fundamento
  independente da ação oficial.
- **Exploratório:** ansatz, simulação ou comparação útil, sem poder de prova.
- **Aberto:** falta construção matemática essencial.
- **Programa futuro:** ideia preservada, mas não usada como premissa atual.

### 1.3 Regra de honestidade científica

Não usar as expressões “prova definitiva”, “ab initio” ou “sem parâmetros” se
o resultado depender de calibração, contorno escolhido após comparação,
normalização não derivada, ansatz auxiliar ou coeficiente fenomenológico.

### 1.4 Camada estruturada `brain/`

A pasta `brain/` passa a ser a camada hierárquica canônica do projeto.
Ela organiza o material por tipo lógico:

- axiomas;
- definicoes;
- teoremas;
- lemas;
- hipoteses;
- resultados condicionais;
- pendencias abertas;
- numericos;
- decisoes;
- futuro;
- referencias.

Use `memory.md` como mapa compacto e `brain/` como memoria estruturada.
O `agent-memory` deve guardar apenas fatos consolidados, decisoes estaveis e
ponteiros para os arquivos canonicos.

Atualizacao de 16 de julho de 2026: a documentacao estruturada no `brain/`
foi iniciada pelo Capitulo 1 do manuscrito. Foram criadas entradas canonicas
para o mapa do capitulo, o acordo terminologico, a rotacao de Wick como ponte
condicional, a difusao universal com inercia geometrica como resultado
condicional, e a lacuna estrutural Wiener--Feynman como problema aberto. O
registro persistente correspondente foi salvo no `agent-memory`.

Na mesma data, o Capitulo 2 foi documentado no `brain/`. Foram criadas
entradas para a acao oficial como axioma dinamico, o bulk local
`R^4 x T^4`, a estrutura Hermitiana--Bismut, a decomposicao de `f`, a medida
ponderada, a forma-relogio lorentziana, o criterio de soliton material e a
existencia de backgrounds materiais como problema aberto setorial. As notas
chamadas pelo capitulo e as auditorias `axiom_to_theorem_audit.md` e
`preservation_map.md` foram registradas em detalhe.

O Capitulo 3 tambem foi documentado no `brain/`. Foram criadas entradas para
a variavel causal complexa `z_tau`, o contorno causal `gamma`, formas exatas,
periodos e residuos, realidade da acao no contorno admissivel, quantizacao por
monodromia e a microcausalidade operacional como problema aberto de medida.
O status consolidado e: o paradoxo de Wick esta resolvido estruturalmente pela
separacao entre `tau`, `t`, `z_tau` e `gamma`; unitariedade, no-signalling e
microcausalidade experimental permanecem teoremas de capitulos posteriores.

O Capitulo 4 foi documentado no `brain/`. Foram criadas entradas para a
consistencia dimensional da acao oficial, dados variacionais da GDQ,
Hessiana fisica e loops, quociente fisico/fantasmas, polarizacao `U(1)`
heat-kernel e a finitude perturbativa em todas as ordens como problema aberto.
O status consolidado e: a acao oficial permanece preservada; `Lambda_C` e
numero de corte adimensional nas coordenadas de Cartan; a nocao fundamental de
loop e `1/2 Tr_phys ln Hess S_GDQ`; fantasmas sao representacao auxiliar do
jacobiano do quociente, nao ontologia; a ausencia do polo de Landau esta
fechada apenas no setor `U(1)` heat-kernel declarado e sob a desigualdade
espectral explicita.

O Capitulo 5 foi documentado no `brain/`. Foram criadas entradas para a
corrente de fase e Noether, equacao de densidade e operador de Bohm, equacao
metrica ponderada, condicoes de bordo pela variacao, setor canonico de
Madelung e a selecao canonica de Madelung como problema aberto/condicional.
O status consolidado e: a primeira variacao da acao oficial esta fechada no
bulk Hermitiano declarado; a corrente de fase, o operador
`Delta sqrt(rho)/sqrt(rho)`, a equacao metrica ponderada, Noether e os bordos
foram derivados. A identidade `Pi_{S_R}=rho` e o termo canonico
`rho partial_t S_R` nao sao identidades off-shell da acao oficial; pertencem
a uma polarizacao fisica/reducao de Routh e a ponte global--local/medida.

O Capitulo 6 foi documentado no `brain/`. Foram criadas entradas para os seis
lemas da ponte global--local: limite apontado, transporte de campos e medida,
convergencia de Hessiana fisica, localizacao e gap uniforme, heranca por
projetores de Riesz e separacao entre topologia e normalizacao continua.
Tambem foram registradas a ponte aplicada ao setor `C3`, a heranca condicional
da normalizacao eletromagnetica e a pendencia do pullback causal de Madelung.
O status consolidado e: a incompatibilidade abstrata entre `T^5 x S^3` e
`R^4 x T^4` esta removida para setores localizados com gap; no setor
estacionario reduzido `C3`, a ponte e teorema aplicado com gap primitivo
`Delta_0=1/2`. Isso nao calcula automaticamente normalizacoes continuas
como `Z_Q`, respostas de aparelhos ou a identidade canonica
`Pi_{S_R}=rho`.

O Capitulo 7 foi documentado no `brain/`. Foram criadas entradas para o
limite classico no setor de Madelung, o limite local cotangente--Kepler, as
conservacoes classicas de Noether, a correspondencia macroscópica de Maxwell,
a correspondencia macroscópica de Einstein e a nota futura sobre anomalias
`g-2`/mesons. O status consolidado e: o principio de correspondencia escalar
esta fechado condicionalmente no setor regular de Madelung, controlado por
`epsilon_cl = hbar/(p L_rho)` e com erro de Bohm de ordem
`O(epsilon_cl^2)`. Maxwell e Einstein aparecem como correspondencias
setoriais usando estruturas ja construidas; as normalizacoes absolutas
`Z_Q`, `alpha`, `G`, backgrounds admissiveis e residuos torsionais permanecem
calculos setoriais proprios. O capitulo nao chama notas pedagogicas externas
diretamente; o `preservation_map.md` preserva a nota legada
`pt-br/notas/28/nota_28.1_anomalias_muon_mesons.md` apenas como programa
fenomenologico futuro, nao como prova do limite classico.

A Questao 2 foi documentada no `brain/` a partir do consolidado
`questão_2.md`. O estado vigente e: a definicao matematica da GDQ como EFT
axiomatica esta fechada com bulk local
`M = R^4 x T^4`, dimensao real 8 e dimensao complexa 4. O bulk permanece
Riemanniano/Hermitiano--Bismut; o espaco-tempo fisico e uma variedade
quadridimensional `N` imersa em `M`. A metrica lorentziana fisica e
constitutiva,
`h = q - 2 u otimes u / q^{-1}(u,u)`, com `q=X^*g`,
`u=X^*dtheta_1` e dominio fisico `X^*dtheta_1 != 0`. Essa condicao e
restricao cinematica/topologica, nao barreira dinamica derivada. Foi
registrada a existencia de estrutura spin por `w2(TM)=0`, as 16 estruturas
spin de `T^4`, e o setor fermiônico antiperiodico vigente
`epsilon_F=(1,0,0,0)`, que gera circulacao `h(n+1/2)`. A escolha desse setor
continua axiomatica ate prova dinamica. Tambem foi registrado que
`X^*dtheta_a` e conexao plana, nao eletromagnetismo local; gauge local exige
conexao de Ehresmann, e a 3-forma de Bismut nao e Maxwell. Massas, cargas,
`alpha`, raios internos e `Lambda_C` permanecem abertos como programa
espectral de Ricci--Bismut, sem reabrir a definicao da teoria.

A Questao 3 foi documentada no `brain/` a partir de `questão_3.md`. O estado
vigente e: a pergunta “por que quatro dimensoes complexas?” esta respondida
pela rota axiomática. A escolha estrutural da Q2,
`M = R^4 x T^4`, implica `dim_R M = 8` e, apos estrutura complexa,
`dim_C M = 4`. Portanto `n=4` e consequência da definicao vigente, nao nova
hipotese independente e nao uma selecao dinamica ja provada. Fica proibido
afirmar no estado atual que `n=4` foi derivado por Atiyah--Singer, anomalias,
grupo `B4` ou ordem diferencial de operadores. A rota Atiyah--Singer foi
registrada em `possibilidades.md` e no `brain/future/` como programa futuro:
para virar prova, precisa de operador, dominio, contorno/decaimento, fibrados,
grupo de gauge, representacoes, espectro quiral, polinomio de anomalia,
tratamento da nao compacidade e demonstracao de cancelamento em `n=4` e falha
em `n != 4`.

A Questao 4 foi documentada no `brain/` a partir de `questão_4.md`. O estado
vigente e: a acao oficial de contorno em `gamma` permanece preservada; a acao
efetiva da Q2 e reducao local/EFT e nao substitui a oficial. A consistencia
variacional esta fechada com `U` constitutiva,
`z_tau = tau + i nu_0 t` e `gamma` como prescricao causal de Sudarshan. A
passagem da integral de contorno para equacoes locais exige o principio de
estacionariedade dos coeficientes de Laurent: a integral seleciona apenas
`E_0 = 0`, enquanto equacoes modo a modo requerem `E_k = 0` para todo `k`.
A quantizacao perturbativa esta fechada apenas condicionalmente como camada
auxiliar/auditoria: BRST/fantasmas nao sao ontologia; o form factor de Cartan
da supressao euclidiana `exp(-k_E^2/Lambda_C^2)` garante finitude superficial
e nao cria novos polos no nivel quadratico por ser inteiro sem zeros. A
formulacao interna mais atual dos loops permanece
`1/2 Tr_phys ln Hess S_GDQ`; finitude all-orders, unitariedade nao
perturbativa, anomalias gerais e backgrounds singulares seguem abertos.

A Questao 5 foi documentada no `brain/` a partir de `questão_5.md`. O estado
vigente e: o dicionario formal dos campos da GDQ esta fechado. Os campos
fundamentais variados na acao oficial sao
`{g_{mu bar nu}, f, bar f}`. A medida `U` e funcional derivado de
`f`, `bar f` e `z_tau`, nao campo independente. As estruturas definidoras sao
`{M,J,gamma,tau,t,z_tau,Lambda_C,nu_0}`; `Lambda_C` deve ser lido conforme a
convencao dimensional posterior como numero de corte adimensional em
coordenadas de Cartan, usando `ell_C`, `k_C` e `E_C` para grandezas
dimensionais. As variaveis `S_I`, `S_R`, `rho`, `R` e `Psi` sao derivadas ou
representacoes efetivas de Madelung, nao substitutos de `f`. Os campos
`X`, `h`, `B`, `A^a` e `psi` pertencem a camada fisica efetiva em `N^4`.
Fantasmas/BRST sao opcionais como auditoria comparativa e nao ontologia da
GDQ. Q5 nao fecha acoplamentos efetivos, constantes observaveis,
beta-funcoes geometricas nem regularidade perturbativa completa.

A Questao 6 foi documentada no `brain/` a partir de `questão_6.md`. O estado
vigente e: `tau` esta definido como parametro real de fluxo
geometrico/difusivo, com dimensao `L^2`. Ele nao e tempo fisico cronologico,
nao e diretamente `log mu` e nao e adimensional. O tempo fisico e `t`; a
variavel causal complexa correta e `z_tau = tau + i nu_0 t`, com
`nu_0 = hbar/(2m_0)`. A medida `d tau/tau` e adimensional e implementa escala
logaritmica no contorno, sem mudar a dimensao de `tau`. A variavel
adimensional e `hat tau = tau/ell_C^2`; a variavel logaritmica e
`s = log(hat tau)`, com `partial_s = tau partial_tau`. No bulk oficial
`d=8`, `n=4`, o kernel fundamental escala como `(4 pi tau)^(-4)`. Formulas
antigas com `tau+it`, `t=-i tau`, `tau` adimensional, `ln mu -> tau` ou
`tau^(-2)` no bulk devem ser tratadas como rascunhos, reducoes ou corrigidas
pelos mapas acima.

A Questao 7 foi documentada no `brain/` a partir de `questão_7.md`. O estado
vigente e: a emergencia do tempo lorentziano tem duas camadas distintas. A
assinatura fisica vem da metrica constitutiva da Q2,
`h = q - 2 u otimes u / q^{-1}(u,u)`, que gera assinatura `(-,+,+,+)` em
referencial adaptado. A reconstrucao quantica lorentziana exige uma camada
Osterwalder--Schrader no setor euclidiano efetivo: se as funcoes de Schwinger
satisfazem OS1--OS5, obtem-se
`H = closure(D_+/N)`, semigrupo `T_E(a)=exp(-aH/hbar)`,
Hamiltoniano autoadjunto positivo `H >= 0` e evolucao unitaria
`U(t)=exp(-itH/hbar)`. `z_tau = tau + i nu_0 t` e `gamma` organizam a
prescricao causal; eles nao substituem a positividade OS. Portanto Q7 esta
fechada como criterio OS condicional, nao como prova universal automatica em
todo background.

A Questao 8 foi documentada no `brain/` a partir de `questão_8.md`. O estado
vigente e: a causalidade fisica e definida no setor efetivo `(N,h)` pelo cone
`C_h(p)={v: h(v,v)<=0}`. Campos escalares, gauge, torcionais, gravitacionais
linearizados e espinoriais devem compartilhar o simbolo principal
`h^{mu nu} k_mu k_nu`. Propagadores retardado e avancado sao solucoes
fundamentais de `P_h`; o comutador e controlado por
`Delta = G_ret - G_adv` e desaparece para separacao espacial. O propagador
simetrico de Sudarshan `G_sym=(G_ret+G_adv)/2` e restricao global de
contorno/fase, nao canal operacional de sinalizacao. A resposta controlavel a
fontes locais e retardada. Q8 esta fechada estruturalmente sob as hipoteses de
operador hiperbolico efetivo com cone `h` e algebra local microcausal; nao
fecha por si so Bell, teoria completa da medida ou dinamica de detector.

A Questao 9 foi documentada no `brain/` a partir de `questão_9.md`. O estado
vigente e: a acao fundamental e exatamente a acao oficial de contorno em
`gamma`. As variaveis independentes sao `g_{mu bar nu}`, `f` e `bar f`;
`U`, `rho`, `R`, `S_I`, `S_R` e `Psi` sao derivados. A acao fisica estacionaria
e `S_phys = Re S_GDQ`. O funcional puro de Perelman e auxiliar geometrico, e
as acoes efetivas em `N^4`, propagadores, setores perturbativos e linguagem
BRST sao reducoes ou auditorias. Q9 deve ser lida com a convencao dimensional
posterior: `Lambda_C` e numero de corte adimensional nas coordenadas de
Cartan; `ell_C`, `k_C` e `E_C` carregam dimensoes fisicas. Nenhuma equacao
central deve ser adicionada independentemente da acao oficial.

A Questao 10 foi documentada no `brain/` a partir de `questão_10.md`, com a
correcao conceitual posterior dos Capitulos 5 e 6. O estado vigente e: a
equacao de continuidade segue da variacao em `S_R` no setor canonico de
Madelung,
`I_Mad = int rho[partial_lambda S_R + 1/2 G^{AB} partial_A S_R partial_B S_R
+ V_eff]`, gerando
`partial_lambda rho + nabla_A(rho v^A)=0`, ou
`partial_lambda(rho sqrt g)+partial_A(rho v^A sqrt g)=0` com medida variavel.
Essa conservacao tambem e Noether da simetria global
`S_R -> S_R + hbar alpha`. A identidade `Pi_{S_R}=rho` e o termo canonico
`rho partial_lambda S_R` nao sao identidades off-shell universais da acao
oficial; pertencem a polarizacao fisica/reducao de Madelung e a ponte
global--local/medida. Assim Q10 esta fechada condicionalmente: selecionado o
setor canonico de Madelung, a continuidade segue por variacao e bordos
adequados.

A Questao 11 foi documentada no `brain/` a partir de `questão_11.md`. O estado
vigente e: no mesmo setor canonico de Madelung da Q10, a variacao em `rho`
produz Hamilton--Jacobi--Bohm. O termo de Fisher
`(hbar^2/8m)|nabla rho|^2/rho` tem derivada variacional
`-(hbar^2/2m) Delta sqrt(rho)/sqrt(rho)`, gerando
`partial_t S_R + |nabla S_R|^2/(2m) + V + Q = 0`, com
`Q = -(hbar^2/2m) Delta sqrt(rho)/sqrt(rho)`. `Q` entra sem derivada extra na
equacao escalar de Hamilton--Jacobi; `nabla Q` aparece apenas depois, na
equacao de Euler/Madelung. Q11 fica fechada condicionalmente ao setor
Madelung reduzido e aos bordos usados na integracao por partes.

A Questao 12 foi documentada no `brain/` a partir de `questão_12.md`. O estado
vigente e: a variacao completa da acao oficial em `g^{mu bar nu}`, com
`f`, `bar f` e `U` fixos nessa variacao, produz a equacao metrica
`E_{mu bar nu}=0`. O tensor energia-momento e definido variacionalmente, nao
por analogia. A equacao estacionaria do bulk Hermitiano/Riemanniano e
eliptica apos fixacao de difeomorfismo; o fluxo associado em `tau` e
Ricci--Perelman/Ricci--Bismut e parabolico apos calibre de DeTurck; a evolucao
fisica causal e hiperbolica somente na camada efetiva lorentziana `(N,h)`. A
torcao entra pela conexao de Bismut e pelo setor `H^2`. Bianchi/conservacao
covariante seguem da invariancia por difeomorfismos e valem on shell.

A Questao 13 foi documentada no `brain/` a partir de `questão_13.md`. O estado
vigente e: a frase `U=rho` e imprecisa na acao oficial. A relacao correta e
`U = rho/(4 pi z_tau)^n`, com `rho=e^{-(f+bar f)/2}`; portanto
`(4 pi z_tau)^n U = rho`. Se for definida a medida sem kernel
`tilde U=(4 pi z_tau)^n U`, entao `tilde U=rho`. `U` e `rho` nao sao duas
solucoes independentes de uma mesma PDE: ambas sao definidas a partir de
`f,bar f`, e o fator `(4 pi z_tau)^(-n)` pertence ao kernel
geometrico/difusivo causal. Na camada efetiva, `|Psi|^2=rho`.

A Questao 14 foi documentada no `brain/` a partir de `questão_14.md`. O estado
vigente e: o mapa Perelman--Madelung e local, regular e setorial, nao uma
bijeção global. No dominio `rho>0`, com fase `S_R` localmente monovalorada e
campos regulares, tem-se `f=-ln rho + i S_R/hbar`,
`rho=e^{-(f+bar f)/2}` e `S_R=(hbar/2i)(f-bar f)`. Nesse setor, o mapa
preserva as equacoes reduzidas: variacao em `S_R` equivale a continuidade, e
variacao em `rho` equivale a Hamilton--Jacobi--Bohm. Nos, fases
multivaloradas, superposicoes, spin, gauge e setores topologicos exigem atlas,
ramos, fibrados ou dados adicionais.

A Questao 15 foi documentada no `brain/` a partir de `questão_15.md`. O estado
vigente e: `f` e complexo e decompoe-se como
`f=-(S_I-i S_R)/hbar = -S_I/hbar + i S_R/hbar`. Logo
`S_I=-hbar Re f`, `S_R=hbar Im f`, `rho=e^{S_I/hbar}=e^{-(f+bar f)/2}` e
`U=rho/(4 pi z_tau)^n`. A positividade da medida vem de `f+bar f`, nao de
`e^{-f}`. A identidade `S_I=hbar W` deve ser removida como identidade local:
`S_I(x)` e campo local, enquanto `W[g,f,tau]` e funcional global. A relacao
local correta e `S_I=hbar ln rho=-hbar Re f`.

A Questao 16 foi documentada no `brain/` a partir de `questão_16.md`. O estado
vigente e: a difusao fundamental do vacuo usa `nu_0=hbar/(2m_0)`, enquanto a
difusao observada por uma excitacao de massa `m` e
`nu_eff=nu_0 Omega^{-1}=hbar/(2m)`, com `Omega=m/m_0`. `Omega` e definicao
operacional no setor estocastico, mas deve ser derivada geometricamente do
soliton em cada especie. Para `Omega(x,t)` variavel, a Fokker--Planck de Ito e
`partial_t rho = -nabla_i(b^i rho) + nu_0 Delta_h(Omega^{-1} rho)`, e a
velocidade osmotica correta e
`u^i=nu(nabla^i ln rho - nabla^i ln Omega)`. O termo de gradiente de `Omega`
nao pode ser omitido salvo no setor de massa constante.

A Questao 17 foi documentada no `brain/` a partir de `questão_17.md`. O estado
vigente e: o problema de Cauchy do fluxo geometrico em `tau` esta localmente
bem posto apos gauge. O setor estacionario e eliptico; o fluxo em `tau` e
quase-linear fortemente parabolico; a evolucao fisica em `t` pertence a
camada lorentziana efetiva. Usa-se DeTurck para `g`, Hodge para `B` e gauge de
medida ponderada de Perelman quando util. Para `U=(g,B,phi,chi)`, o simbolo
principal em gauge e `|xi|_g^2 I`, positivo porque o bulk e Riemanniano. Ha
existencia local, unicidade em gauge, unicidade geometrica modulo
difeomorfismos, dependencia continua e criterio de continuacao enquanto a
metrica, curvatura, torcao e derivadas de `f` permanecerem controladas.

A Questao 18 foi documentada no `brain/` a partir de `questão_18.md`. O estado
vigente e: ha definicao matematica de soliton da GDQ como ponto estacionario
do sistema Ricci--Bismut/Perelman em setor de gauge/topologia fixado. Existe
solucao explicita neutra minima: o soliton gaussiano em `R^d`, com `g=delta`,
`B=0`, `phi=|x|^2/(4 sigma)` e densidade gaussiana normalizada. Ele tem
energia geometrica finita e estabilidade linear modulo simetrias, mas e neutro
e nao representa por si so um fermion carregado. Para declarar uma particula
fisica e necessario fornecer uma ficha completa `S_P=(g_P,B_P,f_P,bar f_P)`
com residuo estacionario, energia finita, massa, carga, spin, Hessiana, modos
zero, assintotica e interacao/espalhamento. Q18 esta fechada como criterio
matematico e solucao neutra minima, nao como obtencao completa de
eletron/proton/neutron.

A Questao 19 foi documentada no `brain/` a partir de `questão_19.md`. O estado
vigente e: monotonicidade dos funcionais torsionais `F_T` e `W_T` nao implica
estabilidade automaticamente. Ela fornece funcional de Lyapunov para o fluxo.
Estabilidade exige: ponto critico real, hipoteses de monotonicidade e bordo,
setor topologico preservado, Hessiana/Jacobi com sinal correto no setor fisico
e modos zero explicados como simetrias/moduli controlados. O soliton gaussiano
neutro tem operador tipo Ornstein--Uhlenbeck controlado. Solitons carregados
ou spinoriais exigem calculo setorial do operador `J_S`.

A Questao 20 foi documentada no `brain/` a partir de `questão_20.md`. O estado
vigente e: o espaco de Hilbert nao e ontologia primaria da GDQ, mas camada
operacional reconstruida. A estrutura e `H_phys = closure(D_+/(N+G))`, com
produto `<[F],[G]>=<Theta F G>_E`. `D_+` sao funcionais cilindricos de
suporte temporal euclidiano positivo, `N` e subespaco nulo de reflexao
positiva e `G` codifica redundancias de difeomorfismo, gauge, carta, modos
longitudinais e bordos exatos. No setor regular de uma particula, reduz para
`L^2(N,E,dSigma_h)` com `Psi=sqrt(rho) exp(i S_R/hbar)`. Q20 esta fechada
estruturalmente; existencia da medida, reflexao positiva, cluster,
autoadjunticidade essencial, quociente e fatorizacao tensorial permanecem
verificacoes setor a setor.

A Questao 21 foi documentada no `brain/` a partir de `questão_21.md`. O estado
vigente e: a evolucao fisica em `t` e unitaria no setor fisico fechado quando
a reconstrucao OS fornece Hamiltoniano autoadjunto `H=H^dagger` em
`H_phys`. O operador de evolucao e `U(t)=exp(-itH/hbar)` e preserva produto
interno e norma. O fluxo em `tau` e geometrico/difusivo/renormalizacional e
nao e a evolucao fisica unitaria. Estados instaveis, NESS, decaimentos e
irreversibilidade aparecem como descricoes efetivas por projecao,
coarse-graining ou teoria aberta, sem quebrar a unitariedade do sistema total.
Q21 fica estruturalmente fechada condicionada a verificacao OS setorial.

A Questao 22 foi documentada no `brain/` a partir de `questão_22.md`. O estado
vigente e: a GDQ fornece `rho=e^{-(f+bar f)/2}` e
`Psi=sqrt(rho) exp(i S_R/hbar)`, mas `rho=|Psi|^2` sozinho so prova densidade
local de posicao. A regra de Born completa vem da estrutura operacional de
Hilbert: uma medida positiva, normalizada, aditiva sobre projetores
ortogonais, nao contextual e compativel com produto tensorial deve ter forma
`mu(P)=Tr(varrho P)`. Para estado puro e projetor de rank 1,
`P(i|psi)=|<i|psi>|^2`. Q22 esta fechada estruturalmente; a implementacao de
uma medicao concreta pertence a Q24.

A Questao 23 foi documentada no `brain/` a partir de `questão_23.md`. O estado
vigente e: a objecao de Wallstrom e resolvida tratando a fase fisica como
secao de fibrado de linha hermitiano `L -> M*`, com
`M*=M\\Z_rho`. A integralidade vem de
`c1(L)=[F_A/(2 pi)] in H^2(M*,Z)`, que implica circulacoes admissiveis
`oint_C nabla S_R dx = N h`. Circulacoes nao inteiras nao sao estados fisicos
do setor porque nao definem secao global monovalorada. Nos `rho=0` sao
removidos do dominio regular e tornam-se defeitos/topologia de bordo. A soma
de Poisson e consequencia da topologia `S^1`, nao origem da quantizacao.

A Questao 24 foi documentada no `brain/` a partir de `questão_24.md`. O estado
vigente e: medicao e modelada como processo aberto `S+A+E`, no qual a
interacao correlaciona projetores `P_i` com estados de ponteiro e registros
macroscopicos `R_i`. A base e selecionada por `H_int` e pela
estabilidade/decoerencia dos estados de ponteiro. As probabilidades vêm de
Q22, `P(i)=Tr(rho_S P_i)`, nao de pesos Born inseridos na particao. A
decoerencia explica mistura reduzida, registros robustos e repetibilidade,
mas nao seleciona sozinha um ramo ontologico. Resultado unico exige a hipotese
GDQ de que a microgeometria real do aparelho/ambiente seleciona uma bacia de
atracao `R_i`. Com essa hipotese, colapso e transicao geometrica efetiva no
setor reduzido, compativel com unitariedade global. Q24 esta fechada
estruturalmente com essa ressalva.

A Questao 25 foi documentada no `brain/` a partir de `questão_25.md`. O estado
vigente e: o problema do sinal fermiônico esta reformulado geometricamente,
mas nao resolvido como algoritmo computacional geral. A medida positiva e
`rho=e^{-(f+bar f)/2}`; a antissimetria fermiônica fica na fase/holonomia,
`S_R(P_ij Z)=S_R(Z)+pi hbar mod 2pi hbar`. Isso remove o sinal da medida, mas
nao prova que observaveis sensiveis a fase possam ser estimados com variancia
polinomial. Para fechamento algoritmico faltam estimador explicito,
variancia, tempo de mistura/autocorrelacao, complexidade por classe de
Hamiltonianos, tratamento nodal/holonomico e benchmarks. A rota proposta e
decomposicao em dominios com matrizes de transmissao/reflexao nas interfaces
de cirurgia.

A Questao 26 foi documentada no `brain/` a partir de `questão_26.md`. O estado
vigente e: spin `1/2` esta fechado estruturalmente como setor spinorial
efetivo, nao como circulacao escalar inteira. O bulk local da Q2,
`M=R^4 x T^4`, tem `w2(TM)=0` e admite estrutura spin; as estruturas spin de
`T^4` sao classificadas por `H^1(T^4,Z2)=(Z2)^4`, gerando 16 possibilidades.
No espaco-tempo fisico efetivo `(N,h)` exige-se `w2(TN)=0` e
`P_Spin(N)->N`. O campo fermiônico e `psi in Gamma(S tensor E)`, com algebra
de Clifford `{gamma^mu,gamma^nu}=2h^{mu nu}` e representacao
`(1/2,0) oplus (0,1/2)` de `Spin^+(3,1)`. Assim `U(2pi)=-I` e
`U(4pi)=I`. A torcao/vorticidade de Cartan interpreta geometricamente o spin,
mas nao substitui a estrutura spinorial. Permanece aberta a selecao dinamica
de uma das 16 estruturas spin e a realizacao espectral completa de massas,
cargas e modos espinoriais.

A Questao 27 foi documentada no `brain/` a partir de `questão_27.md`. O estado
vigente e: estatistica fermiônica esta fechada estruturalmente no setor
efetivo local, Lorentziano, spinorial, de energia positiva e produto interno
positivo. Nesse setor, campos de spin semi-inteiro obedecem CAR,
`{a(f),a^dagger(g)}=<f,g>`, e o espaco de muitos corpos e a algebra exterior
`F_-(H_1)`. Observaveis pares preservam localidade graduada e Pauli segue de
`(a_i^dagger)^2=0`. A contribuicao GDQ preservada do manuscrito original e a
interpretacao da antissimetria como holonomia torsional/spinorial
`Hol_gamma=-1`, ou `Psi(r2,r1)=-Psi(r1,r2)`. A holonomia explica o sinal, mas
o teorema completo depende das hipoteses efetivas relativisticas.

A Questao 28 foi documentada no `brain/` a partir de
`questão_28_final.md`. O estado vigente e: o grupo efetivo, o espectro de uma
geracao e a selecao de tres geracoes estao fechados no modelo estrutural
reduzido. O fibrado interno e `E_int=E_C oplus E_W oplus L_Y`, com grupo
global efetivo `(SU(3)_C x SU(2)_L x U(1)_Y)/Gamma`, `Gamma subset Z6`.
A selecao nao usa `N_G=3` como entrada: conservacao de Noether seleciona o
primeiro junction horizontal fechado, nao colinear e isolado, com tres
estomatos; aditividade APS fornece indice tres; colagem global `Z6` fornece
`A=18` e `N_G=A/6=3`. No setor simetrico vinculado,
`H_rel=3/2 I_2` e os modos nao homogeneos iniciam em `1/(2 tau)` apos
projecoes fisicas, dando gap reduzido positivo. A elevacao integral ainda
exige manter Hessiana vinculada e colagem global dentro da acao oficial.

A Questao 29 foi documentada no `brain/` a partir de
`questão_29_final.md`. O estado vigente e: a quebra eletrofraca esta fechada
estruturalmente no nivel da GDQ. O modo de ordem e geometrico,
`Phi_EW in Gamma(E_W tensor L_Y^{1/2})`, com numeros quanticos
`(1,2)_{1/2}`, obtido como projecao de flutuacoes
`(delta g, delta f, delta bar f, delta B)`. O potencial efetivo tem
`a2<0`, `a4>0` no fechamento estrutural, organiza massas de `W`, `Z` e
preserva o foton sem massa. A determinacao absoluta de `alpha` nao integra as
perguntas obrigatorias de Q29 e permanece aberta: a Fase 2 do colar dinamico
mostrou que os dados derivados nao selecionam colar nao-produto, nao
estabilizam Berger e nao localizam o foton. O objeto ausente e o pullback
metrico--dilatonico da colagem global do estomato,
`I_int^{(a,c,f)}`; escolher seus coeficientes numericamente seria nova
hipotese constitutiva.

A Questao 30 foi documentada no `brain/` a partir de
`questão_30_yang_mills.md` e `questão_30.md`. O estado vigente e: a Q30 esta
fechada estruturalmente no setor efetivo GDQ--`SU(3)_C`, mas nao como solucao
completa do problema Clay de Yang--Mills puro. Pela Q28, `E_C=C^3` gera
`SU(3)_C`, a conexao efetiva `A_C in Omega^1(N,su(3))`, curvatura
`F_C=dA_C+A_C wedge A_C` e Wilson loops como holonomia. A tensao de area
`sigma` e obtida variacionalmente por translacao do tubo minimizador, nao
postulada, levando a `V(r)=sigma r+O(1)` e lei de area no setor efetivo. O
gap geometrico segue condicionalmente da Hessiana positiva apos remocao de
gauge/modos nulos e de hipoteses funcionais como coercividade e
`Ric_f^B >= Lambda_0 g`. Permanecem calculos explicitos: norma interna de
`g_s`, justificativa GDQ da proposta Fredholm `alpha_s^eff=3/(8pi)`, espaco
funcional, coercividade, `sigma`, `lambda_1` e comparacoes hadronicas.

---

## 2. Identidade atual da teoria

A GDQ é um programa de geometrização da matéria e da mecânica quântica. Sua
ideia central é que partículas não são pontos inseridos num fundo rígido, mas
excitações solitônicas, circulações e defeitos de uma geometria Hermitiana
dinâmica, dotada de campo complexo, medida ponderada e torção de
Cartan--Bismut.

O programa procura construir:

\[
\text{geometria + fluxo + contorno + torção}
\longrightarrow
\text{Madelung/quantização}
\longrightarrow
\text{formalismo operacional quântico}
\longrightarrow
\text{limite clássico}.
\]

A mecânica quântica padrão é interpretada como uma redução operacional
eficiente de uma dinâmica geométrica mais geral, não como algo a ser descartado.

### 2.1 Ontologia mínima

- matéria: sólitons e defeitos estáveis da geometria;
- massa: custo inercial/elástico de uma configuração geométrica;
- densidade: parte real do campo complexo de Perelman;
- fase: parte imaginária e circulação do fluido de Madelung;
- spin: circulação/holonomia na representação dupla;
- carga: fluxo ou resíduo topológico orientado;
- magnetismo: vorticidade/torção transversal;
- interação: deformação e resposta do mesmo meio geométrico;
- medição: interação física entre o objeto e o aparelho, tratada como problema
  de fonte, interface, contorno, resposta espectral e registro macroscópico.

### 2.2 O que a GDQ não deve virar

A GDQ não deve ser reescrita como o Modelo Padrão com nomes geométricos. Os
grupos, espinores e Hamiltonianos conhecidos podem aparecer como reduções,
mas precisam emergir da geometria. Yang--Mills, BRST, Dirac, Pauli e Lindblad
são ferramentas de comparação ou limites efetivos, não substitutos da ação
fundamental.

---

## 3. Geometria e ação oficiais

### 3.0A Convenção dimensional do corte — 15 de julho de 2026

A auditoria dos Capítulos 2 e 4 eliminou a ambiguidade dimensional do
prefator oficial. Como o funcional integrado é adimensional, o símbolo
$\Lambda_C$ que aparece em $\hbar/\Lambda_C^2$ fica definido como **número de
corte adimensional**. Escrevendo

$$
k_C=\ell_C^{-1},
\qquad
E_C=\hbar c\,k_C,
\qquad
\Lambda_C=\ell_Ck_C=1
$$

nas coordenadas normalizadas pela própria escala, tem-se

$$
\left[\frac{\hbar}{\Lambda_C^2}\right]=[\hbar].
$$

Portanto a ação oficial foi preservada e $d\tau/\tau$ não foi alterado. Fica
proibido reutilizar $\Lambda_C$ como comprimento, momento ou energia
dimensionais; para isso usam-se respectivamente $\ell_C$, $k_C$ e $E_C$.
Se $\Lambda_C$ fosse interpretado dimensionalmente na fórmula oficial, a ação
seria dimensionalmente inconsistente. A escala física ainda pode precisar ser
derivada, embora o número normalizado na ação seja unitário.

### 3.0 Colheita da ponte em Q37, Q39 e Q40 — 14 de julho de 2026

`impacto_ponte_global_local_q37_q39_q40.md` aplicou o fechamento sem colar e
o gap $C_3$ às três questões:

1. Q40: a compatibilidade global--local do background trimodal e sua
   estabilidade projetada estão fechadas; normalizações contínuas e resposta
   local permanecem independentes;
2. Q39: a multiplicidade $C_3$ é transportada, mas ainda se deve identificar
   o cluster de Rosen--Morse $n=0,1,17$ com o cluster físico da Hessiana;
3. Q37: a incompatibilidade abstrata entre as geometrias foi removida, mas
   $\alpha$ continua aberta até o cálculo da norma do modo eletromagnético e
   do complemento de Schur da Hessiana oficial.

Essa separação decorre do Lema 6: topologia e multiplicidade não fixam uma
normalização contínua de acoplamento.

Atualização de 15 de julho de 2026: o documento
`teorema_heranca_normalizacao_eletromagnetica.md` demonstrou o critério exato
sob o qual uma normalização contínua $Z_Q^E$, calculada no espaço global, é
preservada pela ponte. O argumento usa a direção interna primitiva $U(1)_Q$,
o complemento de Schur da Hessiana oficial, sua corrente simplética, a
convergência das formas, a sincronização das formas-relógio e a ausência de
fuga lateral. Para modo ligado aplicam-se gap, Agmon e projetores. Para o
fóton massless estendido deve-se demonstrar convergência DtN ou de espalhamento
com normalização de fluxo. Sob a hipótese correspondente,

$$
Z_Q^{\rm lab}=Z_Q^E,
\qquad
\alpha_{\rm lab}=\alpha_E.
$$

Isso fornece um **teorema condicional de herança**, não sua avaliação global
nem ainda sua aplicação automática ao fóton. A Q37 continua aberta até que
$Z_Q^E$ seja calculado no background global pela Hessiana oficial, o canal
elétrico seja classificado e a ausência de fuga seja verificada, e qualquer
fórmula cosmológica proposta seja identificada com esse cálculo sem usar o
valor experimental. A corrente elétrica não deve ser confundida com a
corrente global de fase de Madelung.

Avaliação adicional de 15 de julho de 2026: o documento
`37p/derivacao_ZQ_global_acao_oficial.md` restringiu diretamente o termo de
curvatura da ação oficial ao modo métrico primitivo $U(1)_Q$ e obteve

$$
Z_Q^E
=\frac{\hbar}{\Lambda_C^2}
\mathfrak P_\gamma\!\left[
\tau\int_K\mathcal U_*\lVert\xi_Q\rVert^2dV_{q_*}
\right]
+\Delta Z_Q^E.
$$

A fórmula cosmológica candidata requer $Z_Q^E=10{,}904984951787\ldots$ em
unidades naturais. A identidade estrutural está clara, mas a igualdade
numérica ainda não foi provada: faltam o background global explícito dentro
da integral causal e o complemento de Schur. Como $\mathcal U$ é normalizada,
um volume bruto não pode ser contado novamente sem emergir da média ponderada.
Os solvers existentes foram reexecutados. A quantidade
$\mathcal K_Q=41{,}594825709\ldots$ é uma norma radial anterior à matriz de
Gram, não $Z_Q$. A normalização $T_3=Y=1/2$ fornece exatamente o fator $1/4$.
O observável correto é matricial:

$$
\alpha_E
=\frac{(\mathbf q_{\min}^{T}v)^2}
{4\pi\hbar c\,v^T\mathbf Z v}.
$$

No background radial atual, a diagonalização fornece
$Z_\gamma=15{,}1626057595\ldots$ e
$\alpha^{-1}=190{,}5389235\ldots$, ainda incompatíveis com a fórmula
cosmológica. A análise dimensional corrigida mostra que não falta uma potência
de $\ell_C$: $d^4X F_{\rm phys}^2$ é invariante e $\mathbf Z$ é adimensional.
Faltam a matriz Hermitiana horizontal completa e/ou a contribuição causal ou
de Schur derivada da ação. Uma inserção steady suave tem projeção causal nula.
Também foi identificado que a norma $41{,}5948$ pertence ao subbloco de Hopf
em $S^3$, enquanto a direção primitiva da Q37 foi inicialmente definida no
setor toroidal. A normalização física exige a matriz global combinada
$\mathbf Z_E$ nos blocos toroidal, Hopf e cruzado; comparar diretamente os
dois escalares mistura setores distintos.

Teste geométrico subsequente em `37p/rota_schur_dtn_global.md`: compondo o
kernel fotônico radial $K_0=15{,}1626057586\ldots$ com a impedância DtN sem
ajuste de duas extensões do primeiro harmônico pela 4-bola,

$$
K_\partial^{\rm DtN}=\pi^2R^2=39{,}4157186074\ldots,
$$

o complemento de Schur fornece
$\alpha_{\rm DtN}^{-1}=137{,}604601779\ldots$. O erro em $Z_Q$ diante da
fórmula cosmológica é $0{,}414868\%$ e a Hessiana de interface é positiva.
Classificação: estimativa geométrica sem ajuste, não previsão final. A escala,
o sinal e quase toda a magnitude apontam para o DtN warped--Bismut do elo
$S^3$ como termo faltante.

A tentativa de reutilizar o Sturm--Liouville warped da Q29 foi rejeitada por
domínio: sua variável $\chi$ é tangencial em $S^3$, enquanto o DtN necessário
atua na normal $r$ de $B^4\subset\mathbb C^2$ com bordo $S^3$. Além disso, o
solver $W/Z$ existente injeta `ALPHA_INV` e não serve para derivar $\alpha$.
O resultado redondo permanece suficiente como estimativa; o refinamento exige
construir o operador Jacobi normal da Hessiana oficial no preenchimento
$B^4_R$.

Avanço do canal fotônico em `37p/teorema_canal_fotonico_massless.md`: Ward e o
kernel neutro demonstram $m_\gamma=0$; a invariância do background por
$U(1)_Q$ torna o canal um subespaço invariante da Hessiana; a corrente
simplética não flui para representações internas ortogonais. Para frequência
$\omega>0$, a convergência local das formas implica convergência DtN. O limite
massless foi completado no elo normal $(B^4,S^3)$: a identidade de energia da
Hessiana física positiva reduz um modo zero transversal a uma forma harmônica
relativa, e $H^1(B^4,S^3)\simeq H_3(B^4)=0$ exclui essa forma. Assim, o
transporte do canal fotônico está fechado condicionalmente à positividade da
Hessiana física projetada e à topologia normal oficial. Permanece em Q37 a
avaliação absoluta do DtN warped--Bismut, não uma nova hipótese de transporte.

Auditoria da fórmula cosmológica de $\alpha$ em
`37p/identificacao_formula_cosmologica_hessiana.md`: $1920$ foi identificado
corretamente como $|W(D_5)|=2^4 5!$, uma simetria finita da rede e não a
holonomia de Bismut. O grupo que pode entrar na ação é o
estabilizador de $(J,H,f,\mathcal U,Q)$. A escolha axial distingue um ciclo de
$T^5$, de modo que a fórmula antiga $4!2^4\cdot5$ pode conter dupla contagem.
O quociente por grupo finito fornece fator volumétrico linear e não deriva,
sozinho, a raiz quarta. O fator $9/8$ também ainda não foi identificado como
contração da Hessiana. A fórmula histórica permanece conjectura geométrica;
o teste final é o DtN warped--Bismut, cujo valor requerido apenas como
diagnóstico é $38{,}835771227928\ldots$.

Fechamento do refinamento conformal de Q37: na fatia normal 4D, com métrica de
bordo fixa, a forma $\int F\wedge\star F$ é conformalmente invariante. Logo um
warp escalar $g_{\rm WB}=e^{2A}g_{\rm red}$ não altera a rigidez DtN integrada.
Na truncagem disponível, $Z(\eta)F^2$ não gera bloco bilinear em $A_Q=0$. Para
a classe redonda/conformal avaliada, permanecem
$K_\partial=39{,}415718607388\ldots$ e
$\alpha^{-1}=137{,}604601779\ldots$; a fórmula histórica não é consequência
dessa classe. Somente um background normal Hermitiano anisotrópico ou uma
mistura transversal derivada pode reabrir o valor absoluto. Ward não exclui,
sozinho, uma mistura gauge-invariante de $F$ com uma 2-forma torsional de
background.

Interpretação preservada da fórmula legada em
`37p/interpretacao_media_einstein_formula_legada.md`: ela não é o DtN de uma
única 4-bola, mas uma prescrição de média cosmológica. O fator
$\pi^5/1920$ é o peso angular de uma câmara de $T^5/W(D_5)$; a raiz quarta é
a média geométrica do determinante de complacência nas quatro direções
físicas; e $9/(8\pi^4)$ é o projetor isotrópico para o canal elétrico. A
fórmula tem sentido matemático exato sob essa definição, mas permanece
teorema condicional: pesos uniformes e projetor devem ainda ser extraídos da
Hessiana global.

O peso uniforme foi posteriormente fechado pelo lema de ensemble no mesmo
documento. A ação covariante por pullback é constante na órbita completa de
$W(D_5)$; Noether conserva os fluxos contínuos e o grupo discreto preserva a
rede. Sob isotropia global/transitividade,
$Z_E=1920e^{-\beta_EF_0}$ e $p_a=1/1920$. Se as câmaras são redundâncias, a
mesma identidade segue diretamente da integral no quociente. O projetor foi
obtido no setor axial coerente: o quarto momento de Haar em $S^3$ é $1/8$; o
traço coerente das três direções Cartan--Schouten fornece $3^2=9$; e a câmara
angular física fornece $\pi^{-4}$. Logo
$\mathcal P_{\rm iso}=9/(8\pi^4)$. A fórmula legada fica fechada
condicionalmente ao ensemble isotrópico e ao autovetor Hopf axial coerente;
componentes incoerentes produziriam fator $3$, não $9$.

### 3.1 Geometria local fundamental

A reconstrução das Questões 1--3 fixou como base local oficial:

\[
\boxed{M=\mathbb R^4\times T^4},\qquad
\dim_{\mathbb R}M=8,\qquad
\dim_{\mathbb C}M=4.
\]

Estrutura geométrica:

\[
(M,g,J,H,\nabla^B),
\]

com métrica Hermitiana/Riemanniana no bulk, estrutura complexa integrável,
3-forma real de torção e conexão de Bismut compatível com (g) e (J).
O espaço-tempo físico lorentziano é reconstruído/projetado; não se deve
atribuir assinatura lorentziana diretamente ao bulk euclidiano oficial.

A escolha do bulk local real $M=\mathbb R^4\times T^4$ e da classe complexa
permanece estrutural. Uma vez admitidas essas escolhas, $n=4$ não é axioma
independente: segue de $\dim_{\mathbb R}M=8$. As rotas que pretendem selecionar
dinamicamente a própria dimensão real — Atiyah--Singer, anomalias e
estabilidade dimensional — continuam em `possibilidades.md` e não foram
elevadas a prova completa.

### 3.2 Geometria cosmológica auxiliar

(T^5\times S^3) aparece como espaço cosmológico de Einstein e como domínio
espectral/global em cálculos de α, massas e potenciais cotangentes. Ele não
substitui automaticamente o bulk local ℝ⁴×T⁴.

Pendência crítica:

\[
\boxed{
\text{construir explicitamente a redução, fibrado, imersão ou correspondência}
\quad
(\mathbb R^4\times T^4)\leftrightarrow(T^5\times S^3).
}
\]

Até essa ponte existir, resultados que dependem essencialmente de
(T^5\times S^3) são resultados do setor cosmológico/espectral auxiliar,
condicionais à sua incorporação na ação oficial.

Decisão arquitetural de 13 de julho de 2026, consolidada em
`teorema_heranca_espectral_global_local_gdq.md`:

\[
\boxed{
\text{o setor global determina a identidade espectral;}
\qquad
\text{o setor planar determina a resposta local.}
}
\]

A ponte passa a ser formulada como um **teorema condicional de herança
espectral global--local**, apoiado na teoria do índice para famílias, em
limites adiabáticos, em projetores de Riesz e em colagem DtN/APS. Para se
tornar teorema da GDQ, ainda requer a construção explícita de
\(U_\varepsilon\), um gap espectral uniforme, convergência em resolvente ou de
formas quadráticas, e o transporte compatível da conexão de Bismut, da medida
\(\mathcal U\) e do contorno causal \(\gamma\).

Enquanto o gap não fecha, fontes e condições Robin produzem dressing ou
desdobramento local; mudança de classe exige fluxo espectral ou cirurgia. A
prioridade passa a ser provar essa ponte uma única vez. Massas, cargas,
índices, holonomias e multiplicidades globais não devem ser redeterminados em
cada carta planar; os cálculos anteriores permanecem como auditorias e lemas.

Avanço de 14 de julho de 2026, documentado em
`ponte_global_local_lema1.md` e `ponte_global_local_lema2.md`:

- Lema 1A: família Hermitiana homogênea demonstrada;
- Lema 1B: redução radial de Berger construída diretamente com
  $\mathcal R_{\rm GDQ}=R_{\rm LC}-|H|^2/12$ e $H=d^c\omega$, mas a
  existência da sela bulk--interface permanece aberta;
- foi demonstrado condicionalmente que uma carga strong-KT não nula não pode
  existir num colar único, suave, completo e assintoticamente plano sem
  interface; a carga do estômato deve ser relativa no bordo interno;
- Lema 2A: convergência suave apontada da família homogênea para
  $T^4\times\mathbb R^4$ demonstrada, com erro métrico
  $O(R_\varepsilon^{-2})$ em compactos;
- Lema 2B: transporte da deformação localizada formulado em
  $C^{k,\alpha}_{\rm loc}$, condicional às estimativas uniformes da sela do
  Lema 1B.

Esses resultados não demonstram ainda a convergência da Hessiana, o gap ou o
transporte espectral; esses são os Lemas 3--5.

Continuação de 14 de julho de 2026:

- a existência da sela foi isolada em
  `ponte_global_local_hipotese_BI.md`, com condições explícitas de
  estacionariedade, carga relativa, interface, regularidade Hölder,
  tightness, controle causal e semilimitação;
- sob BI, `ponte_global_local_lema3.md` construiu a identificação isométrica
  dos espaços $L^2$ ponderados e demonstrou a convergência da segunda variação
  oficial num núcleo comum;
- $H=d^c_J\omega$ não é campo variacional independente. O espaço mínimo de
  flutuações é $(\delta g,\delta f)$ sujeito aos vínculos Hermitianos;
- a condição de recuperação de Mosco está estabelecida sob BI, mas a condição
  liminf global depende de localização/coercividade. Portanto o Lema 3 global
  e a convergência forte de resolventes ainda dependem do Lema 4.

No Lema 4, `ponte_global_local_lema4.md` demonstrou condicionalmente um
critério de gap uniforme baseado em elipticidade física, limiar assintótico,
quociente de Rayleigh abaixo do limiar, separação interna e controle da
interface. Sob essas condições também foi obtida localização exponencial de
Agmon. A aplicação à GDQ ainda está aberta: o operador Jacobi radial disponível
na Q29 possui matriz principal indefinida antes da restrição do lapse e da
remoção da reparametrização. É necessário construir $P^{\rm phys}$ no
background BI e verificar sua positividade, o limiar $\Sigma_*$ e a separação
do modo ligado. Nenhum gap físico novo foi declarado a partir do operador não
reduzido.

O Lema 5 foi formulado em `ponte_global_local_lema5.md`. Sob BI e as seis
condições quantitativas do Lema 4, a convergência de formas torna-se Mosco no
setor ligado, produz resolvente e semigrupo fortes e transporta os projetores
de Riesz. Localização uniforme mais posto finito constante fornece
convergência em norma dos projetores e dos resolventes comprimidos ao cluster.
Essa conclusão não vale automaticamente para o espectro contínuo e não fixa
normalizações dimensionais de acoplamentos. A aplicação física continua
condicionada à verificação do gap no background BI.

O Lema 6, em `ponte_global_local_lema6.md`, concluiu a separação entre:
invariantes topológicos, espectro ligado, normalizações contínuas e respostas
locais. Índice e classe de Chern podem quantizar setores ou cargas, mas não
fixam sozinhos a magnitude de um acoplamento; autovalores geométricos exigem
uma escala para se tornarem massas dimensionais; fontes e interfaces do
aparelho produzem dressing e registro, não a identidade global do modo. Os
seis lemas da ponte estão agora formulados, porém a aplicação física integral
continua condicional à existência BI e à verificação do gap do Lema 4.

Reconstrução intrínseca de 14 de julho de 2026, em
`ponte_global_local_sela_projetor_gap.md`: a sela deixou de ser formulada como
um ansatz importado e passou a ser o problema de ponto crítico da ação oficial
na folha conjunta de normalização, carga relativa, continuidade de fluxo e
cargas de Noether. Foi obtida a fórmula do projetor conjunto
$P^{\rm phys}$ e da Hessiana vinculada
$D^2\mathcal S-\lambda^aD^2\mathcal C_a$. Essa construção demonstra como as
conservações removem modos espúrios e determinam a colagem, mas também mostra
que elas não provam coercividade, existência do ponto crítico ou positividade
da Hessiana. Permanecem abertos o estabelecimento da estimativa coerciva, a
solução do sistema não linear $(X_*,\lambda_*)$ e a avaliação do gap uniforme
nesse background.

Correção do teste de existência em duas rotas, registrada em
`ponte_global_local_rotas_existencia.md`: a primeira tentativa reutilizou a
redução Q29 na qual $H=h\sigma_{123}$ era tratado como campo independente.
Isso não pertence à convenção vigente $H=d_J^c\omega$; portanto a cúbica
homogênea e sua matriz linearizada foram invalidadas como resultados da ponte.
Na redução correta,
$H=2c(aa'-c)\sigma_{123}$ e a conservação strong-KT impõe
$a'=c/a+h_0/(2ac)$. Esse vínculo deve ser aplicado antes da Hessiana. O
funcional radial oficial corrigido foi escrito explicitamente; as rotas de
existência devem reiniciar a partir dele.

O operador DtN interno foi reconstruído em
`ponte_global_local_dtn_interno.md`. Os quatro momentos de interface foram
derivados diretamente do funcional oficial e a colagem livre é
$\mathcal N_-+\mathcal N_+=0$. A carga fixa atua como restrição de traço
$\delta h=0$. Foi demonstrado que um preenchimento suave por $B^4\simeq
\mathbb C^2$, combinado com $dh=0$, força $h=0$; logo uma carga relativa não
nula exige um núcleo excisado/colo interno ou uma fonte topológica de
transgressão derivada. O DtN linearizado é a Hessiana da ação interna on shell
e foi escrito pela matriz fundamental. Seu valor numérico depende da topologia
e dos dados conservados da segunda ponta, ainda não fixados.
Foi selecionada a rota sem nova fonte: colo interno mínimo refletido. A
minimalidade e a conservação dão $h_0=-2c_0^2$; com carga relativa $q$, isso
fixa $c_0^2=|h_{\rm bg}+2\pi q/\mathcal V_\sigma|/2$. Para garganta redonda,
$a_0=c_0$, e a restrição do lapse fixa $u_0$ juntamente com a corrente
$j_v$. Assim, o DtN interno não contém coeficientes Robin arbitrários. Restam
a existência da raiz de $u_0$, a integração até a interface e a linearização.
Correção variacional: a conservação strong-KT deve ser implementada por um
multiplicador local $\beta[2c(a\dot a-c)-h_0]$ antes da variação. Isso altera
o momento de interface para $\widetilde\Pi_a=\Pi_a+2\beta ac$ e faz o problema
interno um DAE de índice um. O Jacobi vinculado contém o bloco
$\bigl(\begin{smallmatrix}K&C_h^\dagger\\C_h&0\end{smallmatrix}\bigr)$.
Substituir diretamente a lei de fluxo é permitido para reduzir o bloco
algébrico, mas não para calcular o DtN sem recuperar $\beta$.
Correção adicional: o vínculo em coordenada arbitrária é
$\beta[2caa'-N(2c^2+h_0)]$; portanto a restrição do lapse contém
$-\beta(2c^2+h_0)$. Essa parcela se anula na garganta mínima, mas é essencial
durante a integração e introduz $p_a$ na restrição hamiltoniana reduzida.

O DtN exterior foi formulado em `ponte_global_local_dtn_exterior.md`. No
espaço compacto global, $dH=0$ e Stokes impõem $\sum_iq_i=0$; portanto um
estômato carregado isolado não admite exterior strong-KT compacto com uma
única fronteira. Introduzindo apenas componentes físicas compensadoras, a
Hessiana exterior é matricial. Após eliminá-las estacionariamente, a resposta
local é o complemento de Schur
$\Lambda_+^{\rm eff}=\Lambda_{00}-\Lambda_{0c}\Lambda_{cc}^+
\Lambda_{c0}$. A colagem usa
$\widetilde\Lambda_-+\Lambda_+^{\rm eff}$. Falta especificar a configuração
global compensadora e avaliar seus blocos pela Hessiana oficial.
Foi selecionada a configuração global mínima por conservação e simetria:
par antipodal $(q,-q)$ no $S^3$. O DtN exterior reduz-se a
$\bigl(\begin{smallmatrix}D&O\\O&D\end{smallmatrix}\bigr)$, diagonal nos
canais par/ímpar $D\pm O$, e
$\Lambda_+^{\rm eff}=D-OD^+O$. Essa configuração reproduz o Green cotangente
global e seu limite local $1/r$. A pendência exterior reduz-se ao cálculo dos
operadores harmônicos $D_\ell$ e $O_\ell$.

Foi implementado `ponte_global_local_integrador.py`, que integra o DAE
reduzido após eliminar $\beta$ e propaga a matriz variacional. Um teste local
adimensional, documentado em `ponte_global_local_teste_integrador.md`,
preservou a restrição do lapse com erro relativo máximo
$6.95\times10^{-15}$. Isso valida a consistência local do sistema e do sinal
do multiplicador, mas não constitui background físico, colagem ou cálculo de
gap. O próximo resíduo numérico deve variar somente $p_{a,0}$ e impor o DtN
antipodal.

O primeiro tiro antipodal foi auditado em
`ponte_global_local_tiro_antipodal.md`. A carga fixa $c_0$, mas não fixa
$a_0=c_0$; a garganta redonda era um ansatz excessivo. Para comprimento $L$
dado, o problema correto varia $(a_0,p_{a,0},\tau)$ e impõe
$(\dot a,\dot c,\dot u)_{L/2}=0$. Um controle adimensional com $p_v=0$ não
encontrou raiz interna e empurrou $\tau$ à borda da busca. Correção: $p_v$ é
fluxo radial de fase e deve ser zero num background estacionário sem vazamento;
a circulação quantizada pertence à fibra de Hopf,
$v=v_0(r)+m\psi$. Ela acrescenta
$\tau\kappa_\psi a^2m^2/c$ ao potencial. Portanto o tiro executado é somente
o controle $m=0$; o setor físico elementar exige $m=1$ e
$L=\pi R_{\rm cos}$ dado, sem ajuste.
O integrador foi ampliado para esse harmônico. Um teste local com $m=1$,
$\kappa_\psi=1$ e fluxo radial nulo preservou a restrição com erro máximo
$1.42\times10^{-14}$, validando numericamente a implementação do termo de
Hopf, ainda sem realizar a colagem global.
O refinamento local em tolerâncias $10^{-6}$ a $10^{-10}$ e 50 a 400 passos,
contra referência $10^{-12}$/800, manteve a restrição abaixo de
$2.67\times10^{-14}$ e o erro do estado final abaixo de
$6.44\times10^{-15}$. O integrador local está no limite de arredondamento;
essa convergência não resolve a ausência do background exterior.
Uma tentativa multissemente de prolongar o colar até um equador antipodal não
produziu raiz robusta e empurrou parâmetros às bordas. A rota foi invalidada
geometricamente: o colar normal de Berger é local e não folheia globalmente
$T^4\times S^1\times S^3$. Portanto não se deve impor condições antipodais no
mesmo ODE. A rota correta termina o colar em $Y$ e calcula o DtN exterior pela
Hessiana global multidimensional.

O refinamento do DtN exterior de referência foi executado em
`ponte_global_local_gap_referencia.py` e documentado em
`ponte_global_local_refinamento_gap.md`. Para
$\kappa_{\ell,R}^2=\mu^2+\ell(\ell+2)/R^2$, o gap sem limiar local é
$\sqrt3\tanh(\pi\sqrt3)/R$ e fecha quando $R\to\infty$, independentemente do
corte harmônico. Se a Hessiana BI produzir $\mu\geq\mu_*>0$, o gap converge a
$\mu$. Portanto a compactação global não cria gap uniforme; ele precisa vir
do potencial local do background warped. O produto global homogêneo não é
sela normalizada na direção toroidal e não pode ser usado para calcular esse
potencial.

Auditoria refinada em `ponte_global_local_background_global.md`: para o
produto homogêneo normalizado,
$\mathcal R_{\rm GDQ}=4/R^2$ e
$W_{\rm hom}=4\tau/R^2+\log L+3\log R+C_0-4$, de modo que
$\partial_{\log L}W=1$. Portanto ele não é sela se os módulos forem livres.
Isso não exclui a formulação cosmológica em que $L$ e $R$ são dados de
contorno: nesse caso devem ser removidos do espaço de variações ou impostos
por multiplicadores, e a Hessiana precisa incluir
$-\lambda_{\rm cos}D^2\mathcal C_{\rm cos}$. A alternativa é resolver o warp
dinâmico completo.

Fechamento da auditoria da ponte em 14 de julho de 2026, documentado em
`ponte_global_local_fechamento.md` e verificado por
`ponte_global_local_minisuperspace.py`:

- em $x=\log L$ e $y=\log R$,
  $W_{\rm hom}=4\tau e^{-2y}+x+3y$, com
  $\partial_xW_{\rm hom}=1$;
- vínculos cosmológicos lineares $x=x_{\rm cos}$ e $y=y_{\rm cos}$ removem
  os dois módulos globais, mas possuem Hessiana nula nessas coordenadas e não
  geram um limiar positivo para perturbações locais;
- estacionariedade no minisuperspaço homogêneo não demonstra
  estacionariedade no espaço completo de campos;
- a auditoria de `questão_38_final.md` e do Capítulo 22 confirmou que existem
  dados de contorno $R_H,E_H$ e estimativas cosmológicas, mas não um funcional
  local explícito $\mathcal C_{\rm cos}[g,J,f]$ com primeira e segunda
  variações;
- portanto a existência da sela bulk--interface, a avaliação numérica de
  $P^{\rm phys}$ e o gap físico permanecem abertos. O formalismo está fechado
  estruturalmente, mas não deve ser promovido a teorema aplicado;
- as únicas rotas lícitas restantes são derivar
  $\mathcal C_{\rm cos}[g,J,f]$ e sua Hessiana, ou resolver o background
  global warped completo da ação oficial.

Decisão documental posterior: `ponte_global_local_canonica.md` passa a
consolidar a construção da ponte. Ele separa interior local, interface e
exterior cosmológico; preserva os arquivos anteriores como provas/histórico;
e reduz o trabalho aberto a um único bloco global. Nenhum background de Q29,
operador de referência ou ODE local pode substituir esse bloco.

Construção posterior em `ponte_global_local_vinculo_cosmologico.md`: o bloco
$\mathcal C_{\rm cos}$ foi definido sem modificar a ação, usando (i) o
comprimento do ciclo causal, (ii) o raio volumétrico da fibra $S^3$ e (iii) o
Hamiltoniano de Noether associado ao tempo físico reconstruído. As primeiras
e segundas variações dos dois funcionais métricos foram calculadas; a energia
foi definida covariantemente pela forma potencial simplética da ação oficial.
A pendência foi reduzida à avaliação explícita de
$\boldsymbol\Theta_{\rm GDQ}$, à integrabilidade de $\mathcal H_\xi$ e à
solução do exterior warped vinculado.

Continuação em `ponte_global_local_potencial_simpletico.md`: o potencial
simplético oficial foi decomposto nos concomitantes da curvatura ponderada,
dos campos $u=\operatorname{Re}f$, $v=\operatorname{Im}f$ e da torção
dependente $H=d_J^c\omega$. A existência do Hamiltoniano de Noether foi
reduzida à condição de fluxo simplético nulo no contorno. A polarização
cosmológica admissível fixa a classe conforme e os dados globais e usa a
colagem DtN como condição Robin auto-adjunta. Resta expandir o concomitante de
Bismut no ansatz exterior, integrar a carga e resolver a sela warped.

Redução exterior posterior em `ponte_global_local_exterior_warped.md`: foi
escolhido o ansatz de cohomogeneidade um ao longo de $S^1$, com órbitas
$T^4\times S^3$, distinto do colar local de Berger. Foram derivados
$H=d_J^c\omega$, $|H|^2$, $R_{\rm LC}$, a ação oficial reduzida de primeira
ordem e os quatro momentos $(P_x,P_y,P_u,P_v)$. O limite homogêneo reproduz
$\mathcal R_{\rm GDQ}=4/c^2$ e o limite cônico anula a torção normal. Resta
derivar/implementar as equações vinculadas e resolver a colagem global.

Em `ponte_global_local_exterior_equacoes.md`, a redução foi convertida num
sistema canônico de nove variáveis, incluindo a normalização acumulada. A
restrição do lapse é
$\tau(4e^{-2y}-\mathcal K_2)+u-4-\lambda_N=0$, o fluxo de fase satisfaz
$\dot p_v=0$ e o exterior foi corretamente formulado como problema entre duas
interfaces, não como regularidade num único polo. O script
`ponte_global_local_exterior_teste.py` foi criado como teste sintético de
preservação da restrição; ele não representa o background físico.

Execução do teste documentada em
`ponte_global_local_exterior_teste_resultado.md`: três refinamentos de
tolerância/passo preservaram a restrição do lapse com resíduo máximo
$8.882\times10^{-16}$ e produziram o mesmo $Z$ nas casas exibidas. Isso valida
a álgebra canônica e a implementação local, não a existência da sela global.

Correção antes da colagem: o exterior isotrópico eliminava por hipótese o
modo Berger $a/c$ e, portanto, não era suficiente para receber os quatro
traços do DtN interno. Ele foi reclassificado como subsector de teste. Em
`ponte_global_local_exterior_berger.md` foi derivado o exterior completo
$N^2ds^2+A^2g_{T^4}+a^2(\sigma_1^2+\sigma_2^2)+c^2\sigma_3^2$, incluindo
$H=d_J^c\omega$, curvatura, funcional de primeira ordem, restrição do lapse,
momentos, inversão exata e correspondência
$\Pi_a=p_y/a$, $\Pi_c=p_z/c$. Essa é a redução canônica para a colagem.

O script `ponte_global_local_exterior_berger_teste.py` validou o sistema
completo em três refinamentos: $\max|\mathcal C_N|=8.882\times10^{-16}$ e o
mesmo $Z$ nas casas exibidas. O resultado está em
`ponte_global_local_exterior_berger_teste_resultado.md` e é classificado como
teste sintético de consistência, não como background físico.

Colagem organizada em `ponte_global_local_colagem.md` e
`ponte_global_local_colagem.py`: a invariância da forma de Liouville fixa
$p_y=a\Pi_a$, $p_z=c\Pi_c$, $p_u=\Pi_u$ e $p_v=\Pi_v$. O warp toroidal é
Dirichlet na interface na redução mínima, pois o colar interno fatorou o
$T^4$. O resíduo global de duas interfaces foi enumerado. Uma raiz sem o
componente energético $\mathcal C_E$ seria apenas condicional; o teste do
adaptador preserva explicitamente o resíduo refletido sem ajuste.

Execução documentada em `ponte_global_local_colagem_resultado.md`: o resíduo
de interface foi exatamente zero, com restrições interna e externa de
$1.421\times10^{-14}$ e $2.220\times10^{-15}$. O fechamento refletido sem
ajuste falhou com norma $0.8661501$. Isso valida o adaptador, mas exclui o
fixture histórico como sela global.

Busca de duas interfaces em
`ponte_global_local_busca_duas_interfaces.py`: dois colares independentes e o
exterior Berger foram reunidos em dez variáveis/dez resíduos, sem reflexão ou
arredondamento impostos. A etapa exploratória reduziu o custo de $94.507$ para
$6.2161\times10^{-7}$, mas a reavaliação precisa deu
$\|\mathfrak F\|=1.11499\times10^{-3}$ e restrição exterior
$3.21368\times10^{-5}$; portanto não é raiz. Um refinamento com integrações
mais precisas excedeu 150 s sem saída. O próximo método deve usar Jacobiana
variacional ou colocação multidomínio. Fonte:
`ponte_global_local_busca_duas_interfaces_resultado.md`.

Decisão numérica posterior: adotar primeiro Jacobiana variacional, conforme
`ponte_global_local_jacobiana_variacional.md`. Estados e sensibilidades serão
integrados simultaneamente nos dois colares e no exterior, com domínios
normalizados para incluir derivadas em relação aos comprimentos. A colocação
multidomínio será usada como verificação independente, não como fonte de uma
segunda solução ajustada.

Implementação iniciada em
`ponte_global_local_busca_jacobiana_variacional.py`: os dois fluxos internos,
o adaptador e o fluxo exterior transportam matrizes de sensibilidade $S$ em
domínios normalizados. As Jacobianas locais são avaliadas por passo complexo
no campo vetorial, evitando diferenças entre soluções globais. O otimizador
recebe conjuntamente resíduo e Jacobiana transportada; qualquer candidato é
reavaliado pelo integrador preciso anterior.

Resultado da Jacobiana variacional em
`ponte_global_local_jacobiana_variacional_resultado.md`: a derivada
transportada concordou com uma derivada direcional independente com erro
relativo $1.912\times10^{-4}$, mas o espectro singular mostrou posto oito,
com dois valores singulares nulos. A causa é que, no setor estacionário,
$v$ constante e $p_v=0$ tornam dois resíduos identicamente triviais. O sistema
possui oito equações efetivas para dez parâmetros. As duas linhas devem ser
substituídas por $\mathcal C_R=0$ e $\mathcal C_E=0$. Isso explica a deriva do
otimizador sem implicar inexistência ou instabilidade; a busca não deve
continuar antes da avaliação reduzida da energia de Noether.

Atualização posterior em `ponte_global_local_raio_energia_resultado.md`: o
raio volumétrico da órbita Berger foi inserido explicitamente como
$\mathcal C_R=(2y+z)/3-\log R_{\rm cos}$. O teste da Jacobiana transportada
elevou o posto de oito para nove. Resta exatamente uma nulidade, a linha
$p_v=0$ que deve ser substituída por $\mathcal C_E$. A Q38 fornece $R_H$ e
$E_H$ como dados de contorno, mas não fornece ainda a imersão causal do tempo
físico, o gerador $\xi$ em componentes do ansatz Berger nem o pullback de
$\mathbf Q_\xi$. Portanto o Hamiltoniano radial não pode ser identificado com
$E_H$; a busca da sela permanece suspensa até esse transporte causal.

Ciclo causal posterior em `ponte_global_local_exterior_causal.md` e
`ponte_global_local_ciclo_agentico_resultado.md`: foi construída uma imersão
causal local compatível com a Q2 escolhendo
$S^1_{\theta_0}\subset T^4$ como relógio e mantendo $s$ como coordenada
radial. Isso exigiu separar $A_0$ de $A_s$. A torção, a curvatura, a ação
reduzida, a restrição e os momentos foram derivados novamente; a matriz
cinética tem determinante 32 e o limite $A_0=A_s$ recupera exatamente o
exterior Berger anterior. A energia reduzida relativa é a resposta on shell
$\mathcal H_\xi^{\rm red}=(p_0^{\rm full}-p_{0,\rm ref}^{\rm full})/\beta_E$.
O integrador preservou a restrição a $2.665\times10^{-15}$. Correção posterior
por instrução do autor: a normalização energética já pertence ao universo
global de Einstein e é associada a $\alpha$. Em unidades $R_H=1$, usar
$\widehat\beta_E=2\pi$, $\widehat R_{\rm cos}=\pi^2\sqrt\alpha$,
$\widehat E_H=1$ e o background homogêneo sem defeito como referência
$p_{0,\rm ref}=0$. Portanto não faltam novos parâmetros físicos; falta
transportar o prefator da ação para a unidade $E_0=c^4R_H/(2G)$ e executar o
sistema causal. A extensão global do relógio permanece condicional ao
recobrimento universal ou à reconstrução OS; o gap completo ainda exige
$\delta J$ e modos não homogêneos.

Execução final posterior em `ponte_global_local_solver_final.py`, auditada em
`ponte_global_local_solver_final_resultado.md`: o sistema causal $11\times11$
foi efetivamente montado, mas não produziu uma sela. As identificações diretas
$p_0^{\rm red}=\widehat E_H$ e
$p_0^{\rm red}=\Pi_G\widehat E_H$ foram rejeitadas numericamente: a primeira
explode a escala natural da dinâmica; a segunda gera condicionamento de
$10^{38}$--$10^{44}$. Isso não reabre a normalização global por $\alpha$;
isola o mapa ainda não avaliado entre a energia global e o momento cuja ação
reduzida suprimiu os volumes, o prefator $\hbar/\Lambda_C^2$ e a integral em
$\gamma$. Definiu-se o jacobiano faltante $Z_E(\alpha)$ por
$\mathcal C_E=Z_Ep_0^{\rm red}e^{-x_0}-1$. Ele deve ser calculado da redução,
não ajustado pelo solver. Permanecem válidos: $\det M_C=32$, limite isotrópico
exato, conservação da restrição a $2.665\times10^{-15}$ e posto nove após
$\mathcal C_R$. Não há ainda sela, posto final ou gap físico.

Correção pela normalização constitucional: introduzir
$Z_0=\int ds\,\mathscr V$ cancela os volumes coordenados compactos e substitui
o fator anterior por
$\mathcal C_E=K_\gamma(\alpha)p_0^{\rm red}e^{-x_0}/Z_0-1$. O solver foi
ampliado com $\dot Z=\mathscr V$. Com $K_\gamma=1$ apenas como teste, o custo
caiu de $1.3222$ para $0.99865$, mas a busca entrou em região rígida e foi
interrompida sem candidato. Resta avaliar $K_\gamma$ pela integral causal e
usar Jacobiana variacional/colocação para a busca, sem ajustar esse fator.

Auditoria posterior da Porta A em
`ponte_global_local_porta_A_contorno_causal.md`, reconciliada com o documento
canônico mais recente `q29/projetor_causal_cauchy_normalizado.md`: a ação
oficial permanece sem o fator $1/(2\pi i)$, mas a reconstrução física usa o
projetor de Laurent
$\mathfrak P_\gamma[F]=(2\pi iw_\gamma)^{-1}\oint F(z)dz/z$, já implícito nas
Q4 e Q9. Portanto $\mathfrak P_\gamma[1]=1$ e $K_\gamma=1$ está derivado para
o setor estacionário; não é fixture nem ajuste. Para uma família $X(z)$ não
estacionária, porém, o projetor deve agir sobre o integrando completo
$p_0^{\rm red}(z)e^{-x_0(z)}/Z_0(z)$ e não se fatoriza. A sela térmica
$\beta_E^2/16$ estacionariza o kernel $I_1\propto\tau^{-4}
e^{-\beta_E^2/(4\tau)}$; tratá-lo como uma integral real com a medida
$d\tau/\tau$ deslocaria o ponto para $\beta_E^2/20$, mas essa aproximação por
sela não substitui a extração de Laurent. A Porta A está fechada para o ansatz
estacionário e permanece condicional apenas se for necessária uma família
causal genuinamente não estacionária.

Plano operacional consolidado em
`ponte_global_local_plano_loop_agentico.md`: o trabalho restante foi dividido
em quatro portas sequenciais — normalização causal, sela bulk--interface,
projetor/Hessiana física e estabilidade espectral — seguidas de validação
independente. O loop preserva os dados cosmológicos já fixados e, diante de
falha, amplia somente o ansatz apontado pela SVD da Jacobiana ou pelo modo
negativo convergente. Nenhum valor de $K_\gamma$, parâmetro cosmológico ou gap
pode ser escolhido pelo alvo numérico.

Execução completa posterior registrada em
`ponte_global_local_loop_agentico_resultado.md`: o projetor causal normalizado
fecha $K_\gamma=1$ para o setor estacionário. A busca com Jacobiana
variacional e central independente não encontrou sela no ramo integrável
original; o resíduo permaneceu no matching de $(p_a,p_c,p_u)$. A regularidade
força $p_c=p_u=0$. Uma rotação radial de $J$ foi excluída porque
$N_J=0$ implica $\chi'=0$. O Beltrami toroidal constante satisfaz
Maurer--Cartan, mas tem $\delta H=\Pi_\mu=0$ e não se acopla ao resíduo. O
ramo discreto integrável $\chi=\pi/2$ foi formulado como DAE regular e testado,
mas a continuação reduz o resíduo somente enviando ambos os comprimentos de
colar a zero; não há sela interior não degenerada nessa classe. A
infraestrutura de $P^{\rm phys}$ e Hessiana passou nos testes algébricos, mas
estabilidade e gap não podem ser avaliados sem background. A única rota ainda
não excluída é um modo interno não homogêneo de Kodaira--Spencer com condição
elíptica de bordo derivada da Hessiana oficial.

Triagem numérica/representacional registrada em
`ponte_global_local_triagem_kodaira_resultado.md`: para o primeiro harmônico
não constante de $S^3$, a quadratura recuperou
$\int Y_1=0$, $\int Y_1^2=1$ e o autovalor $3$. Como o residual homogêneo é
singlet, o acoplamento linear com um modo puro não singlet se anula por
simetria quando o operador e o domínio de bordo são equivariantes. A primeira
retroação nessa classe é quadrática em sua amplitude, pois $Y_1^2$ contém um
singlet. A triagem escalar não substitui a decomposição do Beltrami tensorial
sob a simetria efetivamente preservada. Assim, a rota correta passa por uma redução de
Galerkin de amplitude finita e pelo cálculo oficial de
$(\lambda_\mu,g_\mu,C_a,C_c,C_u)$, não por inserir diretamente uma nova coluna
linear na Jacobiana.

Continuação da triagem Kodaira--Spencer: a decomposição tensorial sob a
simetria preservada $SU(2)_L\times U(1)_R$ confirmou que o primeiro harmônico
$j=1/2$ não contém singlet e tem acoplamento linear nulo por Schur. Foram
construídas ainda deformações globais integráveis no fator de Hopf, tanto
anisotrópica diagonal quanto ressonante não linear. Em ambos os casos, a
extensão simultânea compatível dos campos é um pullback de $(g,J,f)$; pela
naturalidade da ação oficial, todos os coeficientes estáticos de Galerkin se
anulam. Esses modos são zeros modulares/difeomórficos e devem ser removidos por
$P^{\rm phys}$. Assim, a triagem de modo único não fecha a ponte. O próximo
objeto legítimo é um autovetor não homogêneo da Hessiana conjunta de
$(g,J,f)$, já projetada fora das difeomorfismos e com o domínio DtN da
interface.

Teste mínimo de catástrofe estocástica em
`ponte_global_local_teste_catastrofe_resultado.md`: no candidato quase crítico
da homotopia $h=0{,}18$, obteve-se
$r=4{,}49774\times10^{-5}$ e
$b=-3{,}43326\times10^{-5}$, estável sob seis passos direcionais. Assim
$\sigma_{\rm req}^2=-r/b\simeq1{,}31005>0$: a covariância possui o sinal
correto para cancelar o residual reduzido. O módulo ainda não é físico porque
o modo está normalizado na métrica euclidiana do tiro e $h$ é auxiliar. Falta
normalização pela métrica física e cálculo da covariância causal da GDQ.

Auditoria vetorial posterior em `ponte_global_local_sela_estatistica.md`:
a variância escalar $-r/b\simeq1{,}31005$ anula somente a projeção mole, mas
leva o resíduo vetorial completo a norma aproximadamente $5{,}42$, contra
$1{,}87\times10^{-4}$ antes da correção. Um teste de ruído isotrópico nas
coordenadas do tiro também falhou: o mínimo quadrático exigiria covariância
negativa. Portanto a estocasticidade não fecha a sela por um único parâmetro.
A rota ainda admissível é a equação média completa
$D\mathcal S_{\rm aug}+\tfrac12D^3\mathcal S_{\rm aug}:C^{\rm phys}=0$, com
$C^{\rm phys}$ calculada pelo resolvente causal da Hessiana oficial projetada,
sem ajuste ao resíduo.

A forma cinética Berger oficial foi então auditada em
`ponte_global_local_assinatura_cinetica.py`: antes dos vínculos e da projeção,
sua assinatura é $(2,3,0)$. Portanto a Hessiana bruta não pode ser tratada
como covariância positiva. A Questão 16 fixa a difusão em coordenadas físicas,
$D^{ij}=\nu_0\Omega^{-1}h^{ij}$, mas não o operador de ruído/mobilidade no
espaço de campos ou nos onze parâmetros de colagem. Uma prova por medida
invariante pode usar Krylov--Bogoliubov sob Feller+tightness, porém exige
primeiro esse pullback físico; inserir ruído diretamente nos parâmetros seria
uma hipótese nova.

O pullback foi finalmente calculado em
`ponte_global_local_pullback_estocastico.md`. A difusão espacial da Q16 atua
nos campos por $R\xi=(\mathcal L_\xi g,\mathcal L_\xi J,\mathcal L_\xi f)$,
logo sua covariância levantada é $RDR^\dagger$. Como o projetor físico satisfaz
$P^{\rm phys}R=0$, a covariância física projetada é exatamente nula. O teste
algébrico encontrou supressão relativa $8{,}79\times10^{-17}$ para esse setor.
Essa conclusão vale para difeomorfismos de gauge com traço físico nulo. Um
deslocamento browniano com traço não nulo na interface pode sobreviver como
$B_\partial=P^{\rm phys}RE_\partial$ e induzir
$B_\partial D_\partial B_\partial^\dagger$. Portanto a rota estatística fica
reduzida ao pullback DtN do ruído de borda; o $\sigma(g)$ histórico não deve
ser usado para preencher esse cálculo.

Teste mínimo posterior do setor de borda homogêneo em
`ponte_global_local_teste_covariancia_borda.py`: usando os dois comprimentos de
colar e restringindo $C_\partial=LL^T\ge0$, o ótimo foi covariância
numericamente nula e o resíduo não diminuiu. Assim, ruído interior, modo mole
único, ruído isotrópico e deslocamento homogêneo das interfaces estão
excluídos como fechamento da sela no ansatz atual. Permanecem apenas modos de
forma/angulares da interface ou a sela determinística.

Reavaliação arquitetural posterior: os solvers tratavam o limite cosmológico
$T^5\times S^3$ para o bulk local $\mathbb R^4\times T^4$ como uma interface
física, confundindo-o com a fronteira real do estômato. O teste
`ponte_global_local_teste_sem_colar.py`, documentado em
`ponte_global_local_sem_interface_resultado.md`, transportou diretamente um
estado ligado no limite apontado de $S^3_R$ para $\mathbb R^3$. O estado
permaneceu uniformemente localizado e o autovalor convergiu com erro
$O(R^{-2})$, sem colar ou sela global--local. Isso sustenta reformular a
ponte: convergência apontada entre backgrounds e DtN somente no estômato.
Ainda falta estender o teste à Hessiana oficial completa.

Consolidação em `ponte_global_local_lemas_sem_colar.md`: os seis lemas foram
reformulados como um teorema condicional completo sem Hipótese BI. A família
$T^4\times S^1_{\varepsilon^{-1}}\times S^3_{\varepsilon^{-1}}$ converge
apontadamente para $T^4\times\mathbb R^4$; o defeito localizado é transportado
no chart, as formas físicas convergem em Mosco sob gap local, IMS/Agmon
preservam localização e gap, e resolventes/projetores de Riesz convergem no
cluster. A única hipótese física remanescente é a existência do estômato local
admissível com Hessiana projetada e gap $\Delta_0>0$. Não há mais pendência de
sela global--local. Os documentos dos Lemas 1--6 e o documento canônico
receberam avisos de escopo.

Fechamento aplicado posterior em `ponte_global_local_fechamento_c3.md`: o
background local da Q28 formado por três preenchimentos gaussianos primitivos
satisfaz a hipótese espectral remanescente. O projetor remove rotação comum,
fase constante, normalização, escala e difeomorfismos; a Hessiana física é a
soma dos blocos relativos, radiais e Ornstein--Uhlenbeck. Seu gap é

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0,
$$

igual a $1/2$ em $\tau=1$ e na normalização primitiva. O teste
`ponte_global_local_validar_gap_c3.py` confirmou $1/(2\tau)$ por refinamento
até erro $1{,}10\times10^{-6}$ para $\tau=1$. Assim, a ponte e os seis lemas
estão fechados como teorema aplicado na classe estacionária $C_3$;
backgrounds arbitrários continuam fora desse fechamento.

Em `ponte_global_local_normalizacao_zero_mode.md` foi demonstrado que o
multiplicador de normalização atua por
$u\mapsto u+\lambda_N$, $p\mapsto e^{-\lambda_N}p$, deixando a forma
geométrica e as restrições invariantes. Assim a forma da sela pode ser
buscada em $\lambda_N=0$ e a normalização aplicada depois por
$\lambda_N=\log(Z_0/Z_{\rm cos})$. O script
`ponte_global_local_busca_sela_condicional.py` implementa uma primeira busca
refletida da forma, explicitamente sem o vínculo energético final.

Resultado em `ponte_global_local_busca_sela_condicional_resultado.md`: a
primeira busca omitia a compatibilidade do lapse exterior e foi rejeitada. A
busca corrigida, com seis variáveis, terminou com resíduo $0.0191852$,
restrição exterior $1.12\times10^{-2}$ e parâmetros nos limites; também foi
rejeitada. Isso não exclui a sela GDQ, apenas a hipótese auxiliar de reflexão
exata com $S^3$ redondo no plano médio. A próxima busca deve usar duas
interfaces independentes, sem impor simetria não derivada.

### 3.3 Ação oficial imutável

\[
\boxed{
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
}
\]

Essa é a ação física fundamental. Funcionais de Perelman, ações reduzidas,
Hessianas, operadores efetivos e termos de sonda devem ser derivados dela ou
claramente identificados como completamentos de bordo/fontes externas. A ação
não deve ser trocada por Einstein--Hilbert, Yang--Mills ou uma ação do Modelo
Padrão.

### 3.4 Dicionário Madelung--Perelman

Convenção consolidada:

\[
\rho=e^{-(f+\bar f)/2},\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
\]

A relação é local/setorial; nós, fases multivaloradas, fibrados não triviais
e monodromias exigem dados topológicos adicionais. Não tratar o mapa como
bijeção global automática.

### 3.5 Variáveis e distinções essenciais

- (t): tempo físico reconstruído;
- τ: parâmetro de fluxo/escala, não segunda coordenada temporal física;
- (z_\tau): variável complexa de causalidade/contorno quando aplicável;
- (f): campo complexo fundamental;
- ρ, (S_R): variáveis derivadas de Madelung;
- (H) ou (B): torção de Bismut/Cartan, com convenção a manter uniforme;
- (\Lambda_C): escala geométrica/setorial, não automaticamente massa física;
- γ: contorno causal complexo da ação.

---

## 4. Cadeia dedutiva fundamental já construída

### 4.1 Hidrodinâmica quântica

As Questões 10--16 organizam a variação da ação em variáveis de Madelung:

\[
\delta_{S_R}\mathcal S=0
\Rightarrow
\partial_t\rho+\nabla\cdot(\rho v)=0,
\]

\[
\delta_\rho\mathcal S=0
\Rightarrow
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}+V+Q=0,
\]

\[
Q=-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
\]

A variação métrica fornece o setor de tensão/energia efetivo. Essas equações
não devem ser apresentadas como postulados adicionados depois.

### 4.2 Regularidade e loops

A GDQ sustenta que a regularidade decorre da própria estrutura geométrica e
de seus operadores inteiros/form factors. A quantização perturbativa foi
organizada como EFT condicional. Não afirmar uma prova não perturbativa geral
nem usar “renormalização fundamental”; quando necessário, falar em projeção
finita, vestimento geométrico ou tradução perturbativa externa.

Fantasmas/BRST podem ser usados para auditoria de gauge, mas não constituem
ontologia necessária da GDQ.

### 4.3 Reconstrução quântica

As Questões 7, 20 e 21 usam a rota Osterwalder--Schrader:

\[
\text{dados euclidianos + positividade de reflexão}
\longrightarrow
\mathcal H_{\rm phys},\ H\ge0,
\ e^{-itH/\hbar}.
\]

O fechamento é condicional à verificação setorial completa dos axiomas OS.
No setor total fechado, a evolução é unitária; dissipação e Hamiltonianos não
Hermitianos pertencem a descrições reduzidas/abertas.

### 4.4 Born

A densidade espacial é preservada pela continuidade e identificada com
(|\Psi|^2). No espaço de Hilbert reconstruído, Gleason fornece a medida em
projetores sob suas hipóteses. Para um evento individual, a Q42 fornece a rota
condicionada:

\[
p_t=\operatorname{Tr}(\rho_tP_+),
\]

e, se (p_t) é martingal limitado e termina em (0) ou (1),

\[
\Pr(p_\infty=1)=p_0.
\]

Falta derivar da ação oficial, para um aparelho real, o ruído condicionado,
a mobilidade e a captura quase certa. Escrever (p=\operatorname{Tr}(\rho P))
sozinho não é uma derivação de Born.

### 4.5 Wallstrom e quantização

A rota mais sólida é topológica:

\[
c_1(L)\in H^2(M^*,\mathbb Z)
\Rightarrow
\frac1{2\pi\hbar}\oint p\cdot dx\in\mathbb Z
\]

com extensões antiperiódicas/holonomia para setores de spin. A soma de Poisson
é uma representação útil, mas não deve inserir manualmente a monodromia que se
pretende derivar.

### 4.6 Causalidade

A prescrição de Sudarshan e o contorno complexo organizam a relação entre
setores difusivos e oscilatórios. Microcausalidade e no-signalling devem ser
demonstrados no espaço-tempo físico reconstruído.

Escolha retardada pode ser formulada como problema global de contorno, mas
“difusão retroativa” não está estabelecida como dinâmica física. Qualquer rota
com dados finais precisa provar existência, unicidade, estabilidade e ausência
de sinalização. A formulação causal segura usa propagadores retardados.

### 4.7 Limite clássico

A expectativa estrutural é:

\[
\text{GDQ}
\xrightarrow{\text{linearização/projeção}}
\text{Schrödinger/Pauli/Dirac}
\xrightarrow{\hbar\to0,\;\text{coarse graining}}
\text{Hamilton--Jacobi/Einstein--Maxwell efetivos}.
\]

Esse limite deve ser demonstrado por setor. A ação oficial permanece
independente da base coordenada usada para realizar a redução.

---

## 5. Spin, estatística, Hopf e Stern--Gerlach

### 5.1 Spin como circulação

O manuscrito, especialmente os Capítulos 9, 11 e 34, propõe:

\[
\oint B_\mu dx^\mu=hs,
\qquad s=\frac12
\Rightarrow
\oint B_\mu dx^\mu=\pi\hbar.
\]

A fibração de Hopf

\[
S^1\hookrightarrow S^3\to S^2\simeq\mathbb{CP}^1
\]

fornece representação dupla, retorno após (4\pi) e módulo de orientações.
Na Q42, a fatia normal do estômato foi tratada como ℂ², com elo (S^3), e
o estado axial foi escrito como

\[
P=uu^\dagger,
\qquad P\in\mathbb{CP}^1.
\]

As duas cartas de Hopf foram construídas e verificadas numericamente. O
pullback de uma rotação global no cilindro redondo é zero por isometria:

\[
Z_{\rm bulk}^{\rm orientação\ global}=0.
\]

A rigidez física positiva deve vir de textura não homogênea ou resposta
localizada ao aparelho, não de uma rotação global do background isotrópico.

### 5.2 Spin--estatística e exclusão

O Capítulo 11 contém a cadeia original:

\[
\text{troca + holonomia }\pi
\Rightarrow e^{i\pi}=-1
\Rightarrow\Psi(x_2,x_1)=-\Psi(x_1,x_2)
\Rightarrow\Psi(x,x)=0.
\]

Ela preserva a intuição física da exclusão como nó/pressão geométrica. Para
virar teorema intrínseco completo ainda é necessário calcular a holonomia no
espaço de configuração de dois solitons, justificar o fator de duplicação e
analisar a ordem do zero que controla o potencial de Bohm.

A Q27 fecha estruturalmente o setor ao recorrer ao teorema spin--estatística
no setor local causal, de energia positiva e spinorial reconstruído.

### 5.3 Stern--Gerlach: resultado atual

A GDQ não exige que o aparelho crie o spin. O objeto já chega com circulação,
representação semi-inteira e módulo de orientações. O aparelho clássico apenas
quebra a degenerescência axial e seleciona a base:

\[
S^2_{\rm orientações}
\xrightarrow{J_{\rm app}}
\{P_{\mathbf n}^{+},P_{\mathbf n}^{-}\}.
\]

Resultados consolidados da Q42:

1. elo (S^3), atlas de Hopf e projetores (P=uu^\dagger);
2. dois canais (\pm\hbar/2);
3. simulação de feixe e medições sequenciais;
4. limite não adiabático verificado contra Landau--Zener;
5. processo condicionado que recupera Born sob hipóteses explícitas;
6. background gaussiano normal e cilindro de Hopf construídos;
7. cilindro preferido entre os dois ramos na comparação on-shell reduzida;
8. estabilidade homogênea do raio cilíndrico:
   (\mathcal W''(2\sqrt\tau)=3/(2\tau)>0);
9. resposta DtN radial no cilindro:
   (z_H=3\sqrt\pi/4);
10. correção conceitual: não dividir pela rigidez global nula.

Formulação correta da interface:

\[
(\Lambda_\Phi+\mathsf R_{\rm app})\varphi=0,
\]

onde (\Lambda_\Phi) é o DtN do objeto e (\mathsf R_{\rm app}) deve vir da
fonte clássica e do termo de interface.

Q42 está fechada como reconstrução geométrica-operacional e teste de
consistência. Permanecem fora desse fechamento a estabilidade espectral de
todos os modos tensoriais/não homogêneos e o cálculo de parâmetros de um
detector real diretamente da ação.

---

## 6. Teoria GDQ da medida e da interface clássico--quântico

Este é o próximo eixo unificador do projeto.

### 6.1 Formulação correta

Não introduzir três teorias fundamentais independentes. Manter a ação oficial
e acrescentar fontes e completamento variacional de interface:

\[
\mathcal S_{\rm tot}
=\mathcal S_{\rm GDQ}[\Phi]
+\mathcal S_{\rm fonte}[\Phi,J_{\rm app}]
+\mathcal S_{\partial}[\Phi,\Xi_{\rm app}].
\]

Objetivo principal:

\[
\boxed{
J_{\rm app}^{\rm clássico}
\longrightarrow
\delta\Phi_{\rm app}
\longrightarrow
\operatorname{Hess}\mathcal S_{\rm GDQ}
\longrightarrow
\mathsf R_{\rm app}
\longrightarrow
\text{canais e registro}.
}
\]

Os projetores de Pauli não podem ser inseridos em (\mathsf R_{\rm app}) para
depois serem “derivados”. A geometria intrínseca fornece o módulo de Hopf; o
campo clássico deve fornecer apenas a anisotropia/eixo e o acoplamento.

### 6.2 Blocos necessários

1. critério espectral e adimensional de regime clássico, quântico e interface;
2. variação da ação com fontes macroscópicas;
3. operador de interface e DtN localizado;
4. Hessiana física com gauge removido;
5. mobilidade causal (\mathbb M);
6. banho macroscópico e relação de flutuação--dissipação;
7. amplificação e formação de registro estável;
8. processo condicionado e derivação de Born;
9. limite Pauli/Dirac/Lindblad;
10. extensão multipartida com Bell e no-signalling.

### 6.3 Relaxação e irreversibilidade

A Hessiana fornece rigidez, não tempo. O tempo de resposta exige:

\[
\partial_t\delta\Phi
=-\mathbb M\mathbb H_{\rm eff}\delta\Phi+\xi,
\]

\[
\tau_{\rm relax}^{-1}
=\min\operatorname{Re}\operatorname{spec}
(\mathbb M\mathbb H_{\rm eff}).
\]

O Capítulo 21 já oferece ideias importantes: NESS, Fano e projeção de
Zwanzig--Mori. Elas devem ser reaproveitadas, mas a desigualdade de produção
de entropia e o núcleo de memória precisam ser derivados para o aparelho
concreto. Monotonicidade de Perelman sozinha não prova registro irreversível.

### 6.4 Emaranhamento

Conectividade topológica compartilhada, tubos de fluxo e pontes são
possibilidades, não resultados atuais. A teoria deve primeiro construir o
operador multipartido e demonstrar quantitativamente:

- correlações de Bell;
- independência das escolhas;
- no-signalling;
- compatibilidade com causalidade relativística.

---

## 7. Memória por blocos de questões

### 7.1 Q1--Q9: fundação

| Q | Resultado vigente | Status/memória |
|---|---|---|
| 1 | Auditoria detectou geometrias incompatíveis; proposta única ℝ⁴×T⁴ | Reconstrução adotada; spin como circulação ainda exigia holonomia concreta |
| 2 | Definição matemática, assinatura, spin e ação | EFT axiomática fechada; constantes numéricas abertas |
| 3 | (n=4) complexo | Axioma atual; Atiyah--Singer é programa futuro |
| 4 | Consistência variacional e loops | Fechada como EFT perturbativa condicional |
| 5 | Dicionário dos campos | Fechado |
| 6 | Natureza de τ | Fechado |
| 7 | Emergência do tempo lorentziano/OS | Estruturalmente fechada, verificação setorial OS pendente |
| 8 | Causalidade e escolha retardada | Causalidade fechada; não promover retrocausalidade especulativa a teorema |
| 9 | Ação oficial única | Fechada; ação não pode ser substituída |

### 7.2 Q10--Q19: dinâmica e estabilidade

| Q | Resultado vigente | Status/memória |
|---|---|---|
| 10 | Continuidade por variação | Fechada |
| 11 | Hamilton--Jacobi--Bohm por variação | Fechada |
| 12 | Equação métrica/tensão | Fechada no setor derivado |
| 13 | Medida ℘ e normalização | Fechada |
| 14 | Mapa Perelman--Madelung | Local/setorial, não bijeção global |
| 15 | Relação (f,\rho,S_R) | Fechada |
| 16 | Difusão estocástica | Fechada estruturalmente; manter convenções |
| 17 | Problema de Cauchy | Existência/unicidade local sob gauges e hipóteses de regularidade |
| 18 | Solitons como partículas | Critério e solução neutra mínima; partículas carregadas completas não provadas genericamente |
| 19 | Estabilidade por monotonicidade | Condicional ao espectro do operador de Jacobi |

### 7.3 Q20--Q27: fundamentos quânticos

| Q | Resultado vigente | Status/memória |
|---|---|---|
| 20 | Espaço de Hilbert | Fechado estruturalmente via OS |
| 21 | Unitariedade | Fechada no setor total; aberto/reduzido pode dissipar |
| 22 | Born | Fechada estruturalmente; dinâmica individual ligada à teoria da medida |
| 23 | Wallstrom | Fechada pela integralidade topológica de (c_1) |
| 24 | Medição | Decoerência/atrator estruturados; unicidade física exige dinâmica de interface |
| 25 | Problema do sinal | Resolução conceitual geométrica; algoritmo polinomial, variância e benchmarks abertos |
| 26 | Spin (1/2) | Hopf/circulação estruturados; resíduos ficam como rota complementar |
| 27 | Spin--estatística | Fechada condicionalmente ao setor spinorial local causal |

### 7.4 Q28--Q37: gauge, escalas e constantes

| Q | Resultado vigente | Status/memória |
|---|---|---|
| 28 | Fibrado efetivo (SU(3)\times SU(2)\times U(1)), Killing/Poisson, APS/Bismut | Teorema condicional; classes, η-invariantes e índices explícitos pendentes |
| 29 | Quebra eletrofraca e relações (m_W,m_Z,\theta_W) | Estrutura efetiva fechada; normas e escala numérica pendentes |
| 30 | Conexão (SU(3)), Wilson loops, lei de área e cota de gap | Estruturalmente fechada no setor efetivo; calcular (g_s,\sigma,\lambda_1) |
| 31 | Relaxação torsional do CP forte | Estruturalmente fechada; normalização, EDM e cosmologia quantitativa pendentes |
| 32 | Hessiana e propagador suavizado | Estruturalmente fechada; setor vetorial é efetivo condicional |
| 33 | Escala de corte geométrica | Estruturalmente respondida; não confundir corte setorial com massa física |
| 34 | Ward/Slavnov--Taylor e loops | Fechada no setor geométrico declarado de 34-0 |
| 35 | Ausência de polo de Landau no setor suavizado | Fechada condicionalmente no setor $U(1)$ |
| 36 | Escala absoluta | Fechada por calibração metrológica; teoria deve prever razões adimensionais |
| 37 | Estrutura fina α | Rota geométrica forte no fundo cosmológico; não fechada independentemente do background |

### 7.5 Q38--Q42: gravidade, massas, bárions e medição

| Q | Resultado vigente | Status/memória |
|---|---|---|
| 38 | (C_R), cadeia térmico-axial e \(G\) no espaço cosmológico de Einstein | Fechada como problema global; projeções locais não determinam autonomamente o valor global |
| 39 | Espectro Rosen--Morse global para razões leptônicas | Fechado no modelo espectral global; setor térmico local e ponte ao bulk oficial permanecem condicionais |
| 40 | Construção geométrica de próton/nêutron, bulk+superfície, carga e spin | Fechada estruturalmente; momentos, espalhamento e modos completos em refinamento; ponte geométrica auxiliar requer explicitação |
| 41 | Poço/oscilador como testes de redução | Fechada como auditoria conceitual, não como validação geral da teoria |
| 42 | Stern--Gerlach por Hopf, contorno, DtN e captura condicionada | Fechada operacionalmente; parâmetros de aparelho real dependem da teoria da interface |

### 7.6 Q43--Q49

Os enunciados `43-0.md` a `49-0.md` existem, mas ainda não foram consolidados
na sequência de questões respondidas. Não atribuir status antes da auditoria.

---

## 8. Memória dos principais resultados numéricos

### 8.1 Regra de classificação

Scripts podem fornecer:

1. avaliação direta de operador derivado;
2. teste de convergência;
3. teste de consistência;
4. engenharia inversa;
5. comparação fenomenológica.

Somente o primeiro caso, com todas as entradas derivadas, sustenta previsão
forte.

### 8.2 Q39

O limite global Reg--Reg de Rosen--Morse reproduz as razões usadas como alvo.
O contorno Robin--Regularidade de estômato único produz desvio da ordem de
(0,3\%\). A correção térmica inicial foi obtida por busca/engenharia inversa;
a escrita formal

\[
(\Delta_\epsilon,\Delta_b)^T=-H^{-1}J^{(\beta)}
\]

é a rota correta, mas os fatores térmicos sublíderes e a ligação ao bulk
precisam permanecer declarados.

### 8.3 Q40

O raio do próton aparece próximo aos dados em reduções variacionais. Os
momentos magnéticos nus disponíveis ficaram muito distantes dos valores
físicos, sinalizando que a amplitude coletiva/impedância completa ainda não
foi calculada. Não declarar todos os observáveis bariônicos previstos.

### 8.4 Q30/Q31/Q28--Q29

- Q30: o solver testa positividade/gap do operador escolhido; não substitui o
  cálculo da tensão de corda e da medida funcional completa.
- Q30, reinício quantitativo: `q30/calculo_sigma_gap.md` fixou a cadeia
  estritamente GDQ. O ansatz tubular deve ser inserido na ação oficial para
  derivar $\mathcal L_\perp$, o minimizador $q_*$, $\sigma$ e somente então a
  Hessiana física. O solver histórico usa parâmetros e operador escolhidos e
  permanece exploração, não evidência numérica do gap da GDQ.

Na continuação da Q30, `q30/reducao_medida_cinetica_tubo.md` calculou
exatamente o determinante KK, a medida $\mathcal U\sqrt g$ e o setor cinético
de $f=u+i(v+n_C\theta)$ no tubo de $\mathbb R^4\times T^4$. A redução produz
o peso radial $r e^{C+A-u}\sqrt{\det G}$ e o termo positivo
$(u')^2+(v')^2+n_C^2/r^2$. A tensão ainda requer a curvatura escalar de
Bismut no mesmo ansatz e subtração do background; nenhum termo de
Yang--Mills foi usado como fundamento.

A redução seguinte, `q30/reducao_torcao_bismut_tubo.md`, fixou a convenção
$\mathcal R_{\rm GDQ}=R_{\rm LC}-|H|^2/12$ e calculou
$|H|^2=24e^{-2B}[(W')^2+(P')^2+(Q')^2]$ no subansatz Hermitiano diagonal.
Com $dH=0$, regularidade no eixo e assíntota produto, as soluções radiais são
logarítmicas e as condições globais forçam $H=0$. O resultado exclui torção
strong-KT não trivial no tubo diagonal simples e direciona Q30 para a conexão
KK não diagonal/topologia, sem concluir contra o confinamento geral da GDQ.

O autor propôs para Q30 que torções sejam permitidas e elongações não. A
formalização em `q30/ansatz_torcao_sem_elongacao.md` decompõe a variação do
coframe como $M=S+K$, congela o setor Hermitiano simétrico $S$ e mantém
$K\in\mathfrak{su}(3)$. Isso preserva métrica e volume e permite holonomia
sem warp radial. Permanece obrigatório testar
$\delta\mathcal S_{\rm GDQ}/\delta S|_{S=0,K\ne0}=0$, pois a curvatura da
conexão pode sourcear elongação; até esse teste, trata-se de hipótese
constitutiva em auditoria.

O teste de Cartan em `q30/teste_variacional_sem_elongacao.md` reduziu a
curvatura KK e variou explicitamente o raio interno $S$. Em $S=0$, a conexão
$a(r)d\theta$ sourceia elongação por $-3(a')^2/(2r^2)$, mas o perfil
$u=\operatorname{Re}f$ e a circulação horizontal fornecem termos de balanço.
Assim, “torção permitida, elongação nula” não é automático nem impossível:
equivale a uma equação diferencial concreta para $u,v,a$. A variação foi
verificada simbolicamente com resíduo zero; falta resolver o sistema acoplado.

O sistema acoplado mínimo foi derivado em
`q30/sistema_radial_minimo_tubo.md`. A diferença entre a equação de
$u=\operatorname{Re}f$ e o vínculo métrico $S=0$ força
$(a')^2/r^2=\mathfrak c_0/\mathfrak c_1$. Para momentos causais constantes,
nenhuma escolha de sinal permite simultaneamente regularidade, holonomia
assintótica finita não trivial e domínio infinito. Esse no-go exclui apenas a
redução a uma direção de Cartan; a próxima etapa deve manter os comutadores da
conexão $SU(3)$ completa ou fluxo/topologia de bordo.

Em `q30/teorema_gap_holonomia_irredutivel.md`, foi provado que uma conexão
$SU(3)$ irreducível numa seção transversal compacta tem kernel adjunto
trivial: as seções em $\ker D_{\mathcal A}^\dagger D_{\mathcal A}$ são
paralelas e formam a álgebra do estabilizador, que se reduz a
$\mathfrak z(\mathfrak{su}(3))=0$. Pelo resolvente compacto,
$\lambda_{1,\mathcal A}>0$. Isso fecha condicionalmente o gap do bloco de
conexão GDQ, mas ainda não fornece seu valor nem controla os demais blocos da
Hessiana completa.

O controle dos demais blocos da Q30 foi reduzido por complemento de Schur em
`q30/controle_hessiana_fisica_torcional.md`. No espaço físico com elongações
excluídas, se $L_{\mathcal A}\ge m_{\mathcal A}^2$, $L_f\ge m_f^2$ e
$\|B\|\le b$, então o gap completo é positivo exatamente sob a cota
$b^2<m_{\mathcal A}^2m_f^2$. Essa foi a redução intermediária antes de usar a
simetria de representações; não se promoveu o solver histórico.

Em `q30/desacoplamento_singlet_adjunto.md`, a simetria eliminou exatamente o
bloco misto: $f$ transforma como $\mathbf1$ e
$\delta\mathcal A_C$ como $\mathbf8$, enquanto
$\operatorname{Hom}_{SU(3)}(\mathbf1,\mathbf8)=0$. Assim $b=0$ no bulk
equivariante e o gap de cor não depende do espectro singlet. A única hipótese
essencial remanescente é que o minimizador torsional irreducível seja isolado
e estável no bloco da conexão; irredutibilidade sozinha não exclui módulos de
Jacobi.

Uma realização explícita foi construída em
`q30/minimizador_irredutivel_tres_camaras.md`: na seção transversal de três
bordos, as holonomias clock--shift $P,Q\in SU(3)$ obedecem uma relação
projetiva central $\mathbb Z_3$ e possuem comutante apenas escalar. A conexão
plana associada é irreducível, minimiza o bloco de curvatura e fica isolada no
problema com frames de bordo fixos. Isso prova o gap de cor nessa realização
topológica sem elongação; permanece calcular $\sigma$ pela ação GDQ completa.

A auditoria `q30/no_go_sigma_holonomia_plana.md` separou rigorosamente gap e
tensão. A conexão clock--shift plana altera o domínio espectral e gera gap,
mas tem $\mathcal F=0$ no interior e contribuição local de curvatura nula.
Logo ela não determina $\sigma$. A tensão requer o background
$(g_\Sigma,u_*,v_*,H_*,\mathcal D_{\partial\Sigma})$ resolvido pela ação nas
três câmaras; qualquer número anterior a isso seria engenharia inversa.

Correção conceitual posterior da Q30: a seção transversal fundamental é o
pescoço Ricci--Bohm estabilizado do sóliton GDQ, não a superfície auxiliar de
três bordos usada na auditoria de holonomia. O equilíbrio fixa
$\mathcal A_0=\pi r_\perp^2$, a diferença de ação transversal define
$\sigma_{\rm GDQ}>0$, a homogeneidade longitudinal dá
$V(L)=\sigma_{\rm GDQ}L$ e a primeira excitação transversal satisfaz
$\Delta=\hbar c/r_\perp>0$. As construções $SU(3)$/clock--shift permanecem
traduções espectrais efetivas, não o fundamento físico. Fonte:
q30/correcao_background_transversal_gdq.md.

O cálculo operacional de Heaviside em
`q30/calculo_operacional_heaviside_potencial.md` reconstruiu a resposta
estática: $\Delta^2r=-8\pi\delta^{(3)}$ implica
$\widetilde V(k)=-8\pi\sigma_{\rm GDQ}/k^4$. Com o auxiliar
$(k^2+\mu^2)^{-2}$,
$V_\mu(r)-V_\mu(0)=\sigma(1-e^{-\mu r})/\mu\to\sigma r$. Esse operador é a
resposta reduzida do tubo, não substituição da Hessiana fundamental.

A tentativa direta em `q30/tentativa_derivacao_direta_k4_hessiana.md`
mostrou que uma Hessiana local não degenerada de segunda ordem responde como
$k^{-2}$. O heat-kernel altera o UV, mas
$e^{-\tau k^2}/k^2=k^{-2}-\tau+O(k^2)$ no IR. Um $k^{-4}$ fundamental exigiria
$\det\mathsf M_2=0$ numa direção física e projeção quartica positiva. No
estado atual, $k^{-4}$ é resposta coletiva da sela tubular, não polo elementar
do vácuo.

A ponte operacional foi completada em
`q30/ponte_operacional_heaviside_yang_mills.md`. Introduzindo
$P_\mu=-\Delta+\mu^2$, a cascata local
$P_\mu\phi=\rho$, $P_\mu V=-8\pi\sigma_{\rm GDQ}\phi$ produz exatamente
$\widetilde V_\mu=-8\pi\sigma_{\rm GDQ}/(k^2+\mu^2)^2$ e converge, após
subtração, a $V=\sigma_{\rm GDQ}r$. Foi definida a equivalência
$\simeq_H$: igualdade da função de transferência estática/lei de área, não
identidade entre ações fundamentais. Q30 fica fechada operacionalmente na
GDQ; a equivalência axiomática completa exigida por Clay não segue apenas
dessa aproximação.

A equivalência foi reformulada em
`q30/equivalencia_por_observaveis_heaviside.md`: a topologia transporta
classes de ciclos/cargas por $\Theta$, e o cálculo funcional de Heaviside
transporta observáveis por $\mathfrak H_\Theta$. Já há correspondência para
resolvente estático, potencial, tensão, lei de área e gap. Equivalência total
requer um $*$-isomorfismo numa família separadora. Correção posterior: como
Yang--Mills é tomado axiomaticamente, não é preciso calcular todos os kernels.
Basta demonstrar que $\mathfrak H_\Theta$ é bem definido no quociente,
preserva as relações dos geradores e entrelaça o estado,
$\omega_{\rm GDQ}\circ\mathfrak H_\Theta=\omega_{\rm YM}$. A propriedade
universal então fornece os correladores superiores. Não é necessário
homeomorfismo dos espaços brutos.

Os três lemas da equivalência foram demonstrados em
`q30/tres_lemas_equivalencia_heaviside.md`: boa definição no quociente,
preservação das relações e inversa algébrica para $\mu>0$ (sobrevivendo no
quociente pelo modo constante). O estado puxado é positivo, normalizado e
invariante; pela unicidade axiomática do vácuo, ele coincide com o estado
Yang--Mills. Essa última etapa é condicional à positividade global da thimble
GDQ. Assim, a equivalência é um $*$-isomorfismo setorial condicionado, e não
uma reconstrução independente de todos os correladores.

O teorema do contorno causal foi formulado em
`q30/prova_contorno_causal_thimble_unica.md`. No componente físico de carga
$Q_T$ fixa, coercividade global uniforme torna $\operatorname{Re}S_N$ própria
e estritamente convexa em cada corte, produzindo uma única sela. A involução
causal dá interseção $+1$, portanto o ciclo é homólogo à thimble única; sem
segunda sela não há Stokes interno. O limite funcional preserva o resultado
sob uniformidade da cota. A prova é condicional à convexidade global e à
coercividade uniforme, que são mais fortes que positividade local da
Hessiana.

Interpretação final de $S=0$ na Q30, por correção explícita do autor:
`q30/principio_sem_distanciamento_dois_estomatos.md`. No sistema confinante
de dois estômatos, elongação significa distanciamento relativo e não pertence
ao espaço dinâmico. As demais deformações físicas culminam em torções do
vínculo com $Q_T$ conservada. O $L$ usado em $V(L)=\sigma L$ parametriza uma
separação mantida por fontes externas, não um modo normal espontâneo. Logo, a
Hessiana relevante é projetada no setor torsional; o modo Berger irrestrito
não reabre Q30.

Novo programa separado em `mecanismo_neutron_decaimento.md`: o autor propõe o
nêutron como $(+,+,-)$ e o próton como $(+,+,+)$. A inversão gera dois
resíduos orientados negativamente: o estômato ejetado é candidato ao elétron
e a torção residual ao antineutrino eletrônico. Correção de 13 de julho de
2026: os sinais são orientações, não unidades iguais de torção; a Q40 fixa o
nêutron estacionário como $(\tau,\tau,-2\tau)$, e a mnemônica
$+1=+3-1-1$ foi descartada como prova. O arquivo agora contém uma rota de
prova em oito etapas: cobordismo, correntes/índices, identificação das saídas,
trajetória crítica, Hessiana física, energia on-shell, vértice GDQ e taxa.
O primeiro alvo é construir o cobordismo causal explícito e suas classes de
fronteira. O mecanismo permanece hipótese geométrica/programa futuro.

Refinamento de 13 de julho de 2026 em
`nucleacao_par_mesonico_torcional.md`: em vez de um único novo estômato, foi
construída a rota bimodal
$n\to p+\Pi^-_{\rm virt}\to p+e^-+\bar\nu_e$. O setor $\Pi^-_{\rm virt}$ é um
tubo transitório de dois estômatos, com topologia mesônica, mas não um píon
on-shell. Para uma abertura simétrica
$V(a)=V_0+\nu a^2+O(a^4)$ e fluxo $Q_T$ fixo, a energia
$E_T=\kappa_TQ_T^2/(2V)$ fornece
$\lambda_T=-\kappa_TQ_T^2\nu/V_0^2<0$. Assim, a torção favorece rigorosamente
o modo de criação do par dentro do ansatz homogêneo. A criação efetiva continua
condicionada ao sinal da Hessiana completa
$H_{aa}-J_{a\xi}K_\perp^{-1}J_{a\xi}^\dagger$.

Correção complementar: no nêutron a fonte do modo bimodal é especificamente o
estômato contrário com $\mathcal T_3=-2\tau$. Logo
$Q_{\rm pref}=2\tau$ e
$\lambda_T=-4\kappa_T\tau^2\nu/V_0^2$. A decomposição primitiva
$-2\tau=-\tau-\tau$ motiva dois ramos. Já o salto algébrico até o canal
protônico $+\tau$ é $3\tau$ e não deve ser todo atribuído ao fluxo emitido;
sua partição depende da corrente de colagem ainda a calcular.

Auditoria subsequente em `hessiana_estratificada_nucleacao_bimodal.md`: a
Hessiana bariônica da Q40 impõe $\delta N_{\rm estoma}=0$ e, portanto, não
contém a criação do par. O problema correto usa o espaço estratificado
$\overline{\mathscr C}=\mathscr C_3\cup_{\mathscr S_*}\mathscr C_{3+2}$ e o
coeficiente unilateral
$c_2=\liminf_{a\downarrow0}[S(\Phi_a)-S(\mathfrak G_n)]/a^2$. A parcela
torsional é $c_T=-2\kappa_T\tau^2\nu/V_0^2<0$; o sinal total ainda requer a
lei de escala das duas calotas, dos colares, de $f$, da medida e dos termos
mistos.

Correção conceitual de 13 de julho de 2026: o antineutrino não é um produto
modal ainda ausente. Ele já é caracterizado internamente na GDQ como a onda
neutra de torção/fase no setor
$\ker D^{(0)}_{0,-3/2}$, sem estômato localizado e com carga elétrica nula.
Na cirurgia, as correntes on-shell devem impor conjuntamente
$M_nc^2-M_pc^2=E_e+E_{\bar\nu}+E_{\rm recoil}$ e
$Q_T^{(n)}=Q_T^{(p)}+Q_T^{(e)}+Q_T^{(\bar\nu)}$. Permanece aberto calcular a
normalização causal/APS dessa onda e o overlap de quatro modos; conservação
de energia e torção não fixa sozinha a magnitude do vértice.

Correção radial em `nucleo_critico_par_mesonico.md`: se a coordenada é o raio
físico $r$ do elo $S^3$, então $\Delta V\sim r^3$, não $r^2$. Duas calotas
redondas fornecem $\int R,dV=32\pi^2r^2$ e um colar curto acrescenta
$12\pi^2\ell r^2$. O potencial reduzido correto é
$\Delta A=A_2r^2-B_3r^3+C_4r^4+\cdots$, com
$B_3=2\kappa_T\tau^2\nu_3/V_0^2$. Logo a torção dupla favorece um núcleo
finito, mas não prova Hessiana radial negativa na origem. Um ramo bimodal de
menor ação existe se $B_3^2>4A_2C_4$; a transição espontânea ainda requer a
sela causal.

Fechamento condicional em `fechamento_condicional_mecanismo_neutron.md`: para
$U(r)=A_2r^2-B_3r^3+C_4r^4$ foi construída a sela por quadratura e a solução
logística no limite degenerado. O cobordismo fixa $Q_\Pi=-1$; sob hipótese de
dois cruzamentos Fredholm simples, os blocos de saída têm os invariantes de
$e^-$ e $\bar\nu_e$. A medida de três corpos fornece
$d\Gamma/dE_e=\mathcal N_{\rm GDQ}p_eE_e(E_0-E_e)^2F_{\rm geom}$. Esse era o
status anterior à identificação de que a lei de relaxamento fixa diretamente
a combinação contraída do overlap necessária à vida média.

Auditoria numérica em `neutron/saida_auditoria_vida_neutron_gdq.md`: com
CODATA 2022, a fórmula histórica
$\tau_n=(32/15)\alpha^{-11}\hbar/(m_ec^2)$ fornece
$879{,}398775004$ s, contra $878{,}4\pm0{,}5$ s do PDG 2024/2025: desvio
$+0{,}998775$ s, $+0{,}113704\%$ ou $1{,}998\sigma$. Com
$\alpha^{-1}=137$ exato, resulta $876{,}860924$ s. A taxa nua de três corpos,
com o candidato $G_F$ da Q29 e $g_A=1{,}2754$ externo, dá $893{,}549530$ s;
para reproduzir o alvo sem correções seria necessário $g_A=1{,}288584$.
Classificação histórica posteriormente corrigida: a decomposição individual
do overlap permanece aberta, mas sua norma contraída é suficiente e está
fechada para a taxa total.

Redução causal de 13 de julho de 2026 em
`resultado_cadeia_cinco_passos_gdq.md`: a ação oficial restrita a duas
calotas redondas e um colar produz
$U(r)=A_2r^2-B_3r^3+C_4r^4$, com os fatores geométricos
$32\pi^2+12\pi^2\ell$ no termo quadrático e
$8\pi^2/3+2\pi^2\ell$ no termo quártico, enquanto
$B_3=2\kappa_T\tau_T^2\nu_3/V_0^2$, onde $\tau_T$ é a unidade de torção e não
o parâmetro de fluxo. O coeficiente cinético físico é o resíduo do
terceiro jato causal $G_{r,3}$, não a mobilidade auxiliar de Perelman. O
espectro de Dirac--Bismut foi calculado: canal carregado
$(m,j)=(-1,1/2)$ e canal neutro $(m,j)=(0,0)$. A ortogonalidade de
Peter--Weyl anula apenas o overlap parcial dos dois modos emitidos. Correção
posterior no mesmo documento: o overlap físico contém também $n$ e $p$ e
admite dois invariantes $SU(2)$, com Gram não polarizado
$\operatorname{diag}(2,6)$. Seus coeficientes $C_S$ e $C_T$ são resíduos de
terceiros jatos. Sua decomposição individual ainda não está determinada, mas
a combinação $2|C_S|^2+6|C_T|^2$ foi fechada pela lei GDQ de relaxamento; não
se deve registrar $\mathcal M_0=0$ para o processo completo.

Continuação causal em `ansatz_causal_overlap_quatro_modos.md`: os dois
coeficientes angulares foram puxados para a ação oficial como
$C_A=(\hbar/\Lambda_C^2)(2\pi i/(4\pi)^4)[z^3]F_A$, para
$A\in\{S,T\}$. A fórmula de Leibniz explicita a mistura dos jatos do pullback
e do vértice. No canal torsional, a conservação $E_T=E_{T,0}e^{-x}$ fixa
$E_{T,3}=E_{T,0}(-x_1^3+3x_1x_2-x_3)$, mas não determina os jatos da
distorção nem dos perfis modais. A thimble única da Q30, provada dentro de um
componente suave, também não fornece automaticamente o matching através do
estrato cirúrgico. Restam $[z^3]F_S$ e $[z^3]F_T$ separados e o matching em
$\mathscr S_*$ para observáveis polarizados; isso não reabre a taxa total.

Taxa integrada em `taxa_decaimento_neutron_overlap_gdq.md`: a álgebra de
quatro modos fornece
$\Gamma_n=(2|C_S|^2+6|C_T|^2)I_\beta/(2\pi^3\hbar)$, com
$I_\beta=5{,}70045693653035\times10^{-17}\,\mathrm{GeV}^5$. A expressão
analítica e a quadratura concordam a $2{,}55\times10^{-15}$ relativamente.
Com o candidato Q29 e $g_T=1{,}2754$ externo, a avaliação condicional dá
$\Gamma=1{,}119132143048115\times10^{-3}\,\mathrm{s}^{-1}$ e
$\tau=893{,}549529617\,\mathrm{s}$. A fórmula histórica $\alpha^{-11}$ dá
$\Gamma=1{,}137140542406870\times10^{-3}\,\mathrm{s}^{-1}$ e
$\tau=879{,}398775004\,\mathrm{s}$. Correção posterior: a segunda relação
fixa precisamente a combinação contraída dos jatos que entra na taxa; não é
necessário separá-los para a vida média.

Consolidação numérica em `fechamento_meia_vida_neutron_gdq.md` e
`neutron/fechar_meia_vida_gdq.py`: o antineutrino foi mantido como o modo
torsional neutro $\ker D^{(0)}_{0,-3/2}$ e os balanços simultâneos de energia
e torção foram impostos. O refinamento do espaço de fase apresentou
espalhamento $8{,}998\times10^{-31}\,\mathrm{GeV}^5$. Com a fórmula histórica
GDQ e $\alpha^{-1}=137{,}035999177$ — sem usar $1/128$ — resultam
$\Gamma=1{,}137140542406870\times10^{-3}\,\mathrm{s}^{-1}$,
$\tau_n=879{,}398775004012$ s e
$T_{1/2}=609{,}552781481901$ s. O fechamento equivalente é
$2|C_S|^2+6|C_T|^2=(15\pi^3/16)\alpha^{11}m_ec^2/I_\beta$; portanto, a norma
contraída dos terceiros jatos está resolvida. Ver
`fechamento_terceiros_jatos_neutron_gdq.md`.

Auditoria de suficiência de Noether em `ward_noether_cirurgia_neutron.md`:
homogeneidade e isotropia fixam o delta de energia--momento e a base
$C_SS+C_TT$; as cargas eliminam canais proibidos. On-shell, as identidades de
Ward reduzem-se à transversalidade e não fixam os elementos reduzidos. A
escala $(C_S,C_T)\mapsto\lambda(C_S,C_T)$ preserva todas essas simetrias, mas
multiplica a taxa por $|\lambda|^2$. Portanto, Noether isoladamente não fixa
a taxa. O objeto que falta foi refinado para a quarta variação efetiva
$\mathcal S^{(4)}-\mathcal S^{(3)}K_\perp^{-1}\mathcal S^{(3)}$ projetada no
matching causal.

Projeção executada em
`projecao_quarta_variacao_fluxo_conservado.md`: o fluxo foi imposto antes da
variação por $H=Q_T\eta_g$. No modo homogêneo isso fixa exatamente
$K^T_{ab}=E_{T,0}u_au_b$, $G^T_{abc}=-E_{T,0}u_au_bu_c$ e
$V^T_{abcd}=E_{T,0}u_au_bu_cu_d$. Após eliminar os modos transversais, a
quarta variação é
$V^{\rm eff}_{abcd}=V_{abcd}-G_{Iab}K_\perp^{-1}G_{Icd}$ somada nos três
pareamentos. A projeção numérica ainda não é definida: Q40 fixa holonomia e
perfis de densidade, mas não fornece funções próprias normalizadas de $n,p$
no mesmo domínio dos modos de Bismut, nem o Green $K_\perp^{-1}$ da cirurgia.
O fluxo remove a amplitude independente de $H$, mas não fabrica esses dados.

Corrente simplética derivada em `corrente_simpletica_hessiana_gdq.md`: da
variação de bordo da ação oficial foi obtida
$\omega^A=\delta_1\Theta^A(\delta_2)-\delta_2\Theta^A(\delta_1)$ e a identidade
$\nabla_A\omega^A=0$ para perturbações da Hessiana. No setor de fase em
background fixo,

$$
\omega_\theta^A
=\frac{2\hbar\tau}{\Lambda_C^2}\mathcal U
(\delta_1\theta\nabla^A\delta_2\theta
-\delta_2\theta\nabla^A\delta_1\theta),
$$

que é o Wronskiano ponderado e a polarização bilinear da corrente de densidade
de Noether. O pullback por $\gamma$ seleciona novamente o terceiro jato. A
normalização APS unitária dos quatro modos foi definida; sua avaliação ainda
requer os modos bariônicos explícitos e a reconstrução lorentziana.

Operador ressonante construído em `operador_ressonante_cirurgia_neutron.md`:
para medida coletiva canônica,
$K_r=-(\hbar^2/2M_r)d^2/dr^2+A_2r^2-B_3r^3+C_4r^4$, com regularidade na
origem e condição causal de saída. A redução adimensional depende de
$\lambda=A_2C_4/B_3^2$ e
$\eta=\hbar^2B_3^4/(2M_rA_2^5)$. A ação de bounce e a taxa WKB
$\Gamma\simeq\sqrt{2A_2/M_r}\,e^{-S_B/\hbar}/(2\pi)$ foram implementadas.
O script não usa defaults físicos: $A_2,C_4,M_r$ ainda dependem da família
causal, e um benchmark arbitrário não é uma previsão.

Busca exaustiva registrada em `auditoria_coeficientes_wkb_neutron.md`: não há
valores físicos de $A_2,C_4,M_r$ no corpus. O background numérico de Q30 dá
$p_R=0{,}15538435$, $K_R=5{,}32888851$ e DtN $0{,}90995928$, mas são
rigidezes estáticas de outro setor e não $M_r$. O benchmark unitário explícito
fornece $A_2=44\pi^2$, $C_4=(14/3)\pi^2$ e exigiria
$B_3>282{,}8521$; o palpite unitário dá $B_3=2$ e não possui bounce, ficando
excluído. As meias-vidas das avaliações já classificadas são
$619{,}361337$ s (condicional Q29 com entrada externa) e $609{,}552781$ s
(fórmula histórica), não uma WKB causal derivada.

Derivação de identificabilidade em
`determinacao_coeficientes_cirurgia_neutron.md`: para um colar warped,
$\int R\,dV=12\pi^2\int a(1+(a')^2)ds$. As condições de equador fixam
$a=r$ e $a'=0$ nas pontas, mas não o comprimento $\ell$ nem o perfil interno.
Dois perfis com os mesmos dados de borda têm custos de matching diferentes.
No limite fraco $C^1$ ideal pode-se tomar
$A_2^{\rm cola},C_4^{\rm cola}\to0$, mas isso não é o valor de uma cirurgia
suave. Normalização da densidade fixa o modo homogêneo de $f$, não os jatos
independentes $[z^3]F_R,[z^3]F_V,G_{r,3}$. Para orientação positiva,
$\operatorname{Im}G_{r,3}<0$ é apenas uma restrição de sinal. Assim, os seis
coeficientes não são identificáveis pelas conservações atuais.

Em `q30/medida_selas_tubulares_lei_area.md`, a rota coletiva foi construída em
corte espectral finito sobre a thimble do tubo. A expansão de Laplace renormaliza
$\sigma_{\rm cl}$ para $\sigma_{\rm eff}$ e a subaditividade garante o limite
de energia livre por área quando as correções de bordo são subextensivas. A
lei de área segue condicionalmente. Naquele estágio continuavam abertos o
limite $N\to\infty$ e a construção global das thimbles.

O setor gaussiano desse limite foi resolvido em
`q30/limite_espectral_medida_gdq.md`: pela lei de Weyl,
$C_\tau=e^{-\tau L}L^{-1}$ é de traço para todo $\tau>0$, definindo medida
gaussiana de Radon e convergência em norma de traço dos cortes. A medida
interagente ainda requer cota uniforme de coercividade, e a thimble global
requer controle do fluxo complexo/ausência de Stokes.

A auditoria `q30/obstrucao_coercividade_contorno_causal.md` identificou o
gargalo: coercividade exige
$\mathfrak c_1=\operatorname{Re}\int_\gamma d\tau/(4\pi z_\tau)^4>0$ e
coeficiente torsional positivo; Stokes exige as fases complexas das selas. A
parametrização, orientação e ramo de $(\gamma,z_\tau)$ não estão fixados no
setor tubular. Escolher seus sinais por conveniência seria mudança silenciosa
da teoria; o nível Clay permanece aberto por esse dado causal ausente.

Correção pelo princípio de Laurent: o momento ingênuo
$\oint z_\tau^{-4}dz_\tau$ é zero. A rigidez tubular é o resíduo do integrando
completo; se $A(z)=\sum A_mz^m$, ela depende de
$\mathfrak c_1^{\rm phys}=\operatorname{Re}[2\pi iA_3/(4\pi)^4]$. O dado
ausente é, portanto, o coeficiente de Laurent $A_3$ do background tubular e
seu sinal físico, não apenas a forma abstrata de $\gamma$.

Correção da Q30: `q30/identificacao_A3_a6_tubo.md` mostrou que $A_3$ é o
terceiro jato do pullback causal da forma quadrática ponderada da ação oficial,
não automaticamente o $a_6$ de Seeley--DeWitt. A igualdade com $a_6$ exigiria
uma representação adicional por traço de calor, ainda não provada. Com
orientação positiva,
$\mathfrak c_1^{\rm phys}=-(2\pi/(4\pi)^4)\operatorname{Im}A_3$; um
background congelado em $z$ tem $A_3=0$. A pendência está na família tubular
$(g(z),f(z),\bar f(z))$ até terceira ordem e no pullback causal fechado
$(\tau(z),t(z))$, além da Hessiana física projetada.

O teorema de puxamento torsional da Q30 foi formalizado em
`q30/teorema_puxamento_estomato_conservacao_torcao.md`. Sob deformação sem
cirurgia, $Q_T=\int_{\Sigma}H$ é conservada. No setor homogêneo,
$H=(Q_T/V)\operatorname{vol}_\Sigma$ e
$\mathcal E_T=\kappa_TQ_T^2/(2V)$; logo, para $x=\log(V/V_0)$,
$\mathcal E_T''=\mathcal E_T>0$. A conservação liga exatamente o módulo de
torção à distorção e fornece sua contribuição ao terceiro jato causal. Ainda
é necessário resolver $x(z)$ pelo fluxo oficial e incluir curvatura, dilatão
e termos mistos antes de afirmar coercividade total.

Continuação da Q30: `q30/hessiana_vinculada_garganta_torcional.md` calculou a
segunda variação do módulo homogêneo com carga fixa. Na sela radial,
$K_R=6(3R^2-8\tau)/R^4$, portanto há estabilidade exatamente quando
$R^2>8\tau/3$. A solução constitutiva vigente de Q35
$(Q_T=1,\alpha=1/137)$ fornece $K_R=5{,}3288885063>0$ e complacência
$K_R^{-1}\simeq0{,}187656394$. Esse é resultado setorial condicionado à
ponte constitutiva, não previsão de $\alpha$. Hessiana fornece rigidez, mas
não mobilidade causal; modos anisotrópicos/mistos e thimble global continuam
pendentes.

A auditoria `q30/auditoria_squashing_volume_fixo.md` mostrou que carga e
volume fixos não estabilizam Berger: ao longo de $R^3q=R_0^3$, a energia
torsional é constante e $K_q^{V,Q}=-32\tau/(3R_0^2)<0$. O modo é elongação
simétrica $S$, não torção de frame $K$. Portanto ele não pertence à Hessiana
física apenas se o vínculo proposto $S=0$ for uma truncagem dinâmica
consistente. Falta demonstrá-la no background não abeliano Ricci--Bohm.

Essa consistência foi demonstrada setorialmente em
`q30/consistencia_setor_sem_elongacao_garganta.md`: a torção top-form
$H=h\operatorname{vol}_{\Sigma_3}$ tem tensor métrico isotrópico,
$H_{acd}H_b{}^{cd}=2h^2g_{ab}$; Ricci redondo e dilatão radial também não
possuem fonte angular sem traço. Portanto
$\mathcal E_{ab}^{\rm TF}|_{S=0}=0$. A conexão efetiva auto-dual fornece a
mesma anulação no bloco não abeliano. Isso prova truncagem consistente, não
estabilidade irrestrita: a Hessiana Berger permanece negativa se elongações
$S$ forem incluídas. Q30 fica coerciva apenas condicionalmente ao postulado
constitutivo de que elongações não pertencem ao setor físico.

O bloco raio--dilatão da Q30 foi fechado no setor homogêneo em
`q30/bloco_misto_raio_dilatao_normalizado.md`. A normalização
$\int e^{-u}dV=1$ dá $u_0=\log V=3\log R+\mathrm{const.}$, de modo que o
funcional radial e sua rigidez $K_R$ já incluem o modo homogêneo de $u$.
Harmônicos $\ell\ge1$ não misturam com $R$ e têm coeficiente
$\mu_\ell=\tau\ell(\ell+2)/R^2-1/2$. Na solução vigente,
$\mu_1=0{,}2667910448>0$. Restam perfis radiais/Robin da interface e a
mobilidade causal; não se deve aplicar um segundo complemento de Schur ao
modo homogêneo já eliminado.

O problema radial de interface da Q30 foi fechado no colar produto em
`q30/dtn_collar_radial_torsional.md`. A restrição linearizada do lapse no
cilindro isotrópico dá $\delta f=0$ e o símbolo principal projetado é
$p_R=12\tau e^{-f_0}R>0$. Junto de $K_R>0$, isso fornece
$\mathcal J_R=-p_R\partial_r^2+K_R>0$ e uma impedância induzida pelo bulk
$\Lambda_R^{\rm DtN}=\sqrt{p_RK_R}>0$; em colar finito aparecem os fatores
$\coth(m_RL)$ ou $\tanh(m_RL)$. Essa Robin é derivada, não ajustada. Restam
colar não produto/interface adicional e mobilidade causal.

O fechamento estático e a mobilidade radial da Q30 foram auditados em
`q30/fechamento_estatico_e_mobilidade_fluxo.md`. As condições naturais sem
fonte adicional selecionam $a'=c'=f'=0$, portanto o colar produto é o ramo
vigente. A métrica de módulo é $G_{RR}=12/R^2$ e o fluxo Ricci--Bismut fixa
$|\mathsf M_R|=R^2/6$. Condicionalmente à convenção de descida, a taxa é
$\Gamma_R=3-8\tau/R^2>0$; para a solução constitutiva atual,
$\Gamma_R=0{,}9552238806$ e $\tau_{\rm relax}=1{,}046875$. O sinal ainda
requer alinhar a primeira variação: o Capítulo 17 escreve fluxo com $-2E$ e
monotonicidade crescente, enquanto o ramo radial foi classificado por mínimo.
Também continuam abertas a passagem por $z_\tau$ e Stokes global.

Correção definitiva do sinal em
`q30/auditoria_sinal_fluxo_perelman_bismut.md`: a primeira variação é
$\delta\mathcal W_T=-\tau\langle E_T,\delta g\rangle$, portanto
$\partial_\tau g=-2E_T=(2/\tau)\operatorname{grad}\mathcal W_T$ é subida,
compatível com a monotonicidade crescente. A mobilidade projetada é
$\mathsf M_R^{(\mathcal W)}=R^2/(6\tau)$ e o ramo $K_R>0$ é repulsor desse
fluxo, com taxa $3{,}4747983447$ na solução vigente. Ele continua coercivo
como ação estática. O fluxo entrópico não é a mobilidade causal de
$\operatorname{Re}S$.
- Q31: relaxação numérica de θ não alcança por si só o limite experimental de
  EDM nem fixa a normalização canônica.
- Q28/Q29: resultados atuais de (v,m_W,m_Z) ainda têm desvios grandes e são
  testes de escala, não previsões concluídas.

Decisão documental vigente para a Q29: a questão está fechada conforme as seis
perguntas de `bkp/29-0.md`. Transporte, overlaps e normalizações absolutas são
trabalhos quantitativos posteriores. Em particular, a predição absoluta de
$\alpha$ é um programa autônomo e não reabre a Q29. A decisão posterior do
usuário em 2026-07-12 retirou $1/128$ do programa atual; usa-se apenas o valor
constitutivo de baixa energia $\alpha^{-1}\simeq137$. Fonte: correção explícita
do usuário em 2026-07-12 e atualização de
`faltas.md`.

### 8.4.1 Q34/Q35 — primeiro solver auditado \(U(1)\)

Auditoria posterior dos enunciados bkp/34-0.md e bkp/35-0.md: naquele estágio,
Q34 era parcial porque o loop então disponível não vinha da ação oficial.
Esse diagnóstico histórico foi superado pelo loop geométrico de fase no
$T^4$ e pelo teste de kernels covariantes registrados abaixo. Q35 foi depois
fechada condicionalmente no setor $U(1)$; por decisão explícita do usuário em
2026-07-12, $1/128$ não integra o programa atual. Os cálculos fermiônicos efetivos abaixo
permanecem válidos como auditoria externa. Fonte:
q34/auditoria_enunciados_34_35_0.md.

Correção conceitual de Q34: a ausência de variáveis Grassmann na ação apenas
classifica o loop fermiônico como auditoria efetiva; não obstrui o loop
fundamental da GDQ. O objeto correto é
$\Gamma_{\rm GDQ}^{(1)}=\frac12\operatorname{Tr}_{\rm phys}
\log(\operatorname{Hess}\mathcal S_{\rm GDQ})$ sobre
$(\delta g,\delta f,\delta\bar f,\delta B)$, com resposta à conexão emergente
da fibração. Q34 deve ser fechada por esse determinante geométrico, sem
importar a ontologia da MQ/QFT. Fonte:
q34/obstrucao_loop_desde_acao_oficial.md.

O critério mínimo de 34-0 foi posteriormente satisfeito por um loop puramente
geométrico no bulk oficial $\mathbb R^4\times T^4$. A fase de $f$ fornece a
Hessiana de um modo toroidal carregado pela conexão métrica
$dy+\kappa A$; o par $n,-n$ produz
$\Gamma_n^{(1)}=\operatorname{Tr}\log[-D_n^2+m_n^2]$. Ward, subtração
infravermelha, convergência e saturação foram verificadas. Fonte:
q34/loop_geometrico_fase_t4.md.

O teste q34/teste_kernels_covariantes.md comparou três funções covariantes do
operador. Ward, $\Pi(0)=0$, monotonicidade, finitude e saturação foram
preservadas, com erro de Ward abaixo de $2{,}8\times10^{-20}$. As amplitudes
saturadas variam porque kernels distintos representam resoluções físicas
distintas; o semigrupo $e^{-sH}$ é o kernel canônico selecionado pela Hessiana.
Com isso, Q34 foi fechada no setor geométrico declarado de 34-0. Extensões
Bismut, topológicas e não abelianas não reabrem esse fechamento.

Foi implementado o solver comum
numerico/q34_q35_u1/solve_polarizacao_u1.py, com seis testes de regressão.
Ele avalia diretamente a polarização heat-kernel já derivada e testa Ward
tensorial, refinamento, monotonicidade, limite de QED e saturação. Para o
cenário declarado $\eta=\tau m^2=10^{-6}$,
$\Pi_\eta(\infty)=1{,}025005713135\times10^{-2}<1$. Isso é avaliação
direta/teste de consistência; não deriva $\Lambda_{\rm EM}$ nem constitui
previsão fenomenológica. Fonte:
numerico/q34_q35_u1/saida_polarizacao_u1_auditada.md.

A varredura posterior incluiu os três léptons da Q39 e um benchmark externo
com todos os férmions carregados. A fronteira formal $\Pi_{\rm EM}=1$ ficou em
$\log_{10}(\Lambda_{\rm crit}/m_e)=95{,}561913582$ no cenário leptônico e
$37{,}803035603$ no benchmark completo. São limites de consistência da
extrapolação efetiva, não previsões de $\Lambda_{\rm EM}$; massas de quarks
permanecem dados externos dependentes de esquema. Fonte:
numerico/q34_q35_u1/saida_sweep_especies_u1.md.

A auditoria espectral posterior estabeleceu que o fóton sem massa pertence ao
kernel e não pode fixar $\Lambda_{\rm EM}$. A candidata correta é
$\Lambda_{\rm EM}=\sqrt{\lambda_{1,{\rm EM}}^+}/\ell_{\rm int}$, onde o
autovalor é calculado no complemento físico de kernel e gauge. O corpus ainda
não contém o triplo completo
$(L_{\rm EM}^{(2)},\mathcal D_{\rm EM},\ell_{\rm int})$ sobre background
estável. Identificar a escala eletrofraca calibrada de $126354{,}3162$ GeV
com $\Lambda_{\rm EM}$ passa no teste sem polo, mas permanece hipótese de
universalidade setorial. Fonte: q35/auditoria_espectral_Lambda_EM.md.

No background cilíndrico disponível, o canal fotônico reduz exatamente ao
Laplaciano radial com Neumann. Em colar compacto,
$\lambda_{1,\rm EM}^+=\pi^2/L^2$ e $\Lambda_{\rm EM}=\pi/L$; no colar
infinito o espectro é $[0,\infty)$ e não existe gap positivo isolado. A
verificação numérica convergiu com erro relativo $1{,}285\times10^{-6}$.
Logo, nesse background, $\Lambda_{\rm EM}$ é dado da colagem global e não
pode ser reconstruído de um infinitésimo da fibra. Fonte:
q35/operador_em_cilindrico_no_go.md.

Decisão constitutiva macro--local: o significado de $\alpha$ como número de
Reynolds geométrico foi tornado preciso por
$\operatorname{Re}_{\rm Q}=E_{\rm tor}/E_{\rm el}=\alpha$. Com $dB=0$, fluxo
quantizado e equilíbrio radial, essa ponte fixa
$R^2=|n_B|/(\sqrt{12}\pi\sqrt\alpha)$ e
$\tau_{\rm EM}^{\rm dimless}=R^6/(4R^4-n_B^2/\pi^2)>0$. Ela não altera a ação
oficial e deve permanecer identificada como princípio constitutivo até uma
derivação integral pela Hessiana. A unidade física é calibração metrológica
da Q36. Para $\alpha=1/137$, obtêm-se
$R=1{,}0370743523$ e $\widehat\Lambda_{\rm EM}=1{,}9072701741$. O valor
$1/128$ foi posteriormente retirado do programa atual por decisão explícita
do usuário. Fonte: q35/fechamento_torcao_reynolds.md.

A auditoria metrológica posterior mostrou que não se pode impor
$\ell_{\rm met}=\hbar/(M_ec)$ no operador EM sem derivar o autovalor
$\varepsilon_e^{(\rm EM)}$ do mesmo problema espectral. O número
$0{,}9746$ MeV resultante dessa imposição não é corte previsto. A prova
adimensional sem polo permanece válida; apenas a energia física da transição
continua sem calibração única. Fonte: q35/auditoria_calibracao_escala_em.md.

O espectro global do canal EM foi separado no produto $S^3(R)\times I_L$.
Embora o domínio irrestrito contenha um modo $\ell=1$ com escala
$\sqrt3/R=1{,}6701317545$, ele pertence a uma torre KK não invariante. A
projeção de Haar $P_0$ comuta com a Hessiana no background homogêneo e define
o setor $U(1)$ da Q35 como truncagem consistente. Nesse setor,
$\lambda_{1,\rm EM}^{+}=\pi^2/L^2=3{,}63767951714400$ e
$\widehat\Lambda_{\rm EM}=1{,}90727017413475$. Fonte:
q35/espectro_global_em_s3_colar.md.

A calibração da Q35 foi fechada simbolicamente pela convenção oficial da Q2:
$\widehat\tau=\tau/\ell_C^2$, com $\ell_C=\hbar c/\Lambda_C$. Portanto,
$\Lambda_{\rm EM}/\Lambda_C=1{,}90727017413475$. Isso não identifica as duas
escalas; prevê sua razão. Um valor em GeV requer apenas calibrar o parâmetro
dimensional $\Lambda_C$ já presente na ação. Fonte:
q35/auditoria_calibracao_escala_em.md.

Na Q34, a expansão local da polarização $U(1)$ foi calculada até $r^3$.
Na convenção subtraída, $c_F^{\rm IR}=0$ é a normalização da carga, e
$A_1=\alpha_0e^{-\eta}/(15\pi)$,
$A_2=-\alpha_0e^{-\eta}(1+\eta)/(140\pi)$ e
$A_3=\alpha_0e^{-\eta}(2+2\eta+\eta^2)/(1890\pi)$. A verificação numérica
confirmou erro $O(r^4)$. Permanecem como extensões coeficientes não abelianos
e jacobiano topológico; a comparação de kernels foi executada posteriormente.
Fonte:
q34/coeficientes_locais_U1_heat_kernel.md.

O coeficiente não abeliano líder $a_4$ foi consolidado pela combinação
vetor--jacobiano--matéria. Para o espectro efetivo da Q28,
$b_0^{SU(3)}=7$ e $b_0^{SU(2)}=10/3$; incluir o modo de ordem como doublet
escalar complexo propagante fornece condicionalmente $19/6$. O coeficiente
absoluto de $F^2$ requer gap espectral; no setor sem massa, a integral
absoluta possui problema infravermelho, não ultravioleta. Permanece calcular
$a_6$, o jacobiano topológico e a classe de kernels. Fonte:
q34/coeficiente_nao_abeliano_a4.md.

Na ordem $a_6$, a parcela de matéria de
$\operatorname{tr}(D_\rho F_{\mu\nu})^2$ foi calculada:
$c_{2G}^{\rm matter}=g^2(240\pi^2)^{-1}
\sum_fT(R_f)m_f^{-2}e^{-\tau m_f^2}$. O limite abeliano foi recuperado
exatamente. O termo $\operatorname{tr}(F^3)$ não pode ser inferido da
polarização de dois pontos; permanecem o traço vetor--jacobiano e os
invariantes mistos Bismut. Fonte: q34/a6_materia_e_obstrucao_F3.md.

O traço universal vetor--jacobiano de $a_6$ foi montado e normalizado. A mesma
convenção reproduziu $a_4^{\rm VJ}=11/(96\pi^2)$; os pesos integrados de
$a_6$ foram verificados racionalmente. Resta contrair os índices dos termos
com $E$, reduzir por Bianchi à base $((DF)^2,F^3)$ e restaurar
curvatura/torção/bordo no background GDQ. As referências completas a
Vassilevich (2003) e Gilkey (1975) estão registradas em
q34/a6_vetor_jacobiano_forma_universal.md.

A extensão de $a_6$ à conexão produto Bismut--gauge foi formulada. Termos
mistos puros de $\Omega$ cancelam por tracelessness; misturas sobrevivem via
$E_BF^2$ e dependem de $\mathcal R^B$, $\nabla^BH$, $E_B$ e do domínio de
bordo no mesmo background. O balanço
$R_{ij}-H_{ik\ell}H_j{}^{k\ell}/4=0$ é apenas condição de Ricci e não prova
Bismut-flatness. Referências completas a Bismut (1989) e Vassilevich (2003)
estão em q34/extensao_a6_bismut.md.

A redução plana de $a_6$ foi posteriormente completada. Na convenção
matricial declarada,
$a_6^{\rm VJ}=(4\pi)^{-2}[(19/30)\mathcal B+(1/45)\mathcal C]$, com
$\mathcal B=\int\operatorname{tr}(D_\mu F_{\mu\nu})^2$ e
$\mathcal C=\int\operatorname{tr}(F_\mu{}^\nu F_\nu{}^\rho
F_\rho{}^\mu)$. A verificação usou frações exatas e matrizes não
comutativas. Permanecem a extensão Bismut, os termos de bordo, o jacobiano
topológico; a comparação de kernels foi executada posteriormente. Fonte:
q34/a6_vetor_jacobiano_forma_universal.md.

### 8.5 Q37/Q38

Fundos nus simples falham por muitas ordens de grandeza. Isso mostra que o
ansatz simples é insuficiente; não prova automaticamente que um instanton ou
warp específico é necessário. Em Q38, o relatório final conservador prevalece:

- (R=\pi^2\sqrt\alpha R_H): condição de colagem, não derivada do bulk;
- (e^{-1/(2\alpha)}): condicional a essa colagem;
- α⁴: determinante proposto, ainda condicional;
- (1+\alpha): correção efetiva/fenomenológica;
- (3\sqrt2/5): motivação por canais, matriz de transmissão não calculada.

---

## 9. Ideias importantes do manuscrito que não devem ser esquecidas

1. divergência conceitual Feynman--Wiener e papel do contorno;
2. matéria como geometria deformada, não fonte pontual externa;
3. Madelung e Nelson como ponte hidrodinâmica;
4. causalidade complexa de Sudarshan;
5. ação oficial como funcional de contorno em τ;
6. regularidade como propriedade do espaço, inclusive no perturbativo;
7. cirurgia de Perelman e Mayer--Vietoris no problema do sinal;
8. spin como vorticidade/torção e circulação;
9. spin--estatística por holonomia e exclusão como nó geométrico;
10. Stern--Gerlach como bifurcação física, hoje refinada pela Q42;
11. dominância espectral da equação de calor conjugada/difusão de nêutrons
    para a teoria da medida;
12. NESS, Fano e Zwanzig--Mori para irreversibilidade emergente;
13. incerteza pela positividade de Kähler e termos osmóticos;
14. distinção entre τ e tempo físico;
15. vácuo com energia/tensão e papel das condições cosmológicas;
16. massa como volume/bulk e torção como superfície no bárion;
17. carga como integral de Cauchy/resíduo inteiro;
18. distribuição de torções no nêutron: estômato invertido com resposta
    compensadora, a derivar por Noether/conservação;
19. potenciais locais tipo Kepler (1/r) e potenciais globais cotangentes em
    (S^3);
20. constantes como razões geométricas após uma calibração metrológica;
21. Killing e colchetes de Poisson como rota para álgebras de gauge;
22. Fredholm para (\alpha_s^{eff}=3/(8\pi)), ainda a auditar como derivação;
23. (f_B) via volume Kähler bariônico, pendente de normalização canônica;
24. Hopf, resíduos e atlas em dois patches;
25. compactificação cosmológica de Einstein como condição física, não mera
    troca de coordenadas do plano.

---

## 10. Contradições e armadilhas conhecidas

1. **Geometria:** não misturar ℝ⁴×T⁴ e T⁵×S³ sem mapa explícito.
2. **Kähler/Bismut:** Kähler estrito tem (d\omega=0); torção de Bismut não
   nula exige linguagem Hermitiana/KT adequada.
3. **Dimensão:** o bulk real oito-dimensional é escolha estrutural; dada a
   estrutura complexa, $n=4$ é consequência. Não confundir isso com uma
   derivação dinâmica da topologia ou da dimensão real.
4. **Ação:** Perelman é estrutura auxiliar/reduzida; a ação oficial não muda.
5. **ρ:** manter (\rho=e^{-(f+\bar f)/2}); não redefinir para obter Born.
6. **Tempo:** não confundir τ, (z_\tau) e (t).
7. **Spin:** Maslov (1/2) não prova sozinho spin intrínseco.
8. **Born:** fórmula de projetores não é, por si só, derivação do evento.
9. **Medição:** decoerência não seleciona automaticamente um resultado único.
10. **Retrocausalidade:** problema de contorno global não garante causalidade.
11. **Perelman:** monotonicidade não é automaticamente irreversibilidade
    termodinâmica de um detector.
12. **DtN:** (\Lambda\) é resposta do bulk; (\mathsf R_{app}) é o operador de
    interface. Não fundi-los na definição.
13. **Hessiana:** rigidez não é tempo; falta mobilidade causal.
14. **Problema do sinal:** resolução conceitual não é algoritmo polinomial.
15. **Q38:** fechada no espaço cosmológico de Einstein; coincidência numérica
    não transforma prefatores fenomenológicos em derivação local, e dados de
    uma fibra infinitesimal não determinam o valor global de \(G\).
16. **Q39:** acordo Reg--Reg deve ser testado quanto a independência de
    parâmetros e incorporação ao bulk oficial.
17. **Q40:** raio próximo não compensa momentos magnéticos ainda incorretos.
18. **Modelo Padrão:** não importar representações e depois alegar emergência.
19. **Renormalização:** usar linguagem de vestimento/projeção efetiva, mantendo
    claro quando se compara com QFT externa.
20. **Dados experimentais:** distinguir calibração legítima de ajuste oculto.

---

## 11. Backlog científico prioritário

### Prioridade A — Teoria da medida e interface clássico--quântico

1. escolher um aparelho concreto, inicialmente Stern--Gerlach;
2. escrever suas fontes clássicas sem operadores quânticos inseridos;
3. variar a ação oficial com fonte e bordo;
4. derivar (\mathsf R_{app});
5. calcular Hessiana, DtN e espectro localizado;
6. derivar mobilidade e ruído por eliminação dos graus macroscópicos;
7. calcular (\Gamma_{SG}), (\kappa_H^{SG}), tempo de resposta e manchas;
8. recuperar Pauli/Lindblad como limite;
9. produzir previsão nova e falseável.

### Prioridade B — Reconciliação geométrica

1. definir o papel exato de ℝ⁴×T⁴, T⁵×S³ e das fatias (S^3);
2. construir a redução dimensional/fibrado;
3. mostrar como operadores Rosen--Morse e potenciais cotangentes emergem da
   ação local oficial;
4. reclassificar Q37, Q39 e Q40 após essa prova.

### Prioridade C — Índices e gauge

1. calcular classes características de Q28;
2. avaliar η-invariantes APS/Bismut;
3. obter índices por estômato e três gerações;
4. calcular normas internas (g_s,g,g');
5. derivar Q29--Q31 quantitativamente.

### Prioridade D — Gravidade local posterior

1. resolver background estacionário completo admissível;
2. calcular operador local, determinante e transporte da colagem de Q38;
3. testar compatibilidade com o \(G\) global sem selecionar fatores pelo alvo;
4. recuperar explicitamente Poisson/Newton no limite fraco.

Esses itens não reabrem Q38: são testes da projeção local de um dado definido
globalmente no espaço cosmológico de Einstein. Fonte: decisão explícita do
usuário em 2026-07-12 e `questão_38_final.md`.

### Prioridade E — Numérico e experimental

1. congelar parâmetros antes de consultar alvos;
2. publicar testes de convergência e sensibilidade;
3. separar treino/calibração de previsão;
4. comparar curvas completas, não apenas um número;
5. procurar observável em que GDQ difira da teoria padrão.

---

## 12. Critério para considerar a GDQ preditivamente fechada em um setor

Um setor estará realmente fechado quando existir a cadeia:

\[
\boxed{
\text{ação oficial}
\to
\text{background admissível}
\to
\text{Hessiana física}
\to
\text{operador e contorno}
\to
\text{espectro estável}
\to
\text{observável sem pós-ajuste}
\to
\text{teste experimental}.
}
\]

Além disso, devem ser fornecidos:

- domínio de validade;
- hipóteses explícitas;
- análise dimensional;
- existência/unicidade ou justificativa numérica;
- convergência e estabilidade;
- contagem de parâmetros;
- distinção entre entrada experimental e previsão;
- possibilidade de falsificação.

---

## 13. Avaliação global vigente

A GDQ já não é apenas uma coleção de analogias. Possui ação oficial, dicionário
de campos, redução de Madelung, reconstrução quântica condicional, estrutura
topológica para spin e uma arquitetura operacional de medição. Seu ponto forte
é a tentativa construtiva de explicar estruturas que a teoria padrão usa de
forma operacional.

Ela ainda não é uma teoria física confirmada ou preditivamente completa. Os
maiores bloqueios são a reconciliação dos backgrounds, a derivação quantitativa
dos parâmetros diretamente da ação, a interface clássico--quântico e a
validação experimental sem pós-ajuste.

Classificação recomendada:

> Programa geométrico-quântico original e tecnicamente estruturado, com
> resultados reduzidos promissores e mecanismos interpretativos ricos, mas
> ainda dependente de fechamentos espectrais, variacionais e experimentais
> para competir como teoria física fundamental.

---

## 14. Arquivos-chave para retomada

### Fundação

- `pt-br/04 - A Ação Funcional e Consistência Quântica (Loops).md`
- `questão_2.md`, `questão_3.md`, `questão_4.md`, `questão_9.md`
- `questão_10.md` a `questão_17.md`

### Fundamentos quânticos

- `pt-br/09 - Spin e Geometria de Cartan - A Vorticidade do Espaço-Tempo.md`
- `pt-br/11 - A Geometria do Teorema de Spin-Estatística e a Exclusão de Pauli.md`
- `pt-br/13 - Regra de Born.md`
- `pt-br/16 - Problema da Medida.md`
- `pt-br/21 - O Problema dos NESS.md`
- `questão_20.md` a `questão_27.md`
- `teoria_interface_classico_quantica_gdq.md`
- `derivacao_fonte_classica_interface_sg.md`
- `modelo_aparelho_minimo_gdq.md`
- `teorema_captura_born_interface_gdq.md`
- `detector_ohmico_gdq.md`
- `auditoria_background_macroscopico_interface.md`
- `reducao_hessiana_torcional_aparelho.md`
- `gram_torcional_t4_interface.md`
- `interface_medida/test_gram_t4.py`
- `interface_medida/saida_gram_t4.md`
- `selecao_quiral_hopf_bismut.md`
- `sobreposicao_campo_hopf_gx.md`
- `interface_medida/test_overlap_hopf_field.py`
- `interface_medida/saida_overlap_hopf_field.md`
- `variacional_perfil_torcional_IH.md`
- `interface_medida/test_variacional_IH.py`
- `interface_medida/saida_variacional_IH.md`
- `derivacao_kernels_cH_iH.md`
- `interface_medida/test_boundary_kernels_IH.py`
- `interface_medida/saida_boundary_kernels_IH.md`
- `auditoria_rota_stern_gerlach_gdq.md`
- `auditoria_gamma_magnetica_ZH.md`
- `teorema_noether_zeeman_gdq.md`
- `projecao_hessiana_noether_g2.md`
- `possibilidade_torcao_discriminante_pde.md`
- `interface_medida/test_detector_ohmico_gdq.py`
- `interface_medida/saida_detector_ohmico_gdq.md`

### Setores em desenvolvimento

- `questão_28_final.md`, `questão_29_final.md`
- `questão_30_yang_mills.md`, `questão_31.md`
- `questão_38_final.md`, `questão_39.md`, `questão_40.md`
- `questão_42.md`, `q42/README.md`, `q42/STATUS.md`

### Controle

- `faltas.md`, `faltas_mapa.md`, `faltas_plano.md`
- `numerico/status_numerico_auditado.md`
- `possibilidades.md`
- `estrutura_reorganizacao_manuscrito.md`
- `plano_primeiros_capitulos_gdq.md`
- `manuscrito/index.md`
- `manuscrito/ref/index.md`

---

## 15. Próxima atualização desta memória

Atualizar `memory.md` quando ocorrer qualquer um destes eventos:

1. mudança de axioma ou convenção fundamental;
2. fechamento ou reabertura de questão;
3. nova derivação direta da ação oficial;
4. resultado numérico que passe de ajuste para previsão;
5. reconciliação dos backgrounds;
6. criação da teoria da interface clássico--quântico;
7. consolidação de Q43--Q49.

Ao atualizar, registrar a data, o arquivo-fonte e o motivo da mudança. Não
apagar hipóteses antigas: movê-las para histórico ou `possibilidades.md`.

**Última consolidação:** 15 de julho de 2026.

### Atualização de 15 de julho de 2026 — redução axiomática

Fonte: `manuscrito/02_geometrization/axiom_to_theorem_audit.md` e revisão da
`questão_3.md`.

Foi separado o axioma geométrico da consequência dimensional: a escolha de
$M=\mathbb R^4\times T^4$ e da classe complexa permanece uma entrada, enquanto
$n=4$ segue matematicamente dessas entradas. A mesma auditoria registrou como
teoremas a existência de estruturas de spin e a unicidade da conexão de
Bismut, e manteve como condicionais os resultados que dependem de relógio,
holonomia, background, gap ou classe de contorno.

**Preservação de status da ponte global--local:** a formulação genérica dos
seis lemas é condicional às hipóteses de localização e gap, mas essas hipóteses
já foram verificadas no background estacionário gaussiano $C_3$. Portanto, na
classe $C_3$, a ponte global--local está **fechada como teorema aplicado**, com
$\Delta_0=1/2$ na normalização primitiva. Não rebaixar esse resultado a
“condicional” sem mencionar que a restrição é apenas de domínio: sua extensão
a backgrounds arbitrários permanece aberta. Fontes canônicas:
`ponte_global_local_lemas_sem_colar.md` e
`ponte_global_local_fechamento_c3.md`.

### Reestruturação do Capítulo 3 — 15 de julho de 2026

Fonte: `manuscrito/03_complex_causality/`.

O capítulo de causalidade complexa passou a distinguir explicitamente $t$,
$\tau$, $z_\tau$ e $\gamma$. Revisão de estatuto posterior: o “fim do paradoxo
de Wick” não substitui a rotação formal por uma obrigação de deformar
contornos. A GDQ já nasce com variável causal complexa e com $\gamma$ como
dado estrutural da ação oficial. Os setores oscilatório e difusivo são setores
da mesma construção, não teorias convertidas uma na outra. Formas exatas,
monodromias, períodos e resíduos foram preservados como conteúdo matemático e
físico calculável, não como teste externo de admissibilidade de $\gamma$.

Na classe de contornos GDQ admissíveis, o pareamento conjugado e a condição de
reflexão da 1-forma oficial fazem parte da construção; por isso a realidade da
ação é teorema aplicado nessa classe, e não pendência para um contorno
arbitrário. A reconstrução lorentziana já pertence ao Capítulo 2. Spin
antiperiódico pertence ao capítulo de spin; unitariedade, à reconstrução
quântica; microcausalidade e no-signalling de aparelhos, à teoria da medida.
Esses deslocamentos preservam o registro histórico do Capítulo 3, mas o fecham
como fundamentação causal própria da GDQ.

Revisão pedagógica no mesmo dia: todas as seções foram ampliadas para abrir a
continuação espectral, a diferença entre grupo unitário e semigrupo, a
classificação local das EDPs e o papel físico das condições de contorno. O
tipo local vem do símbolo principal; bordos e prescrições de radiação
selecionam a solução física. A forma afim
$z_\tau=\tau+i\nu_0t$ teve sua homogeneidade e unicidade condicional
demonstradas. A prova de realidade passou a usar a 1-forma oficial puxada ao
contorno,

$$
\omega(\tau)=\mathscr F(\tau)\frac{d\tau}{\tau},
$$

sem substituir automaticamente $d\tau/\tau$ por $dz_\tau/z_\tau$. Também foi
reservado $\gamma$ ao contorno causal e $C$ ao ciclo material de circulação.
A integralidade $\oint_Cp=nh$ requer holonomia trivial; o setor deslocado por
meia unidade requer holonomia de spin $-1$, cuja seleção dinâmica permanece
separada. Resíduos calculam períodos meromorfos, mas não fixam sozinhos a
unidade física nem a classe integral.

### Reestruturação do Capítulo 4 — 15 de julho de 2026

Fonte: `manuscrito/04_action_consistency/`.

O capítulo da ação passou a apresentar em prosa a ação oficial, seus campos,
a dependência constitutiva de $\mathcal U$, o domínio variacional, as
simetrias e o estatuto auxiliar da linguagem perturbativa. Propagadores
padrão, BRST e fantasmas não foram incorporados à ontologia da GDQ. A
afirmação sobre loops permanece limitada à finitude superficial e à ausência
de novos polos no nível quadrático quando o form factor inteiro for derivado
da Hessiana física.

A contagem dimensional foi fechada pela análise adimensional motivada pela
idade de Fermi. Com $z=\ell_C\widehat z$,
$\tau=\ell_C^2\widehat\tau$,
$\mathcal R=\ell_C^{-2}\widehat{\mathcal R}$,
$\mathcal U=\ell_C^{-8}\widehat{\mathcal U}$ e
$dV_g=\ell_C^8dV_{\widehat g}$, o funcional reduzido é adimensional e
$\mathcal S_{\rm GDQ}=\hbar\widehat{\mathcal I}_{\rm GDQ}$. A dimensão de
área de $\tau$ é a idade de Fermi, não uma inconsistência. Deve-se distinguir
o cutoff adimensional $\widehat\Lambda_C=1$, o comprimento $\ell_C$ e a
energia física $E_C=\hbar c/\ell_C$.

### Seleção global--local da forma-relógio — 15 de julho de 2026

Fonte: `manuscrito/02_geometrization/02.10 - Do bulk Riemanniano ao
espaço-tempo físico.md`.

A direção temporal local é selecionada, no background cosmológico adotado,
pela simultaneidade comóvel do
espaço cosmológico de Einstein. Na decomposição
$T^5\times S^3=T^4\times S^1_E\times S^3$, a forma unitária
$\omega_E=R_Ed\Theta_E$ converge, no limite apontado, para
$\omega_0=dx^0$ no fator $\mathbb R^4$. Para a imersão física,
$u=X^*\omega_0$ e $\ker u$ é o limite tangente das folhas cosmológicas de
simultaneidade. A sincronização no ponto-base fixa a escala do relógio e
$\gamma$ fixa sua orientação. Assim, a lorentzianização é teorema algébrico e
a seleção do relógio é teorema dentro do background cosmológico de Einstein
adotado, não uma escolha local arbitrária. A existência e a regularidade da
foliação pertencem aos dados desse background; somente generalizações para
outras classes cosmológicas exigem nova prova de existência.

### Revisão pedagógica do Capítulo 2 — 15 de julho de 2026

Fonte: `manuscrito/02_geometrization/`.

O Capítulo 2 foi reescrito como construção progressiva, preservando a ação
oficial e a separação entre definição, identidade, teorema condicional e
programa aberto. As contas da dimensão real oito e complexa quatro, da
existência de estruturas spin, da medida $(4\pi z_\tau)^{-4}$, da variação de
$\mathcal U$ e da dimensão física da ação foram abertas no corpo do texto.
$\Lambda_C$ permanece o corte adimensional da ação; $\ell_C$, $k_C$ e $E_C$
são as escalas dimensionais distintas.

Foram incorporadas três seções antes apenas projetadas: o critério de
background material, a relação não automática entre circulação, torção e
defeitos, e a cadeia de existência e estabilidade. Um sóliton material exige
estacionariedade vinculada, ação relativa e medida finitas, localização,
classe conservada, Hessiana física projetada estável e resposta espectral.
Uma circulação não nula requer domínio excisado ou holonomia; a torção de
Bismut é uma 3-forma e não foi identificada diretamente com a fase. A relação
física deve ser derivada na interface.

A reconstrução lorentziana foi demonstrada passo a passo: o pullback de uma
métrica positiva continua positivo, enquanto uma forma-relógio global não
nula permite a reflexão

$$
h=q-2\frac{u\otimes u}{q^{-1}(u,u)},
$$

de assinatura $(-,+,+,+)$. A seleção global--local de $u$ continua
condicionada à existência da foliação comóvel cosmológica e às hipóteses de
transporte do setor. Foi removida da auditoria a formulação contraditória que
tratava a seleção local já demonstrada como ainda não promovível; o que segue
aberto é a existência dinâmica da foliação global.

### Revisão pedagógica do Capítulo 4 — 15 de julho de 2026

Fonte: `manuscrito/04_action_consistency/`.

O Capítulo 4 foi reescrito para abrir a construção do princípio variacional,
a análise dimensional, a dependência constitutiva de $\mathcal U$, o vínculo
de normalização, as simetrias, os bordos e a expansão em flutuações. A ação
oficial foi preservada. A escala espectral do semigrupo ficou separada do
corte oficial:

$$
\widehat\Lambda_\tau=\tau^{-1/2},
\qquad
e^{-\tau L^{(2)}}
\longrightarrow
e^{-p_E^2/\widehat\Lambda_\tau^2}.
$$

$\widehat\Lambda_\tau$ não redefine o $\Lambda_C$ adimensional do prefator.
A Hessiana correta é a Hessiana física projetada da ação oficial; seu inverso
define o propagador somente após remover modos de gauge, impor vínculos e
fixar o domínio. A finitude demonstrada pelo amortecimento exponencial foi
classificada como finitude ultravioleta de integrais quadráticas com
crescimento polinomial, condicionada à derivação do form factor. A extensão a
várias voltas permanece dependente dos vértices completos, de estimativas
uniformes, de anomalias e de backgrounds específicos. BRST e fantasmas
continuam apenas como linguagem externa de auditoria.

### Reestruturação do Capítulo 5 — 15 de julho de 2026

Foi criado `manuscrito/05_equations_conservation/` com o capítulo “Equações de
movimento e leis de conservação”. A ordem dedutiva adotada é: ação
estacionária; decomposição $f\leftrightarrow(\rho,S_R)$; variação da fase e
corrente conservada; variação da densidade e redução de Bohm; variação
métrica; Noether, vínculos e bordos; alcance. Os campos dinâmicos centrais da
ação permanecem $(g,f,\bar f)$; $J$ e $H$ só entram numa parametrização
Hermitiano--Bismut explicitamente declarada. As contas da corrente de fase e
da identidade de Bohm foram abertas em notas pedagógicas próprias.

Revisão pedagógica no mesmo dia: as Seções 05.1--05.7 foram ampliadas para
expor as integrações por partes no corpo do texto. A prova de Noether agora
inclui a identidade off shell, a variação localizada, a conservação on shell,
a carga integrada e a condição de não fuga lateral. A variação direta de
$q=\ln\rho$, incluindo $\delta\mathcal U$, forneceu

$$
\tau\left[
\mathcal R+\frac{|\nabla S_R|^2}{\hbar^2}
-4\frac{\Delta_g\sqrt\rho}{\sqrt\rho}
\right]-\ln\rho-n-1=\lambda(\tau).
$$

A variação métrica ponderada foi explicitada na classe com
$(f,\bar f,z_\tau)$ fixos. Ficou registrado que a corrente de fase do bulk
não é ainda, por si só, a continuidade temporal: a forma
$\partial_t\rho+\nabla\cdot(\rho v)=0$ requer que a ponte causal produza a
decomposição do fluxo e o termo canônico $\rho\,\partial_tS_R$. Do mesmo modo,
o coeficiente físico do potencial de Bohm depende da normalização cinética da
redução, embora seu operador de amplitude já tenha sido derivado da ação.
$\lambda(\tau)$ preserva a normalização de $\mathcal U$ em cada seção; a
equação com lado direito nulo pertence apenas ao problema não restringido ou
a uma convenção que absorva essa constante.

### Criação do Capítulo 6 — ponte global--local — 15 de julho de 2026

Fonte: `manuscrito/06_global_local_bridge/`, consolidando
`ponte_global_local_lemas_sem_colar.md`,
`ponte_global_local_fechamento_c3.md`,
`teorema_heranca_espectral_global_local_gdq.md` e
`teorema_heranca_normalizacao_eletromagnetica.md`.

O capítulo foi construído pedagogicamente em dez seções. A passagem de
$T^5\times S^3$ para $\mathbb R^4\times T^4$ foi formulada como limite suave
apontado, não como colagem por uma interface artificial. O operador DtN ficou
reservado ao bordo físico do estômato. Os seis lemas foram abertos na ordem:
família geométrica; transporte de $(g,J,H,f,\mathcal U)$; convergência das
formas da Hessiana física; localização e gap uniforme; resolventes e
projetores de Riesz; separação entre dados herdados e não herdados.

A Hessiana transportada é a Hessiana do funcional vinculado, projetada por
$P^{\rm phys}$; modos de gauge, normalização e Noether não pertencem ao
espectro físico. Modos ligados usam localização de Agmon e projetores. Canais
massless estendidos exigem normalização de fluxo, convergência DtN ou de
espalhamento e ausência de fuga lateral. Assim, topologia, multiplicidade e
clusters ligados são transportados sob gap, enquanto escalas absolutas e
acoplamentos contínuos exigem cálculo próprio da corrente simplética.

No background gaussiano $C_3$, o gap

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}
$$

é positivo e vale $1/2$ na normalização primitiva. Nessa classe, a ponte está
fechada como teorema aplicado; sua extensão a backgrounds arbitrários exige
nova verificação do gap.

O transporte do relógio e a decomposição $3+1$ de uma corrente conservada
foram demonstrados. A identificação final da densidade temporal dessa corrente
com a $\rho$ constitutiva de Madelung permanece condicionada à derivação, pelo
pullback causal da ação oficial, do termo canônico
$\rho\,\partial_tS_R$ com coeficiente unitário. Essa pendência não deve ser
confundida com a ponte espectral, que já está fechada no setor $C_3$.

Auditoria direta posterior em
`manuscrito/notes/equations/Auditoria do termo canonico rho d_t S_R.md`:
a ação oficial fornece

$$
\Pi_{S_R}=n_\mu\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R,
$$

e não $\Pi_{S_R}=\rho$ em geral. A normalização interna preserva o marginal,
mas não elimina $n\cdot dS_R$; uma fase constante fornece contraexemplo
imediato. A transformação de Legendre gera a forma de primeira ordem sem
alterar a ação fundamental, porém o termo $\rho\partial_tS_R$ exige ainda
derivar o vínculo físico $\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}$ e uma
polarização que controle o par da amplitude. Não registrar esse vínculo como
provado apenas pela normalização.

Continuação da auditoria: a rota estacionária $S_R=-Et$ não fecha
universalmente, pois Noether temporal não seleciona monoenergia, a carga de
fase não é automaticamente a carga temporal e impor $Q_S=N_\rho=1$ pode ser
circular. A rota variacional correta é uma redução de Routh. Se o pullback
produzir

$$
H_t[\Pi,\rho]
=\int_\Sigma\frac{\Pi^2}{2A\rho}\,d\Sigma
$$

com $A>0$ constante, Cauchy--Schwarz dá

$$
H_t\geq\frac{Q_S^2}{2A N_\rho},
$$

com igualdade exatamente para
$\Pi=(Q_S/N_\rho)\rho$. No setor primitivamente e independentemente fixado
$Q_S=N_\rho=1$, segue $\Pi=\rho$. Ainda é preciso derivar do pullback que $A$
é uniforme, que não há termos cruzados ou fuga e que $Q_S=1$ não foi escolhido
pelo alvo. Esse é o teorema condicional vigente e a próxima prova necessária.

Fechamento da auditoria hamiltoniana: admitindo provisoriamente um pushforward
local em $t$, o setor oficial de fase reduz-se a

$$
L_S=\frac A2N\sqrt h\,\rho
\left[-(D_tS_R/N)^2+|DS_R|^2\right],
$$

de modo que
$\Pi_{S_R}=-A\sqrt h\rho(D_tS_R/N)$. O setor de amplitude possui momento
independente
$p_\rho=-A\hbar^2\sqrt h(D_t\rho/N)/\rho$. A Hessiana temporal é regular;
logo $C=\Pi_{S_R}-\sqrt h\rho$ não é vínculo primário e $\dot C$ não se anula
identicamente. Em $C_3$ estacionário e comóvel, $C=0$, uma vez selecionado, é
preservado, mas não é derivado pelo gap.

Há ainda uma obstrução anterior: os documentos vigentes não fornecem o mapa
$\gamma:t\mapsto\tau_\gamma(t)$ nem a identidade de 1-formas que converta
$d\tau/\tau$ em $dt$. A sincronização fixa o relógio local, mas não esse
Jacobiano causal. Portanto, o coeficiente $A$ não está calculado. Status
vigente: a estrutura canônica de Madelung é redução estacionária condicional;
não é identidade demonstrada da dinâmica geral da ação oficial.

Auditoria de uma tentativa externa de fechamento Killing--Perelman: a prova
foi rejeitada, mas o arquivo histórico foi preservado por decisão do usuário.
A equação de Killing não implica $\Delta\kappa=0$ para
$\kappa=d\tau_\gamma/dt$. Ademais, $\tau=at+b$ produz
$d\tau/\tau=a\,dt/(at+b)$, não um coeficiente constante. A monotonicidade de
Perelman em $\tau$ não demonstra decaimento de $p_\rho$ no tempo físico,
convergência universal a um sóliton, equivalência com o mínimo de Routh ou
saturação de Cauchy--Schwarz. Permanece válida somente a desigualdade
variacional depois que o setor convexo estacionário foi independentemente
selecionado.

Auditoria da tentativa posterior escala--eliminação adiabática: se o mapa
causal for um homomorfismo contínuo de $(\mathbb R,+)$ em
$(\mathbb R_+,\times)$, então é teorema que
$\tau_\gamma(t)=\tau_0e^{\kappa t}$ e
$\gamma^*(d\tau/\tau)=\kappa dt$. A hipótese de homomorfismo, porém, ainda não
foi derivada da ação ou do contorno; homogeneidade de tiques isolada não a
prova, e $\kappa$ permanece não calculado. A equação com amortecimento
$\dot p_\rho=-\Gamma p_\rho-\delta H_t/\delta\rho$ também não foi derivada:
exige funcional de influência do aparelho, kernel dissipativo, ruído,
flutuação--dissipação, separação de escalas e prova de que o mínimo de Routh é
o atrator. Não registrar essa tentativa como fechamento; preservar como rota
da teoria da medida.

Última rota intrínseca auditada: no espaço de estados normalizados, com
$\Psi=\sqrt\rho e^{iS_R/\hbar}$, vale exatamente

$$
\Theta_{\rm state}
=\hbar\operatorname{Im}\langle\Psi,\delta\Psi\rangle
=\int\rho\,\delta S_R,
\qquad
\Omega_{\rm state}=\int\delta\rho\wedge\delta S_R.
$$

Equivalentemente, a métrica ponderada de alvo
$G=\rho(du^2+dv^2)$, $u=-\ln\rho$, $v=S_R/\hbar$, tem forma Kähler
$\omega_T=-(1/\hbar)d\rho\wedge dS_R$. Logo o par de Madelung é teorema exato
da geometria do espaço de estados. Ele não é, porém, automaticamente a forma
pré-simplética covariante da ação oficial, que contém os pares independentes
$(S_R,\Pi_{S_R})$ e $(\rho,p_\rho)$ e o setor métrico. A Hessiana temporal
oficial é não degenerada, ao passo que a ação first-order é degenerada; termos
de bordo não alteram esse posto. O elo remanescente é um teorema de
polarização/redução invariante
$\Omega_{\rm GDQ}^{\rm phys}=\Omega_{\rm state}$. Não registrar essa igualdade
como provada sem nova condição física ou mudança explícita de axioma.

Decisão interpretativa e documental posterior: o significado físico da
polarização foi incorporado aos Capítulos 5 e 6. A ação oficial possui o
espaço de Cauchy ampliado $(\rho,p_\rho,S_R,\Pi_{S_R})$. O setor de matéria
quântica hidrodinâmica é a subvariedade

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\rho,
$$

na qual resta o par canônico $(\rho,S_R)$. Isso não altera a ação: classifica
a mecânica quântica como setor/polarização efetiva da GDQ. Soluções externas
podem representar modos rápidos, oscilações próprias da densidade ou estados
geométricos fora do equilíbrio, mas nenhuma ontologia experimental lhes foi
atribuída. A generalização para outros setores estáveis é programa de
pesquisa, não resultado já demonstrado.

Extensão registrada em 15 de julho de 2026:
`extensoes/estrutura_de_hilbert_colapso_e_espectros_nao_hermitianos.md`
organiza como programa futuro a possibilidade de tratar espaços de Hilbert
dependentes do background, seleção dinâmica de autofunções e operadores
efetivos não hermitianos. O sistema completo permanece regido pela ação
oficial real; a não hermiticidade só pode surgir após eliminação explícita de
canais do bulk, contorno ou aparelho, com balanço de fluxo, causalidade,
positividade e no-signalling ainda a demonstrar. O registro não declara uma
teoria do colapso já concluída.

### Criação do Capítulo 7 — limite clássico — 15 de julho de 2026

Fonte: `manuscrito/07_classical_limit/`, preservando as ideias úteis do
capítulo legado `pt-br/28 - O Limite Clássico e o Princípio da
Correspondência.md`, mas corrigindo seu estatuto matemático.

O limite clássico foi formulado dentro do setor de Madelung
$p_\rho=0$, $\Pi_{S_R}=\sqrt h\rho$. O parâmetro controlador é

$$
\varepsilon_{\rm cl}=\frac{\hbar}{pL_\rho},
$$

e, sob regularidade da amplitude e ausência de nós,
$|Q_B|/T_{\rm cl}=O(\varepsilon_{\rm cl}^2)$. Foram abertas no corpo do
manuscrito as provas da redução Hamilton--Jacobi--Bohm para Hamilton--Jacobi,
das características de Hamilton e Newton, da continuidade para Liouville e
da hierarquia WKB. O potencial radial harmônico em $S^3$ foi derivado como
$-(\kappa/R_E)\cot(r/R_E)$, cujo limite local é $-\kappa/r$; a forma não fixa
por si só a normalização $\kappa$.

O capítulo não usa rotação de Wick reversa, não identifica $\tau$ com o tempo
físico e não afirma que $\hbar\to0$ anule Bohm uniformemente perto de nós ou
cáusticas. As antigas alegações de obtenção automática de Maxwell e Einstein
foram preservadas como rotas futuras que exigem os setores próprios da
Hessiana oficial, não como consequências da equação escalar de
Hamilton--Jacobi.

Complementação posterior do Capítulo 7: após auditoria integral do capítulo
legado e de sua nota associada, as correspondências vetorial e métrica foram
incorporadas às Seções 7.11 e 7.12. No setor isotrópico de menor ordem, a
restrição quadrática da Hessiana ao modo $U(1)_Q$ fornece $F=dA$, $dF=0$ e a
equação variacional com fonte, recuperando a forma de Maxwell; $Z_Q$ continua
sendo a normalização setorial. No setor métrico estacionário, foram
incorporadas a média torsional, a identidade exata
$\nabla\nabla f_R=\nabla f_R\nabla f_R-\rho^{-1}\nabla\nabla\rho$, o fechamento
hidrodinâmico legado e a redução trace-reversed. A análise dimensional dá
$\kappa_G=C_GG/c^4$, e a comparação de $G_{00}$ com Poisson fixa
$C_G=8\pi$. A avaliação global de $G$, $\Lambda$ e de torção residual não é
fixada por essa correspondência. A nota legada sobre $g-2$ e mésons foi
preservada, mas classificada fora do limite clássico por depender de
coeficientes fenomenológicos ainda não derivados.

### Recuperação canônica das omissões dos Capítulos 1--5 — 15 de julho de 2026

Fonte editorial: `Omissões.md`, reavaliado segundo as Questões 3, 4, 16, 21,
34 e 35. O relatório histórico havia confundido conteúdo ausente do novo
manuscrito com conteúdo cientificamente não demonstrado.

Foram recuperados no manuscrito:

1. em `01.8`, a difusão variável de Nelson com
   $D^{ij}=\nu_0\Omega^{-1}h^{ij}$, a Fokker--Planck completa e os termos de
   Itô; a conta é exata na redução estocástica, enquanto a origem geométrica
   de $\Omega$ e a seleção de $m_0$ permanecem problemas solitônicos;
2. em `01.9` e `05.7`, NESS como descrição efetiva depois de projeção e
   coarse-graining, sem identificar o parâmetro de fluxo $\tau$ com o tempo
   físico $t$;
3. em `04.7`, o fechamento do problema dos fantasmas no setor declarado: o
   objeto intrínseco é o quociente/projetor físico, o determinante de
   Faddeev--Popov é jacobiano geométrico e BRST é auditoria opcional;
4. Ward e Slavnov--Taylor pela covariância espectral
   $L_{A^g}=g^{-1}L_Ag$;
5. a polarização $U(1)$ heat-kernel, sua saturação ultravioleta e a ausência
   condicional do polo de Landau.

As provas pedagógicas foram abertas nas notas
`manuscrito/notes/derivations/Difusão variável de Nelson na GDQ.md`,
`NESS, fluxo geométrico e irreversibilidade efetiva.md`,
`manuscrito/notes/action/Quociente físico, fantasmas e identidades de
calibre.md` e `Polarização heat-kernel e ausência do polo de Landau.md`.

Não foram restauradas como teoremas a antiga função beta, a seleção dinâmica
de $n=4$ por Bohm ou Atiyah--Singer, a autoenergia fermiônica como loop
fundamental, a diluição holográfica de $\rho_\Lambda$ nem $\tau$ como quinta
dimensão física. O resultado vigente para a dimensão é: escolhido
$M=\mathbb R^4\times T^4$, segue $n=4$; a seleção dinâmica da própria classe
geométrica continua separada.
