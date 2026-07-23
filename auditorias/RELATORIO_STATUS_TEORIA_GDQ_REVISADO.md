# Relatório revisado de status da GDQ

Data da revisão: 12 de julho de 2026.

## 1. Regra de interpretação

Esta revisão distingue quatro níveis que estavam misturados nos relatórios
anteriores:

1. resultado da ação oficial no bulk local;
2. teorema condicional, válido depois de hipóteses declaradas;
3. modelo cosmológico ou espectral auxiliar;
4. ajuste, comparação fenomenológica ou teste numérico.

A cadeia exigida para uma previsão forte continua sendo

\[
\boxed{
\text{ação oficial}
\to
\text{background admissível}
\to
\text{Hessiana física}
\to
\text{operador e domínio}
\to
\text{espectro}
\to
\text{observável sem pós-ajuste}.
}
\]

## 2. Correção sobre as duas geometrias

O bulk local oficial permanece

\[
M_{\rm local}=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}M_{\rm local}=8.
\]

O espaço

\[
M_{\rm cos}=T^5\times S^3
\]

pode ser usado como background cosmológico, domínio espectral global ou ciclo
efetivo de calibração. Isso não é, por si só, uma contradição, pois ambos têm
dimensão real oito e exercem papéis diferentes.

A exigência correta é outra: todo resultado atribuído à GDQ fundamental deve
explicitar

\[
\boxed{
M_{\rm local}
\longleftrightarrow
M_{\rm cos/espectral}
}
\]

por redução, projeção, limite tangente, colagem ou correspondência espectral
derivada. Sem esse mapa, o resultado continua válido apenas no modelo
auxiliar, não como consequência de primeiros princípios da ação local.

Também não se deve usar $T^5\times S^3$ como hipersuperfície de fronteira de
uma variedade real 8D: essa fronteira teria dimensão sete. Esse impedimento é
específico à interpretação como fronteira, não ao uso cosmológico global.

## 3. Status revisado por bloco

### 3.1 Fundação e dinâmica — Q2 a Q21

Status geral: bloco estruturalmente maduro, com condições técnicas ainda
localizadas.

Resultados fortes:

1. ação oficial única e ontologia dos campos;
2. bulk local e dimensão complexa quatro fixados axiomaticamente;
3. continuidade e Hamilton--Jacobi--Bohm obtidas variacionalmente;
4. equação métrica e problema de Cauchy formulados;
5. causalidade e reconstrução lorentziana estruturadas.

Pendências reais:

1. verificar OS1--OS5 no setor completo efetivamente usado;
2. completar o espectro de Jacobi para sólitons carregados e spinoriais;
3. não confundir existência do critério de sóliton com construção explícita de
   todas as partículas.

### 3.2 Fundamentos quânticos — Q22 a Q27

Status geral: estrutura forte, mas duas pendências permanecem.

1. Q22 e Q23 estão estruturalmente fechadas: Born no espaço reconstruído e
   quantização de circulação por integralidade topológica.
2. Q24 possui decoerência, dominância espectral e bacias de atração, mas a
   dinâmica de interface que produz um registro individual ainda precisa ser
   fechada em conjunto com a teoria clássico--quântico.
3. Q25 está resolvida conceitualmente como reformulação geométrica, mas não
   como algoritmo: custo, variância, autocorrelação e benchmarks permanecem.
4. Q26 e Q27 estão fechadas estruturalmente sob as hipóteses do setor spinorial
   local e causal.

### 3.3 Gauge, escalas e constantes — Q28 a Q37

1. **Q28:** setor local calculado e consolidado em $N_G=A/6$. O espectro
   tangencial, o índice APS local e a colagem mínima foram avaliados. Falta
   determinar cosmologicamente a carga global $A$ e calcular as normas
   internas; a minimização local não deve ser repetida.
2. **Q29:** fechada apenas no setor efetivo condicionado à Q28; faltam
   $v,g,g'$ e sobreposições fermiônicas calculadas.
3. **Q30:** conexão, Wilson loops, lei de área e cota de gap estão
   estruturados; $\sigma$, $\lambda_1$ e a medida funcional explícita ainda
   não foram avaliados.
4. **Q31:** relaxação torsional de CP está estruturada; $\chi_{\rm top}$,
   normalização canônica, EDM e evolução cosmológica quantitativa permanecem.
5. **Q32:** operador suavizado estruturado; reflexão positiva e suporte causal
   do propagador completo ainda precisam de verificação setorial.
6. **Q34--Q35:** setor $U(1)$ estruturalmente tratado; extensão não abeliana
   quantitativa e $\Lambda_{\rm EM}$ geométrica permanecem.
7. **Q36:** calibração metrológica é metodologicamente válida; cada razão
   anunciada como previsão deve ser auditada para excluir entrada disfarçada.
8. **Q37:** a convergência apontada já relaciona o background cosmológico ao
   bulk local, mas a estrutura fina permanece dependente da norma física do
   modo eletromagnético; não está derivada independentemente.

### 3.4 Gravidade — Q38

O documento canônico é `questoes/q38/questao_38_final.md`. Q38 possui dois resultados que
devem ser mantidos simultaneamente:

1. um fechamento positivo pela condição de contorno cosmológica global;
2. um resultado negativo que exclui a tentativa de gerar o mesmo coeficiente
   por um resíduo do bulk local suave.

No problema cosmológico, o raio causal $R_H$ e a energia total $E_H$ são dados
de contorno. A relação clássica do horizonte fornece

\[
R_H=\frac{2GE_H}{c^4},
\qquad
\boxed{G=\frac{c^4R_H}{2E_H}>0.}
\]

Isso não pretende prever o raio ou a energia particulares do universo. É uma
resposta positiva ao problema de contorno e não é circular quando $E_H$ é
especificado independentemente de $G$.

A regularidade euclidiana fixa

\[
\beta_E=2\pi R_H,
\qquad
\tau_*=\frac{\beta_E^2}{16},
\]

e a cadeia térmico--axial produz

\[
\Delta u_v
=
\frac{\pi^4}{2}\frac{R_H^2}{R^2}.
\]

Sob a condição geométrica de colagem

\[
R=\pi^2\sqrt\alpha\,R_H,
\]

segue

\[
\Delta u_v=\frac1{2\alpha},
\qquad
\frac{\mathcal U_*}{\mathcal U_0}=e^{-1/(2\alpha)}.
\]

Esse setor está fechado condicionalmente aos dados de contorno e à condição
de colagem. A condição de colagem não foi derivada do bulk local, mas é
legítima como dado que define o problema cosmológico particular.

Separadamente, foi demonstrado que a rota local suave não produz o
coeficiente por resíduo. A extração formal é

\[
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma[F_R],
\qquad
G=\frac{c^4}{16\pi C_R}.
\]

Entretanto, no setor bulk suave, normalizado e conservativo,

\[
F_R(z)=a_0+a_1z+\cdots,
\qquad
\operatorname{Res}F_R=0,
\qquad
C_R=0.
\]

Esse resultado negativo exclui a rota meromorfa suave; não anula o valor
positivo determinado pelo contorno global.

O valor numérico candidato

\[
G_{\rm GDQ}=6.6567916\times10^{-11}
\ {\rm m^3\,kg^{-1}\,s^{-2}}
\]

decorre ainda do prefator proposto

\[
\frac{\alpha^4(1+\alpha)}{3\sqrt2/5}e^{-1/(2\alpha)}
\]

e não é ab initio: $1+\alpha$, a admitância $3\sqrt2/5$ e a própria colagem
permanecem constitutivos/condicionais.

Também permanece válido que:

1. a ação oficial contém curvatura escalar linear, não o funcional quadrático
   necessário à rota BPST/BPS;
2. o background produto produz acoplamento misto nulo no complemento de Schur;
3. a ação bulk sem completação de bordo não seleciona a garganta torsional;
4. os fatores instantônico e Fano reduzidos não bastam para derivar $G$.

Status correto:

\[
\boxed{
\text{Q38 fechada positivamente como problema de contorno global e
condicionalmente na cadeia térmico--axial; rota local suave excluída.}
}
\]

### 3.5 Massas leptônicas — Q39

O operador de Rosen--Morse em $S^3$ e seus testes numéricos constituem um
modelo espectral global consistente. Isso não basta para classificá-lo como
derivação completa da ação oficial.

Permanecem dois elos essenciais e uma verificação espectral:

1. derivar o operador e seus coeficientes a partir do background estacionário
   da ação oficial;
2. justificar sem seleção pelo alvo o mapeamento espectral
   $n=(0,1,17)$ e a exclusão dos demais níveis.

O antigo item da ponte geométrica foi resolvido por convergência apontada
direta. A multiplicidade $C_3$ possui gap e projetor físico transportáveis.
Ainda falta identificar os níveis $n=(0,1,17)$ com esse cluster físico, ou
provar diretamente o gap uniforme do operador leptônico.

A afirmação

\[
N_{\rm ger}=|h^{1,1}-h^{2,1}|=3
\]

exige uma variedade complexa e o cálculo explícito de seus números de Hodge;
ela não segue automaticamente da topologia real de $T^5\times S^3$.

Status correto:

\[
\boxed{
\text{Q39 fechada no modelo espectral auxiliar; condicional como previsão
fundamental da GDQ.}
}
\]

### 3.6 Bárions — Q40

Q40 possui uma construção reduzida extensa para carga, spin, massa, raio,
momentos e resposta de sonda. $T^5\times S^3$ já foi corretamente declarado
ciclo global de calibração, não bulk local.

O status forte ainda depende de:

1. solução estacionária explícita que realize a redução variacional usada;
2. Hessiana completa e estabilidade dos modos não homogêneos;
3. derivação dos coeficientes numéricos de volume e superfície sem seleção
   fenomenológica;
4. fatores de forma, fases parciais, $G_F$ e $g_A$ calculados no operador
   final.

Atualização: a compatibilidade global--local e a estabilidade projetada do
background trimodal $C_3$ foram fechadas por convergência apontada e gap
uniforme. Portanto o item 2 está resolvido para essa classe estacionária. O
resultado não fixa automaticamente as normalizações contínuas dos itens 3 e
4, nem substitui a construção estacionária do item 1.

Status correto:

\[
\boxed{
\text{Q40 fechada estruturalmente no modelo reduzido e no transporte }C_3;
\text{ normalizações e fenomenologia permanecem condicionais.}
}
\]

### 3.7 Poço e oscilador — Q41

Q41 está encerrada no escopo correto.

Foram realizados:

1. recuperação variacional de Schrödinger--Madelung;
2. minimização e atrator gaussiano;
3. Hessiana e índice de Morse;
4. impedância Robin como mapa Dirichlet--Neumann ou complemento de Schur;
5. comparação numérica com barreira finita;
6. convergência de segunda ordem, com erro máximo
   $3.437\times10^{-7}$ no teste final.

Status:

\[
\boxed{
\text{Q41 totalmente fechada como teste de redução e correspondência.}
}
\]

Ela não constitui validação independente da dinâmica nova da GDQ, mas não
possui pendência estrutural dentro da pergunta formulada.

### 3.8 Stern--Gerlach e medição — Q42

Q42 avançou além do relatório antigo. Foram construídos:

1. elo $S^3$ da fatia normal $\mathbb C^2$ sob transversalidade;
2. atlas de Hopf em duas cartas;
3. contorno variacional e background estacionário reduzido;
4. operadores Robin, simulações de captura e sequências de medição;
5. ramo cilíndrico de Hopf e resposta Dirichlet--Neumann textural.

O cálculo posterior corrigiu uma hipótese importante:

\[
\boxed{Z_{\rm bulk}^{\rm orientação\ global}=0,}
\]

pois a rotação global de um background isotrópico é isometria/gauge. A
rigidez física deve vir da textura não homogênea e da resposta localizada ao
aparelho.

Ainda faltam:

1. projeção localizada completa da fonte do aparelho;
2. espectro físico de todos os modos radiais e tensoriais relevantes;
3. mobilidade causal e ruído térmico em unidades físicas;
4. cálculo de $\Gamma_{\rm SG}$ e $\kappa_H^{\rm SG}$ para um aparelho real.

Status:

\[
\boxed{
\text{Q42 fechada operacionalmente no modelo efetivo; parâmetros físicos da
interface permanecem abertos.}
}
\]

## 4. Pendências prioritárias reais

### Prioridade 0 — sincronização documental

1. atualizar `faltas.md`, `faltas_mapa.md`, `faltas_plano.md` e
   `numerico/status_numerico_auditado.md` com este relatório;
2. marcar versões históricas de cada questão;
3. incorporar as conclusões consolidadas ao novo manuscrito, não diretamente
   ao texto antigo em `pt-br/`.

### Prioridade 1 — Q28 global

Construir o problema cosmológico de contorno da tensão global e calcular
$A[\mathfrak B_{\rm cosmológico}]$. O alvo $A=18$ não pode ser usado como
entrada. Em paralelo, calcular as normas internas; não repetir a rota local,
que já foi encerrada.

### Prioridade 2 — Q24/Q42

Consolidar a teoria da interface clássico--quântico e calcular parâmetros de
um aparelho concreto a partir da Hessiana oficial.

### Prioridade 3 — Q37/Q39

Calcular a norma eletromagnética e o complemento de Schur da Q37. Em Q39,
identificar o cluster $n=(0,1,17)$ com o cluster físico $C_3$. Q40 não deve
ser reaberta por causa da ponte; seguem apenas suas normalizações e extensões
fenomenológicas.

### Prioridade 4 — Q25 e fenomenologia

Implementar algoritmo, variância e benchmarks do problema do sinal; depois
prosseguir para fatores de forma, espalhamento e comparações experimentais.

## 5. Veredito geral

A GDQ possui uma fundação matemática ampla e uma cadeia variacional coerente
até o setor de Madelung, causalidade e reconstrução quântica condicional. O
principal risco atual não é ausência de ideias, mas confusão entre quatro
níveis de resultado: ação oficial, modelo reduzido, geometria cosmológica e
ajuste fenomenológico.

As pendências centrais são localizadas e identificáveis:

\[
\boxed{
\text{Q28 índices e gauge},
\quad
\text{Q24/Q42 interface de medição},
\quad
\text{Q37 normalização eletromagnética e Q39 cluster leptônico}.
}
\]

Q41 pode ser removida definitivamente do backlog estrutural.
