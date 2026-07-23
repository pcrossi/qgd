# Q51 — Frequência interna e barreira radial alfa

## 1. Dados de contorno

Para cada decaimento:

$$
(A,Z)\to(A-4,Z-2)+\alpha,
$$

os dados externos admissíveis são:

$$
A,\quad Z,\quad Q_\alpha,\quad J^\pi_{\rm pai},\quad J^\pi_{\rm filho}.
$$

Esses dados definem o canal físico. Eles não são parâmetros livres da teoria.

## 2. Canal GDQ

O objeto alfa é tratado como cluster geométrico/torsional de superfície do
background nuclear. O canal reduzido é:

$$
\Phi_{\rm pai}
\longrightarrow
\Phi_{\rm filho}
\oplus
\Phi_\alpha
\oplus
\Phi_{\rm cola}.
$$

A cadeia de fechamento exigida é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm pai,*}
\to
K_{\rm phys}^{\rm nuclear}
\to
K_{\rm rad}^{\alpha{\rm -core}}
\to
\mathsf R_{\alpha{\rm -core}}
\to
\Gamma_\alpha.
$$

## 3. Frequência de tentativa

A frequência efetiva constante:

$$
\nu_0\sim10^{21}\ {\rm s}^{-1}
$$

não é derivação final. A forma GDQ esperada é:

$$
\nu_{\rm GDQ}
=
\frac1{2\pi}
\sqrt{
\lambda_{\alpha,{\rm int}}/M_\alpha^{\rm eff}
}.
$$

Como primeira redução não ajustável, usamos a frequência cinemática interna:

$$
\nu_{\rm int}
=
\frac{v_\alpha}{2R_N},
$$

com:

$$
v_\alpha
=
c\sqrt{\frac{2Q_\alpha}{\mu}},
$$

e:

$$
R_N
=
r_0\left((A-4)^{1/3}+4^{1/3}\right).
$$

Essa expressão ainda não substitui a Hessiana. Ela é o limite cinemático
reduzido do modo radial alfa no poço interno.

## 4. Barreira efetiva

Gamow puro usa:

$$
V_C(r)
=
\frac{2(Z-2)\alpha\hbar c}{r}.
$$

A GDQ completa deve substituir isso por:

$$
V_{\rm eff}^{\rm GDQ}
=
V_C
+V_{\rm surf}
+V_{\rm tors}
+V_{\rm Bohm}
+V_{\rm Schur}.
$$

O termo estrutural que falta é:

$$
V_{\rm Schur}
=
-K_{rI}K_{II}^{-1}K_{Ir},
$$

isto é, a resposta dos modos internos eliminados variacionalmente.

## 5. Métrica radial

A métrica exponencial legada:

$$
g_{rr}^{\rm leg}
=
\exp(-\alpha^2V_C/Q_\alpha)
$$

foi testada numericamente. Ela é pequena demais para corrigir a série e não
melhora Gamow quando usada com parâmetros congelados.

Portanto, a métrica radial física deve ser recalculada como:

$$
g_{rr}^{\rm eff}
=
\text{símbolo radial de }
K_{\rm rad}^{\alpha{\rm -core}}
\text{ após Schur/DtN}.
$$

## 6. Veredito

O avanço real da Q51 não é ajustar o fator exponencial. É calcular a
frequência normal interna e a impedância radial alfa--núcleo a partir da
Hessiana física.

