# Q28 — Auditoria das três rotas propostas para o cobordismo $W_9$

## 1. Critério

Uma rota só pode determinar

$$
k=\operatorname{SF}(D_\tau)=3
$$

se especificar, sem usar o alvo:

1. a ação do grupo sobre o espaço-base e sobre a fibra;
2. o domínio ou cobordismo;
3. o operador tangencial e suas condições de contorno;
4. as representações de isotropia nos pontos fixos;
5. a contribuição assinada de cada setor ao índice.

## 2. Rota do orbifold $\mathbb Z_6$

### 2.1 O $\mathbb Z_6$ já derivado

Na construção vigente, o quociente aparece como cociclo projetivo das
holonomias internas:

$$
U_iU_j=\omega^{n_{ij}}U_jU_i,
\qquad
\omega=e^{2\pi i/6}.
$$

Essa é uma ação na **fibra**. Ela restringe a descida das representações e
produz a sub-rede $A\in6\mathbb Z$, mas não define uma ação

$$
\mathbb Z_6\curvearrowright T^5\times S^3
$$

no espaço-base. Sem uma ação na base não há locus fixo geométrico ao qual
aplicar uma fórmula de Kawasaki.

### 2.2 O subgrupo $\mathbb Z_3$ não implica três pontos fixos

Mesmo introduzindo uma ação geométrica adicional, a ordem do grupo não é o
número de pontos fixos. No toro elíptico de rede de Eisenstein, a rotação por
$\omega_3=e^{2\pi i/3}$ possui

$$
N_{\rm fix}=|\det_{\mathbb R}(I-M_{\omega_3})|=3.
$$

Mas em dimensão complexa $d$, para a ação diagonal,

$$
N_{\rm fix}=3^d.
$$

Logo:

$$
d=1\Rightarrow3,
\qquad
d=2\Rightarrow9,
\qquad
d=4\Rightarrow81.
$$

Se a rotação agir somente numa direção complexa, surgem três **componentes
fixas positivas-dimensionais**, não três pontos isolados. Além disso,
$T^5\times S^3$ não vem equipado, pelos dados atuais, com a estrutura de toro
complexo diagonal necessária a esse cálculo.

### 2.3 Contribuição de Kawasaki

Uma componente fixa não contribui automaticamente com uma unidade. A
contribuição depende dos pesos da ação no fibrado normal e no fibrado de
coeficientes. Esquematicamente,

$$
\operatorname{Ind}_{\rm orb}(D_E)
=\sum_{[g]}
\int_{M^g}
\frac{\widehat A(M^g)\operatorname{ch}_g(E)}
{\det^{1/2}(1-g\,e^{-R_N/2\pi i})}.
$$

Portanto,

$$
\#\operatorname{Fix}(g)=3
\not\Rightarrow
\operatorname{Ind}_{\rm orb}=3.
$$

### 2.4 Veredito da rota 1

A rota é matematicamente investigável, mas **não decorre do $\mathbb Z_6$ já
derivado**. Ela exigiria uma nova ação do grupo sobre a base, a escolha de uma
rede compatível e a especificação das representações de isotropia. Escolher
uma ação somente porque ela possui três pontos fixos seria circular.

## 3. Rota da trialidade de $\operatorname{Spin}(8)$

$\operatorname{Spin}(8)$ possui as representações $8_v$, $8_s$ e $8_c$
permutadas por um automorfismo externo de ordem três. Contudo:

1. dimensão real oito não implica que a trialidade seja uma simetria do
   background;
2. a estrutura Hermitiana da GDQ reduz o grupo estrutural e pode quebrar a
   trialidade;
3. vetor e espinores não são automaticamente três cópias do mesmo kernel;
4. uma órbita de três representações não determina o número assinado de
   cruzamentos de autovalores.

Para essa rota funcionar seria necessário construir um fibrado com
monodromia explícita no grupo de automorfismos externos e provar que a
Hessiana oficial comuta com ela. Nada disso foi derivado até agora.

Assim,

$$
\boxed{
\text{trialidade permite tripletos, mas não força }
\operatorname{SF}=3.
}
$$

## 4. Rota de $\mathbb CP^2$

É verdade que

$$
\chi(\mathbb CP^2)=3,
\qquad
\sigma(\mathbb CP^2)=1.
$$

Mas a característica de Euler não é o índice de Dirac procurado. Além disso,
$\mathbb CP^2$ não é spin; uma construção de Dirac exige ao menos uma
estrutura $\operatorname{spin}^c$ e a escolha de sua linha determinante. A
nucleação de uma componente $\mathbb CP^2$ também não é consequência conhecida
do fluxo utilizado pela ação oficial.

Logo,

$$
\chi(\mathbb CP^2)=3
\not\Rightarrow
\operatorname{Ind}D=3.
$$

Introduzir $\mathbb CP^2$ por possuir Euler três seria engenharia reversa, a
menos que a dinâmica cosmológica a selecione independentemente.

## 5. Comparação

| Rota | Estrutura matemática real | O que falta | Status |
|---|---|---|---|
| Orbifold $\mathbb Z_6$ | cociclo projetivo na fibra | ação na base, locus fixo, pesos de isotropia e resolução | investigável, ainda não derivada |
| Trialidade $\operatorname{Spin}(8)$ | automorfismo externo de ordem três | provar simetria da Hessiana e monodromia cosmológica | possibilidade abstrata |
| Nucleação de $\mathbb CP^2$ | $\chi=3$, $\sigma=1$ | seleção dinâmica, estrutura $\operatorname{spin}^c$ e índice correto | atualmente ad hoc |

## 6. Decisão sem circularidade

A rota 1 é a única que reutiliza uma estrutura já presente, mas o primeiro
passo não é definir

$$
W_9=[0,1]\times(T^5\times S^3)/\mathbb Z_6.
$$

Esse produto é apenas um cilindro orbifold e não descreve por si só uma
resolução. O primeiro passo correto é determinar se o cociclo projetivo da
fibra admite ou exige uma extensão para uma ação efetiva na base:

$$
\varphi:\mathbb Z_6\longrightarrow
\operatorname{Diff}(T^5\times S^3)
$$

compatível com a métrica, a estrutura Hermitiana, o ciclo térmico e a ação
oficial.

Se nenhuma extensão for exigida, a rota de Kawasaki não pertence ao modelo
vigente. Se houver extensões, todas as classes admissíveis devem ser
classificadas antes de observar suas contagens de pontos fixos. Somente então
é lícito calcular o índice orbifold.

## 7. Veredito

As três ideias são possibilidades de pesquisa, mas nenhuma calcula
atualmente $A=18$. Em particular,

$$
\boxed{
\mathbb Z_3\subset\mathbb Z_6
\not\Rightarrow
3\text{ pontos fixos}
\not\Rightarrow
\operatorname{SF}=3.
}
$$

A próxima pergunta não circular é binária:

$$
\boxed{
\text{o }\mathbb Z_6\text{ de hipercarga age apenas na fibra ou a GDQ exige
uma ação correspondente na base?}
}
$$

Com os documentos atuais, ele age apenas na fibra. Portanto, a construção de
um orbifold cosmológico deve permanecer como possibilidade adicional, não
como continuação já derivada da Q28.

