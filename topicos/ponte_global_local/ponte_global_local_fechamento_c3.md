# Fechamento da ponte global--local no background $C_3$ gaussiano

## 1. Escopo

Este documento verifica a única hipótese física remanescente de
`topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md` para a classe estacionária usada na
Q28: três estômatos primitivos com preenchimentos gaussianos
$\mathbb C^2$, fechamento de Noether e simetria $C_3$.

Não afirma estabilidade de todo background possível da GDQ.

## 2. Background local

Em cada fatia normal,

$$
g_* = \delta,
\qquad
f_* = \frac{|x|^2}{4\tau}+f_0,
\qquad
\mathcal U_*dV
\propto e^{-|x|^2/(4\tau)}d^4x.
$$

A torção e a carga relativa pertencem à interface do estômato; o fechamento
coletivo é imposto durante a variação:

$$
\mathcal C(\Phi)=\sum_{a=1}^3\mathbf T_a=0.
$$

O funcional variado é a ação oficial com o multiplicador desse vínculo, não
uma ação modificada.

## 3. Projetor físico

No setor angular dos três centros, seja

$$
\mathbf e_0=\frac1{\sqrt3}(1,1,1)^T.
$$

A rotação comum é removida por

$$
P_{\rm rel}=I_3-\mathbf e_0\mathbf e_0^T.
$$

Nos preenchimentos gaussianos:

- o modo constante da fase é removido pela simetria de Noether;
- o modo constante do dilatão é removido pela normalização de $\mathcal U$;
- difeomorfismos e deformações paralelas são removidos pelo gauge
  Hermitiano--DeTurck;
- a escala é fixada por $\tau$ e pela normalização.

O projetor total é a soma ortogonal desses projetores setoriais e coincide
com a construção conjunta

$$
P^{\rm phys}
=I-\mathbb G^{-1}A^\dagger
(A\mathbb G^{-1}A^\dagger)^+A.
$$

## 4. Hessiana projetada e domínio

O operador ponderado local é

$$
L_f=-\Delta+\frac{x}{2\tau}\cdot\nabla
$$

em $L^2(\mathbb R^4,\mathcal U_*d^4x)$. Sua realização de Friedrichs no
Sobolev gaussiano ponderado é auto-adjunta. Pela conjugação unitária com a
medida gaussiana, ele equivale ao oscilador harmônico deslocado e possui
resolvente compacto.

Depois dos vínculos e do gauge,

$$
\mathbb H_{0,\rm phys}^{(3)}
=H_{\rm rel}\oplus K_r^{(0)}
\oplus K_v^{\rm phys}
\oplus K_{(g,f)}^{\rm HD,phys},
$$

com

$$
H_{\rm rel}=\frac32\kappa_{\rm rel}T^2I_2,
\qquad
K_r^{(0)}=\frac{3}{2\tau}I_3,
$$

$$
K_v^{\rm phys}=2L_f|_{m\ge1},
\qquad
K_{(g,f)}^{\rm HD,phys}=L_f|_{m\ge1}.
$$

O acoplamento angular--radial desaparece pela conservação da classe primitiva:

$$
J_{\theta r}=0.
$$

## 5. Gap local

O espectro de $L_f$ é

$$
\operatorname{spec}L_f
=\left\{\frac{m}{2\tau}:m=0,1,2,\ldots\right\}.
$$

Todos os níveis $m=0$ são normalização, Noether, escala ou gauge. Portanto

$$
\boxed{
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0.
}
$$

Na normalização primitiva da Q28,

$$
\kappa_{\rm rel}T^2=1,
\qquad
\tau=1,
$$

e

$$
\boxed{\Delta_0=\frac12.}
$$

## 6. Verificação numérica independente

`ponte_global_local_validar_gap_c3.py` discretiza o operador conjugado

$$
-\frac{d^2}{dx^2}
+\frac{x^2}{16\tau^2}
-\frac1{4\tau}.
$$

Em $\tau=1$, o primeiro nível físico convergiu como:

| pontos | gap numérico | erro para $1/2$ |
|---:|---:|---:|
| 400 | $0{,}4999300307$ | $6{,}997\times10^{-5}$ |
| 800 | $0{,}4999824653$ | $1{,}753\times10^{-5}$ |
| 1600 | $0{,}4999956109$ | $4{,}389\times10^{-6}$ |
| 3200 | $0{,}4999989021$ | $1{,}098\times10^{-6}$ |

O mesmo refinamento confirmou $1/(2\tau)$ para
$\tau\in\{1/2,1,2,4\}$.

## 7. Aplicação dos seis lemas

Como $\Delta_0>0$, a correção do background transportado é controlada no
complemento físico. Para $\varepsilon$ suficientemente pequeno:

1. existe a família apontada com o mesmo estômato localizado;
2. os campos e a medida convergem localmente;
3. as formas físicas convergem em Mosco;
4. IMS e Agmon preservam localização e um gap uniforme;
5. resolventes e projetores de Riesz convergem no cluster;
6. carga, multiplicidade e identidade espectral são herdadas, enquanto a
   resposta continua local.

Em particular, escolhendo qualquer $0<\delta<\Delta_0/3$, existe
$\varepsilon_0$ tal que

$$
\Delta_\varepsilon
\ge\Delta_0-2\delta>0
$$

para $0<\varepsilon<\varepsilon_0$.

## 8. Veredito

$$
\boxed{
\begin{gathered}
\text{a ponte global--local está fechada na classe estacionária}\
\text{dos três preenchimentos gaussianos primitivos }C_3;\\
\text{não é necessária sela de colagem cosmológico--local.}
\end{gathered}
}
$$

Classificação: teorema aplicado à classe $C_3$ sob o background e vínculos já
derivados na Q28. O valor $\Delta_0=1/2$ é adimensional na normalização comum
da ação; convertê-lo em escala de energia exige a normalização global, mas sua
positividade e o transporte espectral não dependem dessa conversão.

