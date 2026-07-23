---
title: "Interferômetro EO-MZI e escolha retardada"
---

# Interferômetro EO-MZI e escolha retardada

Esta nota registra a aplicação material reduzida da escolha retardada a um
interferômetro de Mach--Zehnder eletro-óptico. Ela não substitui a ação
oficial da GDQ; usa o capítulo como redução de laboratório:

$$
\mathcal S_{\rm GDQ}
\to
\text{setor Madelung reduzido}
\to
\text{interferômetro}
\to
\mathsf R_{\rm app}(t)
\to
\Gamma_{\rm det}
\to
\mathcal C_{\rm det}.
$$

## 1. Dados externos do aparelho

Para uma avaliação concreta, congelamos uma chave EO-MZI com:

$$
\lambda=1550\,{\rm nm},
\qquad
V_\pi=2{,}445\,{\rm V},
\qquad
\tau_{\rm sw}=18{,}1\,{\rm ps},
$$

e limite de crosstalk de potência:

$$
{\rm XT}=-30\,{\rm dB}.
$$

Esses números são dados externos do aparelho. Eles não são axiomas da GDQ e
não entram na ação fundamental.

O crosstalk de potência correspondente é:

$$
p_{\rm leak}=10^{-3}.
$$

Se o vazamento é de potência, a coerência residual de amplitude é:

$$
\mathcal C_{\rm app}
=
\sqrt{p_{\rm leak}}
=
3{,}162277660168\times10^{-2}.
$$

## 2. Impedância temporal do aparelho

A escolha retardada é modelada como impedância temporal:

$$
\mathsf R_{\rm app}(t)
=
\mathsf R_{\rm off}
+
s(t-t_c)
\left(
\mathsf R_{\rm on}
-
\mathsf R_{\rm off}
\right).
$$

Usamos a chave suave:

$$
s(t-t_c)
=
\frac{1}{1+\exp[-(t-t_c)/\tau_{\rm sw}]}.
$$

No estado recombinado ideal:

$$
\mathsf R_{\rm off}=0.
$$

No estado distinguível, o custo assintótico é:

$$
\Gamma_{\rm on}
=
-\ln\mathcal C_{\rm app}
=
-\ln\sqrt{p_{\rm leak}}
=
3{,}453877639491.
$$

Como:

$$
\Gamma_{\rm det}
=
\frac12
\langle
\Delta\Phi_\partial,
\mathsf R_{\rm app}\Delta\Phi_\partial
\rangle,
$$

e adotamos a normalização reduzida:

$$
\|\Delta\Phi_\partial\|^2=2,
$$

segue:

$$
\mathsf R_{\rm on}
=
\Gamma_{\rm on}
=
3{,}453877639491.
$$

## 3. Kernel causal

O histórico do aparelho é pesado por um kernel causal normalizado:

$$
w(t_f,t)
=
\frac{1}{\tau_{\rm mem}}
\exp\left[
-\frac{t_f-t-t_{\rm prop}}{\tau_{\rm mem}}
\right]
\Theta(t_f-t-t_{\rm prop}).
$$

Após normalização:

$$
\int w(t_f,t)\,dt=1.
$$

Para o teste reduzido:

$$
\tau_{\rm mem}=\tau_{\rm sw}=18{,}1\,{\rm ps}.
$$

Para um caminho de $1\,{\rm m}$ no ar:

$$
t_{\rm prop}=\frac{L}{c}=3{,}33564095198\,{\rm ns}.
$$

O custo observado é:

$$
\Gamma_{\rm det}(t_f)
=
\frac12
\int
\langle
\Delta\Phi_\partial(t),
\mathsf R_{\rm app}(t)
\Delta\Phi_\partial(t)
\rangle
w(t_f,t)\,dt.
$$

O coeficiente de coerência é:

$$
\mathcal C_{\rm det}(t_f)
=
e^{-\Gamma_{\rm det}(t_f)}.
$$

No limite tardio:

$$
\Gamma_\infty=3{,}453877639491,
\qquad
\mathcal C_\infty
=
3{,}162277660168\times10^{-2}.
$$

Logo a coerência de amplitude residual é exatamente a esperada do crosstalk de
$-30\,{\rm dB}$ quando esse dado é usado como entrada congelada do aparelho.

## 4. Hessiana material reduzida

No modelo reduzido de braços do Mach--Zehnder, o acoplador lossless é:

$$
C(\theta)
=
\begin{pmatrix}
\cos\theta & i\sin\theta \\
i\sin\theta & \cos\theta
\end{pmatrix}.
$$

O acoplador ideal de $3\,{\rm dB}$ satisfaz:

$$
\theta=\frac{\pi}{4}.
$$

A propagação nos braços é:

$$
P(\phi,\eta)
=
\begin{pmatrix}
e^{i\phi/2} & 0 \\
0 & \eta e^{-i\phi/2}
\end{pmatrix},
$$

onde $\eta$ mede desbalanceamento de amplitude. A matriz total é:

$$
T_{\rm MZI}
=
C(\theta_2)P(\phi,\eta)C(\theta_1).
$$

A fase eletro-óptica obedece:

$$
\phi(V)=\pi\frac{V}{V_\pi}.
$$

Para:

$$
V=V_\pi,
\qquad
\theta_1=\theta_2=\frac{\pi}{4},
\qquad
\eta=1,
$$

o resultado ideal é:

$$
p_{\rm dark}^{\rm ideal}
=
3{,}749399456655\times10^{-33},
\qquad
p_{\rm bright}^{\rm ideal}=1.
$$

Ou seja, o crosstalk estacionário é nulo no aparelho ideal. Crosstalk finito
pertence a imperfeições materiais:

$$
K_{\rm app}^{\rm red}
=
K_0
+
\delta K_\phi
+
\delta K_\eta
+
\delta K_\theta
+
\delta K_{\rm loss}.
$$

O complemento de Schur fornece:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Para produzir $-30\,{\rm dB}$ por imperfeições isoladas, as equivalências
reduzidas são:

$$
\delta\phi
=
6{,}322448399238\times10^{-2}\,{\rm rad},
$$

$$
\delta V
=
4{,}920557195241\times10^{-2}\,{\rm V},
$$

$$
\eta
=
0{,}938693139937,
$$

ou:

$$
\delta\theta
=
3{,}161224199619\times10^{-2}\,{\rm rad},
$$

com split de potência:

$$
\sin^2\left(\frac{\pi}{4}+\delta\theta\right)
=
0{,}531591185416.
$$

## 5. Interpretação física

O resultado separa três níveis:

1. a ação oficial fornece a estrutura variacional;
2. o interferômetro reduzido fornece o domínio e a impedância de aparelho;
3. o crosstalk finito vem de $\delta K_{\rm app}$, isto é, material,
   fabricação, perdas e resposta eletro-óptica concreta.

Portanto, a escolha retardada não exige retrocausalidade física. Ela é:

$$
\boxed{
\text{mudança temporal de contorno}
+
\text{transporte causal da resposta}
+
\text{registro dissipativo final}.
}
$$

