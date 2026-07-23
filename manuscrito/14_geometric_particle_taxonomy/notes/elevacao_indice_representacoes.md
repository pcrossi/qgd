---
title: "Elevação do índice às representações"
---

# Elevação do índice às representações

Esta nota separa três objetos que não devem ser confundidos:

1. $L_G$, a linha geométrica que carrega a unidade local de índice;
2. $E_C$ e $E_W$, os fibrados internos de cor e isospin fraco;
3. $L_Y$, a linha física de hipercarga.

A separação é necessária porque a unidade de índice do estômato não é uma
hipercarga. Ela conta multiplicidade quiral. A hipercarga é uma restrição
global de descida do fibrado efetivo.

## 1. Índice geométrico local

O estômato primitivo fornece:

$$
{\rm ind}D_G^+=1.
$$

Se $V_R$ é uma representação interna topologicamente trivial no patch local,
o operador torcido satisfaz:

$$
{\rm Ind}_G(D_G^+\otimes V_R)
=
{\rm ind}(D_G^+)\,[R].
$$

Portanto:

$$
{\rm Ind}_G(D_G^+\otimes V_R)
=
[R].
$$

Uma unidade local de índice cria uma cópia quiral de cada representação
admissível. Ela não multiplica hipercargas.

## 2. Conteúdo de uma geração

Com as representações internas admissíveis:

$$
E_{\rm gen}
=
(3,2)_{1/6}
\oplus
(\bar3,1)_{-2/3}
\oplus
(\bar3,1)_{1/3}
\oplus
(1,2)_{-1/2}
\oplus
(1,1)_1.
$$

A contagem de componentes de Weyl é:

$$
6+3+3+2+1=15.
$$

Logo, um estômato primitivo coorientado fornece uma geração quiral:

$$
{\rm Ind}_{\rm estômato}=1
\quad\Rightarrow\quad
15\ \text{componentes de Weyl}.
$$

Com três estômatos:

$$
3\times 15=45.
$$

## 3. Por que não usar a mesma linha como hipercarga

Se $L_G$ fosse identificado com $L_Y$, campos com hipercargas diferentes
receberiam potências diferentes da linha de índice. Isso mudaria a
multiplicidade quiral de cada multiplete e destruiria a interpretação de
uma geração comum.

Na GDQ, a estrutura correta é:

$$
E_{\rm int}=E_C\oplus E_W\oplus L_Y,
$$

com $L_G$ apenas como marcador topológico da unidade APS local. A hipercarga
entra por descida global:

$$
\frac{
SU(3)_C\times SU(2)_L\times U(1)_Y
}{
\mathbb Z_6
}.
$$

## 4. Verificação computacional

O script:

$$
{\tt scripts/elevacao_indice_representacoes.py}
$$

calcula a contagem de componentes por multiplete e verifica que uma unidade
de índice gera $15$ componentes de Weyl, enquanto três unidades geram $45$.
