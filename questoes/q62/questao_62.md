# Questão 62 — Potências e unidades

## 1. Enunciado

A questão pede corrigir expressões dimensionalmente ambíguas do tipo:

$$
125\,\mathrm{GeV}^2
$$

quando o sentido físico pretendido é a massa ao quadrado:

$$
(125\,\mathrm{GeV})^2.
$$

Essa distinção é editorial, mas importante: `125 GeV^2` é lido como um número
linear multiplicado por uma unidade quadrática; `(125 GeV)^2` representa o
quadrado da escala de massa.

---

## 2. Arquivos auditados

Foram auditados os arquivos relacionados no enunciado:

- `pt-br/33 - A Barreira Ultravioleta e a Estabilidade Eletrofraca.md`;
- `pt-br/35 - Anomalias Leptônicas e Estrutura Hadrônica Fina.md`.

Também foi corrigida a tradução correspondente:

- `en/33 - The Ultraviolet Barrier and Electroweak Stability.md`.

---

## 3. Correção aplicada

No Capítulo 33 havia a passagem:

$$
M_{H,\text{fisico}}^2
\approx
125\,\text{GeV}^2
+\mathcal O(10^{-6}\,\text{GeV}^2).
$$

Ela foi corrigida para:

$$
M_{H,\text{fisico}}^2
\approx
(125\,\text{GeV})^2
+\mathcal O(10^{-6}\,\text{GeV}^2).
$$

A mesma correção foi aplicada no arquivo em inglês.

---

## 4. O que não foi alterado

A expressão:

$$
\Delta M_H^2
\propto
(1{,}53)^2(0{,}511\,\text{MeV})^2
\approx
0{,}68\,\text{MeV}^2
$$

foi preservada, pois ali `0,68 MeV^2` designa diretamente o valor de uma
quantidade de dimensão massa ao quadrado. Escrever `(0,68 MeV)^2` mudaria o
valor físico.

O Capítulo 35 não continha ocorrência equivalente de potência mal colocada
nos trechos relacionados.

---

## 5. Veredito

$$
\boxed{
\text{Q62 fechada como correção editorial-dimensional.}
}
$$

A correção não modifica a ação oficial, a cadeia dedutiva da GDQ ou qualquer
resultado numérico. Ela apenas remove uma ambiguidade de notação em potência e
unidade.

