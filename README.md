# GDQ / QGD — antigas notas, duas IAs e uma experiência

**[Português](#português) · [English](#english)**

## Português

Este repositório nasceu de uma curiosidade.

Durante anos acumulamos notas pessoais sobre física, geometria e algumas ideias
que acabaram recebendo o nome de **Geometrodinâmica Quântica (GDQ)**. Essas
notas são anteriores ao uso de inteligência artificial. Em algum momento,
resolvemos entregá-las ao Codex/GPT, da OpenAI, e ao Antigravity/Gemini, do
Google, para ver até onde conseguiríamos levar a construção juntos.

É isso que está registrado aqui.

Não se trata de um programa institucional de pesquisa, de uma teoria aceita
ou de uma promessa de que tudo esteja certo. Também não temos tempo nem
pretensão de transformar esta experiência em atividade. É, em grande parte,
uma brincadeira intelectual: dois autores com notas antigas e duas IAs
tentando organizar ideias, fazer contas, escrever programas, encontrar erros
e descobrir se alguma coisa interessante sobrevive.

As IAs não tiveram funções fixas. Dependendo do momento, uma escreveu, outra
revisou, ambas calcularam, criticaram, sugeriram caminhos e também erraram.
Às vezes ajudaram muito; às vezes confundiram a GDQ com teorias conhecidas;
às vezes entraram em círculos. O processo de corrigir esses problemas também
faz parte do experimento.

Como as IAs continuam evoluindo, pretendemos voltar periodicamente ao
material e submetê-lo novamente aos sistemas disponíveis. A ideia é observar
se novas gerações conseguem encontrar erros antes despercebidos, melhorar as
derivações, propor verificações mais fortes ou chegar a conclusões diferentes.
Não sabemos no que isso vai dar — essa é justamente uma das partes mais
interessantes da experiência.

### O que há aqui

A pergunta central é simples de enunciar, embora difícil de investigar:
será possível descrever matéria, fenômenos quânticos e seus limites clássicos
por meio de uma geometria complexa dinâmica, com medida ponderada, contornos
e torção?

O repositório contém três partes principais:

- [`manuscrito/`](manuscrito/): o texto principal em português, com notas,
  derivações e verificações reproduzíveis;
- [`manuscript/`](manuscript/): a tradução em desenvolvimento para o inglês;
- [`formal/`](formal/): algumas partes traduzidas para Lean 4, para verificar
  com precisão o que foi realmente demonstrado e quais hipóteses foram usadas.

O melhor ponto de entrada é o
[`índice do manuscrito`](manuscrito/index.md). As provas formalizadas estão
organizadas em [`formal/index.md`](formal/index.md).

### Como ler

Nem tudo neste material possui o mesmo estatuto. Há definições, deduções,
teoremas condicionais, aproximações, testes numéricos, comparações com dados,
resultados negativos e ideias ainda abertas. O texto procura dizer qual é o
caso em cada ponto.

Uma conta que coincide com um experimento pode ser interessante, mas não
prova sozinha que a explicação geométrica esteja correta. Do mesmo modo, uma
prova em Lean confirma o enunciado formalizado sob suas hipóteses; ela não
decide por nós se essas hipóteses descrevem a natureza.

Portanto, leia isto como um caderno de construção organizado, não como uma
declaração de teoria. Se no fim houver algo correto e útil, ótimo. Se houver
erros, eles também ajudam a mostrar até onde esse tipo de colaboração entre
humanos e IAs consegue ir.

### Por que publicar

As ideias iniciais já haviam sido registradas anteriormente. Este repositório
preserva a etapa seguinte: o percurso feito com as IAs, incluindo as
derivações que permaneceram, os testes que podem ser repetidos e as limitações
que conseguimos reconhecer.

### Licença

O manuscrito e a documentação autoral são disponibilizados sob
**CC BY-NC-ND 4.0**. Os códigos Python e Lean são disponibilizados sob a
**Licença MIT**. Materiais de terceiros não são relicenciados. Consulte
[`LICENSE.md`](LICENSE.md) para os termos completos.

---

## English

This repository began with a curiosity.

For years, we accumulated personal notes on physics, geometry, and a set of
ideas that eventually came to be called **Quantum Geometrodynamics (QGD)**.
Those notes predate our use of artificial intelligence. At some point, we
decided to give them to OpenAI's Codex/GPT and Google's Antigravity/Gemini to
see how far we could develop the construction together.

That is what this repository records.

This is not an institutional research program, an accepted theory, or a
promise that everything in it is correct. Nor do we have the time or the
intention to turn this experiment into a professional activity. It is, to a
large extent, an intellectual game: two authors with old notes and two AIs
trying to organize ideas, perform calculations, write programs, find errors,
and discover whether anything interesting survives.

The AIs did not have fixed roles. At different times, one wrote while the
other reviewed; both calculated, criticized, suggested paths, and made
mistakes. Sometimes they helped a great deal; sometimes they confused QGD
with established theories; sometimes they went in circles. Correcting those
problems is also part of the experiment.

As AI systems continue to evolve, we intend to return to this material
periodically and submit it again to the systems then available. We want to
see whether newer generations can find previously unnoticed errors, improve
the derivations, propose stronger checks, or reach different conclusions. We
do not know where this will lead — and that is precisely one of the most
interesting parts of the experiment.

### What is here

The central question is easy to state, although difficult to investigate:
can matter, quantum phenomena, and their classical limits be described by a
dynamic complex geometry with a weighted measure, boundaries, and torsion?

The repository has three main parts:

- [`manuscrito/`](manuscrito/): the main Portuguese text, including notes,
  derivations, and reproducible checks;
- [`manuscript/`](manuscript/): the English translation currently in
  development;
- [`formal/`](formal/): selected parts translated into Lean 4, allowing us to
  check precisely what was actually proved and which assumptions were used.

The best place to begin is the
[`Portuguese manuscript index`](manuscrito/index.md). The formalized proofs
are organized in [`formal/index.md`](formal/index.md).

### How to read it

Not everything in this material has the same status. It includes definitions,
deductions, conditional theorems, approximations, numerical tests,
comparisons with data, negative results, and ideas that remain open. The text
tries to identify the status of each result where it appears.

A calculation that agrees with an experiment may be interesting, but by
itself it does not prove that the proposed geometric explanation is correct.
Likewise, a Lean proof certifies the formalized statement under its stated
assumptions; it does not decide whether those assumptions describe nature.

Read this, therefore, as an organized construction notebook rather than a
declaration of an established theory. If something correct and useful
survives, wonderful. If there are errors, they also help reveal how far this
kind of collaboration between humans and AIs can go.

### Why publish it

The original ideas had already been recorded before this experiment. This
repository preserves the next stage: the path taken with the AIs, including
the derivations that survived review, the tests that can be repeated, and
the limitations we were able to recognize.

### License

The manuscript and original documentation are released under
**CC BY-NC-ND 4.0**. The Python and Lean code is released under the
**MIT License**. Third-party materials are not relicensed. See
[`LICENSE.md`](LICENSE.md) for the complete terms.
