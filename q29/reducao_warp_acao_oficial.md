# Q29 — Redução warped da ação oficial em $T^5\times S^3$

## 1. Ansatz e domínio

Considere o domínio cosmológico auxiliar

$$
K_\epsilon
=T^5\times[\epsilon,\pi]\times S^2
$$

e a métrica

$$
ds^2=e^{2A(\chi)}ds_{T^5}^2
+R^2\left(d\chi^2+\sin^2\chi\,d\Omega_2^2\right).
$$

O ponto $\chi=\epsilon$ é o contorno do estômato e $\chi=\pi$ é regular. O
cálculo usa somente a parte métrico-dilatônica da ação oficial; não introduz
uma ação de Einstein--Hilbert ou Yang--Mills independente.

## 2. Curvatura reduzida

Para uma fibra plana de dimensão $p=5$,

$$
\mathcal R
=\frac6{R^2}
-\frac{2p}{R^2}\left(A''+2\cot\chi A'\right)
-\frac{p(p+1)}{R^2}A'^2.
$$

Defina a variável invariante da medida

$$
F=f-5A.
$$

Então

$$
e^{5A-f}=e^{-F}.
$$

Depois de integrar o termo $\Delta A$ por partes, o funcional radial, a menos
de fatores positivos comuns, é

$$
\mathcal S_{\rm red}
=\int_\epsilon^\pi e^{-F}\sin^2\chi
\left[
\tau\left(
\frac6{R^2}
+\frac{F'^2-5A'^2}{R^2}
\right)
+F+5A-n
\right]d\chi
+\mathcal B_\epsilon.
$$

O sinal negativo de $A'^2$ é o modo conformal conhecido; ele não deve ser
interpretado isoladamente como instabilidade antes da restrição física e do
termo de bordo.

## 3. Equação variacional do warp

Variando $A$ com $F$ independente,

$$
\boxed{
\frac1{e^{-F}\sin^2\chi}
\frac{d}{d\chi}
\left(e^{-F}\sin^2\chi A'\right)
=-\frac{R^2}{2\tau}.
}
$$

Integrando no domínio,

$$
\left[e^{-F}\sin^2\chi A'\right]_{\epsilon}^{\pi}
=-\frac{R^2}{2\tau}
\int_\epsilon^\pi e^{-F}\sin^2\chi,d\chi.
$$

## 4. Consequência topológica

Sem estômato, regularidade nos dois polos anula o termo de bordo. O lado
direito é estritamente negativo para $\tau<\infty$. Portanto,

$$
\boxed{
T^5\times S^3\text{ compacto, regular e sem bordo não admite este
background shrinking.}
}
$$

Isso reproduz diretamente, pela ação oficial reduzida, a obstrução já
identificada na Q38.

Com o estômato, a equação se fecha se a condição Robin fornecer o fluxo

$$
\boxed{
e^{-F(\epsilon)}\sin^2\epsilon A'(\epsilon)
=\frac{R^2}{2\tau}
\int_\epsilon^\pi e^{-F}\sin^2\chi,d\chi.
}
$$

Assim, o background singular não é escolhido livremente: ele é selecionado
pelo balanço variacional entre bulk e contorno.

## 5. Solução líder para $F$ constante

Com $F'=0$ e regularidade $A'(\pi)=0$,

$$
A'(\chi)
=\frac{R^2}{2\tau}
\frac{\frac{\pi-\chi}{2}+\frac14\sin2\chi}{\sin^2\chi}.
$$

Para os parâmetros internos já calculados na Q29,

$$
R=1{,}99841118477,
\qquad
\epsilon=0{,}011591040463,
\qquad
\tau=1,
$$

resulta

$$
A'(\epsilon)=2{,}33\times10^4.
$$

O perfil é fortemente concentrado no estômato. Portanto, a aproximação de
warp fraco não é válida nessa normalização. Para uma escala cosmológica
$\tau\gg R^2/\epsilon^2$, o gradiente é suprimido.

## 6. Consequência para $W/Y$

O warp escalar comum ainda não distingue os geradores. O transporte
diferencial só pode aparecer quando os modos espectrais satisfizerem condições
de contorno distintas no estômato:

$$
\left(\partial_n+\mathsf R_W\right)\Psi_W=0,
\qquad
\left(\partial_n+\mathsf R_Y\right)\Psi_Y=0.
$$

As matrizes $\mathsf R_W$ e $\mathsf R_Y$ devem ser o pullback da Hessiana de
interface sobre as representações já derivadas, não números escolhidos para
obter $10/21$.

O próximo cálculo bem posto é, portanto, derivar esses dois operadores Robin
e resolver seus problemas de Sturm--Liouville no perfil $A,F$ acima.
