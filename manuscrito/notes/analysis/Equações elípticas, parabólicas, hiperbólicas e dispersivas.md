---
title: "Equações elípticas, parabólicas, hiperbólicas e dispersivas"
tipo: nota
---

# Equações elípticas, parabólicas, hiperbólicas e dispersivas

## Por que classificar equações

A classificação local de uma equação diferencial é determinada pela parte
principal do operador. Entretanto, a expressão diferencial, isoladamente, não
define todo o problema físico. Também é necessário especificar o domínio, os
dados iniciais e as condições de contorno ou de radiação.

Essa distinção, central nos tratamentos de Sommerfeld e de Morse–Feshbach,
separa duas perguntas:

1. qual é o tipo local da expressão diferencial?
2. qual problema físico e espectral foi definido para essa expressão?

Usaremos **tipo da equação** para a classificação pelo símbolo principal e
**problema de contorno** para a realização física completa.

## Equações elípticas

O exemplo elementar é a equação de Laplace:

$$
\Delta u=0.
$$

Ela descreve configurações de equilíbrio. Em geral, problemas elípticos são
formulados com dados de contorno e não definem uma propagação temporal causal.

A equação de Helmholtz fornece um exemplo importante. O operador espacial é
elíptico, mas, num domínio exterior, ainda precisamos escolher o comportamento
assintótico. A condição de radiação de Sommerfeld seleciona ondas de saída ou
de entrada. Ela não muda o tipo elíptico da expressão diferencial; muda a
solução física admissível e a função de Green correspondente.

## Equações parabólicas

O exemplo básico é a equação do calor:

$$
\frac{\partial u}{\partial\tau}
=\kappa\Delta u.
$$

Ela descreve difusão e suavização. Dados iniciais determinam uma evolução na
qual irregularidades de pequena escala são amortecidas.

O fluxo de Ricci possui caráter parabólico depois de corrigida a degeneração
produzida pela invariância por difeomorfismos.

## Equações hiperbólicas

O exemplo básico é a equação de ondas:

$$
\frac{\partial^2u}{\partial t^2}
-c^2\Delta u=0.
$$

Perturbações propagam-se com domínio causal finito. Operadores lorentzianos,
como o operador de Klein–Gordon, pertencem a essa classe sob condições usuais.

O símbolo hiperbólico também não escolhe sozinho entre propagadores avançado e
retardado. Essa escolha depende dos dados e da prescrição causal imposta ao
problema.

## Equações dispersivas

A equação de Schrödinger é

$$
i\hbar\frac{\partial\psi}{\partial t}
=H\psi.
$$

Ela é de primeira ordem no tempo e não é hiperbólica no mesmo sentido da
equação de ondas. É classificada como dispersiva: diferentes componentes
espectrais acumulam fases diferentes, produzindo propagação e interferência
sem o amortecimento característico do calor.

## Relação com a continuação euclidiana

Uma continuação entre tempo lorentziano e tempo euclidiano pode relacionar
operadores hiperbólicos a operadores elípticos e evolução unitária a
semigrupos difusivos. Essa relação depende do operador, do espectro, do domínio
e das condições de contorno; não é consequência automática de substituir uma
letra por outra.

## A equação e o problema de contorno

Na linguagem da física matemática, uma mesma expressão diferencial pode gerar
operadores distintos quando recebe domínios ou condições de contorno
diferentes. Esquematicamente:

$$
\boxed{
\text{operador físico}
=\text{expressão diferencial}
+\text{domínio}
+\text{condições de contorno}.
}
$$

As condições de contorno podem determinar:

- existência e unicidade;
- auto-adjunticidade;
- espectro discreto ou contínuo;
- modos de borda e ressonâncias;
- estabilidade;
- soluções de entrada ou saída;
- função de Green avançada, retardada ou euclidiana.

É nesse sentido que elas participam da classificação física do problema. Elas
não alteram, em geral, o discriminante local da equação, mas determinam qual
realização do operador representa o sistema observado.

Esse é o cuidado encontrado em *Partial Differential Equations in Physics*, de
Arnold Sommerfeld, e em *Methods of Theoretical Physics*, de Philip M. Morse e
Herman Feshbach: equação, domínio, contorno, função de Green e espectro devem
ser tratados como partes de um mesmo problema matemático.

## Aplicação na GDQ

No manuscrito, utilizaremos:

- **elíptico** para operadores espaciais e problemas estacionários;
- **parabólico** para o setor de fluxo e difusão;
- **hiperbólico** para propagação lorentziana relativística;
- **dispersivo ou unitário** para a evolução de Schrödinger.

Essa convenção evita chamar toda dinâmica quântica de hiperbólica e torna mais
precisa a ponte proposta entre os diferentes setores. Para cada operador da
GDQ registraremos separadamente:

1. símbolo principal;
2. domínio;
3. condições iniciais e de contorno;
4. prescrição causal;
5. realização espectral.

[[index|← Análise e probabilidade]]
