# Mapa de migração do Capítulo 1 original

## Finalidade

Este documento impede que ideias do arquivo histórico
`pt-br/01 - O Problema Inicial - A Divergência entre a Integral de Feynman e a de Wiener.md`
sejam perdidas durante a reestruturação. Ele não integra o texto público do
capítulo; é um controle editorial de origem, destino e status científico.

## Critério

Cada bloco do original deve receber exatamente um dos seguintes destinos:

- **incorporado:** já reescrito no novo manuscrito;
- **transferir:** pertence a capítulo posterior;
- **nota:** explicação pedagógica separada;
- **auditar:** contém uma afirmação que precisa de demonstração ou correção;
- **histórico:** preservado como parte da gênese, mas não usado como premissa.

## Rastreabilidade

| Conteúdo do original | Destino | Status |
|---|---|---|
| Divergência entre Wiener e Feynman | `01.3 - Duas integrais sobre caminhos.md` | incorporado |
| Medida positiva de Wiener | `01.3` e nota sobre medidas | incorporado |
| Peso oscilatório de Feynman | `01.3` | incorporado |
| Tabela comparativa dos formalismos | `01.3` e `01.6` | incorporado |
| Rotação de Wick | `01.4` | incorporado |
| Limites de analiticidade, espectro e positividade | `01.4` | incorporado |
| Derivada total na Lagrangiana | `01.5` | incorporado |
| Fase de bordo no kernel de Feynman | `01.5` | incorporado |
| Fator real no kernel euclidiano | `01.5` | incorporado |
| Transformação de calibre e estados de bordo | `01.5` | incorporado com correção de rigor |
| Afirmação de quebra universal de calibre por Wick | não usar como teorema | auditado e corrigido |
| Não diferenciabilidade das trajetórias de Wiener | `01.6` | incorporado |
| Derivadas progressiva e regressiva | `01.6` | incorporado como rota matemática, não fundamento |
| Velocidades de corrente e osmótica | `01.6`, depois Capítulo 2/3 | introduzido; derivação transferida |
| Decomposição polar de Madelung | capítulo de geometrização/estrutura dos campos | transferir |
| Equação de continuidade | capítulo da ação e redução de Madelung | transferir |
| Hamilton–Jacobi com termo quântico | capítulo da ação e redução de Madelung | transferir |
| Interpretação do termo de Bohm como pressão geométrica | capítulo de geometrização; prova após a ação | transferir e auditar |
| Relação entre adjunto, continuidade e fluxo de bordo | nota pedagógica e capítulo variacional | transferir |
| Simetria avançada/retardada associada a Sudarshan | capítulo de causalidade complexa | transferir e auditar |
| Escolha $\nu=\hbar/(2m)$ | capítulo de redução estocástica | transferir; não tratar como derivada ainda |
| Coeficiente universal $\nu_0$ | capítulo da ação/redução | auditar |
| Escala $m_0$ como atrator de confinamento | capítulo de massas/estabilidade | auditar; depende de derivação independente |
| Fator de compressão $\Omega=m/m_0$ | capítulo de massa geométrica | auditar dimensões e origem variacional |
| SDE com difusão $\nu_0\Omega^{-1}$ | capítulo estocástico | auditar cálculo de Itô e métrica |
| Emergência da massa inercial pela compressão | capítulo de massa geométrica | transferir como hipótese até demonstração |
| Fluxo de Ricci e funcional de Perelman | `01.4`, aprofundamento posterior | incorporado como motivação |
| Generalização torsional do fluxo | capítulo geométrico e apêndice técnico | transferir; requer identidade variacional |
| Matéria como configuração geométrica | abertura do Capítulo 2 | transferir |

## Pendências antes de declarar o Capítulo 1 editorialmente completo

1. adicionar referências primárias para Wiener, Feynman e Wick;
2. adicionar referência técnica para integrais oscilatórias e fórmula de
   Feynman–Kac;
3. adicionar referência para derivadas médias progressiva/regressiva;
4. revisar a continuação de potenciais de calibre, incluindo convenções de
   $A_0$, assinatura e transformação dos estados;
5. ligar `01.6` à nota pedagógica sobre medidas em espaços de caminhos;
6. decidir se o acordo terminológico permanece como `01.2` ou volta a ser um
   capítulo preliminar sem alterar seu conteúdo.

## Regra de preservação

Nenhum item marcado como **transferir** pode ser declarado descartado. Nenhum
item marcado como **auditar** pode aparecer no novo manuscrito como resultado
demonstrado antes que sua cadeia dedutiva seja registrada.
