# Q39 — Rota H-01: Rosen--Morse como modelo auxiliar, não ontologia da GDQ

## 1. Objetivo

Este documento registra a falha conceitual identificada em
`problema_h_01.md`, preservando os cálculos numéricos coerentes obtidos pela
rota de Rosen--Morse.

A conclusão é:

$$
\boxed{
\text{Rosen--Morse permanece útil como modelo auxiliar, mas não como
derivação ontológica da hierarquia leptônica na GDQ.}
}
$$

## 2. O erro

A redução radial usada na Q39 produz uma equação formalmente parecida com uma
equação de Schrödinger unidimensional com potencial trigonométrico de
Rosen--Morse.

Essa semelhança matemática foi tratada de forma forte demais: o índice radial
\(n\) do problema auxiliar foi promovido a índice físico de geração.

Com isso, a identificação:

$$
e\leftrightarrow n=0,
\qquad
\mu\leftrightarrow n=1,
\qquad
\tau\leftrightarrow n=17
$$

passou a funcionar numericamente, mas não foi derivada como consequência da
ação oficial da GDQ.

O problema não é o operador auxiliar. O problema é a interpretação:

$$
\text{nível radial auxiliar}
\neq
\text{geração leptônica física da GDQ}.
$$

## 3. Por que os números batiam

O espectro de Rosen--Morse usado tinha autovalores:

$$
\lambda_n
=
(s+n)^2-\frac{b^2}{(s+n)^2}.
$$

Como, para \(n\ge1\), a raiz do autovalor cresce quase linearmente,

$$
\sqrt{\lambda_n}\sim n,
$$

o quociente:

$$
\frac{M_\tau}{M_\mu}
\simeq
16.8
$$

é naturalmente reproduzido se se escolhe \(n_\tau=17\).

Isso gera valores coerentes:

$$
\frac{M_\mu}{M_e}
\simeq
206.7679,
\qquad
\frac{M_\tau}{M_e}
\simeq
3477.1465.
$$

Mas essa coerência é compatibilidade numérica do modelo auxiliar, não prova
de que a GDQ seleciona o décimo sétimo modo radial como tau.

## 4. Classificação correta

A rota Rosen--Morse deve ser reclassificada como:

1. **modelo espectral auxiliar**;
2. **teste de consistência numérica**;
3. **comparação fenomenológica coerente**;
4. **não derivação final da hierarquia leptônica**.

Ela não deve ser chamada de previsão cega enquanto o mapeamento
\(n_\tau=17\) não for obtido da ação oficial, da topologia física ou da
Hessiana física projetada.

## 5. O que permanece aproveitável

Permanecem úteis:

1. o potencial cotangente como limite global em \(S^3\);
2. o contraste entre potencial local \(1/r\) e potencial global
   \(\cot(r/R)\);
3. o estudo de contornos Reg--Reg, Robin--Reg e Robin--Robin;
4. os testes de estabilidade numérica;
5. a constatação de que o estômato finito gera perturbações locais de borda;
6. os valores numéricos como benchmark auxiliar para qualquer nova rota GDQ.

## 6. O que deve ser removido do status forte

Devem ser rebaixadas as afirmações:

1. “Q39 resolvida como espectro global de Rosen--Morse”;
2. “o tau é \(n=17\) por derivação GDQ”;
3. “modos \(2,\ldots,16\) são excluídos por censura já provada”;
4. “Rosen--Morse fornece o espectro completo das três gerações físicas”.

Essas frases podem permanecer apenas como histórico ou como rota auxiliar,
com status explícito de hipótese/diagnóstico.

## 7. Rota GDQ correta a retomar

A rota que deve substituir a identificação \(n=17\) é a rota intrínseca da
GDQ:

$$
\text{ação oficial}
\to
\text{background leptônico admissível}
\to
\text{Hessiana física}
\to
\text{modos de tensão/topologia}
\to
\text{três gerações}
\to
\text{massas}.
$$

Nessa rota, as três gerações devem ser três setores físicos:

$$
e,\quad\mu,\quad\tau,
$$

não três níveis escolhidos de um operador auxiliar com lacunas descartadas.

O tau deve ser tratado como a terceira excitação/topologia/saturação física
da GDQ, não como o décimo sétimo harmônico radial de uma equação reduzida.

## 8. Status vigente após H-01

O status conservador da Q39 passa a ser:

$$
\boxed{
\text{Q39 parcialmente resolvida: massas leptônicas têm benchmarks
numéricos coerentes, mas a derivação GDQ intrínseca da hierarquia permanece
aberta.}
}
$$

A rota Rosen--Morse não deve ser descartada. Ela deve ser preservada como
benchmark porque fornece valores coerentes e pode indicar a forma assintótica
de um operador GDQ mais profundo. Mas ela não pode mais ser o fundamento final
da hierarquia.
