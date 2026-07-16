# Q30 — Teorema do puxamento de estômato com carga torsional conservada

## 1. Enunciado geométrico

Seja $\Sigma_s$ o ciclo tridimensional que envolve a garganta de um estômato,
transportado por uma deformação suave $\Phi_s$, sem cirurgia que atravesse o
defeito. Seja $H_s$ a 3-forma de torção de Bismut no ciclo e suponha

$$
dH_s=0,
\qquad
Q_T:=\int_{\Sigma_s}H_s=\text{constante}.
$$

Então a distorção de $\Sigma_s$ e o módulo da torção não são graus de
liberdade independentes. Escrevendo

$$
H_s=Q_T\eta_s+d\beta_s,
\qquad
\int_{\Sigma_s}\eta_s=1,
$$

o representante de menor norma na classe fixa é o representante harmônico
$H_s=Q_T\eta_s$ e

$$
\boxed{
\mathcal E_T(s)
=\frac{\kappa_T}{2}Q_T^2
\int_{\Sigma_s}|\eta_s|_{g_s}^2d\mu_{g_s}.
}
$$

Logo, toda deformação métrica admissível altera a energia por meio da norma de
Hodge da mesma classe conservada. Esse é o acoplamento local--global da GDQ:
a carga fixa a classe; a geometria fixa seu módulo.

## 2. Caso homogêneo da garganta

Se o setor relevante é homogêneo e

$$
\eta_s=\frac{\operatorname{vol}_{\Sigma_s}}{V(s)},
\qquad
V(s)=\operatorname{Vol}(\Sigma_s),
$$

então, na convenção em que a forma volume unitária tem norma um,

$$
\boxed{
H_s=\frac{Q_T}{V(s)}\operatorname{vol}_{\Sigma_s},
\qquad
|H_s|=\frac{|Q_T|}{V(s)},
\qquad
\mathcal E_T(s)=\frac{\kappa_TQ_T^2}{2V(s)}.
}
$$

Assim, puxar ou comprimir o estômato força uma resposta do módulo torsional.
Não é permitido variar $V$ mantendo simultaneamente $|H|$ fixo.

## 3. Jatos determinados pela conservação

Defina $C_T=\kappa_TQ_T^2/2$. As três primeiras derivadas são

$$
\mathcal E_T'
=-C_T\frac{V'}{V^2},
$$

$$
\boxed{
\mathcal E_T''
=C_T\left[
\frac{2(V')^2}{V^3}-\frac{V''}{V^2}
\right],
}
$$

e

$$
\boxed{
\mathcal E_T'''
=C_T\left[
-\frac{V'''}{V^2}
+\frac{6V'V''}{V^3}
-\frac{6(V')^3}{V^4}
\right].
}
$$

Essas identidades fornecem a contribuição torsional vinculada tanto à
Hessiana quanto ao terceiro jato causal $A_3$.

Para a coordenada logarítmica de distorção $x=\log(V/V_0)$,

$$
\mathcal E_T(x)=\frac{C_T}{V_0}e^{-x},
$$

portanto

$$
\boxed{
\frac{d^2\mathcal E_T}{dx^2}=\mathcal E_T>0,
\qquad
\frac{d^3\mathcal E_T}{dx^3}=-\mathcal E_T.
}
$$

A conservação fornece, assim, rigidez torsional positiva na direção
logarítmica antes da soma com os demais blocos da ação.

## 4. Inserção no coeficiente causal

Se $x=x(z)$ descreve o puxamento ao longo do contorno, a contribuição
torsional ao terceiro jato é

$$
\boxed{
\begin{aligned}
\frac{d^3\mathcal E_T(x(z))}{dz^3}
=\mathcal E_T(x(z))\big[
&-(x')^3+3x'x''-x'''
\big].
\end{aligned}
}
$$

Ela entra em $A_3$ junto com o jacobiano $d\tau/dz$, a medida ponderada e os
blocos de curvatura e de $f$. Portanto, a conservação elimina o módulo de
torção como dado independente e reduz o problema causal ao jato da distorção
$x(z)$, que deve obedecer às equações de fluxo GDQ.

## 5. Alcance do teorema

O teorema prova:

1. conservação de carga sob deformações sem cirurgia;
2. dependência obrigatória do módulo torsional na geometria;
3. rigidez positiva da parcela torsional no modo logarítmico homogêneo;
4. contribuição explícita ao terceiro jato causal.

Ele não prova isoladamente:

1. positividade da Hessiana total, pois curvatura, dilatão e termos mistos
   também contribuem;
2. o sinal de $\operatorname{Im}A_3$, pois ele depende da solução causal
   $x(z)$ e da orientação do contorno;
3. ausência global de saltos de Stokes.

## 6. Classificação

- conservação de $Q_T$: hipótese/topologia vigente da GDQ;
- minimização na classe por representante harmônico: derivação de Hodge;
- fórmulas $\mathcal E_T=C_T/V$ e seus jatos: derivação exata no setor
  homogêneo;
- rigidez torsional positiva: teorema setorial;
- coercividade total e nível Clay: ainda condicionais aos demais blocos.

