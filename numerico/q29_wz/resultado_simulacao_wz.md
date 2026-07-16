# Q29 — Simulação diagnóstica de $W$ e $Z$

## 1. Entrada geométrica

Foi usado exclusivamente

$$
v=246{,}111195996\,\mathrm{GeV}
$$

na matriz de massas

$$
M_0^2
=\frac{v^2}{4}
\begin{pmatrix}
g^2&-gg'\\
-gg'&g'^2
\end{pmatrix}.
$$

Em todos os casos,

$$
\det M_0^2=0
$$

numericamente, mantendo o fóton sem massa.

## 2. Resultados

| Caso | $\alpha^{-1}$ | $\sin^2\theta_W$ | $m_W$ (GeV) | $m_Z$ (GeV) |
|---|---:|---:|---:|---:|
| ponto geométrico | $137{,}035999$ | $3/8$ | $60{,}8518$ | $76{,}9721$ |
| hipótese $2/9$ | $137{,}035999$ | $2/9$ | $79{,}0488$ | $89{,}6329$ |
| resolução EW | $128$ | $3/8$ | $62{,}9630$ | $79{,}6426$ |
| resolução EW com $2/9$ | $128$ | $2/9$ | $81{,}7914$ | $92{,}7427$ |

## 3. Resultado sobre o ângulo

A razão independe da normalização absoluta de $e$:

$$
\frac{m_W}{m_Z}=\cos\theta_W.
$$

Para $3/8$,

$$
\frac{m_W}{m_Z}=0{,}790569,
$$

enquanto para $2/9$,

$$
\boxed{
\frac{m_W}{m_Z}=0{,}881917.
}
$$

Portanto, a hipótese geométrica $2/9$ presente no manuscrito descreve muito
melhor a razão operacional das massas do que o valor $3/8$ do ponto comum.

## 4. Valor efetivo exigido sem ajuste conjunto

Mantendo $\sin^2\theta_W=2/9$ e o $v$ da GDQ, pode-se inverter cada massa
separadamente apenas como diagnóstico:

$$
\alpha_W^{-1}=132{,}537853,
$$

$$
\alpha_Z^{-1}=132{,}403061.
$$

Os dois valores diferem por aproximadamente $0{,}10\%$. Isso mostra que um
único acoplamento eletromagnético efetivo próximo de

$$
\alpha_{\rm EW}^{-1}\simeq132{,}47
$$

seria compatível simultaneamente com ambos dentro do nível de aproximação do
modelo.

Esse número não é ainda uma previsão: foi inferido das massas para localizar
o valor que o transporte geométrico precisa produzir.

## 5. Conclusão

$$
\boxed{
\sin^2\theta_W=\frac29
}
$$

é a rota quantitativamente promissora para o background eletrofraco. Falta
derivar $2/9$ e $\alpha_{\rm EW}^{-1}\simeq132{,}47$ das normas globais, sem
usar $m_W$ ou $m_Z$ como entradas.

O cálculo reproduzível está em `simular_wz_q29.py`.
