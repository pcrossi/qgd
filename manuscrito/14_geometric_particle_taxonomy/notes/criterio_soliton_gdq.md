---
title: "Critério GDQ de sóliton material"
---

# Critério GDQ de sóliton material

Esta nota fixa o que significa chamar uma configuração de “partícula” na GDQ.
Ela impede que um perfil escolhido externamente seja promovido a solução
física sem passar pelo problema variacional.

## 1. Definição

Um sóliton GDQ é uma configuração

$$
\mathfrak S=(g,H,f,\bar f)
$$

em um setor de topologia, calibre e bordo fixado, tal que:

1. satisfaz as equações estacionárias da ação oficial ou do fluxo geométrico
   associado;
2. possui densidade normalizável;
3. possui energia geométrica finita;
4. tem comportamento assintótico controlado;
5. possui invariantes topológicos legíveis como carga e spin quando o setor
   for carregado/spinorial;
6. possui Hessiana física estável após remoção de gauge e modos zero
   admissíveis;
7. tem resposta de interação definida por contornos, DtN/Schur ou acoplamentos
   de interface.

No setor torsional compatível com a conexão de Bismut, a equação estacionária
esquemática é

$$
R_{ij}
-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=
\lambda g_{ij},
$$

com

$$
dH=0,
\qquad
d_\phi^\dagger H=0,
$$

onde

$$
f=\phi+i\chi,
\qquad
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
$$

A fase $\chi=S_R/\hbar$ carrega circulação e holonomia.

## 2. Energia finita

Uma condição suficiente de energia finita é

$$
\int_M\rho\,dV_g=1,
$$

e

$$
\int_M
\left(
|R|
+|\nabla f|^2
+|H|^2
\right)
\rho\,dV_g
<\infty.
$$

A energia efetiva de repouso de um setor material é o excesso em relação ao
vácuo do mesmo problema:

$$
m[\mathfrak S]c^2
=
E[\mathfrak S]-E[\mathfrak S_{\rm vac}].
$$

Portanto, a massa não é um parâmetro primitivo inserido depois. Ela é uma
leitura energética da geometria estacionária.

## 3. Carga

A carga deve vir de circulação, resíduo ou holonomia, não de etiqueta externa.
Para um ciclo admissível $C$,

$$
N_C
=
\frac1{2\pi}\oint_Cd\chi
\in\mathbb Z.
$$

Uma carga efetiva aparece depois da projeção no setor interno:

$$
Q
=
e\sum_aq_aN_a.
$$

Os pesos $q_a$ pertencem ao fibrado interno efetivo e aos quocientes globais do
setor. Eles não são massa.

## 4. Spin

O spin é lido por holonomia spinorial e circulação torsional. No setor
reduzido,

$$
\mathbf J
=
\int_\Sigma
\rho\,\mathbf x\times\nabla S_R\,d\mu_h
+\mathbf J_{\rm torsion}.
$$

Para setores fermiônicos, a condição spinorial mínima é

$$
\Psi\mapsto-\Psi
\quad
\text{sob rotação }2\pi,
$$

e

$$
\Psi\mapsto\Psi
\quad
\text{sob rotação }4\pi.
$$

Assim, uma circulação escalar pode ajudar a visualizar o spin, mas a prova
física do spin $1/2$ usa estrutura spinorial, holonomia e torção.

## 5. Solução explícita mínima

No setor neutro, sem torção, existe o solíton gaussiano:

$$
M=\mathbb R^d,
\qquad
g_{ij}=\delta_{ij},
\qquad
H=0,
$$

com

$$
\phi(x)=\frac{|x|^2}{4\sigma},
\qquad
\sigma>0.
$$

Então

$$
R_{ij}=0,
\qquad
\nabla_i\nabla_j\phi
=
\frac1{2\sigma}\delta_{ij}.
$$

Logo

$$
R_{ij}+\nabla_i\nabla_j\phi
=
\frac1{2\sigma}g_{ij}.
$$

A densidade normalizada é

$$
\rho_N(x)
=
\frac{1}{(4\pi\sigma)^{d/2}}
\exp\left(-\frac{|x|^2}{4\sigma}\right).
$$

Ela é normalizável e possui todos os momentos polinomiais finitos.

Para o funcional de Perelman reduzido,

$$
\mathcal W_{\rm gauss}
=
\int_M
\left[
\sigma|\nabla\phi|^2+\phi-d
\right]
\rho_N\,dV.
$$

Como

$$
|\nabla\phi|^2=\frac{|x|^2}{4\sigma^2},
$$

temos

$$
\sigma|\nabla\phi|^2
=
\frac{|x|^2}{4\sigma}.
$$

Na gaussiana acima, cada coordenada tem variância $2\sigma$, portanto

$$
\left\langle |x|^2\right\rangle=2d\sigma.
$$

Assim,

$$
\left\langle
\frac{|x|^2}{4\sigma}
\right\rangle
=
\frac d2,
\qquad
\langle\phi\rangle=\frac d2.
$$

Logo

$$
\mathcal W_{\rm gauss}
=
\frac d2+\frac d2-d
=
0.
$$

Esse resultado prova existência explícita de uma solução normalizável neutra.
Ele não prova, por si só, elétron, próton ou nêutron.

## 6. Estabilidade linear da referência gaussiana

No setor escalar reduzido, a Hessiana ponderada é modelada pelo operador de
Ornstein--Uhlenbeck

$$
\mathcal L_{\rm OU}
=
-\Delta
+\frac{x}{2\sigma}\cdot\nabla.
$$

Em $L^2(\rho_NdV)$, seu espectro é discreto:

$$
\lambda_k=\frac{k}{2\sigma},
\qquad
k=0,1,2,\ldots
$$

O modo $k=0$ é modo zero de normalização/simetria. Modos de translação,
escala e difeomorfismo devem ser classificados e removidos ou tratados como
moduli. Após projetar esses modos, a estabilidade exige gap positivo no setor
físico.

## 7. Ficha obrigatória para uma partícula física

Para declarar uma partícula, o manuscrito deve fornecer uma ficha:

| Item | Exigência |
|---|---|
| Background | $\mathfrak S_P=(g_P,H_P,f_P,\bar f_P)$ estacionário. |
| Resíduo | $\mathcal E_g=\mathcal E_H=\mathcal E_f=0$ no domínio declarado. |
| Energia | Integral ponderada finita. |
| Massa | Excesso energético contra o vácuo do mesmo setor. |
| Carga | Integral de circulação/resíduo/holonomia. |
| Spin | Holonomia spinorial e/ou integral torsional. |
| Hessiana | $K_{\rm phys}=P_{\rm phys}^\dagger K P_{\rm phys}$. |
| Modos zero | Gauge, translação, rotação, escala ou moduli físicos identificados. |
| Assintótica | Decaimento ou matching de bordo. |
| Interação | Resposta por fonte, contorno, DtN/Schur ou espalhamento. |

Essa ficha é o critério operacional da GDQ para distinguir solução material de
perfil fenomenológico.

