# Geometrodinâmica Quântica — GDQ

Este repositório contém a edição pública do manuscrito da
**Geometrodinâmica Quântica (GDQ)** e sua formalização parcial em Lean 4.

A GDQ é um programa independente de pesquisa que investiga se matéria,
fenômenos quânticos e seus limites clássicos podem ser descritos a partir de
uma geometria complexa dinâmica, com medida ponderada, contornos e torção.

O repositório não apresenta a proposta como teoria experimentalmente
estabelecida. Seu objetivo é tornar públicas e auditáveis as definições,
hipóteses, derivações, reduções efetivas, verificações simbólicas e numéricas,
formalizações e limitações do programa.

## Ação oficial

A estrutura física fundamental adotada pelo manuscrito é:

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(
\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

Fontes, sondas, condições de contorno e reduções efetivas não são tratadas
como alterações silenciosas dessa ação. O texto procura distinguir
explicitamente:

- axiomas e definições;
- derivações e teoremas condicionais;
- reduções efetivas;
- hipóteses e programas futuros;
- evidências numéricas;
- calibrações e engenharia inversa;
- comparações fenomenológicas;
- previsões sem pós-ajuste.

## Organização

- [`manuscrito/`](manuscrito/): edição principal, escrita para Obsidian e
  Quartz, acompanhada de notas, scripts reproduzíveis e fichas
  bibliográficas;
- [`formal/`](formal/): formalização parcial em Lean 4, documentação do
  escopo de cada prova e scripts auxiliares de verificação.

O ponto de entrada para a leitura é o
[índice do manuscrito](manuscrito/index.md). O
[índice das provas formais](formal/index.md) indica o que foi certificado em
Lean e, igualmente importante, quais hipóteses analíticas ou geométricas
permanecem externas a cada módulo.

## Reprodutibilidade

Os scripts incluídos junto aos capítulos documentam avaliações diretas,
testes de consistência, estudos de convergência e comparações
fenomenológicas. Cada resultado deve ser interpretado segundo a classificação
declarada no texto; concordância numérica isolada não demonstra derivação a
partir da ação oficial.

Arquivos gerados automaticamente, caches Python e artefatos locais de
compilação não fazem parte da fonte pública. Para Lean, consulte
[`formal/README.md`](formal/README.md) e o arquivo
[`formal/lean-toolchain`](formal/lean-toolchain).

## Estado científico

Este é um trabalho de pesquisa em desenvolvimento e está aberto a revisão
independente. Algumas cadeias são demonstradas apenas sob backgrounds,
domínios, condições de contorno ou hipóteses de estabilidade explicitamente
declaradas. Resultados condicionais não devem ser citados como demonstrações
universais.

Críticas matemáticas, reprodução dos cálculos, identificação de hipóteses
ocultas e tentativas de refutação são bem-vindas por meio das *Issues*.

## Inteligência artificial e responsabilidade

O desenvolvimento do projeto utiliza Codex/GPT, da OpenAI, e
Antigravity/Gemini, do Google, como sistemas de colaboração intelectual para
organização, cálculo, programação, exploração de hipóteses e revisão crítica.
Não existe uma divisão fixa de funções entre eles.

Resultados produzidos com auxílio de IA somente integram o manuscrito quando
registrados de forma verificável e classificados segundo seu real alcance.
IA não constitui fonte científica, validação experimental nem revisão por
pares. A responsabilidade editorial pela versão publicada permanece com o
autor.

## Citação

Enquanto não houver um arquivo `CITATION.cff` ou uma versão arquivada
específica, cite o repositório pelo título, autor, URL e identificador do
commit consultado. Versões depositadas em repositórios de preservação devem
ser preferidas quando disponíveis.

## Licença

O texto e a documentação autoral são disponibilizados sob
**CC BY-NC-ND 4.0**. Os códigos Python e Lean são disponibilizados sob a
**Licença MIT**. Materiais bibliográficos de terceiros não são relicenciados.
Consulte [`LICENSE.md`](LICENSE.md) para o escopo exato.

