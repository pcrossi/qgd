# Q28 — Hessiana completa do junction torsional

## 1. Correção conceitual

A orientação global homogênea da fibração de Hopf é uma isometria. Logo, o
resultado anterior da Q42 permanece válido:

$$
\kappa_H^{\rm global}=0.
$$

O coeficiente positivo usado no equilíbrio de três canais não pode ser
atribuído à rotação global. Ele deve ser definido como pullback da Hessiana à
**textura relativa** que desloca os estômatos entre si:

$$
\kappa_{\rm rel}
=\left\langle
\partial_{\theta_a}\Phi_*,
\mathbb H_{\rm GDQ}
\partial_{\theta_a}\Phi_*
\right\rangle_{\mathcal U_*}.
$$

Assim,

$$
\kappa_{\rm rel}>0
$$

é uma propriedade a verificar no background multicítrico, não uma
consequência automática da isotropia de $S^3$.

## 2. Decomposição da Hessiana

Depois da fixação Hermitiana--DeTurck e da restrição de normalização da medida,
decomponha as flutuações físicas em

$$
\delta\Phi
=(\vartheta,\xi),
$$

onde:

1. $\vartheta$ contém os dois modos angulares relativos do junction de três
   canais, após remover a rotação comum;
2. $\xi$ contém dilatão, raio não homogêneo, modos métricos escalares e modos
   tensoriais transversais.

A forma quadrática completa é

$$
\delta^2\mathcal S_{\rm GDQ}
=\frac12
\begin{pmatrix}\vartheta&\xi\end{pmatrix}
\begin{pmatrix}
H_{\rm rel}&J\\
J^\dagger&K_\perp
\end{pmatrix}
\begin{pmatrix}\vartheta\\\xi\end{pmatrix}.
$$

No junction equilátero,

$$
H_{\rm rel}
=\frac32\kappa_{\rm rel}T^2I_2.
$$

O bloco transversal é a restrição física da Hessiana já estruturada na Q32:

$$
K_\perp
=\Pi_\perp
\begin{pmatrix}
L_\varphi&L_{\varphi h}\\
L_{h\varphi}&L_{h,{\rm phys}}
\end{pmatrix}
\Pi_\perp,
$$

com a condição de bordo linearizada

$$
\mathcal B_F(h,\varphi)=0
$$

e o vínculo

$$
\int d\mu_*
\left(
\frac{3u}{a}-\varphi
\right)=0.
$$

## 3. Critério exato de Schur

Se $K_\perp$ for positivo e invertível depois da remoção de gauge e dos modos
zero geométricos, a Hessiana completa é positiva se, e somente se,

$$
\boxed{
H_{\rm eff}
=H_{\rm rel}-JK_\perp^{-1}J^\dagger>0.
}
$$

Como $H_{\rm rel}$ é escalar no subespaço relativo, uma condição equivalente
é

$$
\boxed{
\lambda_{\max}
\left(JK_\perp^{-1}J^\dagger\right)
<\frac32\kappa_{\rm rel}T^2.
}
$$

Em norma adimensional,

$$
\boxed{
\left\|
K_\perp^{-1/2}J^\dagger H_{\rm rel}^{-1/2}
\right\|<1.
}
$$

Esse é o critério integral de estabilidade procurado.

## 4. Informação já calculada

O modo homogêneo do raio possui

$$
\lambda_{r,0}
=\mathcal W_{\rm hom}''(2\sqrt\tau)
=\frac{3}{2\tau}>0.
$$

Logo, o neckpinch homogêneo não desestabiliza o junction. O símbolo principal
dos setores escalar e métrico transversal é elíptico e não negativo após a
fixação de DeTurck.

Esses resultados garantem positividade ultravioleta e do modo radial
homogêneo, mas não determinam o menor autovalor completo

$$
\lambda_\perp
=\inf\operatorname{spec}K_\perp.
$$

## 5. Limite suficiente utilizável

Se

$$
K_\perp\ge\lambda_\perp I,
\qquad
\lambda_\perp>0,
$$

então

$$
JK_\perp^{-1}J^\dagger
\le\frac{\|J\|^2}{\lambda_\perp}I.
$$

Portanto, uma condição suficiente é

$$
\boxed{
\frac{\|J\|^2}{\lambda_\perp}
<\frac32\kappa_{\rm rel}T^2.
}
$$

Ela separa precisamente as três quantidades ainda necessárias:

1. rigidez relativa $\kappa_{\rm rel}$;
2. gap transversal $\lambda_\perp$;
3. acoplamento misto $\|J\|$.

## 6. O que acontece para $N>3$

No modelo horizontal reduzido, $N>3$ possui $N-3$ modos zero internos. A
Hessiana completa pode:

1. deslocá-los para valores negativos, tornando o polígono instável;
2. mantê-los nulos, produzindo uma família não isolada;
3. deslocá-los para valores positivos, estabilizando um junction maior.

Logo, a contagem reduzida não exclui matematicamente a terceira possibilidade.
Para provar unicidade absoluta de $N=3$, seria necessário demonstrar que o
Schur complementar nos subespaços extras é não positivo ou possui pelo menos
um modo negativo para todo $N>3$.

## 7. Veredito histórico da avaliação direta disponível

Na etapa em que este diagnóstico foi escrito, tínhamos

$$
\lambda_{r,0}>0,
$$

mas ainda não havia avaliações diretas completas de

$$
\kappa_{\rm rel},
\qquad
\lambda_\perp,
\qquad
J
$$

no background estacionário de três centros. Essa pendência foi posteriormente
resolvida, para a classe $C_3$ de preenchimentos gaussianos primitivos, em
`q28/hessiana_espectral_completa_background_c3.md`.

O resultado desta etapa intermediária era:

$$
\boxed{
N=3\text{ é selecionado pela Hessiana horizontal reduzida,}
}
$$

enquanto

$$
\boxed{
\text{a estabilidade integral depende do critério de Schur acima.}
}
$$

## 8. Cálculo posteriormente realizado

Não foram introduzidos números de teste para fazer a desigualdade funcionar.
O cálculo posterior adotou o background multicítrico

$$
\Phi_*^{(3)}
=(g_*^{(3)},f_*^{(3)},\bar f_*^{(3)})
$$

com as três condições Robin e então avaliar, por diferenciação da ação
oficial,

$$
\kappa_{\rm rel},
\qquad
K_\perp,
\qquad
J.
$$

Na classe simétrica de três preenchimentos gaussianos, a redução espectral
forneceu $J_{\theta r}=0$, gap radial $3/(2\tau)$ e gap não homogêneo
$1/(2\tau)$. O documento canônico atualizado é
`q28/hessiana_espectral_completa_background_c3.md`.
