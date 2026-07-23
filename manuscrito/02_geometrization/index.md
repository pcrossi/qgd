---
title: "02. A geometrização da matéria"
---

# 02. A geometrização da matéria

No primeiro capítulo encontramos duas descrições matemáticas que parecem
apontar para o mesmo fenômeno físico, mas que vivem em regimes analíticos
distintos. A integral de Wiener organiza difusão e probabilidade positiva; a
integral de Feynman organiza fase e interferência. A decomposição de Madelung
mostrou que densidade e fase podem coexistir numa mesma variável complexa, mas
isso ainda não explicou por que o espaço no qual elas evoluem deveria
permanecer imóvel.

Este capítulo introduz a hipótese construtiva central da GDQ: **a matéria será
procurada como uma configuração localizada de uma geometria dinâmica**, e não
como um objeto pontual acrescentado a um fundo rígido. A frase é uma proposta
de investigação, não uma conclusão pronta. Para que uma configuração
geométrica mereça o nome de matéria, teremos de demonstrar estacionariedade,
localização, conservação, estabilidade e resposta observável.

O caminho será construído sem saltos. Primeiro definiremos o domínio e sua
dimensão. Depois introduziremos a estrutura Hermitiana, a conexão de Bismut, o
campo complexo e a medida ponderada. Só então escreveremos a ação oficial e
formularemos critérios para distinguir um sóliton geométrico de um background
material. Ao final, explicaremos como uma métrica lorentziana pode ser
reconstruída sem mudar a assinatura positiva do bulk.

## Roteiro do capítulo

- [[02.1 - Do fundo rígido à geometria dinâmica]]
- [[02.2 - Domínio fundamental e dimensão]]
- [[02.3 - Estrutura Hermitiana e conexão de Bismut]]
- [[02.4 - Campo complexo, densidade e fase]]
- [[02.5 - Medida ponderada e kernel de calor]]
- [[02.6 - Perelman como matriz geométrica auxiliar]]
- [[02.7 - A ação oficial da GDQ]]
- [[02.8 - Da geometria a um background material]]
- [[02.9 - Circulação, torção e defeitos]]
- [[02.10 - Do bulk Riemanniano ao espaço-tempo físico]]
- [[02.11 - Existência, estabilidade e alcance da proposta]]

## Como ler as classificações

Ao longo do capítulo usaremos quatro níveis diferentes:

1. **definição**, quando fixamos a linguagem da teoria;
2. **identidade**, quando uma fórmula segue algebricamente das definições;
3. **teorema condicional**, quando a conclusão exige hipóteses declaradas;
4. **programa**, quando identificamos um cálculo ainda necessário.

Essa separação é indispensável. A geometrização só terá conteúdo preditivo se
as propriedades observáveis forem consequências da ação e de dados de
contorno independentes, e não nomes novos para resultados já conhecidos.

Uma consequência prática dessa regra é que o capítulo não tenta provar tudo de
uma vez. Ele fixa o vocabulário geométrico, mostra quais identidades já seguem
das definições e separa as hipóteses que serão fechadas em setores concretos.
Assim, quando capítulos posteriores calcularem massa, carga, spin ou resposta
a uma sonda, o leitor poderá identificar exatamente qual parte veio da
geometria de base e qual parte veio do background, da Hessiana, do contorno ou
do aparelho.

## Controle editorial

O destino das afirmações do capítulo histórico está registrado em
[[preservation_map|Mapa de preservação do Capítulo 2]]. A redução do conjunto
de postulados aparece em [[axiom_to_theorem_audit|Auditoria de axiomas e
teoremas]]. O controle operacional do capítulo está em
[[checklist_operacional|Checklist operacional do Capítulo 2]].
As provas, lemas e definições associados estão em
[[notes/provas_lemas_definicoes|Provas, lemas e definições associados]].

[[../index|← Home]] | [[02.1 - Do fundo rígido à geometria dinâmica|Next →]]
