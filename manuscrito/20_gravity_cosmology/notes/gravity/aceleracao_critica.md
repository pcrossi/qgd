---
title: "Aceleração crítica galáctica"
---

# Aceleração crítica galáctica

Esta nota deduz a escala de aceleração crítica usada no limite galáctico da
GDQ. O objetivo não é postular MOND, mas mostrar como uma escala do tipo MOND
aparece quando o contorno cosmológico global é projetado no canal local de
circulação.

## 1. Dados geométricos

O dado global é o raio de Hubble:

$$
R_H
=
\frac{c}{H_0}.
$$

Esse raio não é uma constante local do sóliton. Ele é condição de contorno do
problema cosmológico. A aceleração de horizonte associada é:

A escala de horizonte é:

$$
a_H
=
cH_0
=
\frac{c^2}{R_H}.
$$

O canal local relevante para uma resposta radial estacionária é circular. A
circulação completa tem comprimento angular $2\pi$. Portanto, a aceleração por
ciclo projetado é:

A resposta circular por ciclo é:

$$
a_0^{\rm GDQ}
=
\frac{a_H}{2\pi}
=
\frac{cH_0}{2\pi}.
$$

Essa é a fórmula adotada. O fator $2\pi$ não é escolhido para ajustar a escala
fenomenológica: ele é a normalização de circulação do canal radial quando uma
escala global de horizonte é transportada para uma resposta local.

## 2. Distinção entre horizonte de Hubble e de Sitter

Há uma escala auxiliar:

$$
a_{\rm dS}^{(2\pi)}
=
\frac{cH_0\sqrt{\Omega_\Lambda}}{2\pi}.
$$

Ela pertence ao horizonte efetivo de de Sitter. Essa escala é útil em
cosmologia, mas não é a definição principal da aceleração crítica galáctica.
A confusão entre as duas escalas foi a origem de uma inconsistência aritmética
histórica: se o numerador for aproximadamente $5{,}46\times10^{-10}$, então:

$$
\frac{5{,}46\times10^{-10}}{2\pi}
\approx
8{,}69\times10^{-11},
$$

e não $1{,}21\times10^{-10}$.

## 3. Comparação com escala MOND típica

O valor fenomenológico usual é da ordem de:

$$
a_0^{\rm MOND}
\sim
1{,}20\times10^{-10}\,{\rm m/s^2}.
$$

Para $H_0=67{,}4\,{\rm km\,s^{-1}\,Mpc^{-1}}$:

$$
a_0^{\rm GDQ}
=
1{,}0422\times10^{-10}\,{\rm m/s^2}.
$$

Para $H_0=73\,{\rm km\,s^{-1}\,Mpc^{-1}}$:

$$
a_0^{\rm local}
=
1{,}1288\times10^{-10}\,{\rm m/s^2}.
$$

Assim:

| Contorno | $a_0$ em ${\rm m/s^2}$ | erro relativo contra $1{,}20\times10^{-10}$ |
|---|---:|---:|
| $H_0=67{,}4$ | $1{,}042197881145\times10^{-10}$ | $-13{,}150177\%$ |
| $H_0=73$ | $1{,}128789989964\times10^{-10}$ | $-5{,}934168\%$ |
| $H_0=67{,}4$ com $\sqrt{\Omega_\Lambda}$ | $8{,}623833237863\times10^{-11}$ | $-28{,}134723\%$ |

## 4. Limite galáctico

A GDQ não é MOND fundamental. Ela contém um limite galáctico de baixa
aceleração. Nessa redução, a resposta radial observada tem a forma:

$$
g_{\rm obs}
\simeq
\sqrt{g_Na_0^{\rm GDQ}},
$$

com:

$$
g_N
=
\frac{GM_b(r)}{r^2}.
$$

Como $g_{\rm obs}=v^2/r$, segue:

$$
v^4
\simeq
GM_ba_0^{\rm GDQ}.
$$

Essa é a estrutura da relação bariônica de Tully--Fisher. Na GDQ ela surge da
ponte:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast^{\rm cos}
\to
K_{\rm grav}^{\rm phys}
\to
R_H
\to
\frac{1}{2\pi}
\to
a_0^{\rm GDQ}.
$$

## 5. Lentes, aglomerados e CMB

Uma lei escalar de aceleração não é suficiente para lentes e cosmologia
perturbativa. A GDQ trata esses efeitos pela métrica efetiva reconstruída a
partir da Hessiana física:

$$
K_{\rm grav}^{\rm phys}\delta\Phi
=
J_{\rm bar}
+
J_{\rm tor}.
$$

Aqui $J_{\rm bar}$ é a fonte bariônica e $J_{\rm tor}$ representa tensão
geométrica/torsional residual do background Hermitiano--Bismut. A deflexão de
luz deve ser calculada pela geometria óptica:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp(\Phi+\Psi)
\frac{2\,dl}{c^2}.
$$

Em aglomerados, a componente geométrica residual pode ser representada
efetivamente por:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_\nu{}^{\alpha\beta}
-
\frac12 g_{\mu\nu}|H|^2.
$$

Isso separa:

1. gás bariônico dissipativo;
2. galáxias quase balísticas;
3. tensão geométrica residual que contribui para lentes.

No CMB, o setor geométrico residual deve sustentar potenciais gravitacionais
com baixa pressão efetiva. A forma reduzida esperada no regime linear é:

$$
\ddot\delta_{\rm geo}
+
\mathcal H\dot\delta_{\rm geo}
-
4\pi G\rho_{\rm eff}\delta_{\rm geo}
=
O(c_s^2k^2)+O(\sigma_H).
$$

Quando $c_s^2\approx0$ e o acoplamento eletromagnético é nulo, esse setor
comporta-se como componente escura fria efetiva.

## 6. Status

O resultado numérico é uma avaliação direta de uma fórmula reduzida já
deduzida, seguida de comparação fenomenológica. Ele não usa $1{,}20\times
10^{-10}\,{\rm m/s^2}$ como entrada.

A conclusão estrutural é:

$$
\boxed{
a_0^{\rm GDQ}
=
\frac{cH_0}{2\pi}
}
$$

O que fica para extensão metrológica é resolver explicitamente
$K_{\rm grav}^{\rm phys}$ em backgrounds de galáxias, aglomerados e
cosmologia perturbativa, comparando com SPARC/RAR, lentes e espectros
$C_\ell$.
