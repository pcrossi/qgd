# Q30 — Fechamento estático do colar e mobilidade do fluxo

## 1. Colar selecionado pelos dados vigentes

Na redução radial, as condições naturais da ação conjunta sem uma fonte
métrico--dilatônica adicional são

$$
\Pi_a=\Pi_c=\Pi_f=0.
$$

Com

$$
\Pi_a=4\tau e^{-f}(ca'+ac'-acf'),
$$

$$
\Pi_c=2\tau e^{-f}a(2a'-af'),
$$

$$
\Pi_f=2\tau e^{-f}a(acf'-ac'-2ca'),
$$

e $a,c>0$, o sistema implica

$$
f'=2\frac{a'}a,
\qquad
\frac{c'}c=\frac{a'}a,
\qquad
a'=0,
$$

e, portanto,

$$
\boxed{a'=c'=f'=0.}
$$

Assim, no problema de contorno atualmente definido, o ramo estacionário é o
colar produto. Um colar não produto exigiria uma fonte ou Hessiana de
interface adicional ainda não pertencente aos dados. Ele é outra realização
possível, não uma pendência para fechar o ramo vigente.

## 2. Fluxo Ricci--Bismut

O fluxo geométrico registrado no Capítulo 17 é

$$
\frac{\partial g_{ij}}{\partial\tau}
=-2\left(
R_{ij}-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_jf
\right).
$$

Ele é o fluxo de gradiente do funcional Perelman--Bismut em $\tau$. Não deve
ser confundido com evolução unitária em tempo físico $t$.

## 3. Métrica no espaço do módulo radial

Para

$$
g_{ab}(R)=R^2\bar g_{ab}
$$

no ciclo tridimensional normalizado,

$$
\partial_Rg_{ab}=\frac2R g_{ab}.
$$

A norma ponderada desse vetor tangente é

$$
G_{RR}
=\int e^{-f}
g^{ac}g^{bd}
(\partial_Rg_{ab})(\partial_Rg_{cd})dV.
$$

Usando $\int e^{-f}dV=1$ e $\dim\Sigma_3=3$,

$$
\boxed{G_{RR}=\frac{12}{R^2}.}
$$

Pela primeira variação,

$$
\delta\mathcal W_T=-\tau\langle E_T,\delta g\rangle,
$$

e pelo fluxo $\partial_\tau g=-2E_T$, a projeção fornece

$$
G_{RR}\frac{dR}{d\tau}=+\frac2\tau\mathcal W_Q'(R).
$$

Logo, a mobilidade do fluxo ascendente é

$$
\boxed{
\mathsf M_R^{(\mathcal W)}
=\frac2{\tau G_{RR}}
=\frac{R^2}{6\tau}>0.
}
$$

## 4. Auditoria do sinal

O fluxo é subida de $\mathcal W_T$, exatamente compatível com
$d\mathcal W_T/d\tau\ge0$. Assim, um ramo com $K_R>0$ é repulsor, não
atrator, desse fluxo. Ver
`q30/auditoria_sinal_fluxo_perelman_bismut.md`.

## 5. Linearização do fluxo ascendente

Escreva

$$
R(\tau)=R_*+\rho(\tau),
\qquad
\mathcal W_Q'(R_*+\rho)=K_R\rho+O(\rho^2).
$$

No fluxo documentado,

$$
\boxed{
\frac{d\rho}{d\tau}
=+\Gamma_R^{\rm cresc}\rho,
\qquad
\Gamma_R^{\rm cresc}
:=\mathsf M_R^{(\mathcal W)}K_R.
}
$$

Como

$$
K_R=\frac{6(3R^2-8\tau)}{R^4},
$$

segue

$$
\boxed{
\Gamma_R^{\rm cresc}
=\frac{3R^2-8\tau}{\tau R^2}>0
}
$$

exatamente no mesmo domínio de estabilidade $R^2>8\tau/3$.

A solução linearizada, com coeficientes congelados localmente no valor de
$\tau$, é

$$
\boxed{\rho(\tau_f)=
\rho(\tau_i)e^{+\Gamma_R^{\rm cresc}(\tau_f-\tau_i)}.}
$$

## 6. Avaliação da solução vigente

Para $Q_T=1$ e $\alpha=1/137$,

$$
\mathsf M_R^{(\mathcal W)}=0.652068126520676,
$$

$$
\boxed{\Gamma_R^{\rm cresc}=3.47479834473450>0,}
$$

e o tempo de e-folding é

$$
\boxed{\tau_{\rm e-fold}=(\Gamma_R^{\rm cresc})^{-1}
=0.287786484506457.}
$$

Esses números são adimensionais e condicionais à ponte constitutiva usada na
Q35. Não empregam $1/128$.

## 7. Resposta forçada do fluxo auxiliar

Para uma fonte clássica radial $J_R(\tau)$,

$$
\frac{d\rho}{d\tau}-\Gamma_R^{\rm cresc}\rho
=\mathsf M_R^{(\mathcal W)}J_R.
$$

A função de Green formal contém crescimento:

$$
\boxed{
G_R^{(\tau)}(\tau-\tau')
=\mathsf M_R^{(\mathcal W)}
e^{+\Gamma_R^{\rm cresc}(\tau-\tau')}
\Theta(\tau-\tau').
}
$$

Logo, esse fluxo não fornece o kernel causal dissipativo necessário à medida
de Q30.

## 8. Limite do resultado

O cálculo não determina automaticamente a resposta em tempo físico $t$.
Essa passagem exige o pullback de

$$
z_\tau=\tau+i\nu_0t
$$

e o contorno causal $\gamma$. Portanto:

1. mobilidade do fluxo ascendente em $\tau$: derivada;
2. crescimento radial nesse fluxo: calculado;
3. mobilidade causal em $t$: ainda depende da reconstrução complexa;
4. ausência global de Stokes: ainda não demonstrada.

## 9. Status

$$
\boxed{
\text{o setor estático está fechado no colar produto; o fluxo auxiliar é
ascendente e repele o mínimo, não fornecendo a mobilidade causal da ação.}
}
$$
