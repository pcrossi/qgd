# Q30 — Operador radial e rigidez DtN do colar torsional

## 1. Objetivo

Derivar a resposta de interface do modo radial permitido a partir do bulk do
colar, sem acrescentar uma mola Robin fenomenológica.

Usa-se a redução radial oficial já obtida para
$X=(a,c,f)$, com lapse variado antes da gauge $N=1$.

## 2. Restrição linearizada do lapse

No ramo cilíndrico isotrópico,

$$
a=c=R,
\qquad
f=f_0,
\qquad
h^2=4R^4,
$$

e

$$
f_0-n-\lambda=-\frac{4\tau}{R^2}.
$$

A restrição radial é

$$
-\tau T_r+\tau V_r+a^2c(f-n-\lambda)=0.
$$

Como $T_r$ é quadrático nas derivadas, sua primeira variação desaparece no
cilindro. A diferenciação da parte algébrica fornece

$$
\partial_a\mathcal E_N=0,
\qquad
\partial_c\mathcal E_N=0,
\qquad
\partial_f\mathcal E_N=R^3.
$$

Portanto,

$$
\boxed{\delta f=0}
$$

para o perfil radial local que satisfaz a restrição linearizada. O ajuste do
modo constante global de $f$ continua sendo fixado separadamente pela
normalização de Perelman.

## 3. Símbolo principal projetado

A matriz principal da segunda variação é

$$
P=\tau e^{-f_0}
\begin{pmatrix}
4R&4R&-4R^2\\
4R&0&-2R^2\\
-4R^2&-2R^2&2R^3
\end{pmatrix}.
$$

O modo radial isotrópico permitido é

$$
v_R=(1,1,0)^T.
$$

Sua rigidez de gradiente é

$$
\boxed{
p_R=v_R^TPv_R=12\tau e^{-f_0}R>0.
}
$$

Assim, a indefinição da matriz não projetada não sobrevive nessa direção
física após a restrição do lapse.

## 4. Operador de Jacobi radial

Para coeficientes constantes no cilindro e usando a rigidez potencial já
calculada,

$$
K_R=\frac{6(3R^2-8\tau)}{R^4}>0,
$$

o operador reduzido é

$$
\boxed{
\mathcal J_R=-p_R\frac{d^2}{dr^2}+K_R.
}
$$

Sua forma quadrática é

$$
Q_R[\rho]
=\frac12\int_0^L
\left[p_R(\rho')^2+K_R\rho^2\right]dr,
$$

portanto

$$
Q_R[\rho]>0
$$

para toda flutuação radial não nula no domínio admissível.

## 5. Operador Dirichlet--to--Neumann

Defina

$$
m_R=\sqrt{\frac{K_R}{p_R}}.
$$

### 5.1 Colar semi-infinito

Com $\rho(0)=\rho_0$ e $\rho(r)\to0$ quando $r\to\infty$,

$$
\rho(r)=\rho_0e^{-m_Rr}.
$$

A ação on-shell é

$$
Q_R^{\rm on\mbox{-}shell}
=\frac12\sqrt{p_RK_R}\,\rho_0^2.
$$

Logo,

$$
\boxed{\Lambda_R^{\rm DtN}=\sqrt{p_RK_R}>0.}
$$

### 5.2 Colar finito com Dirichlet exterior

Para $\rho(L)=0$,

$$
\boxed{
\Lambda_{R,D}^{\rm DtN}
=\sqrt{p_RK_R}\coth(m_RL)>0.
}
$$

### 5.3 Colar finito com Neumann exterior

Para $\rho'(L)=0$,

$$
\boxed{
\Lambda_{R,N}^{\rm DtN}
=\sqrt{p_RK_R}\tanh(m_RL)>0.
}
$$

Essas são condições Robin induzidas pela minimização do bulk. Nenhum
coeficiente foi escolhido para estabilizar o estômato.

## 6. Acoplamento à interface

Se $I_{\rm int}^{(2)}$ é a Hessiana genuína da interface no mesmo modo, a
condição de colagem é

$$
\left(
\Lambda_R^{\rm DtN}+H_R^{\rm int}
\right)\rho_0=J_R.
$$

Para a interface puramente natural atualmente documentada,
$H_R^{\rm int}=0$, e a impedância positiva vem inteiramente do colar.
Qualquer contribuição adicional deve ser derivada do pullback da interface.

## 7. Resultado

$$
\boxed{
p_R>0,
\quad K_R>0
\Longrightarrow
\mathcal J_R>0
\text{ e }\Lambda_R^{\rm DtN}>0.
}
$$

Isso fecha os perfis radiais do modo torsional homogêneo no colar produto,
condicionalmente à restrição física $S=0$ e ao ramo com
$R^2>8\tau/3$.

## 8. Limites

1. um colar não produto exige usar $p_R(r)$ e $K_R(r)$ e resolver o problema
   de Sturm--Liouville correspondente;
2. a interface métrico--dilatônica completa ainda pode acrescentar uma
   Hessiana própria;
3. o resultado é estático e não determina mobilidade causal;
4. o modo Berger excluído não é estabilizado por esta DtN radial.

## 9. Classificação

- projeção do símbolo principal: derivação direta;
- positividade de $\mathcal J_R$: teorema setorial;
- fórmulas DtN: solução analítica do colar produto;
- extensão não produto e mobilidade: trabalho posterior.

