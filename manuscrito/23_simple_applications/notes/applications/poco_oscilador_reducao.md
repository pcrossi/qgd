---
title: "Poço e oscilador como redução"
---

# Poço e oscilador como redução

Status: redução efetiva autocontida.

## Enunciado

No setor plano, estacionário e unidimensional, a equação de densidade da GDQ
reduz a problemas espectrais conhecidos.

O ponto conceitual é importante: poço infinito e oscilador harmônico não
validam a GDQ por si mesmos. Eles verificam que a cadeia de redução da ação
oficial para o setor físico de Madelung não destrói os limites elementares que
qualquer teoria aceitável deve recuperar.

Partimos das variáveis constitutivas:

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
R=\sqrt\rho.
$$

No setor local, plano e estabilizado pelo relógio físico, a ação reduzida toma
a forma:

$$
I_{\rm red}
=
\int dt\int_\Sigma
\left[
\rho\partial_tS_R
+
\rho\frac{|\nabla S_R|^2}{2m}
+
\rho V
+
\frac{\hbar^2}{8m}\frac{|\nabla\rho|^2}{\rho}
\right]d\Sigma.
$$

Variação em $S_R$ dá:

$$
\partial_t\rho
+
\nabla\cdot\left(\rho\frac{\nabla S_R}{m}\right)
=0.
$$

Variação em $\rho$ dá:

$$
\partial_tS_R
+
\frac{|\nabla S_R|^2}{2m}
+
V
-
\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

Para estados reais estacionários,

$$
S_R=-Et,
\qquad
\nabla S_R=0,
$$

e a equação reduzida fica:

$$
E
=
V
-
\frac{\hbar^2}{2m}
\frac{\Delta R}{R}.
$$

## Poço

Com $S_R=-Et$ e $V=0$:

$$
E
=
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
$$

Logo:

$$
-R''
=
k^2R,
\qquad
k^2=\frac{2mE}{\hbar^2}.
$$

Com $R(0)=R(L)=0$:

$$
R_n=A\sin\left(\frac{n\pi x}{L}\right),
\qquad
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

A mesma quantização pode ser escrita como circulação fechada da fase:

$$
\oint p\,dx=nh.
$$

No poço, uma órbita fechada bate nas duas paredes e volta ao ponto inicial,
portanto:

$$
2pL=nh,
\qquad
p=\frac{nh}{2L}.
$$

Logo:

$$
E_n=\frac{p^2}{2m}
=
\frac{n^2h^2}{8mL^2}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

Na leitura GDQ, essa rota explicita que a condição espectral é uma condição de
fechamento de holonomia/circulação do setor $S_R$ contra o contorno.

## Oscilador

Com $V=m\omega^2x^2/2$:

$$
E
=
\frac12m\omega^2x^2
-
\frac{\hbar^2}{2m}
\frac{R''}{R}.
$$

Para $R=Ae^{-\alpha x^2/2}$:

$$
\frac{R''}{R}
=
\alpha^2x^2-\alpha.
$$

O termo proporcional a $x^2$ anula se:

$$
\alpha=\frac{m\omega}{\hbar}.
$$

Então:

$$
E_0=\frac12\hbar\omega.
$$

Para que a gaussiana não seja interpretada como chute, ela também pode ser
obtida variacionalmente. O funcional estacionário é:

$$
\mathcal E[R]
=
\int_{\mathbb R}
\left[
\frac{\hbar^2}{2m}|R'|^2
+
\frac12m\omega^2x^2R^2
\right]dx,
\qquad
\int_{\mathbb R}R^2dx=1.
$$

Com multiplicador $E$:

$$
\delta
\left(
\mathcal E[R]
-
E\int_{\mathbb R}R^2dx
\right)=0
$$

gera:

$$
-
\frac{\hbar^2}{2m}R''
+
\frac12m\omega^2x^2R
=
ER.
$$

O estado fundamental é o minimizador positivo desse problema elíptico. A
dominância espectral do fluxo de gradiente normalizado também seleciona esse
estado: se

$$
R(\tau,x)=\sum_{n\ge0}c_n(\tau)R_n(x),
$$

então, após retirar a energia fundamental,

$$
c_n(\tau)=c_n(0)e^{-(E_n-E_0)\tau},
\qquad
n>0.
$$

Como $E_n-E_0>0$, as componentes excitadas decaem e resta $R_0$.

Para a escada completa, a regra de circulação com dois pontos de retorno dá:

$$
\oint p\,dx
=
h\left(n+\frac12\right).
$$

Como:

$$
\oint p\,dx=\frac{2\pi E}{\omega},
$$

segue:

$$
E_n=\hbar\omega\left(n+\frac12\right).
$$

O termo $1/2$ é o índice de Maslov dos dois pontos de retorno. Na linguagem da
GDQ, ele é a fase de fronteira/cáustica necessária para fechar a circulação do
canal de fase.

## Hessiana e índice

No poço ideal:

$$
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
-E_n.
$$

No oscilador:

$$
\mathcal J_n
=
-
\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
+\frac12m\omega^2x^2
-E_n.
$$

Os autovalores relativos são $E_k-E_n$. Isso identifica a estabilidade do
estado fundamental e o índice de Morse dos estados excitados.

Para o poço, com $n=1,2,\ldots$, o estado $R_n$ possui $n-1$ direções
negativas na Hessiana restrita à normalização. Para o oscilador, com
$n=0,1,\ldots$, o estado $R_n$ possui $n$ direções negativas. Assim:

$$
\operatorname{ind}_{\rm Morse}^{\rm poço}(R_n)=n-1,
\qquad
\operatorname{ind}_{\rm Morse}^{\rm osc}(R_n)=n.
$$

Isso separa mínimo físico de ponto crítico excitado. A GDQ recupera essa
estrutura como Hessiana reduzida do setor plano, não como operador fundamental
postulado.

## Perturbações geométricas permitidas

Se o fundo reduzido não for exatamente plano, escrevemos em uma dimensão:

$$
ds^2=a^2(x)dx^2,
\qquad
d\mu_g=a(x)dx.
$$

O Laplace--Beltrami é:

$$
\Delta_gR
=
\frac1a\partial_x
\left(
\frac1a\partial_xR
\right).
$$

Para:

$$
a(x)=1+\varepsilon h(x),
\qquad
V_{\rm tor}(x)=\varepsilon W_T(x),
\qquad
|\varepsilon|\ll1,
$$

a coordenada geodésica $dy=a(x)dx$ implica:

$$
x(y)=y-\varepsilon H(y)+O(\varepsilon^2),
\qquad
H'(y)=h(y).
$$

No oscilador:

$$
\frac12m\omega^2x^2
=
\frac12m\omega^2y^2
-
\varepsilon m\omega^2yH(y)
+
O(\varepsilon^2).
$$

A primeira correção geométrica é:

$$
\Delta E_n^{\rm geom}
=
-
\varepsilon m\omega^2
\langle n|yH(y)|n\rangle
+
\varepsilon\langle n|W_T(y)|n\rangle.
$$

Essa expressão só é preditiva quando $h$ e $W_T$ são calculados da equação
métrica/torsional da GDQ. Se forem escolhidos livremente, trata-se apenas de
parametrização fenomenológica.

## Alcance

Esta nota não demonstra a existência de paredes físicas nem de potenciais
externos. Ela mostra apenas que, dados domínio e contorno reduzidos, a GDQ
recupera os operadores esperados.

O fechamento forte material exige calcular a parede, o potencial efetivo ou a
perturbação torsional pela Hessiana física da ação oficial. O fechamento de
correspondência, porém, está completo: no limite plano, estacionário e com
contorno ideal, os espectros conhecidos são recuperados sem inserir nova ação.
