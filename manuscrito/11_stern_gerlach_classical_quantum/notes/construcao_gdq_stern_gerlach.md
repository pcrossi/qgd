---
title: "Construção GDQ do Stern-Gerlach"
---

# Construção GDQ do Stern-Gerlach

## 1. Enunciado

Stern--Gerlach é um problema de contorno magnético clássico aplicado a um
sóliton que já possui circulação/spin.

A cadeia é:

$$
J_{\rm SG}^{\rm clássico}
\to
\Phi_\ast^{\rm SG}
\to
K_{\rm GDQ}
\to
P_{\rm phys}^{\dagger}K_{\rm GDQ}P_{\rm phys}
\to
\mathsf R_{\rm SG}
\to
P_{\mathbf n}^{\pm}
\to
\Delta z_\pm
\to
\text{registro}.
$$

## 2. Fonte magnética

O campo do aparelho define:

$$
\mathbf n(\mathbf x)
=
\frac{\mathbf B(\mathbf x)}{|\mathbf B(\mathbf x)|}.
$$

Ele entra como fonte ou contorno. Não altera a ação oficial.

No nível variacional, a informação física fornecida pelo aparelho é externa:
perfil de campo, região de interação, material e tempo de trânsito. Denotamos
esses dados por $J_{\rm SG}^{\rm clássico}$. A resposta geométrica não é
inserida à mão; ela é obtida pela solução linearizada:

$$
K_{\rm phys}^{\rm obj}\,\delta\Phi_{\rm SG}
=
J_{\rm SG}^{\rm clássico},
$$

onde $K_{\rm phys}^{\rm obj}$ é a Hessiana física do objeto antes da leitura
do aparelho. O campo clássico seleciona a direção $\mathbf n$; a teoria calcula
como o defeito responde a essa seleção.

## 3. Background e Hessiana

O background estacionário com aparelho satisfaz:

$$
\left.
\frac{\delta}
{\delta\Phi}
\left(
\mathcal S_{\rm GDQ}
+
\mathcal S_{\rm SG}
\right)
\right|_{\Phi_\ast^{\rm SG}}
=
0.
$$

A rigidez física é:

$$
K_{\rm phys}^{\rm SG}
=
P_{\rm phys}^{\dagger}
K_{\rm GDQ}[\Phi_\ast^{\rm SG}]
P_{\rm phys}.
$$

Eliminando graus internos:

$$
\mathsf R_{\rm SG}
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

Aqui $Y$ representa os graus de interface observados pelo aparelho e $I$
representa os graus internos não monitorados do objeto. O complemento de Schur
é a forma precisa de dizer que o aparelho não mede diretamente todo o bulk:
ele vê uma impedância efetiva na fronteira. Assim, $\mathsf R_{\rm SG}$ é
resposta de interface, não parâmetro fundamental novo.

## 4. Projetores

O eixo do aparelho define os projetores:

$$
P_{\mathbf n}^{\pm}
=
\frac12
\left(
I\pm\mathbf n\cdot\sigma
\right).
$$

Eles não dizem que o aparelho criou o spin. Dizem que o aparelho escolheu a
decomposição observável.

## 5. Força e deflexão

No canal fixo:

$$
F_z^\pm
=
\pm\mu\frac{\partial B_z}{\partial z}.
$$

Para região de comprimento $L$ e velocidade longitudinal $v_y$:

$$
\Delta z_\pm
=
\pm
\frac{\mu L^2}{2mv_y^2}
\frac{\partial B_z}{\partial z}.
$$

## 6. Pesos

Para preparação $\mathbf a$:

$$
p_\pm(\mathbf n|\mathbf a)
=
\frac{1\pm\mathbf a\cdot\mathbf n}{2}.
$$

Essa parte usa Born operacional no Hilbert reconstruído. A construção GDQ
fornece o eixo, a resposta de interface e os canais.

## 7. Estatuto metrológico

As fórmulas deste capítulo separam três níveis:

1. estrutura universal dos canais, dada por Hopf/Clifford;
2. movimento de centro de massa em um canal fixo, dado pelo campo clássico do
   aparelho;
3. metrologia fina de um instrumento real, dada por $\mathsf R_{\rm SG}$,
   perdas, mobilidade causal e geometria efetiva do detector.

O capítulo fecha os dois primeiros níveis e define o terceiro como aplicação
metrológica. Isso não reabre a estrutura conceitual do Stern--Gerlach; apenas
indica quais dados experimentais são necessários para reproduzir um aparato
real específico.
