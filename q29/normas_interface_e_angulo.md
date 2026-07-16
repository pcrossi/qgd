# Q29 — Normas de Killing na interface deformada

## 1. Cálculo

Os campos de Killing de $SU(2)_L$ e da fibra $U(1)_Y$ foram escritos como
matrizes antissimétricas reais agindo em

$$
u=(x_1+ix_2,x_3+ix_4)\in S^3.
$$

Na interface

$$
r(Y)=R(1+\varepsilon_*Y),
\qquad
\varepsilon_*=0{,}273137642,
$$

a norma induzida de um gerador $A$ é

$$
|\xi_A|^2
=r^2|An|^2+(\delta_A r)^2.
$$

Ela foi integrada com o elemento de área deformado usando $10^6$ pontos
uniformes em $S^3$.

## 2. Resultado

Na esfera redonda,

$$
I_{W_1}=I_{W_2}=I_{W_3}=I_Y=0{,}25.
$$

Na interface deformada,

$$
I_{W_1}=0{,}28566381,
$$

$$
I_{W_2}=0{,}28566810,
$$

$$
I_{W_3}=0{,}28567145,
$$

$$
I_Y=0{,}28567145.
$$

A razão transportada é

$$
\frac{(I_W/I_Y)_{\rm deformado}}
{(I_W/I_Y)_{\rm redondo}}
=0{,}99998718.
$$

Uma verificação analítica posterior mostrou que o valor exato dessa razão é
$1$. Como todo peso depende apenas de $Y=x_4$, a isotropia residual implica

$$
\int x_1^2F(x_4)d\Omega
=\int x_2^2F(x_4)d\Omega
=\int x_3^2F(x_4)d\Omega.
$$

Assim, as diferenças acima são exclusivamente erro Monte Carlo.

Assim,

$$
\frac{g'^2}{g^2}
=0{,}59999231
$$

e

$$
\boxed{
\sin^2\theta_W
=0{,}37499699
\simeq\frac38.
}
$$

## 3. Conclusão

A deformação local $\ell=1$:

1. fornece o modo carregado;
2. produz a quebra e a quártica positiva de interface;
3. não transporta significativamente a razão das normas cinéticas.

Portanto, a diferença entre o valor geométrico $3/8$ e o valor operacional em
baixas energias não vem da interface local. Ela exige a redução global no
background cosmológico $T^5\times S^3$, incluindo os pesos toroidais e o fluxo
entre escalas geométricas.

O script é `q29/calcular_normas_interface_q29.py`.
