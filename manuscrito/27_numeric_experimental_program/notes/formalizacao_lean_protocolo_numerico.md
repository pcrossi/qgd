---
title: "Nota — Formalização Lean do protocolo numérico"
---

# Nota — Formalização Lean do protocolo numérico

O módulo
[`NumericalProtocol.lean`](../../../formal/GDQ/NumericalProtocol.lean)
formaliza a contabilidade lógica do programa numérico. Ele não certifica um
background físico, um solver particular ou uma comparação experimental.

## 1. Classes numéricas

Foram separados sete usos:

1. avaliação direta;
2. teste de convergência;
3. teste de consistência;
4. engenharia inversa;
5. calibração;
6. comparação fenomenológica;
7. previsão cega.

Lean verifica, por construção, que engenharia inversa, convergência e previsão
cega não são a mesma classe.

## 2. Manifesto reprodutível

O tipo `NumericalManifest` registra doze itens: equação, background, domínio,
bordo, vínculos, operador, projetor físico, normalização e unidades, fonte do
aparelho, observável, parâmetros numéricos e uso dos dados experimentais.

O predicado `ReproducibleManifest` exige todos os itens simultaneamente. Isso
é um contrato documental: preencher o manifesto não prova que o cálculo está
correto, mas sua ausência impede auditá-lo adequadamente.

## 3. Previsão cega e comparação forte

O predicado `BlindPredictionEligible` exige:

$$
\begin{aligned}
&\text{fórmula derivada antes da comparação},\\
&\text{parâmetros universais congelados},\\
&\text{dados do aparelho medidos independentemente},\\
&\text{alvo ausente da construção},\\
&\text{convergência verificada},\\
&\text{incerteza numérica declarada},\\
&\text{sensibilidade ao bordo declarada}.
\end{aligned}
$$

O teorema
`not_blindPredictionEligible_of_target_used` prova formalmente que usar o alvo
na construção impede essa classificação. O teorema correspondente para
parâmetros não congelados dá a mesma conclusão.

Uma comparação metrologicamente forte ainda exige incerteza experimental,
erro numérico menor que a discrepância examinada e o mesmo conjunto de
parâmetros em mais de um observável.

## 4. Erro numérico e discrepância física

Para valor calculado $u_h$, limite contínuo $u$ e alvo físico $u_{\rm exp}$,
a desigualdade triangular fornece:

$$
|u_h-u_{\rm exp}|
\le
|u_h-u|
+
|u-u_{\rm exp}|.
$$

O primeiro termo mede discretização; o segundo mede discrepância física do
modelo contínuo. O teorema Lean
`numerical_physical_error_decomposition` impede que esses erros sejam
silenciosamente somados sob um único rótulo.

## 5. Alcance

Esta formalização certifica regras de classificação e identidades de erro.
Ela não promove a previsão:

$$
\text{protocolo correto}
\not\Rightarrow
\text{background correto}.
$$

A previsão física continua exigindo a cadeia da ação oficial até o observável,
com domínio, contornos, estabilidade e ausência de pós-ajuste.
