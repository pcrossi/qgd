# Extensão da GDQ para estruturas de Hilbert variáveis e espectros não hermitianos

## 1. Status deste documento

**Classificação:** programa futuro de extensão.

Este documento não altera a ação oficial da GDQ e não declara resolvidos os
problemas de medição, colapso ou dinâmica não hermitiana. Ele registra uma
consequência possível da interpretação vigente do setor de Madelung: a
mecânica quântica hilbertiana pode ser uma polarização efetiva de uma dinâmica
geométrica maior.

O ponto de partida demonstrado no espaço normalizado de estados é

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar},
$$

com forma simplética

$$
\Omega_{\rm state}
=\int_\Sigma\delta\rho\wedge\delta S_R\,d\Sigma.
$$

Na descrição de Cauchy da ação oficial, entretanto, o espaço dinâmico é mais
amplo:

$$
(\rho,p_\rho,S_R,\Pi_{S_R}).
$$

O setor hidrodinâmico quântico é selecionado pela polarização

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\,\rho.
$$

Portanto, o formalismo de Hilbert usual pode ser interpretado como uma redução
física da GDQ, e não necessariamente como a totalidade de seu espaço de
configurações.

## 2. Problemas que essa extensão pode tratar

### 2.1 Ausência de um único espaço de Hilbert global

Backgrounds, contornos e aparelhos distintos podem selecionar polarizações,
domínios de operadores e produtos internos diferentes. Em vez de postular um
único espaço de Hilbert válido para toda configuração, a estrutura apropriada
pode ser um fibrado

$$
\pi:\mathfrak H\longrightarrow\mathcal B,
$$

onde $\mathcal B$ é o espaço de backgrounds e cada fibra $\mathfrak H_b$
representa o setor físico selecionado no background $b$.

Para que essa formulação seja consistente, será necessário construir uma
conexão de transporte entre as fibras e demonstrar quando esse transporte é
unitário, adiabático ou dissipativo.

### 2.2 Colapso e seleção de autofunções

O colapso pode ser investigado como uma transição dinâmica produzida pela
mudança das condições de interface entre objeto e aparelho. O aparelho
clássico fornece uma fonte ou vínculo externo e modifica o domínio efetivo do
operador físico:

$$
J_{\rm app}^{\rm clássico}
\longrightarrow
\delta\Phi_{\rm app}
\longrightarrow
\operatorname{Hess}\mathcal S_{\rm GDQ}
\longrightarrow
\mathsf R_{\rm app}
\longrightarrow
\text{seleção espectral}.
$$

Nessa interpretação, uma projeção sobre uma autofunção não deve ser inserida
como postulado. Deve resultar da resposta condicionada da geometria às novas
condições de contorno, incluindo mobilidade causal, dissipação e registro
macroscópico.

### 2.3 Operadores efetivos não hermitianos

O sistema completo continua regido pela ação oficial real, no domínio causal
admissível. Entretanto, depois da eliminação dos graus não observados do bulk,
do contorno ou do aparelho, o subsistema pode ser descrito por um operador
efetivo não hermitiano:

$$
H_{\rm eff}(z)
=H_{PP}+H_{PQ}(z-H_{QQ})^{-1}H_{QP}.
$$

Esta é uma redução por complemento de Schur/Feshbach. A parte imaginária não
é um novo termo fundamental da GDQ: ela registra fluxo que deixa o subsistema
observado. Em regime ressonante, os polos podem ser escritos como

$$
z_n=E_n-\frac{i}{2}\Gamma_n,
$$

onde $\Gamma_n\geq0$ representa uma largura de decaimento ou perda para os
canais eliminados.

### 2.4 Coalescência espectral e pontos excepcionais

Uma família de impedâncias de aparelho $\mathsf R_{\rm app}(\lambda)$ pode
produzir uma família de operadores efetivos $H_{\rm eff}(\lambda)$. Pontos nos
quais autovalores e autovetores coalescem podem então aparecer como pontos
excepcionais. A análise correta deverá usar o operador, seu domínio, os
projetores de Riesz e a estabilidade do espectro sob variações do contorno.

## 3. Cadeia de construção exigida

A extensão só estará fundamentada quando for demonstrada a cadeia

$$
\text{ação oficial real}
\longrightarrow
\text{background admissível}
\longrightarrow
\text{Hessiana física projetada}
\longrightarrow
\text{acoplamento GDQ--aparelho}
\longrightarrow
\text{eliminação dos canais não observados}
\longrightarrow
H_{\rm eff}.
$$

Devem ser especificados:

1. espaço completo de Cauchy e projetor físico;
2. operador auto-adjunto do sistema fechado e seu domínio;
3. condições de interface e de radiação;
4. canais observados e canais eliminados;
5. kernel causal de memória produzido pela eliminação;
6. regime em que uma aproximação local ou Markoviana é válida;
7. interpretação dos polos, larguras e projetores espectrais;
8. regra de condicionamento que associa a resposta ao registro experimental.

## 4. Condições mínimas de consistência

Uma descrição efetiva não hermitiana será aceitável somente se forem
verificadas, no sistema completo:

- conservação da probabilidade total ou balanço explícito do fluxo entre os
  setores retido e eliminado;
- positividade das probabilidades dos registros;
- causalidade do kernel de resposta;
- ausência de sinalização superluminal;
- independência dos resultados físicos de escolhas puramente de gauge;
- recuperação do setor unitário quando os canais externos forem fechados;
- estabilidade do espectro físico e controle de modos zero;
- distinção entre dissipação real, erro de truncamento e artefato numérico.

Em particular, perda de norma no subsistema deve satisfazer uma identidade de
balanço do tipo

$$
\frac{d}{dt}\lVert\psi_P\rVert^2
=-\mathcal F_{P\to Q},
$$

com $\mathcal F_{P\to Q}$ calculado como fluxo para os graus eliminados, e não
introduzido por um potencial imaginário escolhido fenomenologicamente.

## 5. O que já segue e o que permanece aberto

### Resultado já disponível

A geometria do espaço normalizado de estados fornece exatamente o par
canônico $(\rho,S_R)$. A dinâmica completa da ação oficial possui ainda os
momentos independentes $(p_\rho,\Pi_{S_R})$. Isso torna matematicamente possível
interpretar a mecânica quântica usual como um setor/polarização da GDQ.

### Consequência estrutural

É legítimo investigar setores nos quais a eliminação de graus geométricos
produza operadores efetivos dependentes do background, dissipativos ou não
hermitianos. Essa possibilidade não exige modificar a ação oficial.

### Questões abertas

- provar a seleção dinâmica da polarização apropriada em uma interação real;
- construir o fibrado de espaços físicos e sua conexão;
- derivar o operador efetivo diretamente da Hessiana oficial;
- demonstrar a identidade de balanço de fluxo;
- derivar o condicionamento de eventos e a regra de registro;
- tratar espectros incompletos, bases biortogonais e pontos excepcionais;
- verificar Born, causalidade e no-signalling na dinâmica condicionada.

## 6. Veredito

O último resultado canônico não prova uma teoria geral do colapso nem torna a
GDQ fundamentalmente não hermitiana. Ele fornece, contudo, o espaço matemático
correto para desenvolver essa extensão: o espaço de Hilbert aparece como setor
físico selecionado, enquanto a não hermiticidade pode surgir legitimamente na
dinâmica reduzida de um subsistema aberto.

Essa rota deve permanecer classificada como **programa futuro**, até que o
operador efetivo, seu domínio, o fluxo eliminado e os registros experimentais
sejam derivados da ação oficial e das condições físicas do aparelho.
