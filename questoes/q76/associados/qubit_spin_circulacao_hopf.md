# Protótipo Q76 — qubit de spin/circulação Hopf

## 1. Motivo da escolha

O protótipo mais econômico para iniciar a Q76 é o qubit de spin/circulação,
porque ele reaproveita construções já estabelecidas:

1. o objeto possui circulação/spin antes da medição;
2. o aparelho seleciona um eixo;
3. o eixo define dois projetores de Hopf/Pauli;
4. os pesos são Born operacional no Hilbert reconstruído;
5. o aparelho entra como fonte/contorno, não como alteração da ação oficial.

Assim, o qubit lógico é:

$$
\mathcal H_Q
=
\operatorname{span}\{\psi_+,\psi_-\},
$$

onde $\psi_\pm$ são os dois modos de circulação relativos a um eixo de
referência.

## 2. Projetores de eixo

Para cada eixo unitário $\mathbf n\in S^2$, define-se:

$$
P_{\mathbf n}^{\pm}
=
\frac12
\left(
I
\pm
\mathbf n\cdot\boldsymbol\sigma
\right).
$$

Esses projetores satisfazem:

$$
(P_{\mathbf n}^{\pm})^2
=
P_{\mathbf n}^{\pm},
\qquad
P_{\mathbf n}^{+}P_{\mathbf n}^{-}
=
0,
\qquad
P_{\mathbf n}^{+}+P_{\mathbf n}^{-}
=
I.
$$

Na leitura GDQ, $\mathbf n$ pertence ao aparelho. O spin/circulação pertence ao
objeto. Portanto não há valor absoluto simultâneo para todos os eixos; há
resposta relativa ao contorno selecionado.

## 3. Background reduzido

O background de qubit é um cluster bidimensional isolado:

$$
K_{\rm phys}
=
\begin{pmatrix}
K_Q & J\\
J^\dagger & K_\perp
\end{pmatrix},
$$

com:

$$
K_Q
\simeq
0_{2\times2},
\qquad
K_\perp
\ge
\Delta_{\rm gap}I.
$$

O bloco $J$ representa acoplamento residual com modos não lógicos. O regime de
qubit estável exige:

$$
\|J\|
\ll
\Delta_{\rm gap}.
$$

O complemento de Schur fornece o bloco lógico efetivo:

$$
K_Q^{\rm eff}
=
K_Q
-
J K_\perp^{-1}J^\dagger.
$$

Esse termo é a forma GDQ reduzida do vazamento virtual: ele corrige a dinâmica
lógica sem destruir o qubit enquanto o gap permanece aberto.

## 4. Portas por contorno

Uma porta de um qubit é obtida variando controladamente o eixo/fonte clássica
do aparelho. No setor lógico, isso reduz a:

$$
U(\theta,\mathbf n)
=
\exp
\left(
-\frac{i\theta}{2}
\mathbf n\cdot\boldsymbol\sigma
\right).
$$

Na GDQ essa fórmula não é ontologia primária. Ela é a holonomia efetiva do
subespaço lógico transportado pelo contorno:

$$
U
=
\operatorname{Pexp}
\left(
-
\int
\mathcal A_Q
\right).
$$

## 5. Readout

Se o estado preparado possui vetor de Bloch $\mathbf a$, sua matriz reduzida é:

$$
\varrho_{\mathbf a}
=
\frac12
\left(
I+\mathbf a\cdot\boldsymbol\sigma
\right).
$$

O aparelho mede no eixo $\mathbf n$. Os pesos dos dois canais são:

$$
p_\pm
=
\operatorname{Tr}
\left(
\varrho_{\mathbf a}P_{\mathbf n}^{\pm}
\right)
=
\frac12
\left(
1\pm\mathbf a\cdot\mathbf n
\right).
$$

Fisicamente, a GDQ interpreta esses pesos como frações operacionais de medida
no Hilbert reconstruído. O evento individual continua sendo seleção de bacia
aparelho--ambiente.

## 6. Taxa de erro reduzida

Um erro lógico pode vir de:

1. vazamento para $P_\perp$;
2. ruído de eixo $\delta\mathbf n$;
3. não adiabaticidade da porta;
4. relaxação térmica do aparelho.

O primeiro estimador reduzido é:

$$
\epsilon_{\rm leak}
\sim
\frac{\|J\|^2}{\Delta_{\rm gap}^2}.
$$

Esse é o ponto prático da GDQ: a correção de erros vira cálculo de $\|J\|$ e
$\Delta_{\rm gap}$, isto é, cálculo da Hessiana e do contorno.

## 7. Status

Este protótipo fecha a primeira construção operacional da Q76:

$$
\boxed{
\text{spin/circulação Hopf fornece um qubit GDQ reduzido consistente.}
}
$$

Mas ainda não fecha hardware real. Para isso falta obter $\Phi_\ast$,
$K_{\rm phys}$, $J$, $K_\perp$, ruído térmico e impedância de leitura de um
dispositivo concreto.

