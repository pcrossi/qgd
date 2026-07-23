# Questão 25 — O problema do sinal foi realmente resolvido?

## 1. Pergunta

A Questão 25 pergunta:

\[
\boxed{
\text{o problema do sinal fermiônico foi realmente resolvido pela GDQ?}
}
\]

As perguntas obrigatórias de `25-0.md` são:

1. onde a fase fermiônica é armazenada?
2. como observáveis sensíveis ao sinal são calculados?
3. qual é a variância do estimador?
4. qual é a complexidade assintótica?
5. quais benchmarks são usados?
6. a superfície nodal precisa ser conhecida?

O critério de resolução é:

\[
\boxed{
\text{um algoritmo reproduzível com erro controlado e custo não exponencial
em uma classe de problemas relevante.}
}
\]

---

## 2. Resposta curta

Não. No estado atual, o problema do sinal não está resolvido como problema
computacional.

O que a GDQ fornece é uma reformulação geométrica importante:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}>0
}
\]

e a fase fermiônica é deslocada para:

\[
\boxed{
S_R=\hbar\,\operatorname{Im}f,
}
\]

com a antissimetria codificada por:

\[
\boxed{
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar
\quad(\mathrm{mod}\ 2\pi\hbar).
}
\]

Logo:

\[
\boxed{
\rho(P_{ij}Z)=\rho(Z).
}
\]

Isso remove o sinal da medida real positiva, mas não prova que todos os
observáveis fermiônicos possam ser estimados com variância polinomial.

Portanto:

\[
\boxed{
\text{Questão 25 não está fechada como resolução algorítmica.}
}
\]

Ela fica fechada apenas como diagnóstico:

\[
\boxed{
\text{a fase está geometricamente armazenada, mas falta algoritmo com erro,
variância, complexidade e benchmarks.}
}
\]

---

## 3. Onde a fase fermiônica é armazenada?

Na decomposição GDQ:

\[
\boxed{
f=-\ln\rho+i\frac{S_R}{\hbar}.
}
\]

A densidade positiva é:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}.
}
\]

A fase é:

\[
\boxed{
\chi=\frac{S_R}{\hbar}=\operatorname{Im}f.
}
\]

Para troca de dois férmions:

\[
\boxed{
P_{ij}:Z\mapsto P_{ij}Z,
}
\]

a condição fermiônica é:

\[
\boxed{
\Psi(P_{ij}Z)=-\Psi(Z).
}
\]

Como:

\[
\boxed{
\Psi(Z)=\sqrt{\rho(Z)}\,e^{iS_R(Z)/\hbar},
}
\]

isso equivale a:

\[
\boxed{
\rho(P_{ij}Z)=\rho(Z),
}
\]

e:

\[
\boxed{
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar
\quad(\mathrm{mod}\ 2\pi\hbar).
}
\]

Logo, o sinal fermiônico não fica na medida \(\rho\), mas na monodromia da
fase/fibrado:

\[
\boxed{
e^{iS_R/\hbar}\mapsto -e^{iS_R/\hbar}.
}
\]

Essa parte está coerente com as Questões 20, 22 e 23.

---

## 4. Por que isso não basta para resolver o problema do sinal?

Porque o problema do sinal computacional não é apenas a existência de uma
medida positiva.

Em Monte Carlo fermiônico, observáveis físicos frequentemente exigem recuperar
informação de fase:

\[
\boxed{
\langle O\rangle
=
\frac{\int O(Z)\,e^{i\theta(Z)}\,|\omega(Z)|\,dZ}
{\int e^{i\theta(Z)}\,|\omega(Z)|\,dZ}.
}
\]

Mesmo que se amostre uma medida positiva:

\[
\boxed{
d\mu_+(Z)=|\omega(Z)|\,dZ,
}
\]

a fase reaparece no estimador:

\[
\boxed{
\langle O\rangle
=
\frac{\mathbb E_{\mu_+}[Oe^{i\theta}]}
{\mathbb E_{\mu_+}[e^{i\theta}]}.
}
\]

O problema do sinal aparece quando:

\[
\boxed{
|\mathbb E_{\mu_+}[e^{i\theta}]|
\sim e^{-cN\beta}.
}
\]

Nesse caso, a variância relativa cresce exponencialmente.

Portanto, dizer:

\[
\boxed{
\rho>0
}
\]

não basta. É preciso mostrar que os observáveis físicos não exigem um
reweighting de fase exponencialmente ruidoso.

---

## 5. Como observáveis sensíveis ao sinal são calculados?

Essa é a lacuna principal.

Observáveis insensíveis ao sinal podem ser calculados com a medida positiva:

\[
\boxed{
\langle O_{\rm even}\rangle
=
\frac{\int O_{\rm even}(Z)\rho(Z)\,d\mu_g}
{\int \rho(Z)\,d\mu_g}.
}
\]

Mas observáveis sensíveis à fase precisam de \(S_R\), holonomia, torção ou
setor spinorial:

\[
\boxed{
O=O(Z,\nabla S_R,B,\mathrm{Hol},\ldots).
}
\]

Uma forma possível seria:

\[
\boxed{
\langle O\rangle
=
\frac{
\int O(Z,\nabla S_R)\rho(Z)\,d\mu_g
}{
\int \rho(Z)\,d\mu_g
}.
}
\]

Mas isso só é válido se:

1. \(S_R\) for conhecido ou computável sem custo exponencial;
2. o observável puder ser expresso localmente em \(Z,\nabla S_R\);
3. não houver denominador de fase com média exponencialmente pequena;
4. o método reproduzir correlações fermiônicas padrão;
5. os nós/holonomias forem tratados exatamente ou com erro controlado.

No texto atual, isso não foi demonstrado.

---

## 6. Variância do estimador

Para resolver a Questão 25, seria necessário fornecer um estimador:

\[
\boxed{
\widehat O_M
=
\frac1M\sum_{k=1}^M O(Z_k,\nabla S_R(Z_k)),
\qquad
Z_k\sim \rho\,d\mu_g.
}
\]

E provar uma cota:

\[
\boxed{
\operatorname{Var}(\widehat O_M)
\le
\frac{C(N,\beta,\varepsilon)}{M}.
}
\]

Para resolver o problema do sinal em sentido forte, seria necessário:

\[
\boxed{
C(N,\beta,\varepsilon)
\le
\operatorname{poly}(N,\beta,\varepsilon^{-1})
}
\]

em uma classe relevante de sistemas.

O capítulo original afirma que a variância “colapsa para a classe padrão”, mas
não fornece:

1. estimador explícito;
2. prova de variância;
3. tempo de mistura da cadeia;
4. autocorrelação;
5. controle de erro sistemático;
6. comparação com resultado exato.

Logo:

\[
\boxed{
\text{a variância ainda não está demonstrada.}
}
\]

---

## 7. Complexidade assintótica

Uma afirmação aceitável teria a forma:

\[
\boxed{
T(N,\beta,\varepsilon)
\le
\operatorname{poly}(N,\beta,\varepsilon^{-1})
}
\]

para uma classe específica, por exemplo:

1. Hubbard 1D;
2. Hubbard 2D em meia ocupação;
3. Hubbard 2D dopado em certo regime;
4. gás de elétrons uniforme;
5. moléculas pequenas com base finita;
6. férmions livres em rede;
7. classe de hamiltonianos com gap e área de emaranhamento controlada.

O texto atual afirma polinomialidade geral:

\[
\boxed{
\mathcal O(\operatorname{poly})
}
\]

independente de número de férmions e baixa temperatura.

Essa afirmação é forte demais. Uma resolução geral exata e polinomial do
problema do sinal para férmions genéricos entraria em conflito com a
NP-dificuldade conhecida do problema em formulações gerais.

Portanto, a versão defensável é:

\[
\boxed{
\text{a GDQ pode sugerir uma nova classe de algoritmos positivos, mas a
complexidade precisa ser provada por classe de problema.}
}
\]

---

## 8. Benchmarks necessários

Para tornar a afirmação auditável, o método precisaria ser testado em
benchmarks padrão.

### 8.1 Casos exatamente solúveis

1. férmions livres em rede;
2. oscilador harmônico fermiônico;
3. Hubbard 1D comparado com Bethe ansatz;
4. pequenos clusters por diagonalização exata.

### 8.2 Casos sem problema de sinal conhecido

1. Hubbard 2D em meia ocupação;
2. modelos bipartidos com simetria partícula-buraco.

Esses servem para validar que o algoritmo não erra onde métodos existentes já
funcionam.

### 8.3 Casos com problema de sinal real

1. Hubbard 2D dopado;
2. modelo \(t\)-\(J\);
3. férmions frustrados;
4. gás de elétrons uniforme;
5. moléculas com forte correlação.

### 8.4 Métricas de comparação

Para cada benchmark:

1. energia do estado fundamental;
2. funções de correlação;
3. observáveis sensíveis à fase;
4. erro estatístico;
5. erro sistemático;
6. tempo de mistura;
7. escala com \(N\);
8. escala com \(\beta\);
9. comparação com diagonalização exata, DMRG, AFQMC, DQMC ou resultados
   conhecidos.

Sem isso:

\[
\boxed{
\text{não há resolução computacional demonstrada.}
}
\]

---

## 9. A superfície nodal precisa ser conhecida?

Na formulação GDQ, a superfície nodal seria:

\[
\boxed{
Z_\rho=\{Z:\rho(Z)=0\}.
}
\]

Para férmions, há pelo menos nós em coincidências:

\[
\boxed{
z_i=z_j.
}
\]

Mas, em estados interagentes genéricos, a superfície nodal completa é muito
mais complexa.

O texto original sugere que a geometria/fluxo determina os nós dinamicamente,
dispensando uma superfície nodal manual.

Isso é uma ideia útil, mas precisa virar algoritmo:

1. como inicializar \(\rho\) sem conhecer os nós?
2. como impedir cruzamentos nodais numericamente?
3. como detectar mudança de topologia nodal?
4. como controlar erro próximo a \(\rho=0\)?
5. como garantir que os nós dinâmicos coincidem com os nós do estado quântico
   correto?
6. qual é o custo de encontrar esses nós?

Enquanto isso não for respondido:

\[
\boxed{
\text{não está provado que a superfície nodal deixou de ser necessária.}
}
\]

---

## 10. O que o capítulo original acerta

O capítulo `pt-br/07 - Sistemas Fermiônicos Fortemente Correlacionados
(Problema do Sinal).md` acerta ao identificar:

1. a densidade positiva:

\[
\boxed{
\rho=e^{-(f+\bar f)/2};
}
\]

2. a simetria da densidade sob permutação:

\[
\boxed{
\rho(P_{ij}Z)=\rho(Z);
}
\]

3. o armazenamento do sinal na fase:

\[
\boxed{
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar;
}
\]

4. a necessidade de nós/barreiras de exclusão;
5. a possibilidade de uma formulação geométrica por domínios, holonomias e
   fluxo.

Esses pontos são compatíveis com a GDQ.

---

## 11. O que o capítulo original afirma forte demais

As seguintes afirmações não estão demonstradas:

1. “extingue a raiz algébrica do problema do sinal”;
2. “variância colapsa para classe padrão”;
3. “complexidade polinomial independente de \(N\) e baixa temperatura”;
4. “o problema matemático foi resolvido”;
5. “completamente blindado contra críticas”;
6. “dispensa o mapeamento prévio manual de superfícies nodais” em geral.

Versão corrigida:

\[
\boxed{
\text{a GDQ reformula o problema do sinal como problema de fase/holonomia e
nós dinâmicos sobre medida positiva.}
}
\]

Mas:

\[
\boxed{
\text{a resolução computacional requer algoritmo, variância, complexidade e
benchmarks.}
}
\]

---

## 12. Distinção correta: resolução geométrica versus resolução algorítmica

A formulação mais justa é separar dois níveis.

### 12.1 Resolução geométrico-estrutural

Nesse nível, o manuscrito possui uma ideia forte e coerente:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}>0
}
\]

remove o sinal da medida real, enquanto:

\[
\boxed{
S_R(P_{ij}Z)=S_R(Z)+\pi\hbar
}
\]

armazena a antissimetria fermiônica na fase/holonomia.

Além disso, a cirurgia topológica proposta no Capítulo 7 tenta substituir a
soma oscilatória global por uma decomposição em domínios:

\[
\boxed{
M=U_1\cup U_2\cup\cdots
}
\]

com costura de Mayer--Vietoris e condições de contorno nas gargantas
geométricas.

Nessa leitura, a GDQ não está tentando amostrar diretamente pesos alternados:

\[
\boxed{
e^{i\theta}|\omega|.
}
\]

Ela tenta reorganizar o problema para que a fase seja convertida em dado de
holonomia, bordo, torção ou transmissão entre domínios.

Portanto, pode-se dizer:

\[
\boxed{
\text{a GDQ fornece uma resolução estrutural/conceitual do lugar onde o sinal
vive.}
}
\]

Essa afirmação é defensável.

### 12.2 Resolução algorítmica

O nível algorítmico é mais forte.

Ele exigiria provar que a decomposição geométrica pode ser implementada com
custo controlado:

\[
\boxed{
T(N,\beta,\varepsilon)
\le
\operatorname{poly}(N,\beta,\varepsilon^{-1})
}
\]

para uma classe relevante de hamiltonianos.

Isso ainda não foi demonstrado.

Logo, a forma correta da conclusão é:

\[
\boxed{
\text{a resolução geométrica é plausível/estrutural; a resolução
computacional permanece aberta.}
}
\]

---

## 13. Rota computacional possível: matriz de transmissão/reflexão

Uma rota prática para transformar a cirurgia em simulação é substituir a
cirurgia geométrica contínua por uma matriz efetiva de correspondência entre
domínios.

Considere uma decomposição:

\[
\boxed{
M^\ast=\bigcup_a U_a
}
\]

com interfaces cirúrgicas:

\[
\boxed{
\Sigma_{ab}=U_a\cap U_b.
}
\]

Em vez de resolver todo o fluxo de Ricci/Bismut em \(M^\ast\), define-se, em
cada interface, uma matriz de espalhamento:

\[
\boxed{
\mathsf S_{ab}
=
\begin{pmatrix}
\mathsf R_{a} & \mathsf T_{ba}\\
\mathsf T_{ab} & \mathsf R_{b}
\end{pmatrix}.
}
\]

Aqui:

- \(\mathsf T_{ab}\) é a transmissão de fluxo/fase de \(U_a\) para \(U_b\);
- \(\mathsf R_a\) é a reflexão na borda vista a partir de \(U_a\);
- \(\mathsf S_{ab}\) carrega holonomia, torção e fase fermiônica efetiva;
- a positividade da medida fica em \(\rho_a\ge0\) dentro de cada domínio.

O problema global passa a ser resolver uma rede de domínios acoplados:

\[
\boxed{
\rho_a^{(t+1)}
=
\sum_b
\mathsf K_{ab}\rho_b^{(t)}
}
\]

com:

\[
\boxed{
\mathsf K_{ab}
=
|\mathsf T_{ab}|^2
\quad\text{ou}\quad
\mathsf K_{ab}
=
\mathsf S_{ab}^\dagger\mathsf S_{ab}
}
\]

dependendo da representação escolhida.

Para ser fisicamente aceitável, a matriz de interface deve satisfazer:

\[
\boxed{
\mathsf S_{ab}^\dagger\mathsf S_{ab}=I
}
\]

em setores fechados, ou:

\[
\boxed{
\mathsf S_{ab}^\dagger\mathsf S_{ab}\le I
}
\]

em setores abertos/dissipativos.

Essa construção transforma a cirurgia em uma condição de matching:

\[
\boxed{
\begin{pmatrix}
\psi_a^{\rm out}\\
\psi_b^{\rm out}
\end{pmatrix}
=
\mathsf S_{ab}
\begin{pmatrix}
\psi_a^{\rm in}\\
\psi_b^{\rm in}
\end{pmatrix}.
}
\]

Essa rota é significativamente mais simples que simular diretamente o espaço
completo de muitos corpos, porque substitui parte da dinâmica global por
blocos locais e matrizes de interface.

### 13.1 O que essa matriz precisa preservar

A matriz de correspondência deve preservar:

1. positividade de \(\rho\);
2. conservação ou dissipação controlada de fluxo;
3. antissimetria fermiônica como holonomia:

\[
\boxed{
\operatorname{Hol}(P_{ij})=-1;
}
\]

4. condições de Wallstrom:

\[
\boxed{
\oint dS_R=Nh;
}
\]

5. ausência de reweighting exponencial por fase;
6. compatibilidade com observáveis locais;
7. costura de Mayer--Vietoris nos overlaps.

### 13.2 Estimador associado

Um estimador possível teria a forma:

\[
\boxed{
\widehat O_M
=
\frac1M\sum_{k=1}^M
O(a_k,Z_k,\mathsf S_{\partial a_k}),
}
\]

onde:

- \(a_k\) é o domínio visitado;
- \(Z_k\in U_{a_k}\);
- \(\mathsf S_{\partial a_k}\) codifica as interfaces adjacentes;
- \(Z_k\) é amostrado com peso positivo \(\rho_{a_k}\).

O objetivo seria provar:

\[
\boxed{
\operatorname{Var}(\widehat O_M)
\le
\frac{\operatorname{poly}(N,\beta,\varepsilon^{-1})}{M}.
}
\]

### 13.3 Status dessa rota

Essa matriz transmissão/reflexão é uma proposta promissora de engenharia
computacional:

\[
\boxed{
\text{cirurgia contínua}
\longrightarrow
\text{rede de domínios + matrizes de interface.}
}
\]

Ela não prova ainda a resolução do problema do sinal, mas transforma a ideia
geométrica do Capítulo 7 em um objeto simulável.

Essa rota deve ser tratada como o caminho natural para tornar a Questão 25
computacionalmente testável.

---

## 14. Critério para fechar a questão no futuro

A Questão 25 só poderá ser fechada oficialmente quando houver um algoritmo
completo:

### 14.1 Entrada

\[
\boxed{
H,\ N,\ \beta,\ \varepsilon,\ \text{condições de contorno}.
}
\]

### 14.2 Saída

\[
\boxed{
\widehat O,\quad
|\widehat O-\langle O\rangle|\le\varepsilon
}
\]

com probabilidade controlada.

### 14.3 Prova

Deve-se provar:

\[
\boxed{
\operatorname{Var}(\widehat O)
\le
\operatorname{poly}(N,\beta,\varepsilon^{-1})
}
\]

e:

\[
\boxed{
T(N,\beta,\varepsilon)
\le
\operatorname{poly}(N,\beta,\varepsilon^{-1})
}
\]

para uma classe especificada.

### 14.4 Benchmarks

O algoritmo deve reproduzir:

1. casos exatamente solúveis;
2. casos com e sem problema de sinal;
3. observáveis sensíveis à fase;
4. escalas de erro e custo.

---

## 15. Resposta final da Questão 25

\[
\boxed{
\text{O problema do sinal está reformulado/estruturado geometricamente, mas
ainda não está resolvido como algoritmo computacional geral.}
}
\]

O que está estabelecido é:

\[
\boxed{
\text{o sinal fermiônico é armazenado na fase/holonomia }S_R,
\text{ enquanto a medida }\rho\text{ permanece positiva.}
}
\]

Mas falta demonstrar:

\[
\boxed{
\text{como calcular observáveis sensíveis ao sinal com variância e custo
polinomiais.}
}
\]

Status:

\[
\boxed{
\text{Questão 25 fechada como distinção: resolução geométrica estrutural sim;
resolução algorítmica oficial ainda não.}
}
\]

---

## 16. Validação algorítmica mínima executada

Atualização operacional: foi construído um pacote numérico autocontido em
`questoes/q25/associados/`, com saída consolidada em:

\[
\boxed{
\texttt{questoes/q25/resultados/saida\_q25\_validacao.md}
}
\]

O pacote implementa uma classe reduzida, não um benchmark fermiônico físico
completo.

### 16.1 O que foi validado

1. Domínios \(U_a\) com pesos positivos \(\rho_a>0\).
2. Interface fechada unitária \(\mathsf S_{ab}^\dagger\mathsf S_{ab}=I\).
3. Interface aberta contrativa \(\mathsf S_{ab}^\dagger\mathsf S_{ab}\le I\).
4. Holonomia de troca preservada:

\[
\operatorname{Hol}(P_{ij})=-1.
\]

5. Estimador de observável holonômico amostrado com medida positiva.
6. Comparação do estimador com integração exata finita.
7. Autocorrelação e limite espectral de mistura em uma cadeia local de
   domínios.
8. Pipeline de referências experimentais locais, sem fabricar dados.

### 16.2 Resultado numérico

No teste de interface, a unitariedade fechada foi satisfeita com erro de
máquina e a norma foi conservada. No estimador holonômico finito, a média
Monte Carlo concordou com o valor exato dentro do erro estatístico esperado.
No teste de escala da cadeia local, o limite espectral de mistura apresentou
comportamento compatível com lei polinomial quadrática:

\[
1/\Delta_{\rm mix}\sim N^{1.93}.
\]

### 16.3 O que isso não prova

Essa validação não fecha o problema do sinal em sentido forte, porque ainda
faltam:

1. operador GDQ físico para cada benchmark;
2. domínio, contorno e Hessiana física do problema fermiônico concreto;
3. dados experimentais quantitativos extraídos localmente;
4. comparação contra observáveis reais;
5. cota analítica de variância por classe;
6. prova de complexidade assintótica.

Portanto, o status atualizado é:

\[
\boxed{
\text{Q25: rota algorítmica mínima implementada; fechamento computacional
forte ainda aberto.}
}
\]

---

## 17. Benchmark físico reduzido

Após a validação mínima, foi construído um benchmark físico reduzido em rede,
sem substituir a GDQ por Hubbard como ontologia. A rede entra como dado externo
do aparelho; a dinâmica interna usada no teste é uma Hessiana reduzida GDQ
positiva no setor de circulação escalonada.

O relatório consolidado está em:

\[
\boxed{
\texttt{questoes/q25/resultados/saida\_q25\_benchmark\_fisico.md}
}
\]

### 17.1 Cadeia executada

Foram executados:

1. validação de dados experimentais locais;
2. construção de domínios físicos em rede \(L\times L\);
3. Hessiana reduzida positiva;
4. interface de impedância por transformada de Cayley;
5. cálculo de correlações spin/circulação;
6. comparação com enumeração exata finita;
7. teste inicial de escala de autocorrelação;
8. tentativa de comparação experimental local.

### 17.2 Resultados principais

Para \(L=4\), foram enumeradas \(2^{16}=65536\) configurações. A Hessiana
reduzida apresentou:

\[
\lambda_{\min}=0.18,
\qquad
\lambda_{\max}=2.98.
\]

A interface derivada da impedância teve erro máximo de unitariedade:

\[
\|\mathsf S^\dagger\mathsf S-I\|_{\max}
\simeq
2.61\times 10^{-16}.
\]

A correlação de primeiro vizinho obtida por enumeração exata foi:

\[
C_s(1)\simeq -0.1698717,
\]

e a estimativa Monte Carlo positiva forneceu:

\[
C_s(1)\simeq -0.16836.
\]

A correlação de segundo vizinho foi:

\[
C_s(2)_{\rm exato}\simeq 0.0571480,
\qquad
C_s(2)_{\rm MC}\simeq 0.05517.
\]

No teste de escala reduzido \(L=4,6,8\), a autocorrelação integrada cresceu
aproximadamente como:

\[
\tau_{\rm corr}\sim N^{0.934}.
\]

No intervalo testado, portanto, não apareceu crescimento exponencial.

### 17.3 Status científico

Esse benchmark físico reduzido é mais forte que o toy inicial porque inclui:

1. rede/aparelho explícito;
2. Hessiana positiva;
3. interfaces derivadas por impedância;
4. correlações de circulação/spin;
5. comparação com enumeração exata;
6. teste de escala.

Após a extração inicial de dados quantitativos de Parsons et al. 2016, a
comparação externa foi executada. O resultado é parcial: o sinal
antiferromagnético e a ordem de grandeza do correlator frio de primeiro
vizinho são reproduzidos, mas o conjunto completo não é descrito
metrologicamente pelo modelo reduzido.

Para o dado frio principal:

\[
C_s(1)_{\rm exp}=-0.190(8),
\qquad
C_s(1)_{\rm GDQ,red}\simeq -0.1698717,
\]

com desvio:

\[
z\simeq 2.516.
\]

O comprimento de correlação reduzido saiu:

\[
\xi_{\rm GDQ,red}\simeq 0.918,
\]

enquanto os dados extraídos de Parsons et al. ficam no intervalo aproximado
\(0.24\) a \(0.51\) sites para os regimes comparados. Portanto a Hessiana
reduzida captura correlação local de primeiro vizinho, mas superestima a
persistência espacial da ordem.

### 17.4 Ensemble térmico

Foi então testada a rota correta de comparação térmica: em vez de comparar
todos os pontos experimentais com uma única Hessiana reduzida fixa, foi
varrida uma família de ensembles positivos:

\[
P_{\rm GDQ,red}(x;\beta_{\rm eff})
=
\frac{1}{Z(\beta_{\rm eff})}
\exp[-\beta_{\rm eff}E_{\rm GDQ,red}(x)].
\]

O script:

\[
\boxed{
\texttt{questoes/q25/associados/q25\_16\_thermal\_ensemble\_map.py}
}
\]

inverte a curva \(C_s(1)(\beta_{\rm eff})\) para os pontos digitizados da
Fig. 2D. O resultado mostra que a curva térmica pode ser representada por uma
família de ensembles GDQ reduzidos com \(\beta_{\rm eff}\) variável.

O ajuste fenomenológico obtido foi:

\[
\beta_{\rm eff}
\simeq
\frac{0.291786}{k_BT/t+0.050000}.
\]

Esse resultado deve ser classificado corretamente:

\[
\boxed{
\text{é uma inversão fenomenológica do mapa térmico, não derivação fundamental
do aparelho.}
}
\]

O ponto digitizado \(T/t=0.55\) apareceu mais negativo que o ponto
\(T/t=0.45\), o que viola a monotonicidade térmica esperada. Portanto essa
série deve ser tratada como digitização aproximada da figura, não como tabela
metrológica final.

### 17.5 Teste de derivação por invariantes da Hessiana reduzida

Para verificar se o mapa térmico poderia ser obtido sem calibração, foram
testados candidatos construídos apenas com invariantes escalares da Hessiana
reduzida:

\[
\lambda_{\min},\quad
\lambda_{\max},\quad
\operatorname{tr}H/N,\quad
\kappa_H,\quad
m_{\rm gap}.
\]

O script:

\[
\boxed{
\texttt{questoes/q25/associados/q25\_17\_hessian\_thermal\_map\_candidates.py}
}
\]

comparou esses candidatos ao mapa térmico invertido. O melhor candidato sem
usar alvo foi:

\[
\beta_{\rm cand}
=
\frac{m_{\rm gap}}{k_BT/t+m_{\rm gap}},
\]

mas ainda apresentou erro relativo RMS de aproximadamente:

\[
0.418.
\]

Conclusão:

\[
\boxed{
\text{os invariantes escalares da Hessiana reduzida não determinam sozinhos o
mapa térmico do aparelho.}
}
\]

O elo faltante não é o ensemble; o ensemble existe. O elo faltante é o bloco
térmico/aparelho completo: mobilidade causal, admitância de banho, contorno
termodinâmico e acoplamento da Hessiana física ao modo medido.

### 17.6 Bloco térmico/aparelho efetivo

Foi construído então o primeiro bloco térmico/aparelho reduzido:

\[
\boxed{
\texttt{questoes/q25/associados/q25\_18\_thermal\_apparatus\_block.py}
}
\]

O mapa testado foi a admitância térmica de contorno:

\[
\beta_{\rm eff}(\Theta)
=
\frac{\mu_A}{\Theta+\Theta_A},
\qquad
\Theta=k_BT/t.
\]

Esse formato tem interpretação física clara: \(\mu_A\) mede a mobilidade ou
admitância térmica efetiva do aparelho, enquanto \(\Theta_A\) é a largura
térmica/temperatura interna residual do contorno.

Primeiro foram testados candidatos sem alvo, usando apenas invariantes da
Hessiana reduzida. Eles não fecharam quantitativamente. Permitindo que
\((\mu_A,\Theta_A)\) sejam dados efetivos de aparelho, obteve-se:

\[
\mu_A\simeq0.573747,
\qquad
\Theta_A\simeq0.721528,
\]

com RMSE:

\[
0.0896.
\]

Esse resultado melhora a representação operacional do mapa térmico, mas a
classificação correta é:

\[
\boxed{
\text{modelo efetivo de aparelho ajustado, não derivação final da ação.}
}
\]

Para fechar a Q25 nesse eixo, \(\mu_A\) e \(\Theta_A\) precisam sair da
Hessiana completa do aparelho/background e da mobilidade causal.

### 17.7 Derivação reduzida por complemento de Schur

Foi implementada uma primeira derivação reduzida de \((\mu_A,\Theta_A)\) por
decomposição sistema--aparelho:

\[
\boxed{
\texttt{questoes/q25/associados/q25\_19\_schur\_apparatus\_derivation.py}
}
\]

O modo observado é o modo local de diferença de circulação no primeiro vínculo
da rede. O complemento ortogonal da rede é tratado como aparelho/banho
reduzido. A Hessiana é escrita em blocos:

\[
K=
\begin{pmatrix}
K_H & J\\
J^\top & K_A
\end{pmatrix}.
\]

Foram obtidos:

\[
K_H\simeq1.93,
\qquad
\chi_A=J K_A^{-1}J^\top\simeq0.222954,
\]

\[
K_{\rm Schur}=K_H-\chi_A\simeq1.707046,
\qquad
\chi_2=J K_A^{-2}J^\top\simeq0.159323.
\]

O melhor candidato não ajustado foi o de resposta de segunda ordem:

\[
\mu_A^{\rm Schur}\simeq0.554522,
\qquad
\Theta_A^{\rm Schur}\simeq0.616922.
\]

Comparado ao par efetivo ajustado:

\[
\mu_A^{\rm fit}\simeq0.573747,
\qquad
\Theta_A^{\rm fit}\simeq0.721528,
\]

a escala de admitância saiu muito próxima, enquanto a largura térmica residual
ainda ficou menor. O erro RMS em \(\beta\) do candidato Schur foi:

\[
0.1028,
\]

contra:

\[
0.0896
\]

do ajuste efetivo.

Conclusão:

\[
\boxed{
\text{a derivação Schur reduzida praticamente recupera a admitância térmica,
mas ainda não fecha a largura de banho/contorno.}
}
\]

Isso desloca a pendência para os modos de banho/aparelho ausentes e para a
mobilidade causal, não para a existência da rota.

### 17.8 Comparação direta com a Fig. 2D

A comparação direta entre a série digitizada da Fig. 2D de Parsons et al. e a
predição GDQ-Schur foi salva em:

\[
\boxed{
\texttt{questoes/q25/resultados/saida\_q25\_20\_compare\_schur\_curve.md}
}
\]

A tabela é:

| \(k_BT/t\) | \(C_s(1)_{\rm exp}\) | \(\beta_{\rm Schur}\) | \(C_s(1)_{\rm GDQ-Schur}\) | desvio |
|---:|---:|---:|---:|---:|
| 0.00 | -0.350 | 0.8989 | -0.4509 | -5.04σ |
| 0.45 | -0.210 | 0.5197 | -0.2107 | -0.04σ |
| 0.55 | -0.240 | 0.4752 | -0.1801 | +2.99σ |
| 0.90 | -0.110 | 0.3656 | -0.1296 | -0.98σ |
| 1.50 | -0.050 | 0.2619 | -0.0936 | -2.18σ |

Portanto, no regime intermediário \(k_BT/t=0.45\), a comparação fica
praticamente exata dentro da incerteza de digitização. Em \(k_BT/t=0.90\),
permanece dentro de aproximadamente \(1\sigma\). Nos extremos térmicos, a
correlação GDQ-Schur ainda é forte demais. O ponto \(0.55\) deve ser tratado
com cautela porque a digitização fornecida o torna mais negativo que o ponto
\(0.45\), quebrando a monotonicidade térmica esperada.

### 17.9 Correção espectral da largura de banho

Foi implementada uma primeira correção espectral para a largura térmica
residual:

\[
\boxed{
\texttt{questoes/q25/associados/q25\_21\_bath\_width\_correction.py}
}
\]

A diferença a explicar era:

\[
\Delta\Theta_A
=
\Theta_A^{\rm fit}-\Theta_A^{\rm Schur}
\simeq
0.104606.
\]

Foram testadas somas espectrais sobre os modos do aparelho:

\[
\Delta\Theta_A
\sim
\sum_k
\frac{|J_k|^2}{\lambda_k(\lambda_k+K_{\rm Schur})},
\]

e variantes próximas. O melhor candidato espectral obteve:

\[
\Delta\Theta_A^{\rm bath}
\simeq
0.074983,
\]

levando a:

\[
\Theta_A^{\rm Schur+bath}
\simeq
0.691904.
\]

Comparado ao valor efetivo:

\[
\Theta_A^{\rm fit}
\simeq
0.721528,
\]

resta:

\[
\Delta\Theta_A^{\rm residual}
\simeq
0.0296.
\]

Conclusão:

\[
\boxed{
\text{a correção espectral do banho explica a maior parte da largura residual,
mas ainda não toda.}
}
\]

O resíduo restante é pequeno o bastante para ser atribuído, de forma
conservadora, a mobilidade causal, pesos térmicos reais do aparelho ou canais
dissipativos ainda omitidos no modelo reduzido.

Status atualizado:

\[
\boxed{
\text{Q25: fechada estruturalmente e operacionalmente no benchmark reduzido;
refinamentos metrológicos ficam como possibilidades futuras.}
}
\]

As pendências restantes não reabrem a questão principal. Elas foram movidas
para `ideias/possibilidades.md` como refinamentos: redigitalização de dados,
extração de novos experimentos, Hessiana completa do aparelho, derivação do
resíduo \(\Delta\Theta_A^{\rm residual}\simeq0.0296\) e cota assintótica de
variância/complexidade.
