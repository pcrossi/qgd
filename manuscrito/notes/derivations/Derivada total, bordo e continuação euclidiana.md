---
title: "Derivada total, bordo e continuação euclidiana"
tipo: derivacao
status: identidade-exata-com-cautela-analitica
---

# Derivada total, bordo e continuação euclidiana

## 1. Ação real

Considere

$$
L'=L+\frac{dF(x,t)}{dt}.
$$

Para um caminho com extremos $(x_0,t_0)$ e $(x_1,t_1)$,

$$
S'[x]
=\int_{t_0}^{t_1}L'\,dt
=S[x]+F(x_1,t_1)-F(x_0,t_0).
$$

Logo,

$$
e^{iS'[x]/\hbar}
=e^{i(F_1-F_0)/\hbar}e^{iS[x]/\hbar}.
$$

O fator independe do interior do caminho, mas depende dos extremos. Para uma
equivalência física, estados de bordo e observáveis devem receber a
transformação compatível.

## 2. Continuação

Suponha que $F(x,t)$ admita continuação analítica para $t=-i\tau$. Defina a
ação euclidiana pela convenção

$$
e^{iS/\hbar}\longrightarrow e^{-S_E/\hbar}.
$$

Se o termo continuado $F_E$ for real, então

$$
S_E'=S_E+F_{E,1}-F_{E,0}
$$

e

$$
e^{-S_E'/\hbar}
=e^{-(F_{E,1}-F_{E,0})/\hbar}e^{-S_E/\hbar}.
$$

O fator é real e pode alterar a normalização aparente do kernel. Se $F_E$ não
for real, a separação entre fase e amortecimento será diferente. Por isso a
natureza do termo não pode ser decidida antes de especificar a continuação.

## 3. O que permanece invariante

A derivada total não altera as equações de Euler--Lagrange no interior quando
as variações dos extremos são fixadas. Ela pode alterar:

1. o funcional gerador na fronteira;
2. as condições naturais quando o bordo varia;
3. a fase ou normalização dos estados;
4. a realização do operador no domínio euclidiano.

Portanto a conclusão correta não é que Wick “quebra o calibre”. A conclusão é
que a equivalência de calibre deve ser continuada conjuntamente no bulk, nos
estados e no bordo.
