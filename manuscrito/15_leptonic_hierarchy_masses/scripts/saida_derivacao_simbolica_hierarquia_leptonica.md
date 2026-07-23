# Saída — derivação simbólica da hierarquia leptônica

Classificação: derivação simbólica / avaliação direta.

## 1. Setor eletrônico

O elétron define a escala reduzida:

$$
R_e=1.
$$

## 2. Razão do múon

Suporte biespacial:

$$
\nu_2=\frac23.
$$

Termo líder:

$$
R_\mu^{(0)}=\frac{1}{\nu_2\alpha}=\frac{3}{2}\alpha^{-1}.
$$

Impedância de interface e autoenergia:

$$
\Delta_\partial=\frac65,
\qquad
\Delta_{\rm self}=2\alpha.
$$

Logo:

$$
R_\mu=
2 \alpha + \frac{6}{5} + \frac{3}{2 \alpha}.
$$

## 3. Saturação geométrica da terceira razão

Com $R_3=z^2$, a condição é:

$$
\frac{10 \left(2 \alpha \left(10 \alpha + 5 z^{2} + 11\right) + 15\right)}{\left(10 \sqrt{\alpha} \left(z + 1\right) + \sqrt{10} \sqrt{4 \alpha \left(5 \alpha + 3\right) + 15}\right)^{2}} = \frac{2}{3}.
$$

O numerador polinomial equivalente é:

$$
10 \left(- 4 \sqrt{10} \sqrt{\alpha} z \sqrt{20 \alpha^{2} + 12 \alpha + 15} - 4 \sqrt{10} \sqrt{\alpha} \sqrt{20 \alpha^{2} + 12 \alpha + 15} + 20 \alpha^{2} + 10 \alpha z^{2} - 40 \alpha z + 22 \alpha + 15\right)=0.
$$

As duas soluções para $R_3$ são:

$$
R_{3,\pm}=
\left[
2(\sqrt{R_1}+\sqrt{R_2})
\pm
\sqrt{3R_1+12\sqrt{R_1R_2}+3R_2}
\right]^2.
$$

A solução simbólica direta do polinômio em $z$ foi usada pelo script; a forma acima é a forma simplificada em termos de $R_1$ e $R_2$.

## 4. Avaliação numérica

| quantidade | valor |
|---|---:|
| alpha^-1 | 137.035999177000 |
| R_mu | 206.768593470629 |
| R_3 ramo leve | 6.491919023877 |
| R_3 ramo pesado | 3477.446405098382 |

## 5. Comparação posterior

| razão | GDQ | referência | erro relativo |
|---|---:|---:|---:|
| M_mu/M_e | 206.768593470629 | 206.768282700000 | 1.502989842682e-06 |
| M_tau/M_e | 3477.446405098382 | 3477.150000000000 | 8.524369048845e-05 |

## Veredito

A derivação simbólica produz a fórmula do múon e os dois ramos da terceira razão sem usar massas experimentais como entrada. A escolha do ramo pesado é uma seleção física do tripleto carregado; o ramo leve permanece matemático até possuir Hessiana própria.
