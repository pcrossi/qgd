# Auditoria e preparação numérica das Portas B/D

## 1. Escopo

O solver histórico `ponte_global_local_solver_final.py` foi preservado sem
alterações. Foi criada uma implementação separada,
`ponte_global_local_solver_portas_bd.py`, para preparar a busca da sela sem
fixar a normalização energética pelo alvo.

Classificação: infraestrutura numérica e teste de consistência. Não é uma
solução da sela nem uma avaliação do gap.

## 2. Erros e limitações encontrados no solver histórico

### 2.1 Normalização energética embutida

O arquivo histórico define

$$
E_H^{\rm hat}=1
$$

e usa diretamente

$$
\frac{p_0e^{-x_0}}{Z}-1=0.
$$

Isso equivale ao caso exploratório $K_\gamma=1$. Como $K_\gamma$ ainda deve
ser derivado pela Porta A, essa linha não pode participar de uma alegação de
sela física.

### 2.2 Jacobiana por diferenças de soluções completas

O otimizador histórico usa `jac='3-point'` e a auditoria final repete
integrações completas perturbadas. Em trajetórias rígidas, essa operação
mistura erro de integração, passo de diferença e derivada do mapa de tiro.

### 2.3 Critério insuficiente para a Porta D

A Jacobiana dos resíduos mede o condicionamento da busca não linear. Ela não
é a Hessiana física

$$
\mathbb H_*
=D_X^2\mathcal S_{\rm GDQ}
-\lambda^aD_X^2\mathcal C_a
$$

e, portanto, seus valores singulares não constituem um espectro de
estabilidade.

## 3. Correções implementadas

### 3.1 Interface energética obrigatória

Sem energia fornecida, o novo módulo retorna deliberadamente o sistema
retangular

$$
\mathfrak F_B:\mathbb R^{11}\longrightarrow\mathbb R^{10}.
$$

O décimo primeiro vínculo só é acrescentado por uma função externa que
retorne

$$
\left(
\mathcal C_E,
D_q\mathcal C_E,
D_\theta^{\rm explícito}\mathcal C_E
\right).
$$

O adaptador `energy_ratio_from_porta_a` exige $K_\gamma>0$ como argumento e
não possui valor padrão. Assim, a Porta B não pode escolher silenciosamente
$K_\gamma=1$.

### 3.2 Transporte variacional

Para cada domínio são integradas simultaneamente

$$
\dot Y=F(Y,\theta),
$$

$$
\dot S
=D_YF\,S+D_\theta F,
\qquad
S=D_\theta Y.
$$

As derivadas locais de $F$ são calculadas por passo complexo, enquanto a
Jacobiana do mapa global resulta do transporte de $S$ e das regras de cadeia
exatas nas interfaces.

### 3.3 Busca condicional

`solve_porta_b` exige explicitamente o funcional energético da Porta A, usa a
Jacobiana transportada no `least_squares` e reavalia o candidato com
tolerâncias mais estritas. O campo `accepted_algebraically` verifica apenas:

$$
\|\mathfrak F\|_\infty<10^{-9}
$$

e posto onze. Os demais critérios físicos da Porta B continuam obrigatórios.

## 4. Testes independentes de $K_\gamma$

O teste `teste_ponte_global_local_solver_portas_bd.py` foi executado na
semente histórica.

Para os dez vínculos que independem da energia:

$$
\operatorname{rank}D\mathfrak F_B=10,
\qquad
D\mathfrak F_B\in\mathbb R^{10\times11}.
$$

O erro direcional relativo entre a Jacobiana variacional e uma diferença
central independente do mapa completo foi

$$
1{,}6586\times10^{-4}.
$$

Os valores singulares foram

$$
\begin{aligned}
(&7{,}9439\times10^3,
2{,}2638\times10^3,
1{,}1943\times10^3,
4{,}2996\times10^2,
7{,}8532,
4{,}5898,\\
&7{,}5969\times10^{-1},
3{,}5924\times10^{-3},
2{,}5153\times10^{-3},
5{,}2179\times10^{-4}).
\end{aligned}
$$

Foi também testada a regra da cadeia da interface energética com um valor
sintético $K=2$. Esse número é exclusivamente um fixture de software, não
foi usado numa busca e não possui interpretação física. O erro direcional foi

$$
3{,}3936\times10^{-4}.
$$

## 5. Situação das portas

- Porta A: ainda deve fornecer o funcional energético físico e sua derivada;
- Porta B: infraestrutura variacional pronta, mas a busca física aguarda a
  Porta A;
- Porta C: requer a sela e os multiplicadores para construir a Hessiana do
  funcional aumentado;
- Porta D: não pode ser executada antes da Porta C. A Jacobiana do tiro não
  substitui o operador espectral.

O próximo teste legítimo, após a Porta A, é executar `solve_porta_b`, verificar
a independência da linha energética na SVD e reproduzir a candidata por uma
discretização de colocação multidomínio.

## 6. Execução com o projetor causal normalizado

O documento `q29/projetor_causal_cauchy_normalizado.md` fixou, no setor
estacionário vigente,

$$
K_\gamma=1.
$$

Esse valor foi então fornecido ao callback da Porta A e mantido congelado.
Não participou de otimização.

Uma homotopia separada moveu primeiro o raio e depois a energia. O raio chegou
ao valor cosmológico. A continuação energética regular alcançou
$h=0{,}20$, mas a menor singular da Jacobiana caiu de
$8{,}00\times10^{-5}$ em $h=0{,}16$ para $3{,}22\times10^{-5}$ em
$h=0{,}20$. Um salto direto para $h=0{,}21$ perdeu o ramo.

Foi implementada continuação pseudo-arclength em
`ponte_global_local_pseudo_arclength.py`. Antes de aceitá-la, porém, a base foi
auditada com integração estrita e Jacobiana central. O melhor ponto em
$h=0{,}18$ permaneceu em

$$
\|\mathfrak F\|_\infty
=1{,}2899\times10^{-4},
$$

na mesma escala do erro direcional anterior. Newton com Jacobiana central não
encontrou passo descendente. Portanto a pseudo-curva exploratória foi
corretamente suspensa: ela não constitui continuação de raízes exatas.

## 7. Ampliação anisotrópica mínima testada

O resíduo dominante estava no matching dos momentos $(p_a,p_c,p_u)$. Foi
criado `ponte_global_local_extensao_pc.py`, preservando o solver 11D, para
liberar $p_c$ nas duas gargantas.

O valor inicial de $u$ foi recalculado pela restrição interna

$$
\mathcal C_{\rm inner}=0,
$$

em vez de reutilizar a fórmula válida somente para $p_c=0$. O mapa revelou
sensibilidade da ordem $10^5$ a $p_c$ e exigiu passos centrais absolutos de
$10^{-9}$.

Nem o modo antipodal único nem os dois momentos independentes reduziram a
norma. O otimizador retornou

$$
p_c^L\simeq3{,}02\times10^{-13},
\qquad
p_c^R\simeq-3{,}67\times10^{-13},
$$

e

$$
\|\mathfrak F\|_\infty
=1{,}2899\times10^{-4}.
$$

Assim, a liberação local de $p_c$ foi excluída como cura da obstrução nesse
ramo. Como a ampliação possui mais variáveis que condições, ela é apenas um
diagnóstico de suficiência do ansatz, não uma nova sela física.

Uma auditoria posterior da expansão local, registrada em
`ponte_global_local_regularidade_garganta.md`, mostrou um resultado mais
forte. Para uma garganta de reflexão suave,

$$
\dot a(0)=\dot c(0)=\dot u(0)=0,
$$

e as equações canônicas com $h_0=-2c_0^2$ implicam unicamente

$$
p_c(0)=p_u(0)=0.
$$

Portanto, o plano $(p_c,p_u)$ não é um par de dados regulares omitidos pelo
solver. Liberá-lo exigiria trocar a garganta por uma fronteira Robin com
fonte derivada, ou restaurar campos adicionais — em particular um modo de
$J$ — que modifiquem a própria relação momento--velocidade.

## 8. Veredito atualizado

Com $K_\gamma=1$ derivado e congelado, não foi encontrada raiz da Porta B no
ramo conectado à semente histórica. A obstrução não foi removida por:

1. aumento de tolerância;
2. Jacobiana central independente;
3. continuação energética fina;
4. pseudo-arclength, que não passou pelo critério de base exata;
5. liberação dos momentos anisotrópicos iniciais.

Logo não há dados legítimos para as Portas C/D. O próximo aumento do ansatz
deve ser escolhido a partir do matching conjunto dos três momentos, e não por
novo ajuste da energia ou do raio.
