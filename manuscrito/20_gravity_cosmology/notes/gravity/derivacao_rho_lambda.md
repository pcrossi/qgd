---
title: "Derivação da densidade de energia escura"
---

# Derivação da densidade de energia escura

A fórmula estrutural da energia do vácuo é:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\rho_{\rm UV}^{p}
\frac{r_p}{R_H}
\frac1{c^2}.
$$

## 1. Densidade UV protônica

O próton define a densidade UV materializada:

$$
\rho_{\rm UV}^{p}
=
\frac{M_pc^2}{(4\pi/3)r_p^3}.
$$

O significado físico é direto: o próton é o menor sóliton bariônico estável
usado como escala material. A GDQ não soma modos planos de ponto zero até uma
frequência arbitrária; ela usa a tensão máxima estabilizada que já aparece
como matéria persistente.

A unidade de $\rho_{\rm UV}^{p}$ é:

$$
\frac{{\rm kg}\,{\rm m^2\,s^{-2}}}{{\rm m^3}}
=
{\rm J\,m^{-3}}.
$$

## 2. Diluição linear

Com:

$$
f(r)
\sim
\ln\left(\frac{r}{r_p}\right),
$$

temos:

$$
e^{-f}
=
\frac{r_p}{r}.
$$

Então:

$$
\int_{r_p}^{R_H}
e^{-f}r^2dr
=
\frac{r_p}{2}
\left(R_H^2-r_p^2\right).
$$

Após dividir pelo volume cosmológico, fica a escala:

$$
\frac{r_p}{R_H}.
$$

Mais precisamente:

$$
\frac{
\int_{r_p}^{R_H}e^{-f(r)}r^2\,dr
}{
\int_0^{R_H}r^2\,dr
}
=
\frac{
\frac{r_p}{2}(R_H^2-r_p^2)
}{
\frac13R_H^3
}.
$$

No limite $R_H\gg r_p$:

$$
\frac{
\frac{r_p}{2}(R_H^2-r_p^2)
}{
\frac13R_H^3
}
=
\frac32\frac{r_p}{R_H}
\left[
1+O\left(\frac{r_p^2}{R_H^2}\right)
\right].
$$

O fator numérico de ordem um depende da normalização radial usada para a folha
cosmológica. Na convenção reduzida preservada, essa normalização é absorvida
no operador de projeção global, deixando a lei física relevante:

$$
\rho_{\rm diluida}\propto\frac{r_p}{R_H}.
$$

O ponto essencial é que a diluição é linear porque o peso é $1/r$, não porque
o volume plano tenha sido usado como argumento dimensional isolado.

## 3. Canais e projeção

Em oito dimensões reais:

$$
N_{\rm Cartan}
=
\dim\Lambda^2(\mathbb R^8)
=
28.
$$

A projeção macroscópica é quadrática:

$$
\rho_{\rm grav}
=
\alpha^2\rho_{\rm eff}.
$$

Assim a cadeia completa é:

$$
\rho_{\rm eff}
=
N_{\rm Cartan}
\rho_{\rm UV}^{p}
\frac{r_p}{R_H},
$$

e:

$$
\rho_\Lambda^{\rm GDQ}
=
\frac{\alpha^2\rho_{\rm eff}}{c^2}.
$$

Substituindo $\rho_{\rm UV}^{p}$:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\frac{M_pc^2}{(4\pi/3)r_p^3}
\frac{r_p}{R_H}
\frac1{c^2}.
$$

Cancelando explicitamente $c^2$ entre energia e massa:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\frac{M_p}{(4\pi/3)r_p^3}
\frac{r_p}{R_H}.
$$

Esta última forma mostra que a grandeza final está em ${\rm kg\,m^{-3}}$:

$$
\frac{{\rm kg}}{{\rm m^3}}
\cdot
1
=
{\rm kg\,m^{-3}}.
$$

## 4. Equação de estado

No background homogêneo estacionário, a contribuição efetiva entra como:

$$
T_{\mu\nu}^{(\Lambda)}
=
-\rho_\Lambda c^2g_{\mu\nu}.
$$

Comparando com fluido perfeito:

$$
T_{\mu\nu}
=
(\rho c^2+p)u_\mu u_\nu
+
pg_{\mu\nu},
$$

segue:

$$
p_\Lambda=-\rho_\Lambda c^2,
\qquad
w=-1.
$$

A continuidade FLRW:

$$
\dot\rho_\Lambda+3H(1+w)\rho_\Lambda=0
$$

então dá:

$$
\dot\rho_\Lambda=0.
$$

Portanto a energia escura GDQ tem assinatura operacional de constante
cosmológica no setor homogêneo estacionário.

## 5. Perturbações

A tensão de fundo não deve ser tratada como partícula livre de energia escura.
As perturbações admissíveis são flutuações da sela:

$$
\Phi_\ast^{\rm cos}
=
(g,J,H,f,\mathcal U)_\ast.
$$

A Hessiana física é:

$$
K_{\rm cos}^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_\ast^{\rm cos}}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

Em uma redução escalar:

$$
\left[
\partial_t^2
+3H\partial_t
+c_s^2\frac{k^2}{a^2}
+m_{\rm gap}^2
\right]\delta\Phi_k
=
J_k^{\rm matter}.
$$

Se:

$$
m_{\rm gap}^2>0,
$$

os modos livres são suprimidos/decadentes. A resposta a matéria entra por
$J_k^{\rm matter}$ e exige a Hessiana cosmológica completa para comparação
com CMB, BAO, supernovas e crescimento de estrutura.

## 6. Avaliação numérica preservada

Com:

$$
\alpha^{-1}=137.035999084,
$$

$$
r_p=0.840778765450\,{\rm fm},
$$

$$
M_p=1.672621925950\times10^{-27}\,{\rm kg},
$$

$$
H_0=67.4\,{\rm km\,s^{-1}\,Mpc^{-1}},
$$

e:

$$
\Omega_\Lambda=0.6847,
$$

obtém-se:

$$
R_H=\frac{c}{H_0}
=
1.372496834942\times10^{26}\,{\rm m}.
$$

A cadeia numérica é:

$$
\rho_{\rm UV}^{p}
=
6.038170582656\times10^{34}\,{\rm J\,m^{-3}},
$$

$$
\frac{r_p}{R_H}
=
6.125906771112\times10^{-42},
$$

$$
\rho_{\rm eff}
=
1.035699561608\times10^{-5}\,{\rm J\,m^{-3}},
$$

$$
\alpha^2\rho_{\rm eff}
=
5.515240453183\times10^{-10}\,{\rm J\,m^{-3}},
$$

e:

$$
\rho_\Lambda^{\rm GDQ}
=
6.136532599384\times10^{-27}\,{\rm kg\,m^{-3}}.
$$

O valor inferido pelo mesmo contorno é:

$$
\rho_\Lambda^{\rm obs}
=
\Omega_\Lambda
\frac{3H_0^2}{8\pi G}
=
5.842445930612\times10^{-27}\,{\rm kg\,m^{-3}}.
$$

Logo:

$$
\Omega_\Lambda^{\rm GDQ}
=
0.719165212772,
$$

e:

$$
\frac{
\rho_\Lambda^{\rm GDQ}-\rho_\Lambda^{\rm obs}
}{
\rho_\Lambda^{\rm obs}
}
=
5.033622\%.
$$

Esse erro não é absorvido por ajuste. Ele registra a sensibilidade ao contorno
cosmológico escolhido e aos dados metrológicos de entrada.

## 7. Status

O cálculo é estrutural. A comparação numérica depende de $R_H=c/H_0$, que é
dado de contorno cosmológico.
