# Formalização Lean da GDQ

Índice módulo por módulo:

- [Índice canônico das provas Lean](index.md)

Este diretório inicia a formalização verificável da Geometrodinâmica
Quântica.

## Projetor físico

O módulo `GDQ/PhysicalProjector.lean` substitui o projetor abstrato por uma
construção ortogonal:

$$
V_{\rm phys}=V_{\rm adm}\cap G^\perp.
$$

Para vínculos linearizados, usa `V_adm=ker DC`. Em dimensão finita a
existência da projeção é automática; em dimensão infinita permanece
explicitamente condicionada ao fechamento/completude do subespaço. O módulo
prova idempotência, auto-adjunticidade, anulação do gauge, auto-adjunticidade
de `P H P` e a passagem de coercividade restrita para gap físico.

O módulo `GDQ/VariationalDynamics.lean` fecha a precedência lógica entre as
camadas. Ele prova que a estacionariedade não projetada equivale ao gradiente
nulo, que a estacionariedade vinculada equivale à componente física do
gradiente nula, que a Hessiana é a derivada desse gradiente na sela e que
`P H P` é somente a restrição da dinâmica linearizada. Assim, projetores e
operadores espectrais não são postulados adicionais da ação oficial.

## Reconstrução OS/Hilbert

`GDQ/OSReconstruction.lean` formaliza o quociente do domínio positivo pela
seminorma nula e seu completamento complexo. A relação
`N + G = N` é provada somente sob a hipótese explícita de que o gauge é nulo
para o pareamento OS. `GDQ/OSReconstructedEvolution.lean` distingue o
semigrupo contrativo euclidiano do grupo isométrico em tempo físico e prova
as propriedades dos pesos espectrais modo a modo. A positividade OS e o
gerador autoadjunto de um background concreto continuam obrigações
analíticas visíveis.

## Fonte clássica e readout

`GDQ/ClassicalApparatusResponse.lean` formaliza
`δΦ=K_phys⁻¹J_app` e a eliminação exata do interior pelo complemento de
Schur. `GDQ/ApparatusBornReadout.lean` exige que os canais diagonalizem a
Hessiana complexificada e prova positividade e normalização dos pesos de
Born do estado-resposta. `GDQ/QNDBornBasins.lean` descarrega a
correspondência Born--bacias na classe finita QND gaussiana: prova a
normalização dos posteriores, a conservação de sua esperança e a igualdade
entre peso inicial e medida da bacia absorvente. Fora dessa classe, a
realização dinâmica permanece uma hipótese a demonstrar.

## Stern--Gerlach reduzido

`GDQ/SternGerlachProjectors.lean` e
`GDQ/SternGerlachSequential.lean` certificam os dois canais, os pesos
angulares e a sequência ortogonal. `GDQ/SternGerlachInterface.lean`
certifica a condição livre ponderada do estômato, a especialização Schur/DtN
da Hessiana, a resposta modal, a positividade da rigidez axial, a
decomposição Noether--Zeeman e a deflexão clássica. Os coeficientes de um
magneto real continuam dados metrológicos a calcular no background e no
contorno correspondentes.

## Transporte e interferência

`GDQ/DetectorDtNSchur.lean` deriva a impedância hiperbólica do detector e
controla o expoente de visibilidade. `GDQ/TransportInterference.lean`
certifica a atenuação evanescente, a saturação geométrica de Hartman no
ansatz reduzido, a identidade coerente de duas amplitudes, seus limites
construtivo e destrutivo e a independência do registro em relação a mudanças
fora do suporte causal. O ansatz `gₓₓ ∝ ρ` permanece hipótese declarada do
setor evanescente, não axioma da ação oficial.

## Aharonov--Bohm e Sagnac

`GDQ/AharonovBohmHolonomy.lean` certifica a invariância de calibre da
holonomia em laço fechado. `GDQ/SagnacHolonomy.lean` certifica o cancelamento
da fase comum e a duplicação do termo ímpar sob reversão de orientação.
`GDQ/HolonomyPatchingStokes.lean` acrescenta a colagem `U(1)` por dois
patches, a invariância por mudanças inteiras do levantamento, a identidade
exata de Stokes para um complexo celular finito e a derivação algébrica de

$$
\Delta t_{\rm Sag}
=
\frac{4\boldsymbol\Omega\cdot\mathbf A}{c^2}
$$

quando a circulação cinemática vale
$2\boldsymbol\Omega\cdot\mathbf A$. A identidade celular não substitui o
teorema suave de Stokes: regularidade, orientação e domínio perfurado do
aparelho concreto continuam hipóteses geométricas explícitas.

## Fase circular e pente de Dirac

O módulo `GDQ/PhaseQuantization.lean` formaliza a quantização da circulação
por fechamento global da fase `U(1)` e registra a soma de Poisson rigorosa
para funções de Schwartz. A nota `QUANTIZACAO_FASE_PENTE_DIRAC.md` distingue
a origem topológica dos índices inteiros da representação distribucional pelo
pente de Dirac. O script autocontido
`scripts/verificar_pente_dirac_regularizado.py` verifica a identidade
regularizada pelo calor.

O módulo `GDQ/PhaseReconstruction.lean` fecha o elo com o campo oficial:
reconstrói a fase unitária e o estado complexo diretamente de `f`, prova
`|Ψ(f)|²=ρ(f)`, certifica a invariância sob `f ↦ f+2πki`, verifica a
invariância do setor constitutivo da densidade pontual oficial e prova
`ΔS_R=nh` para qualquer laço contínuo admissível do próprio potencial. A nota
`RECONSTRUCAO_FASE_GDQ.md` registra hipóteses e limites sem transformar dados
globais de domínio em consequência de uma expressão pontual.

O módulo `GDQ/BoundaryPhaseQuantization.lean` formaliza a generalização
relativa

$$
Q_S\Delta S_R\in h\mathbb Z.
$$

Ele certifica o balanço de carga, separa o deslocamento constante de uma
interpolação de extremidade, prova o no-go da quantização puramente local e
deriva o resultado condicional da ação exponenciada. A nota
`QUANTIZACAO_RELATIVA_BORDO.md` registra as hipóteses geométricas que
permanecem externas à camada algébrica.

Os módulos `GDQ/PhaseFirstVariation.lean`,
`GDQ/NoetherPhaseCurrent.lean` e `GDQ/StokesChargeBalance.lean` fecham o elo
anterior dessa cadeia. Eles expandem diretamente a parcela oficial de fase,
extraem a corrente normalizada
`2 τ 𝒰 g⁻¹dS_R/(ℏ Λ_C²)`, identificam conservação fraca com
estacionariedade fraca e provam o balanço orientado entre duas folhas. A
instanciação do teorema de Stokes num background suave concreto permanece
uma obrigação geométrica explícita.

O módulo `GDQ/SpinHopfMonodromy.lean` porta a construção spinorial/Hopf já
presente no manuscrito para uma integral de contorno efetiva: prova
`∮ (1/2) dz/z = πi`, o resíduo normalizado `1/2`, a circulação `h/2`, a
holonomia `-1` em uma volta e `+1` em duas voltas, além da invariância do
projetor de Hopf sob `u ↦ -u`. A nota
`FORMALIZACAO_SPIN_HOPF.md` explicita que a classe spinorial do defeito é o
dado geométrico de entrada; os valores de resíduo e holonomia são as
consequências formalmente certificadas.

O módulo `GDQ/CechChern.lean` formaliza o inteiro do cociclo numa interseção
tripla e prova que mudanças dos levantamentos locais alteram esse inteiro
exatamente por um cobordo. A nota `CECH_CHERN_U1.md` separa essa prova local
da aplicação geométrica a uma cobertura concreta. O módulo
`GDQ/CechCohomology.lean` constrói cochains, cobordos, prova `δ²=0`, define
`H²=Z²/B²`, constrói `firstChernClass` das transições levantadas e prova sua
independência global sob mudanças dos levantamentos.

## Escopo do primeiro teste

O teste atual formaliza somente:

1. a distinção tipada entre o bulk local e o espaço cosmológico;
2. as dimensões declaradas de cada espaço;
3. os modelos concretos `ℝ⁴ × T⁴` e `T⁵ × S³`;
4. as identidades pontuais de conjugação de `f`;
5. a positividade estrita de `ρ = exp (-Re f)`;
6. os dados tipados de `(g, J, H, f, 𝒰)`;
7. Hermiticidade e positividade de `g` como obrigações explícitas;
8. `J² = -Id` e antissimetria elementar da torção;
9. o kernel complexo `𝒰 = ρ / (4πzτ)^n`;
10. a positividade do kernel na seção euclidiana real;
11. a densidade pontual, sem termos extras, da ação oficial;
12. a separação entre campos brutos e configurações admissíveis;
13. testemunhos explícitos de integrabilidade e compatibilidade de Bismut;
14. a lei constitutiva obrigatória do kernel em dimensão complexa quatro;
15. a distinção entre locus regular e conjunto nodal;
16. a assinatura abstrata da integral da ação;
17. o contorno causal regular e o pullback explícito de `dτ/τ`;
18. a integral dupla parametrizada por uma estrutura mensurável;
19. provas obrigatórias de integrabilidade no bulk e no contorno;
20. invariantes explícitos `R`, `|∇f|²` e `sqrt(det g)` de um background;
21. a densidade oficial com `Re f`, `ρ` e o kernel sem parâmetros
    independentes redundantes;
22. a seção euclidiana positiva como hipótese tipada e comprovada;
23. a integral oficial nessa seção, condicionada a provas de integrabilidade;
24. o contorno exponencial `τγ(t)=τ₀ exp(κt)`;
25. a lei de composição aditiva--multiplicativa do relógio;
26. o pullback constante `γ*(dτ/τ)=κ dt`;
27. a recíproca: todo relógio relativo positivo, contínuo e homogêneo é
    exponencial;
28. a determinação `κ=log(factor(1))` e a unicidade desse gerador;
29. a estrutura Borel do toro e a medida concreta
    `Lebesgue(ℝ⁴) × Haar(T⁴)`;
30. as equações coordenadas de compatibilidade métrica e complexa de Bismut;
31. a identificação coordenada entre a torção da conexão e `H`;
32. as fórmulas de Riemann, Ricci, curvatura escalar, norma de `∇f` e
    `sqrt(det g)`;
33. a construção dos invariantes oficiais a partir do jato coordenado;
34. a prova de integrabilidade a partir de uma função dominante integrável;
35. a densidade oficial de background real sobre contorno complexo;
36. a redução exata dessa densidade à seção euclidiana;
37. famílias de variações da ação oficial, estacionariedade e gradiente;
38. Hessiana, subespaços admissível e de gauge e projetor físico;
39. o teorema de que gap físico positivo implica estabilidade estrita;
40. a anulação dos modos de gauge pelo Hessiano comprimido;
41. a definição lógica de configuração estacionária;
42. a decomposição tipada `T⁵ × S³ ≃ T⁴ × S¹ × S³`;
43. a família apontada de raios `R` e a parametrização `R = ε⁻¹`;
44. a taxa geométrica local `O(R⁻²)` e sua convergência a zero;
45. o transporte apontado de `g`, `J`, `H` e `f`;
46. a convergência de `ρ` e do kernel oficial como consequências da
    convergência de `f`;
47. o transporte norm-preservante pela razão das medidas;
48. a definição de Mosco por liminf fraco e sequência de recuperação;
49. a separação formal entre gap e estimativa de localização de Agmon;
50. a positividade da margem transferida `Δ₀ - 2δ`;
51. certificados de convergência forte de resolventes e em norma de
    projetores de Riesz;
52. a composição lógica dos seis lemas sem colar artificial;
53. a classificação entre invariantes herdados e normalizações contínuas;
54. a composição algébrica da razão reduzida do múon;
55. a construção e ordenação dos dois ramos da saturação leptônica;
56. a impossibilidade de quatro direções independentes em suporte real
    tridimensional;
57. a preservação das razões no background produto e o critério escalar
    subcrítico de Schur.

Os itens 54--57 são certificados por `GDQ/LeptonicHierarchy.lean`. Essa
certificação começa nos dados geométricos do modelo reduzido; ela não deriva
os coeficientes $2/3$, $6/5$ e $2\alpha$ para backgrounds arbitrários da ação
oficial, nem seleciona dinamicamente o ramo pesado.

`GDQ/MagneticResponse.lean` certifica a camada magnética reduzida seguinte:
$g_0=2$ sob o mapa mínimo $\gamma_0=q/(mc)$, norma harmônica
$1/(2\pi)$, composição $a^{(1)}=\alpha/(2\pi)$, separação exata entre fonte
protegida e transversal, identidade do bloco Hessiano líder e anulação de um
canal diretamente ortogonal. O módulo não deriva a normalização cosmológica
de $\alpha$, a sela leptônica 8D ou as correções superiores de $g-2$.

`GDQ/BaryonicReduction.lean` certifica a álgebra do modelo bariônico
reduzido: soma dos três volumes, equilíbrio e cisalhamento de `(1,1,-2)`,
identidades das razões de massa, positividade da norma beta e eliminação
quártica por Schur. O módulo não deriva a seleção da sela trimodal, os
coeficientes de superfície, a projeção $3$--$4$--$5$ nem a lei histórica
$\alpha^{-11}$; esta última aparece apenas como hipótese de uma identidade
algébrica.
54. o projetor relativo dos três centros e sua idempotência;
55. a fórmula positiva do gap `C₃`;
56. a prova exata de `Δ₀ = 1/2` na normalização primitiva;
57. a ligação do gap `C₃` à Hessiana como segunda variação da ação oficial;
58. o Jacobiano explícito do vínculo de fechamento dos três centros;
59. a identidade de Gram
    `D C† D C = (3/2) T² P_rel`;
60. a anulação exata do modo comum;
61. a coercividade do bloco angular em modos relativos;
62. os níveis `m/(2τ)` do operador OU como fórmula espectral declarada e
    seus limites positivos para `m ≥ 1`;
63. a positividade do bloco radial `3/(2τ)`;
64. a redução do complemento de Schur quando o bloco misto se anula;
65. a fórmula conjunta do menor gap reduzido;
66. a seleção de três centros por posto--nulidade sob posto horizontal dois
    e isolamento módulo rotação comum;
67. a fórmula `N-3` para modos nulos internos de um junction horizontal;
68. o fechamento exato das três tensões equiláteras;
69. a aditividade do índice APS primitivo e a contagem `15/45` de componentes
    quirais;
70. o potencial, a densidade e o gradiente do background gaussiano local;
71. a expansão exata do colchete oficial nesse background;
72. a estacionariedade da variação pura de fase;
73. os quocientes simétricos exatos de primeira e segunda variação;
74. a positividade do bloco de fase para prefator, fluxo e norma de
    gradiente positivos;
71. a passagem exata da densidade pontual para a variação integrada, sob
    hipóteses explícitas de integrabilidade;
72. a identificação da segunda variação integrada com a integral do
    coeficiente Hessiano pontual;
73. a extensão da família quadrática para coeficientes dependentes do
    parâmetro real do contorno;
74. a preservação exata da estrutura quadrática depois das integrais no bulk
    e no contorno causal;
75. a identificação da segunda variação da parte real da ação iterada com
    duas vezes a parte real do coeficiente quadrático integrado;
76. a fatoração exata do peso causal por `κ` no relógio exponencial;
77. a preservação da positividade do bloco de fase quando `κ>0` e o
    coeficiente integrado sem peso é real e positivo;
78. a finitude da medida de Haar do toro compacto `T⁴`;
79. a reconstrução exata `Ψ(f)=sqrt(ρ(f)) exp(i Im f)`;
80. a identidade `|Ψ(f)|²=ρ(f)` e a não anulação no locus regular;
81. a invariância de `ρ`, do kernel e do setor constitutivo da densidade
    oficial sob deslocamentos imaginários constantes;
82. a identificação `f ~ f+2πki` no estado físico reconstruído;
83. a quantização `ΔS_R=nh` para laços contínuos admissíveis do próprio
    potencial complexo;
79. a integrabilidade da gaussiana multidimensional em `ℝ⁴`;
80. a integrabilidade de sua extensão constante em `T⁴` na medida produto
    oficial de referência;
81. a igualdade exata entre essa envolvente e a densidade constitutiva
    gaussiana, salvo a normalização `exp(-f₀)`;
82. certificados concretos de dominação para a densidade gaussiana e para
    blocos que sejam múltiplos espaciais constantes dela;
83. um construtor geral de dominação para densidades mensuráveis cujo módulo
    seja limitado por uma gaussiana explícita;
84. uma envolvente gaussiana integrável na direção causal;
85. a prova de que um integrando temporal constante não nulo diverge em toda
    a reta;
86. uma janela de segmento causal finito, estendida por zero, com
    integrabilidade provada;
87. construtores separados de dominação causal por decaimento e por suporte
    finito;
88. um construtor de `ControlledComplexContourActionData` a partir de bounds
    gaussianos explícitos no bulk e no contorno.
89. a construção de um controle gaussiano Kähler/plano, reunindo métrica
    Hermitiana plana, estrutura complexa padrão, torção nula, potencial,
    densidade e kernel oficial, explicitamente excluído do setor material;
90. a regularidade global desse background e seus invariantes euclidianos
    explícitos;
91. a desigualdade
    `(1+r)e^{-br} ≤ (1+2/b)e^{-(b/2)r}` para `b>0`, `r≥0`;
92. a integrabilidade dos momentos `|x|²e^{-b|x|²}` e `|x|²ρ_*` no bulk
    local;
93. a redução exata da densidade oficial gaussiana completa a um perfil
    afim em `|x|²` multiplicado por `ρ_*`;
94. a integrabilidade da densidade oficial completa, para cada ponto do
    contorno;
95. um certificado concreto `gaussianOfficialBulkControl`;
96. a construção da ação oficial sobre um segmento causal finito usando a
    medida externa restrita, sem alterar o integrando.
97. a separação tipada `MaterialAdmissibleConfiguration`, que exige prova de
    torção não nula;
98. o ansatz Hermitiano conformal `ω=e^{2φ}ω₀`;
99. a construção coordenada de `dω` e `H=d_J^cω`;
100. a antissimetria da 3-forma torsional;
101. a componente explícita `H₄₅₁=2a e^{2φ}` e sua não anulação para
     `a≠0`.
102. a positividade da métrica Hermitiana conformal;
103. a construção de `conformalMaterialConfiguration`, que habita
     tipadamente o setor material e carrega a prova de `H≠0`.
104. a conexão explícita
     `Γᴮ=Γᴸᶜ+(1/2)g⁻¹H` do ansatz conformal;
105. as identidades coordenadas `∇ᴮg=0`, `∇ᴮJ=0` e `Tᴮ=H`;
106. a fatoração que torna os coeficientes de `Γᴮ` constantes para
     `φ=a x⁰`;
107. o `CoordinateBismutBackground` material completo;
108. o volume `sqrt(det g)=e^{8φ}` e a norma
     `|∇f|²_g=e^{-2φ}|∇f|²_flat`;
109. a contração exata da curvatura de Bismut
     `Rᴮ=-60a²e^{-2φ}`;
110. a inserção desses invariantes na densidade literal da ação oficial,
     sem termo fundamental adicional `|H|²`.
111. a ação torsional reduzida normalizada
     `q exp(-28u)(2-24u)+fBase-2+128u`;
112. sua derivada exata
     `q exp(-28u)(672u-80)+128`;
113. o limiar torsional exato `q_c=8/5`;
114. a existência de uma raiz `0<u<5/42` quando `q>8/5`;
115. a monotonicidade estrita da equação de sela nesse intervalo;
116. a unicidade da raiz torsional;
117. a positividade do coeficiente de segunda variação na direção conformal;
118. a bifurcação em dois ramos
     `a_*=±sqrt(u_*/τ)`;
119. a separação explícita entre estabilidade reduzida em `a` e a futura
     Hessiana física acoplada.
120. a construção explícita do ramo positivo
     `a_*=sqrt(u_*/τ)>0`, com primeira variação nula e coeficiente de segunda
     variação positivo; o ramo negativo segue da paridade.
121. a prova de que a raiz torsional é um mínimo local da ação normalizada
     como função de `u=τa²`;
122. a identificação formal da Hessiana reduzida
     `d²A_red/du²=q exp(-28u)(2912-18816u)`;
123. a prova algébrica do critério de Schur para um modo adicional acoplado:
     `K_XX-K_aX²/K_aa>0`.

A integral oficial foi codificada somente na seção euclidiana real positiva,
condicionada a um background admissível, invariantes geométricos fornecidos e
provas de integrabilidade. A ação completa sobre um contorno genuinamente
complexo ainda exige campos suaves complexificados, medida volumétrica
derivada da métrica e controle analítico. A assinatura abstrata presente
neste teste não constitui alteração nem substituição da ação física.

### Interpretação do teorema do relógio

O tipo geral `CausalContour` admite curvas complexas que não precisam ser
exponenciais. Entretanto, quando um contorno representa um relógio físico
positivo, contínuo, normalizado e homogêneo sob composição temporal, o
teorema `PositiveClockHomomorphism.eq_exp` demonstra que ele é
necessariamente exponencial. O gerador é
`κ = log (factor 1)` e sua unicidade também foi provada. Assim, dentro dessa
classe física, a exponencial não é um ansatz; contornos mais gerais apenas não
podem ser identificados com o relógio homogêneo sem uma prova adicional.

## Estado lógico dos seis novos elos

| Elo | O que foi formalizado | Status rigoroso |
|---|---|---|
| medida local | Borel no toro, Haar em `T⁴`, Lebesgue em `ℝ⁴` e produto | construído |
| Bismut | equações coordenadas explícitas para `g`, `J`, conexão e `H` | um background conformal torsional local foi construído; existência global geral continua aberta |
| invariantes | contrações de Riemann/Ricci, `R`, norma de `∇f` e volume | derivados explicitamente no background conformal; gerais sob certificado de jato |
| integrabilidade | teorema de dominação e construção da ação a partir do certificado | condicional à apresentação de uma envolvente integrável |
| contorno complexo | densidade e integral de background real ao longo de `γ` | construída para a classe controlada; campos totalmente complexificados não tratados |
| Hessiana física | família oficial, primeira variação, Hessiana, gauge, projetor e gap | estrutura e teoremas gerais; operador de um background GDQ concreto ainda deve ser calculado |

Na família torsional conformal normalizada, a primeira variação reduzida já
seleciona uma sela não nula quando o dado de contorno satisfaz
`q=zτ/τ>8/5`. Esse resultado é uma sela derivada no setor unidimensional
`a`; não demonstra ainda a estabilidade nas demais direções físicas.

O objeto `CoordinateBismutBackground` é um jato coordenado globalmente
indexado. Ele torna as equações auditáveis, mas ainda não substitui a
construção de um atlas suave e a prova de compatibilidade nas interseções das
cartas.

`mathlib v4.32.0` está fixada como dependência. O diretório `.lake` é um link
simbólico para `/home/pedro/.cache/gdq-formal-lake`, mantendo fontes e
artefatos pesados fora do Dropbox.

## Compilação

```bash
source /home/pedro/.elan/env
cd /home/pedro/Dropbox/obs/todo/formal
```

## Verificação com memória controlada

Os módulos devem ser construídos individualmente ou em pequenos grupos. Não
executar a construção genérica de todo o grafo de dependências:

```bash
lake build +GDQ.Constitutive
lake build +GDQ.Spaces
lake build +GDQ.LocalMeasure
lake build +GDQ.Fields
lake build +GDQ.FlowKernel
lake build +GDQ.Admissibility
lake build +GDQ.CausalContour
lake build +GDQ.ClockHomomorphism
lake build +GDQ.ActionDensity
lake build +GDQ.ActionIntegration
lake build +GDQ.GeometricInvariants
lake build +GDQ.CoordinateGeometry
lake build +GDQ.EuclideanOfficialAction
lake build +GDQ.ControlledIntegrability
lake build +GDQ.ComplexContourAction
lake build +GDQ.VariationalHessian
lake build +GDQ.CosmologicalFamily
lake build +GDQ.GlobalLocalTransport
lake build +GDQ.SpectralBridge
lake build +GDQ.C3Application
lake build +GDQ.C3ConcreteHessian
lake build +GDQ.GenerationJunction
lake build +GDQ.GaussianOfficialReduction
lake build +GDQ.GaussianContourReduction
lake build +GDQ.GaussianBulkDomination
lake build +GDQ.GaussianCausalDomination
lake build +GDQ.GaussianAdmissibleBackground
lake build +GDQ.GaussianOfficialIntegrability
lake build +GDQ.ConformalBismutTorsion
lake build +GDQ.ConformalBismutConnection
lake build +GDQ.ConformalBismutBackground
lake build +GDQ.ConformalBismutInvariants
lake build +GDQ.ConformalOfficialDensity
lake build +GDQ.ConformalTorsionSaddle
lake build +GDQ.ConformalTorsionHessian
lake build +GDQ.ConformalTorsionProjectedHessian
lake build +GDQ.ConformalTorsionConstraintTangent
lake build +GDQ.PhaseQuantization
lake build +GDQ.PhaseReconstruction
lake build +GDQ.BoundaryPhaseQuantization
lake build +GDQ.CechChern
lake build +GDQ.CechCohomology
lake build +GDQ.OfficialAction
lake build GDQ
```

Não usar `import Mathlib`; importar somente os módulos necessários.

## Próxima etapa

O arquivo `STATUS_PONTE_GLOBAL_LOCAL.md` separa detalhadamente o que já é
teorema Lean das obrigações analíticas ainda certificadas.

1. reconstruir dentro de Lean a expansão em coordenadas normais que fornece
   a constante concreta do erro `O(R⁻²)`;
2. construir um atlas suave explícito e provar a compatibilidade nas
   interseções;
3. derivar do background físico o bound causal externo ou selecionar
   explicitamente o segmento causal; para o background gaussiano plano, o
   controle espacial da densidade oficial completa já está demonstrado;
4. internalizar em Lean os momentos gaussianos que ligam diretamente a
   integral oficial à ação torsional reduzida; a derivação analítica completa
   está em `DERIVACAO_SELA_TORSIONAL_CONFORMAL.md`;
5. avaliar, na base física completa, os blocos mistos `K_aX` e `K_XX` da
   segunda variação métrico--dilatônica--torsional gauge-fixada; o bloco
   `K_aa`, sua origem como segunda derivada em `a`, o projetor do setor
   reduzido, o critério de Schur e uma cota suficiente de gap por dominância
   diagonal já estão demonstrados; `fBase` foi formalmente excluído como
   candidato a modo `X`, pois sua derivada é unitária e o vínculo fixa
   `δf₀=128 τ a δa`;
6. derivar o projetor contínuo total a partir dos geradores de Noether/gauge;
7. internalizar os teoremas funcionais de Mosco, Agmon e Riesz necessários
   para eliminar os certificados correspondentes;
8. tratar separadamente backgrounds warped, mistos e canais massless.

A quantização escalar de circulação não está nessa lista de pendências:
`GDQ.PhaseQuantization` já constrói o levantamento de qualquer laço contínuo
em `U(1)` e prova o incremento `2πn`. `GDQ.CechChern` e
`GDQ.CechCohomology` constroem o cociclo inteiro, `H²`, a classe `c₁` e sua
independência sob mudanças dos levantamentos. Restam a instanciação numa
cobertura concreta da variedade, Čech--singular e Chern--Weil; são
refinamentos geométricos, não lacunas da circulação.
