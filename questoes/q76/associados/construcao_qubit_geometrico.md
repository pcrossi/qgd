# Construção inicial — qubit geométrico GDQ

## 1. Objetivo

Construir a primeira versão matemática do qubit geométrico sem introduzir uma
ação nova. O objetivo não é modelar ainda um hardware específico, mas fixar a
estrutura geral que qualquer implementação física deverá satisfazer.

O enunciado técnico é:

$$
\boxed{
\text{um qubit GDQ é um cluster espectral bidimensional isolado da Hessiana física.}
}
$$

## 2. Dados de partida

Partimos da ação oficial da GDQ e de um background estacionário admissível:

$$
\Phi_\ast
=
(g_\ast,J_\ast,H_\ast,f_\ast).
$$

A segunda variação física, após remoção de gauge e imposição dos vínculos de
contorno, define:

$$
K_{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_\ast}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

O produto físico vem da medida ponderada:

$$
\langle u,v\rangle_{\mathcal U}
=
\int_M
\overline u\,v\,\mathcal U_\ast\,dV_{g_\ast}.
$$

Em discretização ou base finita, isso vira um problema generalizado:

$$
Kc
=
\lambda Gc,
$$

onde $G$ é a matriz de Gram positiva.

## 3. Cluster lógico

Escolhemos dois autovalores físicos $\lambda_0,\lambda_1$ e exigimos:

$$
\Delta_{\rm gap}
=
\operatorname{dist}
\left(
\{\lambda_0,\lambda_1\},
\operatorname{spec}(K_{\rm phys})\setminus\{\lambda_0,\lambda_1\}
\right)
>
0.
$$

O projetor lógico é o projetor de Riesz:

$$
P_Q
=
\frac{1}{2\pi i}
\oint_\Gamma
(z-K_{\rm phys})^{-1}\,dz.
$$

No problema generalizado, é conveniente reduzir primeiro para uma forma
Hermitiana ordinária. Se $G=S^\dagger S$, então:

$$
\widetilde K
=
S^{-{\dagger}}KS^{-1}.
$$

O projetor é calculado em $\widetilde K$ e transportado de volta pelo mapa de
Gram.

## 4. Critério de estabilidade

Se uma perturbação de aparelho/ruído muda a Hessiana por $\delta K$, o cluster
permanece isolado quando:

$$
\|\delta K\|_G
<
\frac{\Delta_{\rm gap}}{2}.
$$

Nesse regime, a norma da variação do projetor é limitada, em primeira ordem,
por:

$$
\|\delta P_Q\|
\lesssim
\frac{2\|\delta K\|_G}{\Delta_{\rm gap}}.
$$

Interpretação física:

$$
\boxed{
\text{ruído subcrítico não destrói o qubit; ele apenas deforma o subespaço lógico.}
}
$$

Esse é o núcleo técnico da proteção geométrica. A proteção absoluta exigiria
$\delta P_Q=0$ para qualquer ruído, o que não é verdadeiro em geral.

## 5. Porta lógica por transporte

Uma porta corresponde a uma família de contornos/aparelhos parametrizada por
$\eta$:

$$
K_{\rm phys}(\eta).
$$

Se o cluster permanece isolado para todo $\eta\in[\eta_0,\eta_1]$, o transporte
adiabático no subespaço lógico é:

$$
U_Q(\eta_1,\eta_0)
=
\operatorname{Pexp}
\left(
-
\int_{\eta_0}^{\eta_1}
\mathcal A_Q(\eta)\,d\eta
\right),
$$

com conexão:

$$
(\mathcal A_Q)_{ij}
=
\langle\psi_i(\eta),\partial_\eta\psi_j(\eta)\rangle_{\mathcal U}.
$$

O erro de porta deve ser separado em:

$$
1-\mathcal F
=
\epsilon_{\rm leak}
+
\epsilon_{\rm nonad}
+
\epsilon_{\rm therm}
+
\epsilon_{\rm app}.
$$

## 6. O que já está construído

Esta nota constrói:

1. definição de qubit como cluster espectral;
2. projetor lógico por Riesz;
3. critério de estabilidade por gap;
4. forma geral de porta por transporte de contorno;
5. distinção entre proteção subcrítica e erro zero.

## 7. O que ainda falta

Para transformar isso em previsão física, falta escolher um protótipo:

1. spin/circulação tipo Stern--Gerlach;
2. qubit de fluxo;
3. qubit de carga;
4. íon aprisionado;
5. cavidade/fóton;
6. modo topológico abstrato.

Depois disso será necessário calcular $\Phi_\ast$, $K_{\rm phys}$,
$\Delta_{\rm gap}$, $\delta K_{\rm noise}$, $U_Q$ e a fidelidade contra dados
de um aparelho real.

