# Q72 — Hessiana material reduzida do Mach--Zehnder eletro-óptico

## 1. Objetivo

Esta nota continua a Q72 após a comparação com crosstalk externo. O objetivo é
separar o que pode ser calculado diretamente do aparelho reduzido do que exige
dados materiais adicionais.

O alvo é construir:

$$
K_{\rm app}^{\rm red}
\to
\mathsf R_{\rm app}
\to
\Gamma_{\rm det}.
$$

## 2. Modelo reduzido de braços

No nível de engenharia óptica, o Mach--Zehnder pode ser descrito por dois
acopladores e uma fase diferencial eletro-óptica.

O acoplador lossless é:

$$
C(\theta)
=
\begin{pmatrix}
\cos\theta & i\sin\theta \\
i\sin\theta & \cos\theta
\end{pmatrix}.
$$

O acoplador ideal de $3\,\mathrm{dB}$ satisfaz:

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

onde $\eta$ mede desbalanceamento de amplitude.

A matriz total é:

$$
T_{\rm MZI}
=
C(\theta_2)P(\phi,\eta)C(\theta_1).
$$

## 3. Fase eletro-óptica

O dado $V_\pi$ fixa:

$$
\phi(V)
=
\pi\frac{V}{V_\pi}.
$$

Portanto, para $V=V_\pi$:

$$
\phi=\pi.
$$

Com acopladores ideais e $\eta=1$, um dos portos é escuro:

$$
p_{\rm dark}=0.
$$

Isso é importante: $V_\pi$ e $\tau_{\rm sw}$ determinam a fase e a dinâmica de
comutação, mas não determinam sozinhos o crosstalk estacionário finito.

## 4. Onde entra o crosstalk

O crosstalk finito vem de imperfeições materiais:

1. erro de fase $\delta\phi$;
2. desbalanceamento de amplitude $\eta\neq1$;
3. erro de acoplador $\theta\neq\pi/4$;
4. perda diferencial;
5. dispersão e resposta eletro-óptica não uniforme.

Na linguagem GDQ reduzida, esses termos pertencem ao operador material:

$$
K_{\rm app}^{\rm red}
=
K_0
+
\delta K_{\phi}
+
\delta K_{\eta}
+
\delta K_{\theta}
+
\delta K_{\rm loss}.
$$

O complemento de Schur fornece a impedância efetiva:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## 5. Resultado numérico

O script:

- `questoes/q72/associados/calcular_hessiana_material_mzi_q72.py`

gera:

- `questoes/q72/associados/saida_hessiana_material_mzi_q72.md`.

O resultado central é:

$$
\boxed{
\text{em MZI ideal, }p_{\rm dark}=0.
}
$$

Para obter $-30\,\mathrm{dB}$ isoladamente por erro de fase, é necessário:

$$
\delta\phi\simeq6{,}3224\times10^{-2}\,\mathrm{rad}.
$$

Isso equivale a um erro de tensão:

$$
\delta V\simeq4{,}9206\times10^{-2}\,\mathrm V
$$

para $V_\pi=2{,}445\,\mathrm V$.

Equivalentes isolados:

$$
\eta\simeq0{,}938693139937
$$

para desbalanceamento de amplitude, ou:

$$
\delta\theta\simeq3{,}1612\times10^{-2}\,\mathrm{rad}
$$

para erro diferencial de um acoplador, correspondente a um split de potência:

$$
\sin^2\left(\frac{\pi}{4}+\delta\theta\right)
\simeq0{,}531591185416.
$$

Portanto, o crosstalk de $-30\,\mathrm{dB}$ é compatível com uma imperfeição
material pequena, mas ele não é dedutível apenas de $V_\pi$ e
$\tau_{\rm sw}$.

## 6. Conclusão

O cálculo mostra exatamente onde termina a predição reduzida atual:

$$
\boxed{
\text{a GDQ reduzida deriva a forma de } \mathsf R_{\rm app};
\text{ o valor estacionário exige } \delta K_{\rm app}.
}
$$

Assim, a Q72 permanece fechada estruturalmente. A etapa de primeiros princípios
material seria calcular $\delta K_{\rm app}$ a partir da geometria, composição e
eletro-óptica do dispositivo real.
