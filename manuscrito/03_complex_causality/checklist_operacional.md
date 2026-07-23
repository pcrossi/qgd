---
title: "Checklist operacional — Capítulo 3"
---

# Checklist operacional — Capítulo 3

Este checklist segue o protocolo metodológico do Capítulo 27.

O capítulo deve resolver o paradoxo de Wick no sentido estrutural da GDQ:
separar a rotação de Wick como técnica analítica da definição causal própria da
ação oficial.

## 1. Objetivo do capítulo

O Capítulo 3 deve demonstrar didaticamente que:

1. Wick relaciona grupo unitário e semigrupo sob hipóteses, mas não define
   sozinho causalidade;
2. tempo físico $t$, parâmetro de fluxo $\tau$ e variável causal $z_\tau$ são
   objetos distintos;
3. a GDQ usa uma variável causal complexa dimensionalmente homogênea;
4. o contorno causal $\gamma$ é parte do domínio da ação oficial;
5. formas exatas, períodos, resíduos, cortes e monodromias têm papéis
   diferentes;
6. setores retardado e avançado são linguagem de contorno, não sinal físico do
   futuro;
7. a realidade da ação é um teorema no contorno admissível;
8. quantização por circulação exige holonomia, classe integral e normalização;
9. microcausalidade operacional e no-signalling pertencem à teoria da medida.

Status do capítulo: **fechado estruturalmente para a arquitetura causal da
GDQ**.

## 2. Situação do corpo principal

| Seção | Status | Observação |
|---|---|---|
| `03.1` | pronta em primeira versão | Formula corretamente o paradoxo de Wick. |
| `03.2` | pronta em primeira versão | Separa $t$, $\tau$ e $z_\tau$. |
| `03.3` | pronta em primeira versão | Distingue formas exatas, períodos e resíduos. |
| `03.4` | pronta em primeira versão | Reinterpreta avançado/retardado como setor de contorno. |
| `03.5` | pronta condicionalmente | Realidade depende de pareamento por conjugação/reflexão. |
| `03.6` | pronta condicionalmente | Quantização por monodromia depende de integralidade e normalização. |
| `03.7` | aberta como extensão operacional | Microcausalidade/no-signalling são tarefas da teoria da medida. |
| `03.8` | pronta em primeira versão | Consolida o sentido exato do “fim do paradoxo”. |

## 3. Notas chamadas e função lógica

| Nota | Função |
|---|---|
| `Derivadas exatas, estados de extremidade e continuação causal` | Mostra como termos exatos transformam estados de extremidade. |
| `Variável causal complexa - dimensão, simetrias e unicidade condicional` | Justifica $z_\tau=\tau+i\nu_0t$ na classe afim mínima. |
| `Formas exatas, períodos e resíduos no contorno causal` | Separa cancelamento, cohomologia e resíduos. |
| `Sudarshan como linguagem de contorno` | Preserva avançado/retardado sem retrocausalidade operacional. |
| `Realidade de uma ação integrada em contorno complexo` | Demonstra realidade por pareamento no contorno admissível. |
| `Quantização por monodromia e classe integral` | Mostra por que resíduo sozinho não basta para quantização física. |

Avaliação: as notas principais existem e estão alinhadas ao texto.

## 4. Material legado preservado

Fonte legada principal:

o capítulo legado correspondente

Blocos preservados:

1. crítica à rotação de Wick como substituição formal;
2. papel dos termos de contorno;
3. intuição Sudarshan avançado/retardado;
4. fechamento de contorno;
5. circulação e quantização;
6. preocupação com unitariedade;
7. possibilidade de dinâmica de rotação causal;
8. relação histórica com Wiener/Feynman.

Correções de status em relação ao legado:

1. Wick não “falha” genericamente; ele exige domínio, espectro, bordos e
   positividade;
2. derivada total não quebra calibre em geral; ela exige transformação
   conjunta de estados e observáveis;
3. setor avançado não implica retrocausalidade operacional;
4. contorno fechado não prova sozinho unitariedade;
5. teorema dos resíduos não gera automaticamente $nh$;
6. a equação dinâmica para ângulo $\theta$ permanece programa futuro;
7. não se identifica $S_I=\hbar\mathcal W$ como prova da equivalência rigorosa
   Feynman–Wiener.

## 5. Resultados e limites

### Demonstrado ou definido

1. separação conceitual entre $t$, $\tau$ e $z_\tau$;
2. homogeneidade dimensional de $z_\tau=\tau+i\nu_0t$;
3. papel de $\gamma$ como contorno causal da ação;
4. cancelamento de formas exatas regulares em ciclos fechados;
5. possibilidade de períodos e resíduos quando hipóteses globais falham;
6. realidade da ação na classe refletida de contornos admissíveis.

### Condicional

1. unicidade de $z_\tau$ somente na classe afim mínima;
2. realidade da ação depende de reflexão/conjugação;
3. quantização por monodromia depende de classe integral e normalização;
4. microcausalidade operacional depende da teoria de aparelho e registro.

### Não demonstrado neste capítulo

1. unitariedade completa;
2. no-signalling experimental;
3. reconstrução do espaço de Hilbert;
4. dinâmica do colapso/medida;
5. equação variacional para um ângulo de Wick dinâmico;
6. equivalência rigorosa universal entre Feynman e Wiener.

## 6. Referências necessárias

Fichas já presentes:

- Wick 1954;
- Osterwalder–Schrader 1973;
- referências de Feynman/Wiener usadas no Capítulo 1.

Referências futuras possíveis:

- Cauchy/resíduos, se quisermos fichas históricas;
- Sudarshan, caso o trecho avançado/retardado permaneça citado
  historicamente;
- teoria de funções de Green retardadas/avançadas.

O usuário adicionará as referências depois; o capítulo não depende delas para
o controle operacional atual.

## 7. Scripts numéricos e simbólicos

Scripts obrigatórios para fechamento do Capítulo 3: **nenhum**.

Motivo: o capítulo fixa a arquitetura causal e seus teoremas elementares. Não
há previsão metrológica.

Scripts opcionais criados em [[scripts/README|scripts/]]:

1. [[scripts/verificar_z_tau_dimensional.py|verificar_z_tau_dimensional.py]]  
   Checar a homogeneidade dimensional de $z_\tau=\tau+i\nu_0t$.

2. [[scripts/verificar_integral_forma_exata.py|verificar_integral_forma_exata.py]]  
   Mostrar numericamente que uma forma exata regular integra zero em ciclo
   fechado e comparar com uma forma de período não trivial.

3. [[scripts/verificar_pareamento_realidade_contorno.py|verificar_pareamento_realidade_contorno.py]]  
   Ilustrar que pares conjugados no contorno produzem contribuição real.

Classificação dos três: teste simbólico/ilustração pedagógica, não previsão.

## 8. Pontos didáticos a revisar na leitura final

Antes de considerar o Capítulo 3 editorialmente pronto:

1. garantir que “fim do paradoxo” não soe como “Wick está errado”;
2. reforçar que $\gamma$ pertence à ação oficial da GDQ;
3. não deixar avançado/retardado parecer sinalização para o passado;
4. separar monodromia, resíduo e quantização física;
5. manter microcausalidade como extensão da teoria de medida;
6. revisar a fluidez entre as seções `03.3`, `03.4` e `03.5`;
7. conferir links e renderização.

## 9. Veredito operacional

O Capítulo 3 está **estruturalmente montado**.

Ele cumpre sua função: substituir a dependência de uma rotação de Wick externa
por uma arquitetura causal própria da GDQ, baseada em $z_\tau$ e no contorno
$\gamma$.

As pendências restantes são:

1. revisão didática;
2. referências históricas adicionais;
3. scripts opcionais de ilustração;
4. tratamento posterior de microcausalidade/no-signalling na teoria da medida.

## Revisão didática de 2026-07-19

O capítulo foi conferido na fase de revisão científica/didática. O corpo está
autocontido: não depende de arquivos históricos, rótulos de auditoria ou
pastas de trabalho. O `index.md` recebeu um parágrafo que explicita a mudança
de pergunta: a GDQ não prova a causalidade por rotação de Wick, mas por
contorno causal complexo já pertencente à ação oficial. A seção `03.5` foi
ajustada para evitar falso positivo editorial com terminologia histórica.

Os três scripts do capítulo foram reexecutados. Eles continuam classificados
como verificações simbólicas/ilustrações pedagógicas:

1. homogeneidade dimensional de $z_\tau$;
2. diferença entre integral de forma exata e período angular;
3. realidade por pareamento conjugado.

Nenhum deles é previsão metrológica e nenhum usa alvo experimental.
