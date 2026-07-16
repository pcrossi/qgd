# Plano de demonstração da ponte espectral global--local da GDQ

## 1. Objetivo

Construir e demonstrar, sem alterar a ação oficial, uma ponte matemática entre
o espaço cosmológico/espectral global

$$
M_E=T^5\times S^3
$$

e o bulk local oficial

$$
M_P=\mathbb R^4\times T^4.
$$

A ponte deve explicar rigorosamente como a identidade espectral global de um
modo localizado é transportada para o problema planar, no qual fontes,
aparelhos, condições de contorno e espalhamento determinam sua resposta.

O resultado pretendido não é a invariância de todo o espectro. A
descompactificação transforma parte do espectro discreto em espectro
contínuo. O objetivo preciso é provar a persistência dos setores físicos
localizados pelo estômato.

---

## 2. Enunciado de trabalho

Usando a decomposição

$$
T^5=T^4\times S^1,
$$

definir a família de variedades apontadas

$$
\boxed{
M_\varepsilon
=
T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon},
\qquad
L_\varepsilon,R_\varepsilon\longrightarrow\infty
\quad(\varepsilon\downarrow0).
}
$$

A escolha inicial mínima será

$$
L_\varepsilon=R_\varepsilon=\varepsilon^{-1},
$$

mas a prova deverá registrar quais resultados continuam válidos quando
$L_\varepsilon/R_\varepsilon$ tende a uma constante positiva diferente de
um.

Escolhendo pontos-base $p_\varepsilon$ no centro do estômato, pretende-se
provar

$$
(M_\varepsilon,g_\varepsilon,p_\varepsilon)
\xrightarrow[\varepsilon\downarrow0]{C^k\text{ apontado}}
(\mathbb R^4\times T^4,g_P,p_P).
$$

Sobre essa família serão transportados a estrutura Hermitiana, a conexão de
Bismut, a torção, o campo complexo, a medida ponderada, a Hessiana da ação
oficial e seus setores espectrais localizados.

---

## 3. Dados que devem ser fixados antes da prova

### 3.1 Background global

Especificar, para cada $\varepsilon$,

$$
\mathfrak B_\varepsilon
=
(g_\varepsilon,J_\varepsilon,H_\varepsilon,
f_\varepsilon,\mathcal U_\varepsilon,\gamma_\varepsilon),
$$

e demonstrar que ele é admissível para a ação oficial ou declarar exatamente
qual parte é background cosmológico auxiliar.

### 3.2 Estômato e ponto-base

Definir uma vizinhança $\mathcal N_\varepsilon$ do defeito, sua seção
$S^3$, sua carga topológica e as condições de regularidade ou de interface.
O ponto-base não pode ser escolhido numa região que elimine o defeito no
limite.

### 3.3 Espaços de Hilbert

Definir

$$
\mathcal H_\varepsilon
=
L^2(M_\varepsilon,E_\varepsilon,
\mathcal U_\varepsilon d\operatorname{vol}_{g_\varepsilon})
$$

e

$$
\mathcal H_P
=
L^2(M_P,E_P,
\mathcal U_Pd\operatorname{vol}_{g_P}),
$$

incluindo o fibrado, a estrutura de spin ou $\operatorname{spin}^c$, o
domínio do operador e as condições de contorno.

### 3.4 Observáveis a transportar

Separar desde o início:

1. invariantes topológicos: índice, carga, classe de Chern e fluxo espectral;
2. dados espectrais: autovalores ligados, multiplicidades e gap;
3. normalizações contínuas: massas dimensionais e acoplamentos;
4. respostas locais: deslocamentos, larguras, taxas e fatores de forma.

---

## 4. Lema 1 -- Construção da família geométrica

### Enunciado pretendido

Existe uma família suave de métricas e estruturas compatíveis sobre

$$
M_\varepsilon
=T^4\times S^1_{\varepsilon^{-1}}
\times S^3_{\varepsilon^{-1}}
$$

que contém o estômato com carga fixada e admite cartas de raio crescente em
torno de $p_\varepsilon$.

### Tarefas

1. Fixar as métricas normalizadas em $T^4$, $S^1$ e $S^3$.
2. Escrever explicitamente $g_\varepsilon$, inicialmente no produto e depois
   com a deformação localizada do estômato.
3. Construir $J_\varepsilon$ e verificar sua compatibilidade Hermitiana.
4. Construir $H_\varepsilon$ e verificar as condições de Bismut adotadas.
5. Fixar a classe topológica do defeito independentemente de $\varepsilon$.
6. Verificar dimensões, completude e regularidade uniforme fora do núcleo.

### Critério de aceitação

Fornecer fórmulas explícitas para os dados da família e provar que não há
mudança silenciosa de topologia, dimensão ou ação fundamental.

### Produto

Uma seção matemática contendo o ansatz completo e um verificador simbólico
das identidades métricas e de torção.

---

## 5. Lema 2 -- Convergência geométrica apontada

### Enunciado pretendido

Para todo compacto $K\subset\mathbb R^4\times T^4$, existem, para
$\varepsilon$ suficientemente pequeno, imersões

$$
\iota_\varepsilon:K\longrightarrow M_\varepsilon
$$

tais que

$$
\iota_\varepsilon^*g_\varepsilon\longrightarrow g_P
$$

em $C^k(K)$, com controle uniforme da curvatura e do raio de injetividade.

### Construção esperada

Usar coordenada reescalada no círculo e coordenadas normais na esfera:

$$
S^1_{L_\varepsilon}\longrightarrow\mathbb R,
\qquad
S^3_{R_\varepsilon}\longrightarrow\mathbb R^3.
$$

Consequentemente,

$$
T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon}
\longrightarrow
T^4\times\mathbb R\times\mathbb R^3
=T^4\times\mathbb R^4.
$$

### Tarefas

1. Calcular a expansão da métrica de $S^3_R$ em coordenadas normais.
2. Estimar o erro $O(R_\varepsilon^{-2}|x|^2)$ em cada compacto.
3. Demonstrar convergência das conexões e curvaturas.
4. Verificar que a deformação do estômato tem um limite local não trivial.
5. Distinguir convergência apontada de equivalência topológica global.

### Critério de aceitação

Prova com estimativas explícitas em compactos. A frase “o espaço fica plano”
não é suficiente.

---

## 6. Lema 3 -- Transporte dos campos e da Hessiana oficial

### Enunciado pretendido

Existem identificações locais unitárias

$$
U_\varepsilon:
\mathcal H_\varepsilon^{\rm loc}\longrightarrow\mathcal H_P
$$

tais que, sobre um núcleo comum de funções teste,

$$
\iota_\varepsilon^*J_\varepsilon\to J_P,
\qquad
\iota_\varepsilon^*H_\varepsilon\to H_P,
$$

$$
\iota_\varepsilon^*f_\varepsilon\to f_P,
\qquad
\iota_\varepsilon^*\mathcal U_\varepsilon\to\mathcal U_P,
$$

e as formas quadráticas da Hessiana convergem:

$$
q_\varepsilon[U_\varepsilon^{-1}\Psi]
\longrightarrow q_P[\Psi].
$$

### Definição inicial do transporte

Usar

$$
U_\varepsilon\Psi
=J_{\iota_\varepsilon}^{1/2}
\,\iota_\varepsilon^*\Psi,
$$

com o jacobiano e a medida ponderada incluídos na condição de unitariedade.

### Tarefas

1. Variar duas vezes a ação oficial no background $\mathfrak B_\varepsilon$.
2. Exibir todos os blocos da Hessiana:

   $$
   K_\varepsilon=
   \begin{pmatrix}
   K_{gg}&K_{gf}&K_{gH}\\
   K_{fg}&K_{ff}&K_{fH}\\
   K_{Hg}&K_{Hf}&K_{HH}
   \end{pmatrix}.
   $$

3. Fixar gauge geométrico apenas como método de análise, sem mudar a ação.
4. Tratar modos zero, vínculos, bordo e complemento de Schur.
5. Provar coercividade uniforme no complemento dos modos de simetria.
6. Demonstrar convergência Mosco ou equivalente das formas quadráticas.
7. Verificar o transporte do contorno causal $\gamma$ e a dominação necessária
   para trocar limite e integração em $\tau$.

### Critério de aceitação

A Hessiana planar deve surgir como limite da segunda variação oficial, não
como operador escolhido por analogia com Dirac, Yang--Mills ou o Modelo
Padrão.

---

## 7. Lema 4 -- Localização e gap uniforme dos modos do estômato

### Enunciado pretendido

Existe um intervalo espectral isolado $I_a$ e uma constante
$\Delta_*>0$, independentes de $\varepsilon$, tais que os modos físicos do
estômato satisfazem

$$
\operatorname{spec}K_\varepsilon\cap I_a
=\{\lambda_{a,\varepsilon}\}
$$

e

$$
\operatorname{dist}
\left(
\lambda_{a,\varepsilon},
\operatorname{spec}K_\varepsilon
\setminus\{\lambda_{a,\varepsilon}\}
\right)
\geq\Delta_*.
$$

Além disso, as autofunções devem permanecer localizadas:

$$
\int_{d(x,\mathcal N_\varepsilon)>R}
|\Phi_{a,\varepsilon}|^2
\mathcal U_\varepsilon d\operatorname{vol}_{g_\varepsilon}
\leq Ce^{-2\mu R}.
$$

### Tarefas

1. Identificar o potencial efetivo criado pelo estômato na Hessiana completa.
2. Determinar o limiar do espectro essencial no limite planar.
3. Usar estimativas de Agmon ou método equivalente para localização.
4. Provar uma cota inferior uniforme no complemento do modo ligado.
5. Tratar separadamente modos topológicos zero e modos ligados não nulos.
6. Verificar estabilidade sob perturbações Robin, APS e DtN menores que o
   gap.
7. Registrar explicitamente qualquer setor em que o gap feche.

### Teste numérico de apoio

Discretizar uma sequência crescente de $(L_\varepsilon,R_\varepsilon)$ e
acompanhar:

- autovalores ligados;
- limiar do contínuo discretizado;
- massa fora de uma vizinhança fixa do estômato;
- sensibilidade às condições de contorno externas.

O teste numérico é evidência, não substitui a estimativa uniforme.

### Critério de aceitação

O gap deve ser demonstrado sem escolher parâmetros após observar massas ou
acoplamentos experimentais.

---

## 8. Lema 5 -- Convergência em resolvente e dos projetores de Riesz

### Enunciado pretendido

Para $z$ fora do espectro relevante,

$$
U_\varepsilon
(K_\varepsilon-z)^{-1}
U_\varepsilon^\dagger
\longrightarrow
(K_P-z)^{-1}
$$

fortemente, e idealmente em norma no setor ligado.

Para um contorno $\Gamma_a$ contido no gap uniforme,

$$
P_{a,\varepsilon}
=\frac{1}{2\pi i}
\oint_{\Gamma_a}
(K_\varepsilon-z)^{-1}dz
$$

satisfaz

$$
U_\varepsilon P_{a,\varepsilon}U_\varepsilon^\dagger
\longrightarrow P_{a,P}.
$$

### Rota de prova

1. Usar a convergência de formas do Lema 3.
2. Usar coercividade e gap do Lema 4.
3. Provar convergência do semigrupo:

   $$
   U_\varepsilon e^{-tK_\varepsilon}U_\varepsilon^\dagger
   \longrightarrow e^{-tK_P}.
   $$

4. Obter o resolvente pela transformada de Laplace quando as cotas permitirem.
5. Integrar o resolvente em $\Gamma_a$ para transportar o projetor.
6. Demonstrar constância da dimensão do autoespaço e convergência dos
   autovalores ligados.

### Critério de aceitação

Fornecer um teorema com topologia de convergência, domínio, conjunto de
$z$, uniformidade e tratamento explícito do espectro contínuo.

---

## 9. Lema 6 -- Separação entre topologia, espectro e normalização

### Enunciado pretendido

A ponte transporta diferentes classes de quantidades por mecanismos
distintos. Elas não devem ser reunidas sob uma alegação genérica de
“invariância espectral”.

### 9.1 Setor topológico

Calcular e comparar:

$$
\operatorname{Ind}_{\rm APS}D_\varepsilon^B,
\qquad
\operatorname{SF}(D_{\varepsilon,s}^B),
\qquad
c_k(E_\varepsilon),
\qquad
\operatorname{Hol}(\nabla_\varepsilon^B).
$$

Demonstrar sua preservação enquanto não houver fechamento do gap ou cirurgia.

### 9.2 Setor espectral ligado

Calcular

$$
\lambda_{a,P}
=\lim_{\varepsilon\to0}\lambda_{a,\varepsilon}
$$

e verificar multiplicidade e normalização dos modos transportados.

### 9.3 Setor de acoplamentos

Para cada modo de conexão $\Phi_{Q,\varepsilon}$, calcular sua norma física:

$$
\frac{1}{e_P^2}
=
\lim_{\varepsilon\to0}
\left\|U_\varepsilon\Phi_{Q,\varepsilon}\right\|_{
\mathcal U_P}^2,
$$

incluindo o complemento de Schur e os termos de interface derivados. A classe
de Chern pode quantizar a carga, mas não fixa sozinha a magnitude contínua do
acoplamento.

### 9.4 Observáveis locais

Após o transporte, calcular no bulk planar:

$$
K_{P,\rm eff}
=P_a(K_P+J_{\rm app}+\mathsf R_{\rm app})P_a,
$$

distinguindo identidade global de dressing, desdobramento, largura, taxa e
espalhamento.

### Critério de aceitação

Produzir uma tabela para cada aplicação da GDQ contendo:

- quantidade;
- mecanismo de transporte;
- hipótese usada;
- cálculo global;
- cálculo local;
- dependência de calibração;
- status preditivo.

---

## 10. Dependência lógica dos seis lemas

$$
\boxed{
L1\longrightarrow L2\longrightarrow L3
\longrightarrow L4\longrightarrow L5\longrightarrow L6.
}
$$

O Lema 4 é o ponto crítico. Sem localização e gap uniforme, a convergência
geométrica ainda existe, mas não preserva necessariamente os estados físicos
discretos.

O Lema 6 não pode ser antecipado usando concordância numérica. Primeiro se
prova o transporte; depois se calculam os observáveis.

---

## 11. Ordem operacional de execução

### Fase A -- Geometria e campos

1. finalizar Lema 1;
2. provar Lema 2;
3. construir o pullback de $J,H,f,\mathcal U$;
4. obter a Hessiana reduzida necessária ao Lema 3.

### Fase B -- Análise espectral

1. identificar o operador transversal do estômato;
2. provar localização;
3. estabelecer o gap;
4. provar convergência de formas, semigrupo e resolvente;
5. transportar os projetores de Riesz.

### Fase C -- Aplicações

Aplicar o mesmo teorema, sem reconstruí-lo, a:

1. Q28: índices, três gerações, cargas e normas de calibre;
2. Q29: normalização eletrofraca e transporte de $g,g'$;
3. Q37: normalização eletromagnética e $\alpha$;
4. Q38: separação entre dado cosmológico global e resposta gravitacional
   local;
5. Q39: transporte do espectro leptônico;
6. Q40: identidade bariônica global e resposta/cirurgia planar.

---

## 12. Testes de falsificação

A ponte será rejeitada ou restringida se ocorrer qualquer um dos seguintes
casos:

1. o background não satisfaz a variação da ação oficial no regime declarado;
2. $J_\varepsilon$ ou $H_\varepsilon$ não possui limite compatível com o bulk
   oficial;
3. a medida normalizada desaparece localmente sem localização do estômato;
4. o gap fecha durante a descompactificação;
5. o modo ligado dissolve-se no contínuo;
6. os domínios auto-adjuntos não convergem;
7. o índice muda sem fluxo espectral ou cirurgia identificável;
8. a normalização de um acoplamento diverge ou tende a zero;
9. o valor fenomenológico só aparece após seleção de contorno ou coeficiente
   pelo alvo.

Um resultado negativo deve identificar quais quantidades ainda podem ser
transportadas. A falha de uma massa não invalida automaticamente o transporte
de um índice topológico.

---

## 13. Critério de fechamento da ponte

A ponte global--local será considerada demonstrada somente quando houver:

1. família geométrica explícita e admissível;
2. convergência apontada com estimativas;
3. transporte convergente de $g,J,H,f,\mathcal U$ e $\gamma$;
4. Hessiana derivada da ação oficial;
5. domínio auto-adjunto e vínculos definidos;
6. localização exponencial dos modos físicos;
7. gap uniforme;
8. convergência em resolvente;
9. convergência dos projetores de Riesz;
10. separação demonstrada entre índice, autovalor e norma de acoplamento;
11. pelo menos uma aplicação não usada na construção reproduzida sem
    pós-ajuste;
12. atualização consistente de `memory.md`, `faltas.md`, `faltas_mapa.md` e
    dos documentos das questões afetadas.

### Status inicial

$$
\boxed{
\text{rota geométrica identificada; seis lemas planejados; prova ainda aberta.}
}
$$

O primeiro trabalho executável é o Lema 1: escrever o background explícito
$\mathfrak B_\varepsilon$, incluindo a geometria localizada do estômato, e
verificar sua compatibilidade com a estrutura Hermitiana--Bismut usada pela
ação oficial.

---

## 14. Registro de execução

### Etapa 1 — iniciada

O arquivo `ponte_global_local_lema1.md` construiu explicitamente a família
homogênea

$$
T^4_{\mathbb C}\times(S^1\times S^3)_{\rm Hopf},
$$

incluindo coframe, estrutura complexa, forma Hermitiana e torção de Bismut.
Também foram identificadas duas condições que não podem ser omitidas:

1. a carga do estômato deve ser relativa/localizada, pois o fluxo da torção
   homogênea escala com $R_\varepsilon^2$;
2. a medida deve formar uma família tight para não desaparecer localmente no
   limite de volume infinito.

Status atual:

$$
\boxed{
L1A\text{ concluído};
\qquad
L1B\text{ possui redução radial explícita, mas requer existência da sela.}
}
$$

### Etapa 2 — redução localizada construída

Em `ponte_global_local_lema1.md` foi fixado um colar de Berger com funções
$a(r),c(r)$ e campo $f=u+iv$. Foram derivados diretamente

$$
H=2c(aa'-c)\,\sigma_1\wedge\sigma_2\wedge\sigma_3,
$$

$$
|H|^2=24\frac{(aa'-c)^2}{a^4},
$$

o escalar de Levi--Civita e o funcional radial da ação oficial com
$\mathcal R_{\rm GDQ}=R_{\rm LC}-|H|^2/12$.

Também foi demonstrado que uma carga strong-KT não nula não pode residir num
colar único, suave, completo e assintoticamente plano sem interface. A carga
do estômato deve ser uma classe relativa no bordo interno. O próximo passo é
derivar o funcional bulk--interface e as EDOs métricas completas.

### Etapa 3 — Lema 2A demonstrado

O arquivo `ponte_global_local_lema2.md` construiu as imersões apontadas e
demonstrou

$$
T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon}
\longrightarrow T^4\times\mathbb R^4
$$

em $C^k$ apontado, com erro $O(R_\varepsilon^{-2})$ em compactos. O setor
localizado foi formulado em $C^{k,\alpha}_{\rm loc}$ e permanece condicional à
existência da sela do Lema 1B. O mesmo cálculo recupera
$R^{-1}\cot(r/R)\to1/r$ fora da fonte.

### Etapa 4 — Hipótese BI e Lema 3A

A existência da sela localizada foi isolada em
`ponte_global_local_hipotese_BI.md` como hipótese técnica futura, com nove
condições auditáveis. Sob essa hipótese, `ponte_global_local_lema3.md`
construiu o transporte isométrico ponderado e demonstrou a convergência da
segunda variação oficial em um núcleo comum.

O espaço físico de variações é $(\delta g,\delta f)$, com
$\delta H=\delta(d^c_J\omega)$ vinculado; não há bloco torsional independente.
A condição de recuperação de Mosco foi obtida. A condição liminf global exige
localização/coercividade e, portanto, será tratada junto ao Lema 4.

### Etapa 5 — critério do Lema 4

`ponte_global_local_lema4.md` demonstrou um critério suficiente de gap e a
estimativa uniforme de Agmon sob seis desigualdades quantitativas. A aplicação
ao Jacobi radial da Q29 mostrou que sua matriz principal é indefinida antes da
restrição do lapse e da remoção da reparametrização. Portanto, o gap ainda não
está demonstrado para a GDQ.

O cálculo decisivo, após obter um background BI, é construir
$P^{\rm phys}$, verificar sua positividade uniforme, calcular o limiar
$\Sigma_*$ e provar que o quociente de Rayleigh do modo do estômato permanece
separado desse limiar.

### Etapa 6 — Lema 5 condicional demonstrado

`ponte_global_local_lema5.md` combinou a convergência de formas do Lema 3 com
a localização e o gap do Lema 4. Foram obtidos, sob BI e L4.1--L4.6,
resolvente forte, semigrupo forte, projetores de Riesz e convergência em norma
no cluster ligado de posto finito. A multiplicidade é preservada porque o gap
e a estimativa min--max fixam previamente o posto; convergência forte isolada
não seria suficiente.

O resultado não afirma convergência em norma no espectro contínuo nem fixa
normalizações de acoplamentos.

### Etapa 7 — Lema 6 concluído

`ponte_global_local_lema6.md` separou os quatro mecanismos da ponte:
topologia/índice, espectro ligado/projetores, normalizações/formas quadráticas
e resposta local/fontes. Foi demonstrado que classes inteiras não determinam
automaticamente acoplamentos contínuos, que autovalores adimensionais não
fixam massas absolutas e que a Hessiana não fornece sozinha uma escala de
tempo.

Com isso, os seis lemas estão formulados. L1B e a verificação quantitativa de
L4 permanecem como problemas físicos abertos; L3--L5 são teoremas
condicionais a esses dados.
