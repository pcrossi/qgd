# Geometrodinâmica Quântica — GDQ

Bem-vindo à edição reestruturada do manuscrito da **Geometrodinâmica
Quântica (GDQ)**.

Este diretório reúne a versão destinada à leitura contínua e à publicação com
Obsidian e Quartz. O material histórico, as auditorias, os cálculos
exploratórios e as simulações permanecem no repositório de trabalho, mas não
são automaticamente tratados como partes demonstradas do manuscrito.

## Do que trata a proposta?

A GDQ investiga a possibilidade de descrever matéria, fenômenos quânticos e
seus limites clássicos a partir de uma geometria complexa dinâmica, dotada de
fluxo, medida ponderada, contornos e torção.

Em vez de assumir partículas pontuais inseridas num fundo geométrico rígido, o
programa explora a hipótese de que matéria e suas propriedades observáveis
possam corresponder a configurações localizadas, circulações e defeitos da
própria geometria.

O problema inicial nasce da comparação entre duas integrais sobre caminhos:

- a integral de Wiener, baseada numa medida probabilística positiva e
  associada à difusão;
- a integral de Feynman, baseada em amplitudes complexas oscilatórias e
  associada à interferência quântica.

O manuscrito procura determinar se esses regimes podem ser reconstruídos como
aspectos compatíveis de uma mesma dinâmica geométrica, sem identificar
indevidamente probabilidades com amplitudes nem tratar a rotação de Wick como
uma equivalência automática.

## Um experimento de construção iterativa com inteligência artificial

Além da proposta física, este repositório registra um método de desenvolvimento
atípico. Intuições, conexões conceituais e rascunhos acumulados ao longo do
tempo são organizados e testados iterativamente com o auxílio de modelos de
inteligência artificial.

O desenvolvimento utiliza principalmente dois ambientes de IA:

- **Codex/GPT, da OpenAI**;
- **Antigravity/Gemini, do Google**.

Não existe uma divisão fixa de funções entre eles. Conforme a etapa do
trabalho, qualquer um dos dois pode ser usado para organizar o manuscrito,
propor ideias, desenvolver derivações, construir testes numéricos, pesquisar
rotas alternativas ou revisar criticamente um resultado. Em outros momentos,
um sistema é utilizado para conferir, corrigir ou ampliar o trabalho produzido
pelo outro. As respostas relevantes são posteriormente comparadas com os
documentos, com a ação oficial, com os testes numéricos e com as referências
disponíveis.

A IA é utilizada como ferramenta de amplificação intelectual para:

- organizar fragmentos e dependências;
- explicitar hipóteses antes implícitas;
- desenvolver e conferir passagens algébricas;
- construir testes numéricos;
- localizar contradições e lacunas;
- separar resultados de conjecturas e ajustes.

Codex/GPT e Antigravity/Gemini participam deste trabalho como sistemas de
colaboração intelectual, contribuindo para a elaboração, a organização, o
cálculo e a revisão crítica. O valor de cada contribuição é determinado por sua
consistência, por sua rastreabilidade e por sua capacidade de resistir à
verificação, independentemente de ter sido inicialmente formulada pelo autor ou
por um dos sistemas de IA. Nenhuma resposta isolada constitui validação
científica nem substitui demonstração, evidência experimental ou revisão
independente.

## Estado científico do trabalho

Este é um manuscrito de pesquisa em desenvolvimento, produzido como projeto
intelectual independente. Física teórica e matemática avançada não são as
áreas profissionais de atuação do autor. O texto deve, portanto, ser lido como
uma construção aberta à crítica, à correção e à verificação externa.

Para evitar que uma hipótese seja confundida com uma conclusão, a edição
reestruturada distingue:

- definição e axioma;
- derivação e teorema condicional;
- redução efetiva;
- hipótese e programa futuro;
- teste de consistência;
- ajuste ou engenharia inversa;
- comparação fenomenológica;
- previsão sem pós-ajuste.

Uma concordância numérica, por si só, não demonstra que um resultado foi
derivado da ação fundamental. Sempre que faltar um elo entre a ação, o
background, o operador, as condições de contorno e o observável, essa pendência
deverá permanecer explícita.

## Organização desta edição

O diretório é estruturado como um cofre do Obsidian compatível com Quartz:

- [`index.md`](index.md): índice público da edição;
- `01_initial_problem/`: Capítulo 1 e suas seções;
- `02_geometrization/`: geometrização da matéria e ação oficial;
- `03_complex_causality/`: causalidade complexa e continuação;
- `04_action_consistency/`: princípio variacional e consistência quântica;
- `05_equations_conservation/`: equações de movimento e Noether;
- `06_global_local_bridge/`: ponte do Universo de Einstein ao laboratório;
- `07_classical_limit/`: limite clássico e princípio da correspondência;
- `ref/`: fontes bibliográficas, OCR integral e OCR por página;
- `notes/`: notas pedagógicas destinadas a explicar a linguagem matemática;
- futuros diretórios numerados: capítulos e apêndices ainda não
  reestruturados.

Os nomes dos diretórios são escritos em inglês e sem caracteres especiais para
preservar URLs estáveis. Os títulos públicos em português são definidos no
campo `title` do cabeçalho YAML de cada `index.md`.

As equações seguem a convenção do Quartz: expressões curtas são escritas em
matemática inline; equações destacadas usam delimitadores de cifra dupla em
linhas próprias.

## Como ler

O ponto de entrada é o [Índice geral do manuscrito](index.md). A leitura
sequencial começa em
[01. O problema inicial](01_initial_problem/index.md), que formula a
divergência entre as integrais de Feynman e Wiener antes de introduzir a
geometrização da matéria.

As notas pedagógicas podem ser consultadas sem interromper a linha principal.
Elas explicam conceitos e notações, mas não substituem as demonstrações
técnicas, que serão mantidas nos capítulos ou apêndices correspondentes.

## Crítica e colaboração

Críticas matemáticas, testes independentes, identificação de hipóteses ocultas
e tentativas de refutação são bem-vindos. O objetivo desta publicação não é
apresentar uma teoria concluída por decreto, mas tornar sua cadeia lógica
visível o suficiente para que possa ser examinada.
