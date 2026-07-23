# Teorema de herança espectral global–local da GDQ

> [!important] Formulação vigente
> A prova sem interface cosmológico--local está em
> `topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md`. DtN refere-se somente ao estômato.
> A hipótese local foi verificada para o background gaussiano $C_3$ em
> `topicos/ponte_global_local/ponte_global_local_fechamento_c3.md`.

## 1. Finalidade

Este documento consolida a distinção entre:

1. quantidades determinadas no espaço global de Einstein;
2. identidade espectral herdada pelo objeto;
3. dinâmica no bulk planar de laboratório;
4. resposta a fontes externas ou dinâmicas;
5. deslocamentos produzidos por condições de contorno;
6. mudanças verdadeiras de setor por fluxo espectral ou cirurgia.

Seu objetivo é impedir que massas, cargas, índices e multiplicidades globais
sejam repetidamente redeterminados a partir de um fragmento local da fibra.

O princípio orientador é

$$
\boxed{
\text{o setor global determina o que o objeto é;}
\qquad
\text{o problema planar determina como ele responde.}
}
$$

O teorema aqui formulado é uma proposta condicional da GDQ. A maquinaria
matemática necessária existe em teoria do índice para famílias, limites
adiabáticos, decomposição espectral e fórmulas de colagem. A aplicação
específica entre as duas geometrias da GDQ ainda exige construir e verificar
o mapa global–local.

---

## 2. Geometrias e regimes

### 2.1 Espaço global de Einstein

Denote

$$
M_E=T^5\times S^3.
$$

Esse espaço é usado como domínio cosmológico e espectral global. Nele são
calculados, conforme o setor:

- autovalores e multiplicidades;
- índices e classes topológicas;
- holonomias;
- massas de repouso;
- hierarquias e setores de geração;
- invariantes globais de torção.

Essas quantidades não devem ser inferidas observando apenas um infinitésimo de
uma fibra local.

### 2.2 Bulk planar oficial

O bulk local oficial é

$$
M_P=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}M_P=8,
\qquad
\dim_{\mathbb C}M_P=4.
$$

Ele é o domínio natural para:

- propagação local;
- resposta a aparelhos;
- fontes e sondas;
- interfaces;
- espalhamento;
- condições Robin, APS e DtN;
- dinâmica de cirurgia;
- reconstrução do espaço-tempo físico.

### 2.3 Quatro situações planares

Todo cálculo planar deve ser classificado em uma destas situações:

| Código | Situação | Interpretação |
|---|---|---|
| P0 | sem perturbação | objeto isolado no bulk local |
| P1 | fonte experimental prescrita | campo externo congelado, sem retroação |
| P2 | fonte dinâmica | objeto, aparelho e interface variam conjuntamente |
| P3 | contorno perturbado | Robin, APS ou DtN desloca e seleciona modos |

Uma fonte prescrita pertence ao aparelho e não redefine a identidade global
do objeto. Uma fonte dinâmica entra na Hessiana e pode produzir dressing,
mistura, instabilidade ou cirurgia.

---

## 3. Ação preservada

O teorema não substitui nem completa a ação oficial:

$$
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
$$

O operador local, a Hessiana, o mapa de redução e os termos de interface
devem ser derivados dessa ação ou declarados como dados externos do aparelho.

---

## 4. Decomposição espectral

Seja $D_E^B$ o operador global de tipo Dirac–Bismut no setor de Einstein:

$$
D_E^B\phi_{a\mu}=\lambda_a\phi_{a\mu},
$$

onde $a$ rotula o autovalor e $\mu$ sua multiplicidade. Formalmente, um campo
completo admite a decomposição

$$
\boxed{
\Psi(x,y)
=\sum_{a,\mu}\psi_{a\mu}(x)\phi_{a\mu}(y).
}
$$

Essa expressão é a superposição relevante: uma decomposição em autoespaços
globais. Ela não significa que todos os setores permaneçam dinamicamente
acoplados no limite planar.

Defina o projetor espectral

$$
P_a
=\frac{1}{2\pi i}
\oint_{\Gamma_a}(D_E^B-\zeta)^{-1}\,d\zeta,
$$

onde $\Gamma_a$ envolve somente o setor $\lambda_a$.

Se existe um gap uniforme,

$$
\operatorname{dist}
\left(
\lambda_a,
\operatorname{spec}D_E^B\setminus\{\lambda_a\}
\right)\ge\Delta_a>0,
$$

então perturbações menores que o gap preservam o subespaço projetado e apenas
produzem dressing interno.

---

## 5. Enunciado proposto

### Teorema — herança espectral global–local

Considere:

1. o setor global $(M_E,g_E,J_E,H_E,\mathcal U_E,D_E^B)$;
2. o setor planar $(M_P,g_P,J_P,H_P,\mathcal U_P,D_P^B)$;
3. uma família de mapas parciais

   $$
   U_\varepsilon:
   \mathcal H_E\longrightarrow\mathcal H_P,
   \qquad \varepsilon\downarrow0,
   $$

   induzida por uma degeneração adiabática, cobordismo, cobertura,
   descompactificação controlada ou correspondência espectral explicitamente
   construída;
4. um setor isolado $E_a=\operatorname{Ran}P_a$;
5. condições de contorno auto-adjuntas convergentes;
6. conservação das classes de torção, índice e carga;
7. convergência da medida ponderada e do contorno causal.

Suponha que ocorra convergência em resolvente no setor:

$$
\boxed{
U_\varepsilon
(D_E^B-z)^{-1}
U_\varepsilon^\dagger
\longrightarrow
P_a(D_{\mathrm{eff}}^{(a)}-z)^{-1}P_a,
}
$$

uniformemente para $z$ em compactos do conjunto resolvente.

Então:

1. o autoespaço global $E_a$ define um setor de superseleção do problema
   planar;
2. massa, carga, índice, holonomia e multiplicidade globais são transportados
   como dados do setor local;
3. o operador efetivo é

   $$
   \boxed{
   D_{\mathrm{eff}}^{(a)}
   =
   P_a(D_P^B+\mathcal A_H+\mathcal V_{\mathrm{int}})P_a;
   }
   $$

4. fontes e contornos locais podem deslocar e desdobrar o nível,

   $$
   \lambda_a\mapsto
   \lambda_a+\delta\lambda_a[J_{\mathrm{app}},\mathsf R],
   $$

   mas não alteram sua classe topológica enquanto o gap não fecha;
5. uma mudança de classe só ocorre por cruzamento espectral,

   $$
   \Delta\operatorname{Ind}
   =
   \operatorname{SF}(D_s),
   $$

   ou por uma cirurgia admissível;
6. todo observável local converge ao observável efetivo do setor herdado,

   $$
   \langle\Psi_\varepsilon,\mathcal O_\varepsilon\Psi_\varepsilon\rangle
   \longrightarrow
   \langle\psi_a,\mathcal O_{\mathrm{eff}}^{(a)}\psi_a\rangle.
   $$

### Interpretação

O teorema não afirma que a massa global está fisicamente concentrada em cada
ponto da fibra. Ele afirma que o subsistema local pertence a uma
representação espectral global e, por isso, sua dinâmica planar é resolvida
dentro desse setor.

---

## 6. Forma adiabática esperada

Quando existe uma fibração ou degeneração adiabática regular, espera-se uma
expansão do tipo

$$
D_\varepsilon^B
=\varepsilon^{-1}D_F^B
+D_{\mathrm{hor}}^B
+\mathcal A_{\mathrm{Bismut}}
+O(\varepsilon).
$$

Os modos de energia finita pertencem ao fibrado de autoespaços do operador
vertical. Projetando:

$$
\boxed{
D_{\mathrm{eff}}^{(a)}
=P_a
\left(
D_{\mathrm{hor}}^B+\mathcal A_{\mathrm{Bismut}}
\right)
P_a.
}
$$

No caso de kernel vertical, usa-se o fibrado $\ker D_F^B$. Para um autovalor
isolado não nulo, usa-se seu projetor de Riesz. A conexão induzida no fibrado
de autoespaços produz os acoplamentos geométricos locais.

---

## 7. Interfaces, fontes e condições de contorno

### 7.1 Colagem por DtN

Se uma hipersuperfície $\Sigma$ separa dois domínios, a informação global
entra no problema local pelo operador de Dirichlet-to-Neumann. A fórmula BFK
tem esquematicamente a forma

$$
\det_\zeta D_M
=
\det_\zeta D_{M_1,D}
\det_\zeta D_{M_2,D}
\det_\zeta(\Lambda_1+\Lambda_2)
\times e^{\mathcal L_\Sigma},
$$

onde $\mathcal L_\Sigma$ é local na interface. Portanto, dois problemas
locais não são independentes: o operador de interface transporta a
compatibilidade global.

### 7.2 Robin

Uma condição

$$
(\nabla_n+\eta_R)\psi|_\Sigma=0
$$

pode deslocar autovalores e ativar um modo ligado ou uma instabilidade. Ela
não redefine automaticamente a massa global. O resultado é:

$$
m_a
\longrightarrow
m_a+\delta m_a(\eta_R,J_{\mathrm{app}}),
$$

isto é, dressing ou resposta local.

### 7.3 APS e fluxo espectral

APS seleciona o subespaço admissível de borda. Se um parâmetro atravessa um
cruzamento, o fluxo espectral mede a alteração de índice. Sem cruzamento, o
índice global é estável.

---

## 8. O que deixa de precisar ser refeito

Uma vez provado o teorema, não será necessário:

1. redeterminar massas globais em cada carta planar;
2. inferir a carga total de um infinitésimo da fibra;
3. reconstruir multiplicidades globais para cada aparelho;
4. recalcular índices topológicos em cada problema local sem cirurgia;
5. justificar observável por observável que o mesmo objeto global aparece no
   laboratório;
6. tratar toda condição Robin ou APS como nova ontologia;
7. usar um cálculo local estático para substituir um invariante espectral
   global.

Essas quantidades entram como rótulos do setor $E_a$.

### 8.1 Triagem retrospectiva do trabalho existente

O novo princípio não apaga os cálculos anteriores. Ele muda sua função:

| Bloco | Parte global que não deve ser repetida no planar | Parte local que permanece necessária | Uso dos cálculos existentes |
|---|---|---|---|
| Q34–Q35 | identidade do setor eletromagnético e dados espectrais globais | polarização, running, fonte, escala experimental e contorno | auditoria da redução efetiva e dos kernels |
| Q39 | espectro e hierarquia globais de massa | dressing, resposta térmica e seleção observável de modos | teste da herança e refinamento metrológico |
| Q40 e decaimento do nêutron | classe global, carga, spin e paridade do objeto | cirurgia, fluxo, overlap causal, taxa e produtos de saída | lemas dinâmicos do problema planar |
| Q30 | classe e conteúdo do setor GDQ | background transversal, gap e resposta de dois estômatos | prova efetiva e teste de estabilidade |
| mésons perturbados | classe candidata do par de estômatos | nucleação por fonte/Robin, estabilidade e energia de saída | programa local condicional |
| medida | spin e circulação intrínsecos do objeto | Hessiana, DtN, impedância do aparelho, mobilidade e registro | teoria de interface clássico–quântica |

Portanto, “não precisava” significa **não precisava ser novamente usado para
determinar a identidade global**. Os mesmos cálculos podem continuar
necessários como prova de resposta local, controle de contorno, estabilidade,
taxa, convergência numérica ou teste da própria ponte.

---

## 9. O que continua sendo necessário

O teorema não elimina:

1. a construção explícita de $U_\varepsilon$;
2. a prova da convergência em resolvente;
3. a verificação do gap;
4. o transporte da conexão de Bismut e da torção;
5. a convergência da medida $\mathcal U$;
6. a compatibilidade do contorno causal $\gamma$;
7. o tratamento de modos zero;
8. a escolha e prova do domínio auto-adjunto;
9. a resposta local a fontes;
10. a retroação aparelho–objeto;
11. a dinâmica de cirurgia;
12. taxas, correlações e espalhamento;
13. testes numéricos de convergência;
14. previsões experimentais congeladas.

Em particular, a Hessiana fornece rigidez; o tempo físico ainda requer a
reconstrução causal e a mobilidade apropriada.

---

## 10. Cuidado topológico essencial

$T^5\times S^3$ e $\mathbb R^4\times T^4$ não são declarados aqui
automaticamente difeomorfos nem fibras de uma fibração suave comum.

Uma família suave própria de submersões preservaria o tipo difeomórfico das
fibras sob hipóteses usuais. Como os dois espaços possuem topologias globais
distintas, a ponte GDQ deve usar uma construção adequada, por exemplo:

1. limite apontado local;
2. descompactificação;
3. cobordismo;
4. degeneração adiabática;
5. cobertura seguida de quociente;
6. correspondência espectral por operador parcial;
7. composição dessas rotas.

Esse requisito não é detalhe técnico. Ele é a hipótese principal que impede
identificar silenciosamente o domínio espectral global com o bulk planar.

---

## 11. Protocolo obrigatório para novos resultados

Todo observável deve receber a etiqueta

$$
\boxed{
(\text{espaço},\text{fonte},\text{contorno},\text{escala},\text{estatuto}).
}
$$

Exemplos:

$$
(\text{Einstein},\text{sem fonte},\text{global},
\text{espectral},\text{derivado}),
$$

$$
(\text{planar},\text{fonte prescrita},\text{Robin},
\text{laboratório},\text{resposta efetiva}),
$$

$$
(\text{planar},\text{fonte dinâmica},\text{causal},
\text{cirurgia},\text{teorema condicional}).
$$

Antes de iniciar uma derivação, responder:

1. A quantidade é global ou local?
2. Ela define a identidade do objeto ou sua resposta?
3. A fonte é externa congelada ou dinâmica?
4. O contorno seleciona o setor ou altera sua classe?
5. Existe cruzamento espectral?
6. O resultado é fundamental, herdado, efetivo ou experimental?

Se a quantidade já é um rótulo global herdado, não deve ser novamente
ajustada no problema planar.

---

## 12. Rota de prova na GDQ

### Etapa A — operador global

Fixar no mesmo documento:

$$
(M_E,g_E,J_E,H_E,\mathcal U_E,D_E^B)
$$

e seus setores espectrais isolados.

### Etapa B — operador planar

Fixar:

$$
(M_P,g_P,J_P,H_P,\mathcal U_P,D_P^B)
$$

com domínio, contorno, gauge e reconstrução causal.

### Etapa C — ponte

Construir $U_\varepsilon$ por uma das rotas do §10 e provar:

$$
U_\varepsilon^\dagger U_\varepsilon\to P_a,
\qquad
U_\varepsilon U_\varepsilon^\dagger\to P_{\mathrm{loc}}^{(a)}.
$$

### Etapa D — convergência

Provar convergência em resolvente ou, no mínimo, convergência das formas
quadráticas de Mosco:

$$
\mathfrak q_\varepsilon
\xrightarrow{\mathrm{Mosco}}
\mathfrak q_{\mathrm{eff}}^{(a)}.
$$

Isso implica convergência apropriada dos semigrupos e, sob hipóteses
adicionais, dos autovalores isolados.

### Etapa E — índices e contornos

Verificar:

$$
\operatorname{Ind}_{\mathrm{global}}
=
\operatorname{Ind}_{\mathrm{local}}
+\operatorname{SF}
+\text{termo de borda APS}.
$$

### Etapa F — observável discriminante

Escolher pelo menos um observável cuja resposta planar dependa de um rótulo
global sem recalibração local. Congelar os parâmetros antes da comparação.

---

## 13. Estatuto científico

| Parte | Status |
|---|---|
| decomposição espectral | teorema padrão |
| índice para famílias | teorema padrão |
| limite adiabático em fibrações regulares | teoremas existentes |
| colagem por DtN/APS | teoremas existentes |
| estabilidade de índice sem fechamento do gap | teorema padrão |
| aplicação a $T^5\times S^3\to\mathbb R^4\times T^4$ | proposta condicional |
| construção de $U_\varepsilon$ | aberta |
| convergência do operador de Bismut GDQ | aberta |
| herança das massas GDQ no planar | consequência condicional |
| dressing por fonte/Robin | problema local efetivo |
| mudança de classe por cirurgia | problema dinâmico separado |

Conclusão conservadora:

$$
\boxed{
\text{a maquinaria matemática existe;}
\quad
\text{a ponte específica da GDQ deve ser demonstrada uma única vez.}
}
$$

Quando essa ponte estiver provada, ela substituirá muitas derivações
caso a caso e funcionará como teorema arquitetural central da teoria.

---

## 14. Referências externas

### Índice para famílias e superconexões

1. Jean-Michel Bismut, “The Atiyah–Singer Index Theorem for Families of
   Dirac Operators: Two Heat Equation Proofs”, Inventiones Mathematicae 83
   (1986), 91–151.
   [Texto do autor](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1986c.pdf).
   Fundamenta o transporte de índices e o formalismo de superconexão em
   famílias de operadores de Dirac.

2. Jean-Michel Bismut e Jeff Cheeger, “Families Index for Manifolds with
   Boundary, Superconnections, and Cones. I. Families of Manifolds with
   Boundary and Dirac Operators”, Journal of Functional Analysis 89 (1990).
   [Página bibliográfica](https://www.sciencedirect.com/science/article/pii/0022123690900986).
   Trata famílias com bordo e condições do tipo APS.

### Limites adiabáticos

3. Jean-Michel Bismut e Jeff Cheeger, “η-Invariants and Their Adiabatic
   Limits”, Journal of the American Mathematical Society 2 (1989), 33–70.
   [DOI](https://doi.org/10.2307/1990919).
   Mostra como invariantes espectrais do espaço total se decompõem no limite
   adiabático em dados da base e da família vertical.

4. Xianzhe Dai, “Adiabatic Limits, Nonmultiplicativity of Signature, and
   Leray Spectral Sequence”, Journal of the American Mathematical Society 4
   (1991), 265–321.
   [PDF](https://web.math.ucsb.edu/~dai/paper/dJAMS.pdf).
   Refina o limite adiabático e explicita correções associadas à sequência
   espectral de Leray.

5. Rafe Mazzeo e Richard B. Melrose, “The Adiabatic Limit, Hodge Cohomology
   and Leray’s Spectral Sequence for a Fibration”, Journal of Differential
   Geometry 31 (1990), 185–213.
   [PDF](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mazmel1.pdf).
   Fornece uma descrição analítica do limite adiabático e da cohomologia
   herdada pela base.

6. Bo Liu, “Bismut–Cheeger Eta Form and Higher Spectral Flow”,
   International Mathematics Research Notices 2023, 10964–10996.
   [Artigo](https://academic.oup.com/imrn/article/2023/13/10964/6603938).
   Reúne fórmulas de variação, imersão, limite adiabático e fluxo espectral
   superior em famílias equivariantes.

### Colagem, determinantes e DtN

7. Dan Burghelea, Leonid Friedlander e Thomas Kappeler,
   “Meyer–Vietoris Type Formula for Determinants of Elliptic Differential
   Operators”, Journal of Functional Analysis 107 (1992), 34–65.
   [DOI](https://doi.org/10.1016/0022-1236(92)90099-5).
   Demonstra a fatoração do determinante regularizado por dados dos
   subdomínios e por um operador de Neumann/DtN na interface.

8. Yoonweon Lee, “Burghelea–Friedlander–Kappeler’s Gluing Formula and the
   Adiabatic Decomposition of the Zeta-Determinant of a Dirac Laplacian”
   (2003).
   [arXiv](https://arxiv.org/abs/math/0304347).
   Relaciona condições Dirichlet e APS em cilindros e prova decomposição
   adiabática do determinante de um Laplaciano de Dirac.

9. Yoonweon Lee, “Burghelea–Friedlander–Kappeler’s Gluing Formula for the
   Zeta-Determinant and Its Applications to the Adiabatic Decompositions of
   the Zeta-Determinant and the Analytic Torsion” (2003).
   [arXiv](https://arxiv.org/abs/math/0304250).

### Torção e operador de Bismut

10. Jean-Michel Bismut, “A Local Index Theorem for Non-Kähler Manifolds”,
    Mathematische Annalen 284 (1989), 681–699.
    [Texto do autor](https://www.imo.universite-paris-saclay.fr/~jean-michel.bismut/Bismut/1989b.pdf) e
    [DOI](https://doi.org/10.1007/BF01443359).
    A referência estabelece o operador e a conexão com torção
    antissimétrica no contexto do teorema local do índice. A aplicação à
    ação física da GDQ continua sendo uma etapa própria do projeto.

### Perturbação, convergência, APS e topologia

11. Tosio Kato, *Perturbation Theory for Linear Operators*, 2ª ed., Classics
    in Mathematics, Springer, 1995.
    [DOI e ficha da editora](https://doi.org/10.1007/978-3-642-66282-9).
    É a referência para projetores de Riesz, estabilidade de autoespaços
    isolados e perturbações de operadores e formas quadráticas.

12. Michael F. Atiyah, Vijay K. Patodi e Isadore M. Singer, “Spectral
    Asymmetry and Riemannian Geometry. I”, Mathematical Proceedings of the
    Cambridge Philosophical Society 77 (1975), 43–69.
    [DOI](https://doi.org/10.1017/S0305004100049410).
    Fundamenta o problema de índice em variedades com bordo e as condições
    espectrais APS usadas na rota de fechamento.

13. Kazuhiro Kuwae e Takashi Shioya, “Convergence of Spectral Structures: A
    Functional Analytic Theory and Its Applications to Spectral Geometry”,
    Communications in Analysis and Geometry 11 (2003), 599–673.
    [PDF do periódico](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cag/2003/0011/0004/CAG-2003-0011-0004-a001.pdf).
    Dá um quadro preciso para convergência de formas, resolventes e semigrupos
    quando os espaços de Hilbert também variam.

14. Charles Ehresmann, “Les connexions infinitésimales dans un espace fibré
    différentiable”, em *Colloque de topologie (espaces fibrés), Bruxelles,
    1950*, Georges Thone, Liège; Masson, Paris, 1951, pp. 29–55.
    O teorema de fibração associado explica por que uma submersão própria e
    regular não pode ser usada silenciosamente para trocar o tipo
    difeomórfico das fibras; uma ponte entre as duas geometrias da GDQ deve
    admitir degeneração, descompactificação ou outra construção explícita.

### Referências metrológicas para $\alpha$

15. Eite Tiesinga, Peter J. Mohr, David B. Newell e Barry N. Taylor,
    “CODATA Recommended Values of the Fundamental Physical Constants: 2022”,
    ajuste CODATA publicado pelo NIST.
    [Tabela oficial](https://physics.nist.gov/cuu/pdf/wallet_2022.pdf).
    Registra $\alpha^{-1}=137{,}035999177(21)$ para a constante de estrutura
    fina de baixa energia.

16. Particle Data Group, “Electroweak Model and Constraints on New Physics”,
    *Review of Particle Physics*, atualização de 2025.
    [Revisão oficial](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf).
    É a referência externa para distinguir a constante de baixa energia do
    acoplamento eletromagnético efetivo dependente da escala.

---

## 15. Referências internas da GDQ

1. [memory.md](memory.md): ação, bulk oficial, espaço espectral e status da
   ponte global–local.
2. [questoes/q39/questao_39.md](questoes/q39/questao_39.md): espectro global e hierarquia de massas.
3. [questoes/q40/questao_40.md](questoes/q40/questao_40.md): backgrounds bariônicos e observáveis.
4. [auditorias/RELATORIO_TORCAO_SPIN_S3_R4T4.md](auditorias/RELATORIO_TORCAO_SPIN_S3_R4T4.md):
   distinção e compatibilidade dos setores de torção.
5. [questoes/q28/associados/indice_global_t5_s3.md](questoes/q28/associados/indice_global_t5_s3.md): índice global.
6. [questoes/q28/associados/resultado_indice_global_t5_s3.md](questoes/q28/associados/resultado_indice_global_t5_s3.md):
   avaliação correspondente.
7. [questoes/q29/associados/warp_oficial_t5_s3.py](questoes/q29/associados/warp_oficial_t5_s3.py): cálculo do
   background global usado em Q29.
8. [topicos/geometria_torcao_hopf/corrente_simpletica_hessiana_gdq.md](topicos/geometria_torcao_hopf/corrente_simpletica_hessiana_gdq.md):
   normalização local e corrente da Hessiana.
9. [topicos/geometria_torcao_hopf/projecao_quarta_variacao_fluxo_conservado.md](topicos/geometria_torcao_hopf/projecao_quarta_variacao_fluxo_conservado.md):
   projeção física com torção conservada.
10. [questoes/q30/associados/principio_sem_distanciamento_dois_estomatos.md](questoes/q30/associados/principio_sem_distanciamento_dois_estomatos.md):
    distinção entre modo interno e separação mantida por fonte externa.
11. [topicos/geometria_torcao_hopf/nucleacao_par_mesonico_torcional.md](topicos/geometria_torcao_hopf/nucleacao_par_mesonico_torcional.md):
    exemplo em que Robin e perturbação podem ativar um setor local sem
    redefinir sua topologia global.
12. [topicos/medida_interface/teoria_interface_classico_quantica_gdq.md](topicos/medida_interface/teoria_interface_classico_quantica_gdq.md):
    cadeia fonte–Hessiana–resposta–registro.
13. [questoes/q34/questao_34.md](questoes/q34/questao_34.md) e os relatórios em [questoes/q34/associados](questoes/q34/associados): construção
    local dos kernels, loops e identidades do setor $U(1)$.
14. [questoes/q35/questao_35.md](questoes/q35/questao_35.md) e os relatórios em [questoes/q35/associados](questoes/q35/associados): escala
    eletromagnética, torção setorial, espectro global e running efetivo.

---

## 16. Decisão arquitetural

A partir deste documento:

1. nenhuma quantidade global deve ser redeterminada localmente sem uma razão
   explícita;
2. todo cálculo deve declarar sua etiqueta de regime;
3. contornos não são penalizados por existirem, mas devem ser derivados ou
   identificados como dados do aparelho;
4. uma coincidência local não prova uma identidade global;
5. uma quantidade herdada não deve ser chamada de ajuste;
6. uma resposta local não deve ser promovida a novo axioma;
7. a prioridade arquitetural é provar a ponte uma única vez, não repetir
   verificações por observável.

Guardas de continuidade herdadas das auditorias anteriores:

1. GDQ não deve ser confundida com QCD; QCD pode aparecer apenas como
   comparação ou redução externa explicitamente declarada;
2. $\alpha^{-1}\simeq137{,}036$ é a referência de baixa energia. Um valor
   próximo de $128$ pertence a um acoplamento efetivo em alta energia e não
   deve substituir o valor cosmológico ou fundamental adotado pela GDQ;
3. $T^5\times S^3$ continua sendo espaço global cosmológico/espectral, não o
   bulk local oficial;
4. conservação de torção, proibição de elongação e mecanismos de estômatos
   devem conservar seus estatutos próprios: axioma, hipótese, teorema
   condicional ou dinâmica ainda a demonstrar;
5. uma taxa numericamente próxima do experimento continua sendo ajuste,
   comparação ou avaliação direta conforme o modo pelo qual os parâmetros
   entraram no cálculo.

Este documento substitui a prática anterior de tentar reconciliar os dois
espaços separadamente em cada questão. Os cálculos anteriores permanecem como
auditorias, testes de hipóteses e fontes dos lemas necessários.
