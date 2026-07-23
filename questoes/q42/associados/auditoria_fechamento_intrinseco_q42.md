# Q42 — Auditoria do material existente para o fechamento intrínseco

## Objetivo

Verificar se as duas pendências intrínsecas da Q42 já estavam resolvidas em
outro ponto do manuscrito:

1. estabilidade completa do background cilíndrico;
2. pullback axial em dois patches e normalização \(Z_{\rm bulk}\).

## 1. Material encontrado sobre Hopf

O Capítulo 34, `pt-br/34 - Monopolos e a Fibração de Hopf.md`, contém:

\[
 S^3=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^2=1\},
\]

\[
 \xi=z_1/z_2,
 \qquad S^1\hookrightarrow S^3\to S^2,
\]

e a interpretação da monodromia \(4\pi\). Isso fornece a topologia e as
coordenadas locais necessárias.

O que o capítulo não contém é a imersão no espaço dos campos fundamentais:

\[
 \iota:P\longmapsto(g(P),f(P),\bar f(P)).
\]

Também não calcula

\[
 T_A=\partial_A\iota(P)
\]

nem sua norma pela Hessiana oficial. Portanto, o capítulo não determina
\(Z_{\rm bulk}\).

## 2. Material encontrado sobre a Hessiana

O adendo `questoes/q32/associados/reducao_hessiana_gauge_fixada.md` fornece:

- o bloco escalar reduzido;
- o símbolo de Lichnerowicz--drift no setor métrico;
- o gauge Hermitiano--DeTurck;
- a forma matricial abstrata dos blocos mistos.

Entretanto, o próprio documento declara que os coeficientes completos dos
blocos mistos em fundo geral permanecem posteriores. A forma disponível é

\[
 L_{\rm GDQ}^{(2)}=
 \begin{pmatrix}
 L_\varphi&L_{\varphi h}\\
 L_{h\varphi}&L_{h,\rm phys}
 \end{pmatrix},
\]

mas \(L_{\varphi h}\) e \(L_{h\varphi}\) não estão reduzidos explicitamente
no cilindro. Sem esses blocos não é possível contar rigorosamente todos os
modos negativos radiais e tensoriais.

## 3. Resultados de estabilidade anteriores

As Questões 18 e 19 analisam o operador Ornstein--Uhlenbeck e a estabilidade
do solíton gaussiano, módulo simetrias. Elas não contêm a decomposição
espectral do shrinker

\[
 \mathbb R_+\times S^3_{2\sqrt\tau}.
\]

Logo não completam a estabilidade tensorial do background usado na Q42.

## 4. Material sobre torção de \(S^3\)

`auditorias/RELATORIO_TORCAO_SPIN_S3_R4T4.md` demonstra que a forma de volume homogênea
de \(S^3\) é fechada e coclosed e pode representar a torção paralelizante.
Esse resultado fortalece a admissibilidade geométrica do ramo cilíndrico.

O mesmo relatório registra explicitamente que o mapa completo de redução
dimensional entre a torção em \(S^3\) e o setor físico efetivo não foi
construído. Portanto ele também não fornece o pullback axial procurado.

## 5. Conclusão da busca

Não existe, nos documentos atuais, uma derivação escondida que complete os
dois pontos. O material encontrado permite afirmar:

\[
 \boxed{V_H=2/\tau},
 \qquad
 \boxed{z_H=3\sqrt\pi/4},
\]

e prova a estabilidade do modo homogêneo do raio. Mas não permite afirmar:

\[
 \boxed{Z_{\rm bulk}=\text{número determinado}},
\]

nem

\[
 \boxed{\operatorname{spec}
 L_{\rm GDQ,cyl}^{(2)}\setminus\{\text{gauge}}\subset[0,\infty)}.
\]

## 6. Próxima derivação que realmente acrescenta informação

Para evitar novo ciclo, o próximo trabalho deve produzir dois objetos novos,
e não outro background:

1. **atlas axial:** campos \(\Phi_N(P),\Phi_S(P)\) e transformação de colagem
   no equador, a partir dos dados \((z_1,z_2)\) já existentes;
2. **operador cilíndrico completo:** redução explícita dos blocos
   \(L_h,L_\varphi,L_{h\varphi},L_{\varphi h}\), imposição da restrição de
   medida e projeção Hermitiano--DeTurck.

Sem esses dois produtos, qualquer valor numérico de \(Z_{\rm bulk}\) ou
declaração de estabilidade completa repetirá uma hipótese já identificada.

