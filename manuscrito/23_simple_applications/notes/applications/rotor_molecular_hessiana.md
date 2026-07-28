---
title: "Rotor molecular e Hessiana coletiva"
---

# Rotor molecular e Hessiana coletiva

Status: redução efetiva condicional.

## Coordenadas coletivas

Para uma molécula diatômica:

$$
R(t)\in\mathbb R_+,
\qquad
\Omega(t)\in S^2.
$$

Após projeção física:

$$
L_{\rm eff}
=
\frac{\mu}{2}\dot R^2
+
\frac{\mu R^2}{2}|\dot\Omega|^2
-
V(R).
$$

## Setor angular

No equilíbrio $R_0$:

$$
I_0=\mu R_0^2.
$$

O operador angular é:

$$
K_{\rm ang}
=
-
\frac{\hbar^2}{2I_0}\Delta_{S^2}.
$$

Como:

$$
-\Delta_{S^2}Y_{Jm}=J(J+1)Y_{Jm},
$$

temos:

$$
E_J=BJ(J+1),
\qquad
B=\frac{\hbar^2}{2I_0}.
$$

## Distorção centrífuga

Com:

$$
V(R)=V_0+\frac12\mu\omega_e^2(R-R_0)^2+\cdots,
$$

minimizar:

$$
E(R;J)
=
\frac{\hbar^2J(J+1)}{2\mu R^2}
+
\frac12\mu\omega_e^2(R-R_0)^2
$$

é a etapa em que a distorção centrífuga aparece. Defina:

$$
L^2=\hbar^2J(J+1),
\qquad
R=R_0+x.
$$

Para baixa rotação, $|x|\ll R_0$, então:

$$
\frac{1}{(R_0+x)^2}
=
\frac{1}{R_0^2}
\left(
1-\frac{2x}{R_0}
+\frac{3x^2}{R_0^2}
\cdots
\right).
$$

Substituindo:

$$
E(x;J)
=
\frac{L^2}{2\mu R_0^2}
-
\frac{L^2}{\mu R_0^3}x
+
\frac{3L^2}{2\mu R_0^4}x^2
+
\frac12\mu\omega_e^2x^2
+
\cdots .
$$

Na ordem necessária para obter o termo $L^4$, o mínimo satisfaz:

$$
\mu\omega_e^2x
-
\frac{L^2}{\mu R_0^3}
=
0.
$$

Logo:

$$
x_\ast(J)
=
\frac{L^2}{\mu^2\omega_e^2R_0^3}
=
\frac{\hbar^2J(J+1)}
{\mu^2\omega_e^2R_0^3}.
$$

Substituir $x_\ast$ de volta na energia dá:

$$
E_J
=
BJ(J+1)
-
D[J(J+1)]^2+\cdots,
$$

onde:

$$
D
=
\frac{\hbar^4}{2\mu^3\omega_e^2R_0^6}.
$$

O sinal negativo tem significado físico: ao girar, a molécula alonga
ligeiramente a ponte, aumenta o momento de inércia efetivo e reduz a energia
rotacional em relação ao rotor perfeitamente rígido.

Em número de onda:

$$
D\simeq\frac{4B^3}{\omega_e^2}.
$$

## Parâmetro elástico legado

Se o texto legado escrevia:

$$
D
=
\gamma_{\rm elastic}
\frac{\hbar^4}{4I_0^3\omega_e^2},
$$

com $I_0=\mu R_0^2$, a derivação harmônica acima implica:

$$
D
=
\frac{\hbar^4}{2I_0^3\omega_e^2}.
$$

Portanto, nessa normalização:

$$
\gamma_{\rm elastic}^{\rm red}=2.
$$

Esse número não é uma nova constante fundamental. Ele é apenas a tradução do
modelo radial harmônico mínimo para a notação antiga. Em uma molécula real, a
Hessiana completa pode acrescentar anisotropia, torção, anharmonicidade e
resposta de contorno; esses efeitos devem ser calculados, não absorvidos em
um parâmetro universal.

## Alcance

Se $B$ e $\omega_e$ são dados experimentais, a conta é comparação
fenomenológica. Para previsão absoluta, a GDQ deve calcular $\mu$, $R_0$ e
$\omega_e$ pela Hessiana da ponte molecular.
