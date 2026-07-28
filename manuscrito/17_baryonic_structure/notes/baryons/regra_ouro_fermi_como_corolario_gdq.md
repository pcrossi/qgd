---
title: "Regra de Ouro de Fermi como corolário da dinâmica GDQ"
---

# Regra de Ouro de Fermi como corolário da dinâmica GDQ

## 1. Enunciado

A Regra de Ouro de Fermi não é acrescentada à ação oficial. Ela é o limite de
tempo longo da dinâmica linear de transição no setor físico reconstruído.

A cadeia dedutiva é:

$$
\mathcal S_{\rm GDQ}
\longrightarrow
\Phi_*
\longrightarrow
K_{\rm phys}
\longrightarrow
H_0
\longrightarrow
V_{\rm phys}
\longrightarrow
\Gamma.
$$

Aqui:

- $\Phi_*$ é um background estacionário admissível;
- $K_{\rm phys}$ é a Hessiana após a remoção dos modos de gauge e vínculos;
- $H_0$ é o gerador autoadjunto da dinâmica física reconstruída;
- $V_{\rm phys}$ é a resposta variacional que conecta os canais inicial e
  final;
- $\Gamma$ é a taxa assintótica de transição.

Uma variação euclidiana da ação não é identificada diretamente com energia.
O gerador físico é construído depois do pullback causal, da projeção física e,
quando existem velocidades, da transformação de Legendre.

## 2. Elemento de matriz GDQ

Seja $\mathcal H_{\rm phys}$ o espaço físico reconstruído e suponha que $H_0$
seja autoadjunto em um domínio denso $\mathcal D(H_0)$. Para

$$
H_0|i\rangle=E_i|i\rangle,
\qquad
H_0|f\rangle=E_f|f\rangle,
$$

o operador físico de transição é

$$
V_{\rm phys}
=
P_{\rm phys}V_{\rm eff}P_{\rm phys}.
$$

No canal beta, a quarta variação projetada possui a estrutura

$$
V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}
K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutações}.
$$

O elemento de matriz com dimensão de energia é

$$
\mathcal M_{fi}
=
\langle f|V_{\rm phys}|i\rangle.
$$

## 3. Amplitude em tempo finito

No quadro de interação e na primeira ordem em $V_{\rm phys}$:

$$
c_f^{(1)}(T)
=
-\frac{i}{\hbar}
\int_{-T/2}^{T/2}
e^{i(E_f-E_i)t/\hbar}
\mathcal M_{fi}\,dt.
$$

Definindo $\Delta E=E_f-E_i$:

$$
I_T(\Delta E)
:=
\int_{-T/2}^{T/2}
e^{i\Delta E t/\hbar}\,dt
=
\frac{2\hbar\sin(\Delta E T/2\hbar)}{\Delta E}.
$$

Consequentemente:

$$
\frac{|c_f^{(1)}(T)|^2}{T}
=
\frac{|\mathcal M_{fi}|^2}{\hbar^2}
\frac{|I_T(\Delta E)|^2}{T}.
$$

## 4. Limite distribucional

Considere o kernel positivo

$$
\delta_T(E)
:=
\frac{|I_T(E)|^2}{2\pi\hbar T}.
$$

Parseval fornece

$$
\int_{-\infty}^{\infty}|I_T(E)|^2\,dE
=
2\pi\hbar T,
$$

e, portanto,

$$
\int_{-\infty}^{\infty}\delta_T(E)\,dE=1.
$$

Para uma função teste suave $\varphi$, faça

$$
x=\frac{ET}{2\hbar}.
$$

Então:

$$
\int_{-\infty}^{\infty}
\delta_T(E)\varphi(E)\,dE
=
\frac1\pi
\int_{-\infty}^{\infty}
\left(\frac{\sin x}{x}\right)^2
\varphi\left(\frac{2\hbar x}{T}\right)\,dx.
$$

Como

$$
\frac1\pi
\int_{-\infty}^{\infty}
\left(\frac{\sin x}{x}\right)^2dx
=1,
$$

o teorema da convergência dominada implica

$$
\delta_T(E)
\xrightarrow[T\to\infty]{\mathcal D'}
\delta(E).
$$

Logo:

$$
\lim_{T\to\infty}
\frac{|c_f^{(1)}(T)|^2}{T}
=
\frac{2\pi}{\hbar}
|\mathcal M_{fi}|^2
\delta(E_f-E_i).
$$

O fator $2\pi/\hbar$ decorre da normalização de Fourier entre o tempo físico e
a energia; ele não é um parâmetro fenomenológico.

## 5. Teorema condicional

Se:

1. o background é estacionário durante a observação;
2. $H_0$ é autoadjunto no setor físico;
3. o acoplamento é suficientemente fraco para a aproximação de primeira ordem;
4. o tempo de observação excede o tempo de correlação do canal;
5. os estados finais formam um contínuo com medida espectral regular;
6. não há recorrências relevantes no intervalo observado;
7. o estado inicial é aproximadamente monoenergético;
8. $\mathcal M_{fi}$ é regular na casca de energia;

então

$$
\Gamma_{i\to\mathcal F}
=
\frac{2\pi}{\hbar}
\int_{\mathcal F}
|\mathcal M_{fi}|^2
\delta(E_f-E_i)\,d\mu_f.
$$

Quando

$$
d\mu_f=\rho_f(E_f)\,dE_f
$$

localmente e o elemento de matriz varia lentamente na casca:

$$
\boxed{
\Gamma_{i\to f}
=
\frac{2\pi}{\hbar}
|\mathcal M_{fi}|^2
\rho_f(E_i)
}.
$$

Esta é a Regra de Ouro de Fermi como teorema condicional de redução da GDQ.

## 6. Corolário beta

Para

$$
n\to p+e^-+\bar\nu_e,
$$

a média não polarizada fornece

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2
=:
\mathcal J_3^2.
$$

A integração da delta de quatro-momento sobre o espaço de fase final, no
limite líder de recuo nulo, resulta em

$$
\boxed{
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2
},
$$

onde

$$
p_e=\sqrt{E_e^2-m_e^2},
\qquad
m_e\le E_e\le\Delta M.
$$

Integrando:

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta,
$$

com

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e.
$$

Assim, a distribuição contínua de energia já derivada no capítulo é o
corolário beta da Regra de Ouro aplicada ao elemento de matriz geométrico da
GDQ.

## 7. Alcance e limitações

O teorema determina como um elemento de matriz físico produz uma taxa. Ele não
calcula automaticamente esse elemento de matriz.

No setor beta:

- a forma da Regra de Ouro está derivada;
- a quarta variação, o projetor e a combinação
  $\mathcal J_3^2=2|C_S|^2+6|C_T|^2$ estão derivados estruturalmente;
- a avaliação absoluta de $C_S$ e $C_T$ no background bariônico 8D completo
  permanece condicional.

Para transições fortes, níveis finais discretos isolados, tempos curtos,
limiares espectrais singulares ou canais com memória longa, deve-se conservar
o kernel de tempo finito ou resolver a dinâmica acoplada completa.

Verificação reproduzível:
[[../../scripts/saida_verificar_limite_regra_ouro|Saída — limite de tempo longo da Regra de Ouro]].
