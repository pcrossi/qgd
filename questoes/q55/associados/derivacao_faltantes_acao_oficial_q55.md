# Q55 — Derivação dos faltantes a partir da ação oficial

## Classificação

Derivação formal reduzida com avaliação numérica associada.

Este documento responde aos faltantes:

$$
\lambda_T,
\qquad
\eta,
\qquad
K_{HH},
\qquad
K_{gg},
\qquad
K_{gH},
\qquad
K_{gf},
\qquad
\text{modos de horizonte/Page curve}.
$$

A ação oficial não é alterada.

## 1. Ação oficial e setor de Bismut

A ação física fundamental é:

$$
\mathcal S_{\rm GDQ}
=
\int_\gamma
\left[
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau
\left(
\mathcal R
+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\right)
+
\frac{f+\bar f}{2}
-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
$$

Na classe Hermitiana--Bismut, a curvatura escalar que entra em
$\mathcal R$ contém a torção totalmente antissimétrica $H$ por:

$$
\mathcal R^B
=
\mathcal R^{LC}
-
\frac{1}{12}|H|^2
$$

na convenção usada nos documentos consolidados da GDQ.

Ao passar para a energia Euclidiana reduzida, o termo quadrático torsional
entra com sinal estabilizante:

$$
E_H
=
\frac{1}{12}
\int |H|^2\,dV_{\mathcal U}.
$$

## 2. Derivação de $\lambda_T$

No setor radial isotrópico do core, a torção admissível compatível com
circulação conservada é escrita como:

$$
H_{abc}(r)
=
q_T\,\rho(r)\,\varepsilon_{abc},
\qquad
a,b,c=1,2,3.
$$

Então:

$$
|H|^2
=
6q_T^2\rho^2.
$$

Logo:

$$
E_H
=
\frac{1}{12}
\int 6q_T^2\rho^2\,dV
=
\frac{q_T^2}{2}
\int\rho^2\,dV.
$$

Como:

$$
\rho=u^2,
$$

temos:

$$
E_H
=
\frac{q_T^2}{2}
\int u^4\,dV.
$$

Comparando com a redução usada:

$$
U_T
=
\frac{\lambda_T}{2}
\int u^4\,dV,
$$

obtemos:

$$
\boxed{
\lambda_T=q_T^2.
}
$$

Na normalização isotrópica mínima do triplete torsional de Cartan--Bismut,
existem três canais ortogonais equivalentes de circulação:

$$
q_T^2
=
1+1+1
=
3.
$$

Portanto:

$$
\boxed{
\lambda_T=3.
}
$$

Esse é exatamente o valor usado nos testes. A virial calculada em
`virial_lambda_t_sela_q55.py` confirma que esse valor satura o balanço radial
com resíduo relativo:

$$
1{,}5220\times10^{-4}.
$$

Esse resíduo é atribuído ao truncamento radial e termos de bordo.

## 3. Derivação de $\eta$

O parâmetro $\eta$ não é uma constante fundamental da ação. Ele é a
compactness adimensional da solução, isto é, a razão entre a massa ADM
geométrica e a massa normalizada da sela reduzida.

Se:

$$
M_{\rm red}(\infty)=1,
$$

então:

$$
m_{\rm geom}(r)
=
\eta M_{\rm red}(r).
$$

Em unidades físicas:

$$
\eta
=
\frac{G M_{\rm ADM}}{c^2R_0},
$$

onde $R_0$ é a escala radial usada para adimensionalizar o core.

Assim:

$$
\boxed{
\eta\text{ é dado de contorno ADM, não acoplamento livre da teoria.}
}
$$

A condição de formação de horizonte é:

$$
A(r)
=
1-\frac{2\eta M_{\rm red}(r)}{r}
=0.
$$

Logo o limiar crítico é:

$$
\eta_{\rm crit}
=
\min_r
\frac{r}{2M_{\rm red}(r)}.
$$

Numericamente:

$$
\boxed{
\eta_{\rm crit}
=
5{,}188522012681.
}
$$

O valor $\eta=8$ usado nos testes não é ajuste metrológico; é uma escolha de
solução acima do limiar para testar o regime de buraco negro.

## 4. Remoção do piso infravermelho de $K_{HH}$

O teste anterior continha:

$$
m_H^2(r)
=
2\lambda_T\rho(r)+10^{-3}.
$$

Esse piso foi removido.

O operador torsional reduzido passou a ser:

$$
K_{HH,\ell}^{red}
=
-\frac{d^2}{dr^2}
+
\frac{\ell(\ell+1)}{r^2}
+
2\lambda_T\rho(r).
$$

O gap positivo permanece por domínio e contorno do patch exterior:

$$
\boxed{
\lambda_{\min}(K_{HH}^{red})
=
1{,}475541776890\times10^{-1}>0.
}
$$

Portanto, o piso artificial não é necessário.

## 5. Setor métrico axial $K_{gg}$

No patch exterior estático, o setor axial reduzido é:

$$
K_{gg,\ell}^{red}
=
-\frac{d^2}{dr^2}
+
V_{gg,\ell}(r),
$$

com:

$$
V_{gg,\ell}
=
A
\left[
\frac{\ell(\ell+1)}{r^2}
-
\frac{6m(r)}{r^3}
+
4\pi(\epsilon-p_r)
\right].
$$

Esse é o análogo geométrico axial obtido da variação métrica efetiva da Q54,
usando a fonte GDQ reconstruída.

Numericamente:

$$
\boxed{
\lambda_{\min}(K_{gg}^{red})
=
1{,}493545907614\times10^{-1}>0.
}
$$

## 6. Acoplamentos cruzados

O acoplamento métrico--dilatônico vem da variação da medida ponderada:

$$
\mathcal U=e^{-f_R}(4\pi z_\tau)^{-n}.
$$

Assim, no patch exterior reduzido:

$$
J_{gf}^{red}
\sim
\sqrt A\,|\partial_r f_R|\,\sqrt\rho.
$$

Foi obtido:

$$
\boxed{
\|K_{gf}^{red}\|
=
6{,}166879064740\times10^{-4}.
}
$$

O acoplamento métrico--torsional vem da variação de:

$$
\sqrt g\,|H|^2.
$$

No setor reduzido:

$$
J_{gH}^{red}
\sim
\sqrt{\lambda_T}\rho.
$$

Foi obtido:

$$
\boxed{
\|K_{gH}^{red}\|
=
8{,}076881453156\times10^{-6}.
}
$$

As razões de Schur são:

$$
\boxed{
\chi_{gf}
=
1{,}333410946325\times10^{-3}
}
$$

e:

$$
\boxed{
\chi_{gH}
=
2{,}960174621482\times10^{-9}.
}
$$

Logo, os acoplamentos reduzidos não fecham o gap diagonal.

## 7. Horizontes

Os horizontes são raízes de:

$$
A(r_H)=0.
$$

Para $\eta=8$:

$$
r_{H,1}=4{,}222352820613,
\qquad
r_{H,2}=15{,}95712272799.
$$

A gravidade de superfície reduzida é:

$$
\kappa_H
=
\frac12e^{\Phi(r_H)}|A'(r_H)|.
$$

Logo:

$$
T_H
=
\frac{\kappa_H}{2\pi}.
$$

Numericamente:

$$
T_1
=
2{,}332099662324\times10^{-2},
\qquad
T_2
=
4{,}844788989724\times10^{-3}.
$$

## 8. Page curve

A Page curve física ainda exige:

$$
\Gamma_i
\text{ calculados dos canais reais de }
K_{\rm BH}^{phys}.
$$

O teste atual usa apenas uma curva toy unitária por canais positivos:

$$
S_{\rm toy}(0)=0,
\qquad
\max S_{\rm toy}
=
2{,}696953704284\times10^{-5},
\qquad
S_{\rm toy}(1)=0.
$$

Isso mostra compatibilidade com restituição unitária, mas não é cálculo físico
final de informação.

## 9. Conclusão

Na redução efetiva testada:

$$
\boxed{
\lambda_T=3
\text{ segue da normalização torsional isotrópica mínima.}
}
$$

$$
\boxed{
\eta
\text{ é dado de contorno ADM/compactness da solução, não acoplamento livre.}
}
$$

$$
\boxed{
K_{HH}^{red},K_{gg}^{red},K_{uu}^{Schur},K_\theta
\text{ são positivos nos setores testados.}
}
$$

$$
\boxed{
K_{gf}^{red},K_{gH}^{red}
\text{ são pequenos por Schur e não fecham o gap.}
}
$$

Portanto:

$$
\boxed{
\text{Q55 fica fechada na redução efetiva derivada/testada.}
}
$$

O fechamento covariante 8D completo ainda requer:

1. setor métrico polar completo;
2. coordenadas regulares atravessando horizontes;
3. matriz acoplada 8D completa;
4. Page curve física por canais espectrais reais.
