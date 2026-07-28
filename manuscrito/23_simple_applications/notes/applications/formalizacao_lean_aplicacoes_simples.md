---
title: "Formalização Lean das aplicações simples"
---

# Formalização Lean das aplicações simples

O módulo novo
[SimpleApplications.lean](../../../../formal/GDQ/SimpleApplications.lean)
certifica as identidades algébricas próprias deste capítulo. Os resultados de
parede e Hartman reutilizam módulos canônicos já empregados no Capítulo 12:

- [DetectorDtNSchur.lean](../../../../formal/GDQ/DetectorDtNSchur.lean);
- [TransportInterference.lean](../../../../formal/GDQ/TransportInterference.lean).

Essa reutilização evita apresentar o mesmo teorema como se fosse uma nova
hipótese física.

## 1. Poço ideal

O espectro reduzido é definido por:

$$
E_n
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

O módulo prova sua não negatividade para $m>0$ e $L\neq0$, e sua positividade
quando também $\hbar\neq0$ e $n\neq0$.

A rota de circulação usa:

$$
2pL=nh,
\qquad
p=\frac{nh}{2L}.
$$

Com $h=2\pi\hbar$:

$$
\frac{p^2}{2m}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}.
$$

Assim, quantização por Dirichlet e fechamento da circulação fornecem
exatamente a mesma energia no domínio ideal.

## 2. Oscilador gaussiano

Para:

$$
R(x)=Ae^{-\alpha x^2/2},
$$

temos:

$$
\frac{R''}{R}
=
\alpha^2x^2-\alpha.
$$

A energia estacionária reduzida é:

$$
E(x)
=
\frac12m\omega^2x^2
-
\frac{\hbar^2}{2m}
\left(
\alpha^2x^2-\alpha
\right).
$$

O módulo prova que:

$$
\alpha=\frac{m\omega}{\hbar}
$$

cancela exatamente a dependência em $x$ e produz:

$$
E_0=\frac12\hbar\omega.
$$

Também certifica o espaçamento constante:

$$
E_{n+1}-E_n=\hbar\omega
$$

para a escada reduzida $E_n=\hbar\omega(n+1/2)$.

## 3. Casimir ideal

Usando a parte finita transversal e o valor espectral:

$$
-\frac{1}{6\pi}
\pi^3
\frac1{120},
$$

o módulo simplifica exatamente:

$$
-\frac{1}{6\pi}
\pi^3
\frac1{120}
=
-\frac{\pi^2}{720}.
$$

Consequentemente:

$$
\frac{\Delta E}{A}
=
-\frac{\pi^2\hbar c}{720a^3}.
$$

A relação algébrica com a pressão é:

$$
P(a)
=
\frac{3}{a}\frac{\Delta E}{A}
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

Para $\hbar>0$, $c>0$ e $a\neq0$, o módulo prova $P<0$. A continuação
dimensional e $\zeta(-3)=1/120$ continuam a técnica espectral declarada da
prova humana; Lean certifica a álgebra que leva aos coeficientes $720$ e
$240$.

## 4. Rotor molecular

Na ordem necessária para obter o termo $L^4$, a energia radial é:

$$
E(x)
=
\frac{L^2}{2\mu R_0^2}
-
\frac{L^2}{\mu R_0^3}x
+
\frac12\mu\omega_e^2x^2.
$$

O deslocamento estacionário é:

$$
x_\ast
=
\frac{L^2}{\mu^2\omega_e^2R_0^3}.
$$

Substituindo:

$$
E(x_\ast)
=
\frac{L^2}{2\mu R_0^2}
-
\frac{L^4}{2\mu^3\omega_e^2R_0^6}.
$$

Com $L^2=\hbar^2J(J+1)$:

$$
B
=
\frac{\hbar^2}{2\mu R_0^2},
\qquad
D
=
\frac{\hbar^4}{2\mu^3\omega_e^2R_0^6}.
$$

O módulo prova ainda:

$$
D
=
\frac{4B^3}{\hbar^2\omega_e^2}.
$$

Essas identidades não calculam $\mu$, $R_0$ ou $\omega_e$ de uma molécula
real. Esses dados devem ser obtidos da Hessiana do background molecular para
que o resultado se torne uma previsão absoluta.

## 5. Parede e Hartman

Os módulos já existentes provam:

1. o perfil da parede reduzida;
2. a impedância positiva $\lambda\coth(\lambda L)$;
3. a não negatividade do Schur de interface sob as hipóteses físicas;
4. a saturação:

$$
D_{\rm prop}(L)
\longrightarrow
\frac{\sqrt{g_0}}{\kappa}.
$$

A relação $g_{xx}\propto\rho$ permanece hipótese do canal evanescente
reduzido. A formalização não a promove a identidade universal da ação
oficial.

## 6. Alcance

A formalização certifica correspondência e reduções ideais. Ela não afirma
ter calculado:

1. a impedância de uma parede material específica;
2. o pacote temporal e o detector de uma barreira real;
3. a resposta dispersiva de placas reais;
4. o background molecular completo;
5. novos parâmetros fundamentais.
