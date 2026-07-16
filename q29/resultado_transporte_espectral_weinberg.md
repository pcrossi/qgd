# Q29 — Transporte espectral do ângulo de Weinberg

As rigidezes são definidas pelos traços de calor da Hessiana:

$$
K_a(\tau)
=C_{\rm GDQ}\operatorname{Tr}(T_a^2e^{-\tau\mathcal O_a}),
\qquad K_a=\frac1{g_a^2}.
$$

No ponto comum, $I_2=2$, $I_Y=10/3$ e

$$
\sin^2\theta_W(0)=\frac{K_W}{K_W+K_Y}=\frac38.
$$

Após a quebra, usando $s_0^2=3/8$, $c_0^2=5/8$,

$$
H_{W_3}=s_0^2H_\gamma+c_0^2H_Z,
\qquad
H_Y=c_0^2H_\gamma+s_0^2H_Z,
$$

$$
H_{W,\rm av}=\frac{2H_W+H_{W_3}}3,
$$

$$
K_W=2H_{W,\rm av},
\qquad
K_Y=\frac{10}{3}H_Y.
$$

Nenhuma função beta independente foi introduzida.

| $\tau$ | $\sin^2\theta_W(\tau)$ |
|---:|---:|
| $10^{-2}$ | $0{,}374999993$ |
| $1$ | $0{,}374999977$ |
| $10^4$ | $0{,}374782309$ |
| $10^5$ | $0{,}372802888$ |
| $10^6$ | $0{,}351231044$ |
| $10^7$ | $0{,}156188008$ |
| $10^8$ | $0{,}107142857$ |

A curva cruza

$$
\sin^2\theta_W=\frac29
$$

em

$$
\boxed{\tau_*=5{,}9090386\times10^6.}
$$

## Convergência

| pontos | modos | $\tau_*$ |
|---:|---:|---:|
| 2500 | 40 | $5{,}9091202\times10^6$ |
| 3500 | 100 | $5{,}9090386\times10^6$ |
| 5000 | 40 | $5{,}9094987\times10^6$ |
| 8000 | 40 | $5{,}9062646\times10^6$ |

A variação relativa é inferior a $6\times10^{-4}$. Na escala do cruzamento,
os modos excitados já foram suprimidos; o resultado é governado pelos gaps
fundamentais de $\gamma/W/Z$.

O resultado estabelece

$$
\boxed{
\frac38
\xrightarrow{\text{transporte espectral da Hessiana}}
\frac29.
}
$$

O cálculo ainda não prova que $\tau_*$ é a escala física eletrofraca. Falta
obter independentemente

$$
Q^2=Q^2(\tau,\Lambda_C,z_\tau)
$$

e verificar a coincidência. Usar $M_Z$ para escolher esse mapa seria circular.

Status:

$$
\boxed{
\text{mecanismo espectral derivado e estável;
identificação física da escala pendente.}
}
$$

Uma auditoria dimensional posterior distinguiu o parâmetro adimensional do
semigrupo, agora denotado $s$, do parâmetro dimensional. O resultado é

$$
\frac{Q_*}{\Lambda_0}
=\frac1{\sqrt{s_*}}
=4{,}113784964\times10^{-4}.
$$

Ver `q29/mapa_escala_transporte_espectral.md`.

A normalização absoluta por traços brutos foi testada e rejeitada: ela mistura
o transporte angular com a diminuição comum da densidade espectral. A
separação correta entre razão espectral e fluxo eletromagnético protegido está
em `q29/normalizacao_absoluta_fluxo_em.md`.
