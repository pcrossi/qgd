# Q29 — Construção explícita do modo eletrofraco em $S^3$

## 1. Coordenadas de Hopf

Escreva

$$
S^3
=\left\{
u=\begin{pmatrix}z_1\\z_2\end{pmatrix}\in\mathbb C^2:
u^\dagger u=1
\right\}.
$$

O grupo $SU(2)_L$ age por

$$
u\longmapsto U_Lu,
\qquad U_L\in SU(2),
$$

e a fibra de Hopf age por

$$
u\longmapsto e^{i\vartheta/2}u.
$$

Logo,

$$
\boxed{u\sim(1,2)_{1/2}.}
$$

Esse é exatamente o tipo de representação exigido para o modo de ordem
eletrofraco.

## 2. Harmônico fundamental

As componentes $z_1,z_2$ são harmônicos escalares de nível $\ell=1$ em
$S^3(R)$. Portanto,

$$
-\Delta_{S^3}u
=\frac{\ell(\ell+2)}{R^2}u
=\frac3{R^2}u.
$$

O projetor espectral procurado na formulação abstrata da Q29 passa a ser
explícito:

$$
\Pi_{(1,2)_{1/2}}
=\Pi_{\ell=1,m_R=1/2}.
$$

## 3. Campo de ordem geométrico

Defina

$$
\boxed{
\Phi_{\rm EW}(x,y)=\frac{\rho(x)}{\sqrt2}\,u(y).
}
$$

Aqui $u$ fornece orientação e números quânticos, enquanto $\rho$ é a
amplitude geométrica associada à magnitude do fluxo/raio estabilizado.

No vácuo,

$$
\rho=v.
$$

Uma transformação de $SU(2)_L\times U(1)_Y$ permite escolher

$$
u_0=\begin{pmatrix}0\\1\end{pmatrix}.
$$

O gerador que preserva $u_0$ é

$$
Q=T_3+Y.
$$

Assim,

$$
\boxed{
SU(2)_L\times U(1)_Y\longrightarrow U(1)_{\rm EM}.
}
$$

## 4. Matriz de massa

Com

$$
D_\mu
=\partial_\mu
-igW_\mu^a\frac{\sigma_a}{2}
-ig'B_\mu\frac12,
$$

o pullback da energia cinética em $\Phi_{\rm EW}=vu_0/\sqrt2$ fornece

$$
m_W^2=\frac{g^2v^2}{4}
$$

e, no setor $(W^3,B)$,

$$
M_0^2
=\frac{v^2}{4}
\begin{pmatrix}
g^2&-gg'\\
-gg'&g'^2
\end{pmatrix}.
$$

Como

$$
\det M_0^2=0,
$$

o fóton permanece sem massa, enquanto

$$
m_Z^2=\frac{v^2}{4}(g^2+g'^2).
$$

## 5. Relação com a torção

Uma flutuação real da 3-forma pode usar as quatro componentes reais do
dupleto:

$$
\delta B_{\rm EW}
=\operatorname{Re}(\beta^\dagger u)\,operatorname{vol}_{S^3}.
$$

Como os harmônicos $\ell=1$ têm integral nula, essa flutuação preserva o fluxo
inteiro homogêneo:

$$
\int_{S^3}\delta B_{\rm EW}=0.
$$

Assim, o fluxo $n_B$ estabiliza a magnitude global, enquanto o harmônico de
Hopf fornece a orientação eletrofraca carregada.

## 6. Resultado

O autovetor que faltava deixa de ser abstrato:

$$
\boxed{
\Phi_{\rm EW}
=\frac{\rho}{\sqrt2}u,
\qquad
u\in\ker\left(-\Delta_{S^3}-\frac3{R^2}\right),
\qquad
u\sim(1,2)_{1/2}.
}
$$

Ainda falta calcular a normalização física de $\rho=v$ e o transporte das
normas cinéticas no background anisotrópico quebrado.
