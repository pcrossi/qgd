---
title: "Checklist operacional — Capítulo 6"
---

# Checklist operacional — Capítulo 6

Este checklist registra o estado de consolidação do Capítulo 6 e separa o que
foi demonstrado, o que é condicional e o que deve ser tratado em capítulos ou
apêndices posteriores.

O capítulo não identifica globalmente o universo cosmológico de Einstein com o
bulk local da GDQ. Ele constrói uma ponte controlada entre os dois regimes.

## 1. Enunciado do capítulo

O problema é mostrar quando resultados obtidos no espaço cosmológico auxiliar

$$
T^5\times S^3
$$

podem ser transportados para o bulk local oficial

$$
\mathbb R^4\times T^4
$$

sem confundir os dois espaços.

A ponte deve transportar mais do que uma intuição de limite plano. Ela deve
controlar:

- geometria apontada;
- campos $g$, $J$ e $f$;
- torção de Bismut reconstruída como $H=d_J^c\omega$;
- medida ponderada $\mathcal U$;
- Hessiana física;
- domínio dos operadores;
- vínculos e modos de gauge;
- gap físico;
- resolventes e projetores espectrais;
- separação entre invariantes topológicos e normalizações contínuas.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Limite apontado | Demonstrado | A família $M_\varepsilon$ converge localmente para $T^4\times\mathbb R^4$. |
| Transporte de campos e medida | Condicional | Exige background admissível, regularidade, dominação uniforme e correção de cutoff. |
| Hessiana física | Condicional | Depende da remoção conjunta de vínculos, redundâncias e modos zero. |
| Localização e gap | Condicional | O gap relevante é físico/local, não o gap de compactificação. |
| Resolventes e Riesz | Condicional | Segue de Mosco, gap uniforme e localização. |
| Separação topologia/normalização | Demonstrada | Topologia transporta inteiros/classes; normalizações contínuas exigem cálculo próprio. |
| Setor $C_3$ reduzido | Teorema aplicado | No background estacionário trimodal, o gap primitivo é $\Delta_0=1/2$. |
| Identidade canônica de Madelung | Condicional | Não é identidade off-shell da ação oficial; vale no setor polarizado/reduzido. |

## 3. Cadeia dedutiva vigente

A cadeia do capítulo é:

$$
M_\varepsilon
\to
\text{limite apontado}
\to
\text{transporte de }(g,J,f,\mathcal U)
\to
P^{\rm phys}
\to
K^{\rm phys}
\to
\text{gap local}
\to
\text{projetores de Riesz}
\to
\text{herança espectral local}.
$$

Essa cadeia é suficiente para justificar a passagem global--local em setores
localizados que satisfaçam as hipóteses declaradas.

Ela não calcula automaticamente constantes contínuas, escalas absolutas,
respostas de detectores ou normalizações de canais massless.

## 4. Pontos que o capítulo já deve preservar

- O espaço cosmológico $T^5\times S^3$ é auxiliar/global/espectral.
- O bulk local oficial é $\mathbb R^4\times T^4$.
- Não existe colar físico entre cosmologia e laboratório.
- Operadores DtN e complementos de Schur pertencem ao bordo material do
  estômato, não a uma parede cosmologia--laboratório.
- A torção não é transportada como campo independente; ela é reconstruída a
  partir de $g$ e $J$.
- O projetor físico deve ser conjunto. Produtos de projetores separados podem
  falhar quando os subespaços não comutam.
- Descompactificação elimina gaps artificiais de compactificação; só o gap da
  Hessiana física do defeito conta.
- Projetores espectrais, não autovetores isolados, são os objetos corretos de
  herança.
- Normalização de carga, $\alpha$, respostas de aparelho e unidades de energia
  exigem cálculos de fluxo, Hessiana, DtN ou contorno.

## 5. Notas chamadas e função delas

O capítulo chama a nota:

[[../notes/equations/Auditoria do termo canonico rho d_t S_R]]

Essa nota deve permanecer como auditoria conceitual do termo canônico. Sua
função é evitar a afirmação incorreta de que

$$
\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}
$$

é uma identidade off-shell da ação oficial.

O status correto é:

- a corrente de fase segue da ação oficial;
- a continuidade local segue após reconstrução do setor de laboratório;
- a polarização canônica de Madelung é uma redução física condicionada;
- a condição pode ser selecionada por setor estacionário com suporte conectado,
  carga primitiva e mínimo de Routh;
- a prova completa da dinâmica de aparelho pertence à teoria da medida.

## 6. Scripts opcionais recomendados

Os scripts deste capítulo devem ser apenas verificações didáticas e
reprodutíveis. Eles não substituem as provas dos lemas.

Recomenda-se criar, se necessário, a pasta:

`manuscrito/06_global_local_bridge/scripts/`

com os seguintes testes autocontidos:

| Script | Função |
|---|---|
| `verificar_limite_apontado_torus_esfera.py` | Mostra numericamente que $S^1_R$ e $S^3_R$ se tornam planos em janelas fixas quando $R\to\infty$. |
| `verificar_transporte_medida_ponderada.py` | Testa a normalização de uma densidade ponderada sob mudança de carta com Jacobiano correto. |
| `verificar_gap_localizacao_toy.py` | Ilustra que um modo ligado preserva gap local enquanto o volume externo cresce. |
| `verificar_resolvente_riesz_toy.py` | Compara resolventes e projetores de Riesz em uma família de operadores finitos. |
| `verificar_homomorfismo_relogio.py` | Verifica a forma $\tau_\gamma(t)=\tau_0 e^{\kappa t}$ a partir do homomorfismo entre translações e dilatações. |

Cada script deve salvar sua saída em Markdown, declarar se é toy model,
verificação de consistência ou avaliação direta, e não deve ser usado para
ajustar constantes físicas.

## 7. Extensões que não reabrem o capítulo

Estas extensões não invalidam a ponte global--local como capítulo estrutural:

- cálculo metrológico final de $\alpha$;
- cálculo absoluto de $G$;
- resposta de um aparelho real específico;
- normalização completa de canais massless;
- espectro completo de backgrounds warped/mistos;
- Page curve, buracos negros ou detectores não lineares.

Esses problemas usam a ponte, mas não são a própria ponte.

## 8. Critério de fechamento do Capítulo 6

O Capítulo 6 está pronto para o manuscrito se:

1. as duas geometrias forem sempre distinguidas;
2. os seis lemas forem mantidos com seu status correto;
3. a herança espectral for apresentada como condicional ao gap;
4. o setor $C_3$ for apresentado como aplicação demonstrada, não como prova de
   todos os backgrounds;
5. a identidade $\Pi_{S_R}=\rho$ for descrita como polarização/redução
   condicional;
6. normalizações contínuas forem remetidas a cálculos próprios de fluxo,
   Hessiana, DtN ou contorno.

Com esses cuidados, o capítulo pode servir como ponte técnica entre os
capítulos fundacionais e os capítulos posteriores de espectro, partículas,
medida e metrologia.

## Revisão didática de 2026-07-19

O Capítulo 6 foi conferido na fase de revisão científica/didática. A
terminologia do checklist foi ajustada para separar extensões metrológicas de
lacunas fundacionais: $\alpha$, $G$, canais massless, detectores e backgrounds
warped/mistos usam a ponte, mas não são a própria ponte.

O script `verificar_homomorfismo_relogio.py` foi atualizado para o cabeçalho
autocontido padrão: objetivo, fonte teórica, classificação, equação, domínio,
parâmetros e saída. Todos os scripts do capítulo devem permanecer como
verificações didáticas, não como previsões físicas.
