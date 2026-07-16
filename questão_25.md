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
