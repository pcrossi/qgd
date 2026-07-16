# Q29 — Resultado espectral radial de $\gamma/W/Z$

## Operador avaliado

Foi discretizado por elementos finitos o problema

$$
-\frac{d}{d\chi}(p\Psi_a')
=\lambda_aw\Psi_a,
$$

com regularidade no antipolo e o termo Robin variacional no estômato. Foram
usados o background acoplado $(A,F)$ e os coeficientes de interface derivados,
sem massas experimentais como entrada.

## Espectro

Com $5000$ pontos, os quatro primeiros autovalores são:

| canal | $\lambda_0$ | $\lambda_1$ | $\lambda_2$ | $\lambda_3$ |
|---|---:|---:|---:|---:|
| $\gamma$ | $-1{,}79\times10^{-11}$ | $1{,}53765878$ | $2{,}92597852$ | $4{,}64975717$ |
| $W$ | $2{,}31936613\times10^{-7}$ | $1{,}53765902$ | $2{,}92597883$ | $4{,}64975767$ |
| $Z$ | $3{,}71093800\times10^{-7}$ | $1{,}53765917$ | $2{,}92597902$ | $4{,}64975797$ |

O pequeno valor negativo do fóton está abaixo do erro absoluto do resolvedor e
representa o modo zero:

$$
\boxed{\lambda_\gamma=0.}
$$

Os canais quebrados são positivos e ordenados:

$$
0<\lambda_W<\lambda_Z.
$$

## Normas dos perfis

Normalizando $\Psi_a(\epsilon)=1$,

$$
N_\gamma=10{,}4085853620,
$$

$$
N_W=10{,}4101105728,
\qquad
N_Z=10{,}4110257529.
$$

Logo,

$$
\frac{N_W}{N_Z}=0{,}999912091.
$$

O transporte radial diferencial é inferior a $10^{-4}$, muito distante do
fator $10/21$ necessário para converter $3/8$ em $2/9$.

## Convergência de malha

| pontos | $\lambda_W$ | $\lambda_Z$ | $N_W$ | $N_Z$ |
|---:|---:|---:|---:|---:|
| 2500 | $2{,}3195165\times10^{-7}$ | $3{,}7110830\times10^{-7}$ | $10{,}4100960$ | $10{,}4110024$ |
| 5000 | $2{,}3193661\times10^{-7}$ | $3{,}7109380\times10^{-7}$ | $10{,}4101106$ | $10{,}4110258$ |
| 10000 | $2{,}3196657\times10^{-7}$ | $3{,}7112343\times10^{-7}$ | $10{,}4101143$ | $10{,}4110318$ |

As normas e os níveis excitados convergem estavelmente. Os autovalores
fundamentais, sete ordens abaixo da escala dos níveis excitados, apresentam a
flutuação esperada do shift-invert, sem alterar sinal, ordenação ou conclusão.

## Explicação analítica

Para Robin pequeno, o modo fundamental é quase constante. O quociente de
Rayleigh fornece

$$
\lambda_a
=\frac{\mathsf M_{\partial,a}|\Psi(\epsilon)|^2}
{\int_\epsilon^\pi w|\Psi|^2d\chi}
+O(\mathsf M_\partial^2).
$$

Portanto,

$$
\frac{\lambda_W}{\lambda_Z}
=\frac{g^2}{g^2+g'^2}
+O(\mathsf M_\partial),
$$

e o warp escalar comum não altera significativamente o ângulo do ponto de
correspondência.

## Veredito

O solver fecha corretamente o espectro radial no ansatz calculado:

$$
\boxed{
m_\gamma=0,
\qquad
m_W^2>0,
\qquad
m_Z^2>m_W^2.
}
$$

Ele também exclui esse mecanismo como origem de $2/9$. Para transporte forte,
é indispensável um operador interno não universal:

$$
q_W(\chi)\ne q_Y(\chi)
$$

ou uma holonomia/torção mista que produza perfis distintos antes da aplicação
do contorno de Hopf. Introduzir tal diferença apenas no valor Robin não basta.
