---
title: "Formalização Lean do estado lógico"
---

# Formalização Lean do estado lógico

O módulo [LogicalStatus.lean](../../../formal/GDQ/LogicalStatus.lean) não
introduz uma equação física. Ele formaliza a gramática usada para impedir que
categorias diferentes sejam confundidas.

## 1. Classes de afirmação

O tipo `ClaimClass` distingue:

1. axioma;
2. definição;
3. derivação;
4. teorema condicional;
5. redução efetiva;
6. evidência numérica;
7. engenharia inversa;
8. comparação fenomenológica;
9. programa futuro.

Como essas classes são construtores distintos, o Lean certifica, por exemplo:

$$
\text{evidência numérica}\ne\text{axioma},
$$

$$
\text{redução efetiva}\ne\text{axioma}.
$$

## 2. Axiomas e dados do problema

O registro `CoreAxioms` contém apenas:

1. ação oficial;
2. classe Hermitiana/Bismut.

O registro `ProblemData` contém separadamente:

1. contorno causal;
2. topologia admissível;
3. condições de bordo;
4. calibração metrológica.

Essa separação tipada expressa uma decisão física importante: mudar o
aparelho, o contorno ou a calibração não muda silenciosamente a ação
fundamental.

## 3. Cadeia mínima de fechamento

Uma previsão forte é definida pela conjunção:

$$
\begin{aligned}
&\text{ação oficial}
\land
\text{background admissível}
\land
\text{Hessiana física}\\
&\land
\text{operador e domínio}
\land
\text{condições de bordo}
\land
\text{espectro estável}\\
&\land
\text{observável sem pós-ajuste}.
\end{aligned}
$$

O Lean prova que a ausência de um background admissível ou o uso de
pós-ajuste impedem a classificação como previsão forte. Isso não declara o
resultado falso; apenas impede uma classificação mais forte que a cadeia
demonstrada.

## 4. Redução controlada

Uma redução é controlada somente quando:

$$
\text{preserva a ação}
\land
\text{declara o domínio}
\land
\text{declara o bordo}
\land
\text{usa o projetor físico}.
$$

Se a ação for trocada, a redução deixa formalmente de ser uma redução GDQ.
Esse critério protege o manuscrito contra a importação silenciosa de uma
ontologia externa.

## 5. Significado de “backlog estrutural zerado”

No inventário vigente, essa expressão tem sentido restrito:

> a triagem das questões não registra uma contradição estrutural não
> classificada que impeça a continuação do programa.

Ela não significa:

1. que todo background admissível já foi construído;
2. que toda Hessiana 8D já foi diagonalizada;
3. que todo teorema condicional virou teorema incondicional;
4. que toda metrologia ou aparelho real já foi calculado.

Esses itens continuam nos status próprios de condicional, redução,
refinamento ou programa futuro.
